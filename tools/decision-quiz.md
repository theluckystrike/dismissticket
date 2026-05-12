---
layout: default
title: "What Should I Do With My Traffic Ticket? — Free Decision Quiz"
description: "Answer 5 quick questions to get a personalized recommendation for your traffic ticket. Find out if you should take traffic school, fight it in court, or hire an attorney."
permalink: /tools/decision-quiz/
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Traffic Ticket Decision Quiz",
      "description": "Interactive quiz that recommends the best way to handle your traffic ticket based on your state, violation type, and driving history.",
      "url": "https://dismissticket.com/tools/decision-quiz/",
      "applicationCategory": "UtilityApplication",
      "operatingSystem": "Web",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      },
      "author": {
        "@type": "Organization",
        "name": "DismissTicket",
        "url": "https://dismissticket.com/"
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://dismissticket.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Decision Quiz",
          "item": "https://dismissticket.com/tools/decision-quiz/"
        }
      ]
    }
  ]
}
</script>

<style>
/* ===== Decision Quiz Styles ===== */
.quiz-container {
  max-width: 640px;
  margin: 0 auto;
  padding: 0;
}

.quiz-progress {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 32px;
}

.quiz-progress-bar {
  flex: 1;
  height: 8px;
  background: #e5e7eb;
  border-radius: 4px;
  overflow: hidden;
}

.quiz-progress-fill {
  height: 100%;
  background: #2563eb;
  border-radius: 4px;
  transition: width 0.4s ease;
  width: 0%;
}

.quiz-progress-text {
  font-size: 14px;
  color: #6b7280;
  white-space: nowrap;
  min-width: 80px;
  text-align: right;
}

.quiz-step {
  display: none;
  animation: quizFadeIn 0.35s ease;
}

.quiz-step.active {
  display: block;
}

@keyframes quizFadeIn {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}

.quiz-question {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 8px;
  color: #111827;
  line-height: 1.3;
}

.quiz-subtitle {
  font-size: 15px;
  color: #6b7280;
  margin-bottom: 24px;
}

.quiz-options {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 24px;
}

.quiz-option {
  display: block;
  width: 100%;
  padding: 16px 20px;
  font-size: 16px;
  font-weight: 500;
  text-align: left;
  background: #fff;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.15s ease;
  color: #1f2937;
  line-height: 1.4;
  font-family: inherit;
}

.quiz-option:hover {
  border-color: #2563eb;
  background: #eff6ff;
}

.quiz-option:active {
  transform: scale(0.98);
}

.quiz-option.selected {
  border-color: #2563eb;
  background: #eff6ff;
  color: #1e40af;
}

.quiz-select-wrapper {
  margin-bottom: 24px;
}

.quiz-select {
  width: 100%;
  padding: 16px 20px;
  font-size: 16px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  background: #fff;
  color: #1f2937;
  cursor: pointer;
  appearance: none;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20' fill='%236b7280'%3E%3Cpath fill-rule='evenodd' d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 16px center;
  font-family: inherit;
}

.quiz-select:focus {
  outline: none;
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
}

.quiz-nav {
  display: flex;
  gap: 12px;
  margin-top: 16px;
}

.quiz-btn {
  padding: 14px 28px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  transition: all 0.15s ease;
  font-family: inherit;
}

.quiz-btn:active {
  transform: scale(0.97);
}

.quiz-btn-back {
  background: #f3f4f6;
  color: #374151;
}

.quiz-btn-back:hover {
  background: #e5e7eb;
}

.quiz-btn-next {
  background: #2563eb;
  color: #fff;
  flex: 1;
}

.quiz-btn-next:hover {
  background: #1d4ed8;
}

.quiz-btn-next:disabled {
  background: #93c5fd;
  cursor: not-allowed;
}

/* ===== Result Styles ===== */
.quiz-result {
  display: none;
  animation: quizFadeIn 0.4s ease;
}

.quiz-result.active {
  display: block;
}

.quiz-result-card {
  background: #f0fdf4;
  border: 2px solid #22c55e;
  border-radius: 16px;
  padding: 28px;
  margin-bottom: 24px;
}

.quiz-result-label {
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #16a34a;
  margin-bottom: 8px;
}

.quiz-result-title {
  font-size: 28px;
  font-weight: 800;
  color: #15803d;
  margin-bottom: 12px;
  line-height: 1.2;
}

.quiz-result-body {
  font-size: 16px;
  color: #166534;
  line-height: 1.6;
}

.quiz-result-body p {
  margin-bottom: 12px;
}

.quiz-result-body p:last-child {
  margin-bottom: 0;
}

.quiz-result-cta {
  display: inline-block;
  margin-top: 16px;
  padding: 14px 28px;
  background: #22c55e;
  color: #fff;
  font-size: 16px;
  font-weight: 700;
  border-radius: 10px;
  text-decoration: none;
  transition: background 0.15s;
}

.quiz-result-cta:hover {
  background: #16a34a;
  color: #fff;
  text-decoration: none;
}

.quiz-alternatives {
  margin-top: 32px;
}

.quiz-alternatives h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 16px;
  color: #374151;
}

.quiz-alt-card {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 12px;
}

.quiz-alt-card h4 {
  font-size: 16px;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 6px;
}

.quiz-alt-card p {
  font-size: 14px;
  color: #6b7280;
  margin: 0;
  line-height: 1.5;
}

.quiz-summary {
  margin-top: 24px;
  padding: 20px;
  background: #f9fafb;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
}

.quiz-summary h3 {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 12px;
  color: #374151;
}

.quiz-summary-row {
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  font-size: 14px;
  color: #6b7280;
}

.quiz-summary-row span:last-child {
  font-weight: 600;
  color: #1f2937;
}

.quiz-restart {
  display: inline-block;
  margin-top: 24px;
  padding: 12px 24px;
  background: #f3f4f6;
  color: #374151;
  font-size: 14px;
  font-weight: 600;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  font-family: inherit;
}

.quiz-restart:hover {
  background: #e5e7eb;
}

/* ===== Mobile ===== */
@media (max-width: 640px) {
  .quiz-question {
    font-size: 20px;
  }
  .quiz-option {
    padding: 14px 16px;
    font-size: 15px;
  }
  .quiz-result-title {
    font-size: 22px;
  }
  .quiz-result-card {
    padding: 20px;
  }
}
</style>

<div class="quiz-container" id="decisionQuiz">
  <!-- Progress bar -->
  <div class="quiz-progress">
    <div class="quiz-progress-bar">
      <div class="quiz-progress-fill" id="quizProgressFill"></div>
    </div>
    <div class="quiz-progress-text" id="quizProgressText">Step 1 of 5</div>
  </div>

  <!-- Step 1: State -->
  <div class="quiz-step active" data-step="1">
    <h2 class="quiz-question">What state did you receive your ticket in?</h2>
    <p class="quiz-subtitle">Rules vary significantly by state. Select yours below.</p>
    <div class="quiz-select-wrapper">
      <select class="quiz-select" id="quizState">
        <option value="">Select your state...</option>
      </select>
    </div>
    <div class="quiz-nav">
      <button class="quiz-btn quiz-btn-next" id="quizNext1" disabled>Continue</button>
    </div>
  </div>

  <!-- Step 2: Violation type -->
  <div class="quiz-step" data-step="2">
    <h2 class="quiz-question">What type of violation?</h2>
    <p class="quiz-subtitle">Select the violation listed on your citation.</p>
    <div class="quiz-options" id="violationOptions">
      <button class="quiz-option" data-value="speeding">Speeding</button>
      <button class="quiz-option" data-value="red_light">Red Light / Stop Signal</button>
      <button class="quiz-option" data-value="stop_sign">Stop Sign</button>
      <button class="quiz-option" data-value="cell_phone">Cell Phone / Distracted Driving</button>
      <button class="quiz-option" data-value="other">Other Moving Violation</button>
    </div>
    <div class="quiz-nav">
      <button class="quiz-btn quiz-btn-back" data-back="1">Back</button>
    </div>
  </div>

  <!-- Step 3: Speed over limit (only for speeding) -->
  <div class="quiz-step" data-step="3">
    <h2 class="quiz-question">How fast were you going over the speed limit?</h2>
    <p class="quiz-subtitle">This affects your eligibility for traffic school and fine amounts.</p>
    <div class="quiz-options" id="speedOptions">
      <button class="quiz-option" data-value="1-10">1 - 10 mph over</button>
      <button class="quiz-option" data-value="11-20">11 - 20 mph over</button>
      <button class="quiz-option" data-value="21-30">21 - 30 mph over</button>
      <button class="quiz-option" data-value="31+">31+ mph over</button>
    </div>
    <div class="quiz-nav">
      <button class="quiz-btn quiz-btn-back" data-back="2">Back</button>
    </div>
  </div>

  <!-- Step 4: First offense -->
  <div class="quiz-step" data-step="4">
    <h2 class="quiz-question">Is this your first traffic violation in the past 12 months?</h2>
    <p class="quiz-subtitle">Most states require a clean recent record for traffic school eligibility.</p>
    <div class="quiz-options" id="firstOffenseOptions">
      <button class="quiz-option" data-value="yes">Yes, this is my first violation recently</button>
      <button class="quiz-option" data-value="no">No, I have had other violations</button>
    </div>
    <div class="quiz-nav">
      <button class="quiz-btn quiz-btn-back" id="backFromStep4">Back</button>
    </div>
  </div>

  <!-- Step 5: CDL -->
  <div class="quiz-step" data-step="5">
    <h2 class="quiz-question">Do you hold a Commercial Driver's License (CDL)?</h2>
    <p class="quiz-subtitle">CDL holders face stricter penalties and limited dismissal options.</p>
    <div class="quiz-options" id="cdlOptions">
      <button class="quiz-option" data-value="yes">Yes, I have a CDL</button>
      <button class="quiz-option" data-value="no">No, standard driver's license</button>
    </div>
    <div class="quiz-nav">
      <button class="quiz-btn quiz-btn-back" data-back="4">Back</button>
    </div>
  </div>

  <!-- Result -->
  <div class="quiz-result" id="quizResult">
    <div class="quiz-result-card" id="resultCard">
      <div class="quiz-result-label">Our Recommendation</div>
      <div class="quiz-result-title" id="resultTitle"></div>
      <div class="quiz-result-body" id="resultBody"></div>
      <a class="quiz-result-cta" id="resultCta" href="/traffic-school/" style="display:none;">Find an Approved Course</a>
    </div>

    <div class="quiz-summary" id="resultSummary">
      <h3>Your Answers</h3>
      <div id="summaryRows"></div>
    </div>

    <div class="quiz-alternatives" id="resultAlternatives">
      <h3>Other Options to Consider</h3>
      <div id="altCards"></div>
    </div>

    <button class="quiz-restart" id="quizRestart">Start Over</button>
  </div>
</div>

<script>
(function() {
  'use strict';

  /* ===== State Data ===== */
  var STATES = [
    'Alabama','Alaska','Arizona','Arkansas','California','Colorado',
    'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho',
    'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
    'Maine','Maryland','Massachusetts','Michigan','Minnesota',
    'Mississippi','Missouri','Montana','Nebraska','Nevada',
    'New Hampshire','New Jersey','New Mexico','New York',
    'North Carolina','North Dakota','Ohio','Oklahoma','Oregon',
    'Pennsylvania','Rhode Island','South Carolina','South Dakota',
    'Tennessee','Texas','Utah','Vermont','Virginia','Washington',
    'West Virginia','Wisconsin','Wyoming'
  ];

  /* State-specific rules for the 10 supported states */
  var STATE_RULES = {
    'California':      { tsEligible: true, tsSpeedCap: 25, tsFreq: 18, deferred: false, trialByDecl: true },
    'Texas':           { tsEligible: true, tsSpeedCap: 25, tsFreq: 12, deferred: true,  trialByDecl: false },
    'Florida':         { tsEligible: true, tsSpeedCap: 30, tsFreq: 12, deferred: false, trialByDecl: false },
    'New York':        { tsEligible: true, tsSpeedCap: 999, tsFreq: 18, deferred: false, trialByDecl: false, pointReductionOnly: true },
    'Georgia':         { tsEligible: true, tsSpeedCap: 24, tsFreq: 12, deferred: true,  trialByDecl: false },
    'Ohio':            { tsEligible: true, tsSpeedCap: 25, tsFreq: 36, deferred: false, trialByDecl: false },
    'Virginia':        { tsEligible: true, tsSpeedCap: 20, tsFreq: 24, deferred: false, trialByDecl: false },
    'Illinois':        { tsEligible: true, tsSpeedCap: 25, tsFreq: 12, deferred: true,  trialByDecl: false },
    'North Carolina':  { tsEligible: true, tsSpeedCap: 25, tsFreq: 12, deferred: true,  trialByDecl: false },
    'Pennsylvania':    { tsEligible: false, tsSpeedCap: 0, tsFreq: 0, deferred: false, trialByDecl: false }
  };

  /* ===== Quiz State (inside IIFE, not global) ===== */
  var answers = {
    state: '',
    violation: '',
    speedOver: '',
    firstOffense: '',
    cdl: ''
  };

  var currentStep = 1;
  var totalSteps = 5;

  /* ===== DOM References ===== */
  var stateSelect = document.getElementById('quizState');
  var progressFill = document.getElementById('quizProgressFill');
  var progressText = document.getElementById('quizProgressText');
  var nextBtn1 = document.getElementById('quizNext1');
  var resultDiv = document.getElementById('quizResult');

  /* ===== Initialize State Dropdown ===== */
  function populateStates() {
    if (!stateSelect) { return; }
    for (var i = 0; i < STATES.length; i++) {
      var opt = document.createElement('option');
      opt.value = STATES[i];
      opt.textContent = STATES[i];
      stateSelect.appendChild(opt);
    }
  }

  /* ===== Step Navigation ===== */
  function showStep(stepNum) {
    var steps = document.querySelectorAll('.quiz-step');
    for (var i = 0; i < steps.length; i++) {
      steps[i].classList.remove('active');
    }
    resultDiv.classList.remove('active');

    var target = document.querySelector('.quiz-step[data-step="' + stepNum + '"]');
    if (target) {
      target.classList.add('active');
    }
    currentStep = stepNum;
    updateProgress();
  }

  function updateProgress() {
    var effectiveTotal = totalSteps;
    var effectiveStep = currentStep;

    /* If not speeding, step 3 is skipped: total is 4 */
    if (answers.violation !== '' && answers.violation !== 'speeding') {
      effectiveTotal = 4;
      if (currentStep >= 4) {
        effectiveStep = currentStep - 1;
      }
    }

    var pct = Math.round((effectiveStep / effectiveTotal) * 100);
    if (progressFill) { progressFill.style.width = pct + '%'; }
    if (progressText) { progressText.textContent = 'Step ' + effectiveStep + ' of ' + effectiveTotal; }
  }

  function advanceFromStep(fromStep) {
    if (fromStep === 2 && answers.violation !== 'speeding') {
      /* Skip step 3 (speed over limit) */
      answers.speedOver = 'n/a';
      showStep(4);
    } else if (fromStep === 5) {
      showResult();
    } else {
      showStep(fromStep + 1);
    }
  }

  function goBack(toStep) {
    if (toStep === 3 && answers.violation !== 'speeding') {
      showStep(2);
    } else {
      showStep(toStep);
    }
  }

  /* ===== Option Buttons ===== */
  function setupOptionGroup(containerId, answerKey, stepNum) {
    var container = document.getElementById(containerId);
    if (!container) { return; }

    container.addEventListener('click', function(e) {
      var btn = e.target.closest('.quiz-option');
      if (!btn) { return; }

      var value = btn.getAttribute('data-value');
      if (!value) { return; }

      answers[answerKey] = value;

      /* Clear previous selection */
      var opts = container.querySelectorAll('.quiz-option');
      for (var i = 0; i < opts.length; i++) {
        opts[i].classList.remove('selected');
      }
      btn.classList.add('selected');

      /* Auto-advance after short delay */
      setTimeout(function() {
        advanceFromStep(stepNum);
      }, 200);
    });
  }

  /* ===== Back Buttons ===== */
  function setupBackButtons() {
    var backBtns = document.querySelectorAll('[data-back]');
    for (var i = 0; i < backBtns.length; i++) {
      backBtns[i].addEventListener('click', function() {
        var target = parseInt(this.getAttribute('data-back'), 10);
        if (target >= 1 && target <= 5) {
          goBack(target);
        }
      });
    }

    /* Special back from step 4 (may need to skip 3) */
    var backFrom4 = document.getElementById('backFromStep4');
    if (backFrom4) {
      backFrom4.addEventListener('click', function() {
        if (answers.violation === 'speeding') {
          showStep(3);
        } else {
          showStep(2);
        }
      });
    }
  }

  /* ===== Parse Speed Over ===== */
  function getMaxSpeedOver(speedStr) {
    if (!speedStr || speedStr === 'n/a') { return 0; }
    var map = { '1-10': 10, '11-20': 20, '21-30': 30, '31+': 40 };
    return map[speedStr] || 0;
  }

  /* ===== Recommendation Engine ===== */
  function makeRec(primary, title, body, showCta, alts) {
    return { primary: primary, title: title, body: body, showCta: !!showCta, alternatives: alts || [] };
  }

  function computeRecForAttorney(state, rules, violation, speedOver) {
    if (violation === 'speeding' && speedOver >= 31) {
      return makeRec('attorney', 'Hire a Traffic Ticket Attorney', buildExcessiveSpeedBody(state, rules), false, buildExcessiveSpeedAlts(rules));
    }
    return null;
  }

  function computeRecForDismissal(state, rules, violation, speedOver, isFirstOffense) {
    var tsEligible = checkTrafficSchoolEligibility(rules, violation, speedOver, isFirstOffense);
    if (tsEligible) {
      return makeRec('traffic_school', 'Take Traffic School', buildTrafficSchoolBody(state, rules), true, buildTrafficSchoolAlts(state, rules));
    }
    if (rules && rules.deferred && isFirstOffense) {
      return makeRec('deferred', 'Request Deferred Disposition', buildDeferredBody(state), false, [
        { title: 'Fight It in Court', desc: 'You can contest the ticket at a hearing. If the officer does not appear or you present a valid defense, the case may be dismissed.' },
        { title: 'Hire an Attorney', desc: 'A traffic attorney can negotiate reduced charges or full dismissal, often without you appearing in court.' }
      ]);
    }
    return null;
  }

  function computeRecommendation() {
    var state = answers.state;
    var rules = STATE_RULES[state] || null;
    var speedOver = getMaxSpeedOver(answers.speedOver);
    var isFirstOffense = (answers.firstOffense === 'yes');
    var isCdl = (answers.cdl === 'yes');
    var violation = answers.violation;

    /* CDL holders: almost always need an attorney */
    if (isCdl) {
      return makeRec('attorney', 'Hire a Traffic Ticket Attorney', buildCdlBody(state, rules), false, [
        { title: 'Fight It Yourself', desc: 'You can represent yourself in court, but CDL violations carry severe consequences including license suspension. Professional representation is strongly recommended.' }
      ]);
    }

    /* Excessive speed */
    var attorneyRec = computeRecForAttorney(state, rules, violation, speedOver);
    if (attorneyRec) { return attorneyRec; }

    /* Traffic school or deferred */
    var dismissalRec = computeRecForDismissal(state, rules, violation, speedOver, isFirstOffense);
    if (dismissalRec) { return dismissalRec; }

    /* Default: fight it */
    var fightAlts = [
      { title: 'Hire an Attorney', desc: 'A traffic ticket attorney can represent you in court and may negotiate a reduced charge or dismissal. Many offer flat-fee pricing.' }
    ];
    if (rules && rules.deferred) {
      fightAlts.push({ title: 'Deferred Disposition', desc: 'Ask the court about deferred adjudication programs that may be available even for repeat offenders, depending on the judge.' });
    }
    return makeRec('fight', 'Fight Your Ticket in Court', buildFightBody(state, rules), false, fightAlts);
  }

  function checkTrafficSchoolEligibility(rules, violation, speedOver, isFirst) {
    if (!rules) {
      /* Unknown state: assume eligible if first offense and moderate speed */
      return isFirst && speedOver <= 25;
    }
    if (!rules.tsEligible) { return false; }
    if (!isFirst) { return false; }
    if (violation === 'speeding' && speedOver > rules.tsSpeedCap) { return false; }
    return true;
  }

  function buildCdlBody(state, rules) {
    var text = '<p>As a CDL holder, traffic violations carry severe consequences including points on both your CDL and personal license, potential CDL disqualification, and impact on your livelihood.</p>';
    text += '<p>A traffic ticket attorney experienced with commercial driver cases can often negotiate the charge down to a non-moving violation or get it dismissed entirely. Many offer free consultations.</p>';
    if (state) {
      text += '<p>In ' + escHtml(state) + ', CDL holders are generally not eligible for standard traffic school dismissal for moving violations received in a commercial vehicle.</p>';
    }
    return text;
  }

  function buildExcessiveSpeedBody(state, rules) {
    var text = '<p>Going 31+ mph over the speed limit is a serious violation. In many states, this can be charged as reckless driving, which is a criminal offense carrying potential jail time, heavy fines, and license suspension.</p>';
    text += '<p>A traffic ticket attorney can negotiate the charge down, potentially to a non-criminal moving violation, saving your record and your insurance rates.</p>';
    if (rules && !rules.tsEligible) {
      text += '<p>Note: Traffic school is generally not available for this level of speed violation in ' + escHtml(state) + '.</p>';
    }
    return text;
  }

  function buildExcessiveSpeedAlts(rules) {
    var alts = [
      { title: 'Fight It Yourself', desc: 'You can represent yourself at a court hearing. Request calibration records for the speed measurement device and check for procedural errors on your citation.' }
    ];
    if (rules && rules.deferred) {
      alts.push({ title: 'Deferred Disposition', desc: 'Some courts may offer deferred adjudication even for higher-speed violations. Ask the court clerk about availability.' });
    }
    return alts;
  }

  function buildTrafficSchoolBody(state, rules) {
    var text = '<p>Based on your answers, you are likely eligible for traffic school in ' + escHtml(state || 'your state') + '. This is the best option for most drivers because:</p>';
    text += '<p><strong>No points</strong> added to your driving record.<br>';
    text += '<strong>No insurance increase</strong> (your insurer never sees the ticket).<br>';
    text += '<strong>Saves $1,000 - $4,500</strong> in avoided insurance hikes over 3 years.</p>';

    if (rules) {
      text += '<p>In ' + escHtml(state) + ', you can use traffic school once every ' + rules.tsFreq + ' months.';
      if (rules.pointReductionOnly) {
        text += ' Note: New York traffic school provides a point reduction (up to 4 points) but does not fully dismiss the ticket. You still pay the fine, but it prevents insurance surcharges.';
      }
      text += '</p>';
    }
    return text;
  }

  function buildTrafficSchoolAlts(state, rules) {
    var alts = [
      { title: 'Fight It in Court', desc: 'If you believe you were wrongly cited, you can contest the ticket. If successful, you save the fine and course fees entirely.' }
    ];
    if (rules && rules.trialByDecl) {
      alts.push({ title: 'Trial by Written Declaration (CA)', desc: 'In California, you can contest your ticket by mail without appearing in court. If you lose, you can still request an in-person trial (Trial de Novo).' });
    }
    if (rules && rules.deferred) {
      alts.push({ title: 'Deferred Disposition', desc: 'Ask the court about deferred adjudication, which dismisses the case after a probation period with no course required.' });
    }
    return alts;
  }

  function buildDeferredBody(state) {
    var text = '<p>In ' + escHtml(state) + ', you may be eligible for deferred disposition (also called deferred adjudication). Under this option:</p>';
    text += '<p><strong>No conviction</strong> is entered on your record.<br>';
    text += '<strong>Case dismissed</strong> after a probation period (typically 60-180 days).<br>';
    text += '<strong>Conditions</strong> may include paying court costs and receiving no new violations during probation.</p>';
    text += '<p>Contact your court to ask about deferred disposition eligibility for your specific violation.</p>';
    return text;
  }

  function buildFightBody(state, rules) {
    var text = '<p>Based on your answers, traffic school may not be available for your situation. Your best option is to contest the ticket at a court hearing.</p>';
    text += '<p><strong>Common defenses:</strong></p>';
    text += '<p>';
    text += 'Officer does not appear at the hearing (case often dismissed).<br>';
    text += 'Errors on the citation (wrong date, location, vehicle description).<br>';
    text += 'Missing or obscured traffic signage.<br>';
    text += 'Equipment calibration issues (radar, lidar, camera).<br>';
    text += 'Emergency or necessity defense.</p>';
    if (rules && rules.trialByDecl) {
      text += '<p>In California, you can also try Trial by Written Declaration first. If you lose, you can still request an in-person hearing.</p>';
    }
    return text;
  }

  /* ===== Card Theme Colors ===== */
  var CARD_THEMES = {
    attorney: { bg: '#fef3c7', border: '#f59e0b', label: '#d97706', title: '#92400e', body: '#78350f' },
    fight:    { bg: '#eff6ff', border: '#3b82f6', label: '#2563eb', title: '#1e40af', body: '#1e3a5f' },
    deferred: { bg: '#f5f3ff', border: '#8b5cf6', label: '#7c3aed', title: '#5b21b6', body: '#4c1d95' },
    traffic_school: { bg: '#f0fdf4', border: '#22c55e', label: '#16a34a', title: '#15803d', body: '#166534' }
  };

  function styleResultCard(card, titleEl, bodyEl, recType) {
    if (!card) { return; }
    var theme = CARD_THEMES[recType] || CARD_THEMES['traffic_school'];
    card.style.background = theme.bg;
    card.style.borderColor = theme.border;
    var labelEl = card.querySelector('.quiz-result-label');
    if (labelEl) { labelEl.style.color = theme.label; }
    if (titleEl) { titleEl.style.color = theme.title; }
    if (bodyEl) { bodyEl.style.color = theme.body; }
  }

  function styleResultCta(ctaEl, rec) {
    if (!ctaEl) { return; }
    if (rec.showCta) {
      ctaEl.style.display = 'inline-block';
      ctaEl.textContent = 'Find an Approved Traffic School Course';
      ctaEl.href = '/traffic-school/';
      ctaEl.style.background = '#22c55e';
    } else if (rec.primary === 'attorney') {
      ctaEl.style.display = 'inline-block';
      ctaEl.textContent = 'Find a Traffic Ticket Attorney';
      ctaEl.href = '/traffic-school/';
      ctaEl.style.background = '#f59e0b';
    } else {
      ctaEl.style.display = 'none';
    }
  }

  /* ===== Render Result ===== */
  function showResult() {
    var rec = computeRecommendation();
    if (!rec) { return; }

    /* Hide all steps */
    var steps = document.querySelectorAll('.quiz-step');
    for (var i = 0; i < steps.length; i++) {
      steps[i].classList.remove('active');
    }

    /* Update progress to 100% */
    if (progressFill) { progressFill.style.width = '100%'; }
    if (progressText) { progressText.textContent = 'Complete'; }

    /* Fill result card */
    var titleEl = document.getElementById('resultTitle');
    var bodyEl = document.getElementById('resultBody');
    var ctaEl = document.getElementById('resultCta');
    var resultCard = document.getElementById('resultCard');

    if (titleEl) { titleEl.textContent = rec.title; }
    if (bodyEl) { bodyEl.innerHTML = rec.body; }

    styleResultCard(resultCard, titleEl, bodyEl, rec.primary);
    styleResultCta(ctaEl, rec);
    renderAlternatives(rec.alternatives);
    renderSummary();

    resultDiv.classList.add('active');
  }

  function renderAlternatives(alts) {
    var container = document.getElementById('altCards');
    var section = document.getElementById('resultAlternatives');
    if (!container || !section) { return; }

    if (!alts || alts.length === 0) {
      section.style.display = 'none';
      return;
    }

    section.style.display = 'block';
    container.innerHTML = '';

    for (var i = 0; i < alts.length && i < 5; i++) {
      var card = document.createElement('div');
      card.className = 'quiz-alt-card';
      card.innerHTML = '<h4>' + escHtml(alts[i].title) + '</h4><p>' + escHtml(alts[i].desc) + '</p>';
      container.appendChild(card);
    }
  }

  function renderSummary() {
    var container = document.getElementById('summaryRows');
    if (!container) { return; }

    var violationLabels = {
      'speeding': 'Speeding',
      'red_light': 'Red Light / Stop Signal',
      'stop_sign': 'Stop Sign',
      'cell_phone': 'Cell Phone / Distracted Driving',
      'other': 'Other Moving Violation'
    };

    var rows = [
      ['State', answers.state || 'Not selected'],
      ['Violation', violationLabels[answers.violation] || answers.violation],
    ];

    if (answers.violation === 'speeding') {
      rows.push(['Speed Over Limit', answers.speedOver + ' mph']);
    }

    rows.push(['First Offense (12 mo)', answers.firstOffense === 'yes' ? 'Yes' : 'No']);
    rows.push(['CDL Holder', answers.cdl === 'yes' ? 'Yes' : 'No']);

    container.innerHTML = '';
    for (var i = 0; i < rows.length; i++) {
      var row = document.createElement('div');
      row.className = 'quiz-summary-row';
      row.innerHTML = '<span>' + escHtml(rows[i][0]) + '</span><span>' + escHtml(rows[i][1]) + '</span>';
      container.appendChild(row);
    }
  }

  /* ===== Utility ===== */
  function escHtml(str) {
    if (!str) { return ''; }
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }

  /* ===== Restart ===== */
  function resetQuiz() {
    answers = { state: '', violation: '', speedOver: '', firstOffense: '', cdl: '' };
    currentStep = 1;

    /* Reset selections */
    if (stateSelect) { stateSelect.value = ''; }
    if (nextBtn1) { nextBtn1.disabled = true; }

    var allSelected = document.querySelectorAll('.quiz-option.selected');
    for (var i = 0; i < allSelected.length; i++) {
      allSelected[i].classList.remove('selected');
    }

    resultDiv.classList.remove('active');
    showStep(1);
  }

  /* ===== Event Binding ===== */
  function init() {
    populateStates();

    /* State select */
    if (stateSelect) {
      stateSelect.addEventListener('change', function() {
        answers.state = stateSelect.value;
        if (nextBtn1) { nextBtn1.disabled = !stateSelect.value; }
      });
    }

    /* Next button for step 1 */
    if (nextBtn1) {
      nextBtn1.addEventListener('click', function() {
        if (answers.state) { advanceFromStep(1); }
      });
    }

    /* Option groups */
    setupOptionGroup('violationOptions', 'violation', 2);
    setupOptionGroup('speedOptions', 'speedOver', 3);
    setupOptionGroup('firstOffenseOptions', 'firstOffense', 4);
    setupOptionGroup('cdlOptions', 'cdl', 5);

    /* Back buttons */
    setupBackButtons();

    /* Restart */
    var restartBtn = document.getElementById('quizRestart');
    if (restartBtn) {
      restartBtn.addEventListener('click', resetQuiz);
    }
  }

  /* ===== Boot ===== */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>

---

## How This Tool Works

This quiz analyzes your specific situation based on five factors:

1. **Your state** — Traffic laws and dismissal options vary significantly by state
2. **Violation type** — Some violations qualify for traffic school, others do not
3. **Speed over limit** — Most states cap traffic school eligibility at 25 mph over
4. **Driving history** — First-time offenders have more dismissal options
5. **CDL status** — Commercial drivers face stricter rules and higher stakes

Based on your answers, we recommend the option most likely to result in the best outcome: no points, no insurance increase, and the lowest total cost.

**This tool covers state-specific rules for:** California, Texas, Florida, New York, Georgia, Ohio, Virginia, Illinois, North Carolina, and Pennsylvania. Other states use general best-practice recommendations.

---

*This tool provides general information, not legal advice. Rules change and individual circumstances vary. Consult a licensed attorney for specific legal guidance.*
