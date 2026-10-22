"""Safely package and verify the SAME immutable artifact produced by the existing Jekyll job."""
import argparse
import hashlib
import json
import os
import re
from pathlib import Path, PurePosixPath
import subprocess
import tarfile
from package_dismissticket_assets import package


def sha_file(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def file_manifest(root):
    rows = []
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError('Symlink refused')
        if path.is_file():
            rows.append({'path': path.relative_to(root).as_posix(), 'sha256': sha_file(path), 'bytes': path.stat().st_size})
    return rows


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def config(worker):
    path = Path('.cloudflare/wrangler.jsonc')
    value = json.loads(path.read_text())
    expected = {'name': worker, 'compatibility_date': '2026-10-22', 'workers_dev': True, 'assets': {'directory': '../_ssl_bundle/assets', 'html_handling': 'none', 'not_found_handling': 'none'}}
    if value != expected:
        raise ValueError('Config must remain assets-only without routes, domains, bindings or Worker code')
    return sha_file(path)


def source_commit():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()


def safe_extract(archive, directory):
    directory.mkdir()
    total = 0
    with tarfile.open(archive, mode='r:*') as tar:
        for member in tar:
            path = PurePosixPath(member.name)
            if path.is_absolute() or '..' in path.parts or any(ord(c) < 32 or ord(c) == 127 for c in str(path)) or not (member.isdir() or member.isfile()):
                raise ValueError('Unsafe rendered artifact entry')
            target = directory.joinpath(*path.parts)
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            total += member.size
            if total > 25 * 1024 * 1024 or member.size > 25 * 1024 * 1024 or target.exists():
                raise ValueError('Rendered artifact exceeds bounds or repeats a path')
            target.parent.mkdir(parents=True, exist_ok=True)
            with tar.extractfile(member) as incoming, target.open('wb') as output:
                for chunk in iter(lambda: incoming.read(65536), b''):
                    output.write(chunk)


def export(archive, output, worker, domain):
    commit = source_commit()
    if os.environ.get('GITHUB_SHA', commit) != commit:
        raise ValueError('Checkout differs from this build workflow commit')
    if os.environ.get('GITHUB_RUN_ID') and not re.fullmatch(r'[0-9]+', os.environ.get('RENDERED_ARTIFACT_ID', '')):
        raise ValueError('The existing build must identify its immutable rendered artifact')
    output.mkdir()
    extracted = output.parent / ('_rendered_input_' + output.name)
    safe_extract(archive, extracted)
    manifest = package(extracted, output / 'assets')
    if not (output / 'assets/index.html').is_file():
        raise ValueError('Rendered index.html is required')
    manifest.update({'domain': domain, 'worker_name': worker, 'source_commit': commit, 'source_rendered_artifact_tar_sha256': sha_file(archive), 'source_github_run_id': os.environ.get('GITHUB_RUN_ID'), 'source_rendered_artifact_id': os.environ.get('RENDERED_ARTIFACT_ID'), 'wrangler_config_sha256': config(worker)})
    (output / 'package-manifest.json').write_text(json.dumps(manifest, sort_keys=True, indent=2) + '\n')
    (output / 'root-manifest.sha256').write_text(manifest['package_manifest_sha256'] + '\n')
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as stream:
            stream.write('root_digest=' + manifest['package_manifest_sha256'] + '\n')
            stream.write('rendered_tar_sha256=' + manifest['source_rendered_artifact_tar_sha256'] + '\n')
    print(json.dumps({'source_commit': commit, 'rendered_tar_sha256': manifest['source_rendered_artifact_tar_sha256'], 'root_manifest_sha256': manifest['package_manifest_sha256'], 'runtime_files': manifest['runtime_files'], 'withheld_metadata_paths': [row['path'] for row in manifest['withheld_public_metadata']]}, sort_keys=True))


def verify(output, worker, domain, cfg, expected):
    if cfg != Path('.cloudflare/wrangler.jsonc'):
        raise ValueError('Unexpected config path')
    manifest = json.loads((output / 'package-manifest.json').read_text())
    rows = file_manifest(output / 'assets')
    if manifest['files'] != rows or manifest['package_manifest_sha256'] != digest(rows) or expected != digest(rows):
        raise ValueError('Downloaded asset bytes or trusted root digest changed')
    if manifest['source_commit'] != source_commit() or manifest['worker_name'] != worker or manifest['domain'] != domain or manifest['wrangler_config_sha256'] != config(worker):
        raise ValueError('Artifact provenance or assets-only config changed')
    if manifest['source_github_run_id'] != os.environ.get('GITHUB_RUN_ID'):
        raise ValueError('Artifact came from a different workflow run')
    print(json.dumps({'verified_files': len(rows), 'source_commit': manifest['source_commit'], 'root_manifest_sha256': expected}, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=Path('_github_pages/artifact.tar'))
    parser.add_argument('--output', type=Path, default=Path('_ssl_bundle'))
    parser.add_argument('--worker', required=True)
    parser.add_argument('--domain', required=True)
    parser.add_argument('--verify', action='store_true')
    parser.add_argument('--expected-digest')
    args = parser.parse_args()
    if args.verify:
        if not args.expected_digest:
            parser.error('--verify requires --expected-digest')
        verify(args.output, args.worker, args.domain, Path('.cloudflare/wrangler.jsonc'), args.expected_digest)
    else:
        export(args.input, args.output, args.worker, args.domain)
