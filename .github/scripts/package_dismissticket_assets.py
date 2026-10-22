"""Package one already-rendered immutable Jekyll artifact; never build Jekyll again."""
import argparse,hashlib,json,pathlib,re,urllib.parse
from html.parser import HTMLParser
from render_worker_routes import generate
WITHHELD={'CNAME','Gemfile','_headers','_redirects'}
PRIVATE={'private key': b'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', 'GitHub token': b'\\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,})\\b', 'Porkbun key': b'\\b(?:pk1|sk1)_[A-Za-z0-9]{20,}\\b', 'AWS access key': b'\\b(?:AKIA|ASIA)[A-Z0-9]{16}\\b', 'Stripe secret': b'\\b(?:sk|rk)_live_[A-Za-z0-9]{20,}\\b', 'credential literal': b'(?:CLOUDFLARE_API_TOKEN|CF_API_TOKEN|PORKBUN_API_SECRET|secretapikey|password)\\s*[=:]\\s*[\\"\\\'][^\\"\\\'\\n]{16,}[\\"\\\']'}

def scan_private(data,rel):
    for kind,pattern in PRIVATE.items():
        if re.search(pattern,data,re.I if kind=='credential literal' else 0):raise RuntimeError(kind+' signal in rendered artifact; values withheld')
    if re.search(r'\.(?:php\d*|phtml|phar|env|key|pem)$',rel,re.I):raise RuntimeError('Private or server-code file refused')

def sha(data):return hashlib.sha256(data).hexdigest()
class References(HTMLParser):
    def __init__(self):super().__init__();self.refs=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if v and k.lower() in ['href','src','action','poster','data','srcset']:self.refs.append(v)

def package(source,output):
    source=pathlib.Path(source).resolve();output=pathlib.Path(output).resolve()
    if not source.is_dir() or output.exists():raise RuntimeError('Source must exist and output must be new')
    source_rows=[];runtime=[];violations=[];total=0
    for p in sorted(source.rglob('*')):
        if p.is_symlink():raise RuntimeError('Symlink refused')
        if not p.is_file():continue
        rel=p.relative_to(source).as_posix();parts=pathlib.PurePosixPath(rel).parts
        if '..' in parts or any(part.startswith('.') for part in parts) or any(ord(c)<32 for c in rel):raise RuntimeError('Hidden or unsafe artifact path')
        data=p.read_bytes();scan_private(data,rel);total+=len(data)
        if total>25*1024*1024:raise RuntimeError('Artifact exceeds reviewed bounded package size')
        row={'path':rel,'bytes':len(data),'sha256':sha(data)};source_rows.append(row)
        if rel in WITHHELD:continue
        if rel in ['wrangler.toml','wrangler.json','wrangler.jsonc','package.json','package-lock.json'] or rel.endswith(('.php','.env','.key','.pem')):raise RuntimeError('Unexpected build/server file in rendered artifact')
        if p.suffix.lower() in ['.html','.css','.js','.xml','.json','.txt']:
            text=data.decode('utf-8',errors='strict');refs=[]
            if p.suffix.lower()=='.html':
                parser=References();parser.feed(text);refs+=parser.refs
            refs+=re.findall(r'''(?:url\(\s*|(?:fetch|importScripts)\(\s*)["']?([^\s"')]+)''',text)
            # Supplement parser checks with quoted URL tokens, including encoded metadata paths.
            refs+=re.findall(r'''["']([^"'<>\r\n]+)["']''',text)
            for value in refs:
                value=urllib.parse.unquote(urllib.parse.unquote(value));path=urllib.parse.urlsplit(value).path
                if path.lstrip('./') in WITHHELD:violations.append({'file':rel,'metadata_target':path})
        runtime.append((rel,data,row))
    if violations:raise RuntimeError('An application reference points to withheld metadata')
    if {r['path'] for r in source_rows if r['path'] in WITHHELD}!=WITHHELD:raise RuntimeError('Expected four metadata inputs missing; review artifact change')
    output.mkdir(parents=True)
    for rel,data,row in runtime:
        target=output/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    routes,routing=generate(output);(output/'_redirects').write_text(routes)
    files=sorted([row for _,_,row in runtime]+[{'path':'_redirects','bytes':len(routes.encode()),'sha256':sha(routes.encode())}],key=lambda r:r['path'])
    digest=sha(json.dumps(files,sort_keys=True,separators=(',',':')).encode())
    return {'private_security_signals':[],'private_scan_policy':'Reject private key, GitHub/Porkbun/AWS/Stripe credential and explicit credential-literal signatures; case-insensitive PHP/server/private extensions; no matched values logged.','source_file_count':len(source_rows),'runtime_files':len(runtime),'runtime_bytes':sum(r['bytes'] for _,_,r in runtime),'runtime_bytes_unchanged':True,'withheld_public_metadata':[r for r in source_rows if r['path'] in WITHHELD],'metadata_reference_findings':violations,'metadata_reference_check':'Parsed HTML URL attributes plus CSS URLs, fetch/importScripts and quoted URL tokens across rendered text assets; URL percent escapes decoded twice. No application code executes.','public_metadata_behavior':'/CNAME /Gemfile /_headers /_redirects intentionally become404. The new _redirects file is reserved static routing configuration and is not served as an asset. No old _headers or alias rules are activated.','routing':routing,'package_manifest_sha256':digest,'files':files,'not_found_handling':'none','not_found_policy':'Provider generic404; no SPA fallback and no fabricated404.html. GitHub-branded default404 body is intentionally not preserved.'}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('source');parser.add_argument('output');parser.add_argument('--manifest',required=True);a=parser.parse_args();manifest=package(a.source,a.output);pathlib.Path(a.manifest).write_text(json.dumps(manifest,sort_keys=True,indent=2)+'\n');print(json.dumps({k:v for k,v in manifest.items() if k not in ['files','withheld_public_metadata']}))
