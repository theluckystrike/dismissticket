---
layout: default
title: "Traffic Ticket True Cost Calculator — See What Your Ticket Really Costs"
description: "Calculate the real cost of your traffic ticket including fines, court fees, and 3 years of insurance increases. See how much you save with traffic school."
permalink: /tools/cost-calculator/
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebApplication",
      "name": "Traffic Ticket True Cost Calculator",
      "description": "Calculate the true 3-year cost of a traffic ticket including fines, fees, and insurance increases. Compare costs with and without traffic school.",
      "url": "https://dismissticket.com/tools/cost-calculator/",
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
          "name": "True Cost Calculator",
          "item": "https://dismissticket.com/tools/cost-calculator/"
        }
      ]
    }
  ]
}
</script>

<style>
/* ===== Calculator Container ===== */
.calc-container {
  max-width: 960px;
  margin: 0 auto;
  padding: 0;
}

.calc-intro {
  text-align: center;
  margin-bottom: 32px;
}

.calc-intro p {
  font-size: 17px;
  color: #6b7280;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

/* ===== Input Section ===== */
.calc-inputs {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 28px;
  margin-bottom: 32px;
}

.calc-inputs h2 {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 24px;
  color: #111827;
}

.calc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.calc-field {
  display: flex;
  flex-direction: column;
}

.calc-field.full-width {
  grid-column: 1 / -1;
}

.calc-label {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 6px;
}

.calc-label-hint {
  font-size: 12px;
  color: #9ca3af;
  font-weight: 400;
}

.calc-select,
.calc-input {
  width: 100%;
  padding: 14px 16px;
  font-size: 16px;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  background: #fff;
  color: #1f2937;
  font-family: inherit;
  box-sizing: border-box;
}

.calc-select {
  appearance: none;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20' fill='%236b7280'%3E%3Cpath fill-rule='evenodd' d='M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
  padding-right: 40px;
  cursor: pointer;
}

.calc-select:focus,
.calc-input:focus {
  outline: none;
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
}

/* Speed Slider */
.calc-slider-wrap {
  display: flex;
  align-items: center;
  gap: 16px;
}

.calc-slider {
  flex: 1;
  -webkit-appearance: none;
  appearance: none;
  height: 8px;
  background: #e5e7eb;
  border-radius: 4px;
  outline: none;
}

.calc-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #2563eb;
  cursor: pointer;
  border: 3px solid #fff;
  box-shadow: 0 1px 4px rgba(0,0,0,0.2);
}

.calc-slider::-moz-range-thumb {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #2563eb;
  cursor: pointer;
  border: 3px solid #fff;
  box-shadow: 0 1px 4px rgba(0,0,0,0.2);
}

.calc-slider-value {
  min-width: 80px;
  text-align: center;
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
  background: #fff;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  padding: 8px 12px;
}

/* ===== Results Section ===== */
.calc-results {
  display: none;
  animation: calcFadeIn 0.4s ease;
}

.calc-results.visible {
  display: block;
}

@keyframes calcFadeIn {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Savings Banner */
.calc-savings-banner {
  background: linear-gradient(135deg, #059669 0%, #10b981 100%);
  border-radius: 16px;
  padding: 28px;
  text-align: center;
  margin-bottom: 28px;
  color: #fff;
}

.calc-savings-label {
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  opacity: 0.9;
  margin-bottom: 4px;
}

.calc-savings-amount {
  font-size: 48px;
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 8px;
}

.calc-savings-sub {
  font-size: 15px;
  opacity: 0.85;
}

/* Comparison Cards */
.calc-compare {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 28px;
}

.calc-card {
  border-radius: 16px;
  padding: 24px;
  border: 2px solid;
}

.calc-card-bad {
  background: #fef2f2;
  border-color: #ef4444;
}

.calc-card-good {
  background: #f0fdf4;
  border-color: #22c55e;
}

.calc-card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 20px;
}

.calc-card-icon {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 700;
  flex-shrink: 0;
}

.calc-card-bad .calc-card-icon {
  background: #fee2e2;
  color: #dc2626;
}

.calc-card-good .calc-card-icon {
  background: #dcfce7;
  color: #16a34a;
}

.calc-card-title {
  font-size: 16px;
  font-weight: 700;
}

.calc-card-bad .calc-card-title {
  color: #991b1b;
}

.calc-card-good .calc-card-title {
  color: #166534;
}

.calc-line {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 8px 0;
  border-bottom: 1px solid rgba(0,0,0,0.06);
}

.calc-line:last-child {
  border-bottom: none;
}

.calc-line-label {
  font-size: 14px;
  color: #6b7280;
}

.calc-line-value {
  font-size: 14px;
  font-weight: 600;
  color: #1f2937;
}

.calc-line-total {
  padding-top: 12px;
  margin-top: 4px;
  border-top: 2px solid rgba(0,0,0,0.1);
  border-bottom: none;
}

.calc-line-total .calc-line-label {
  font-size: 16px;
  font-weight: 700;
  color: #1f2937;
}

.calc-line-total .calc-line-value {
  font-size: 22px;
  font-weight: 800;
}

.calc-card-bad .calc-line-total .calc-line-value {
  color: #dc2626;
}

.calc-card-good .calc-line-total .calc-line-value {
  color: #16a34a;
}

/* CTA */
.calc-cta-section {
  text-align: center;
  padding: 24px;
  background: #f0fdf4;
  border: 2px solid #22c55e;
  border-radius: 16px;
  margin-bottom: 28px;
}

.calc-cta-section p {
  font-size: 16px;
  color: #166534;
  margin-bottom: 16px;
  line-height: 1.5;
}

.calc-cta-btn {
  display: inline-block;
  padding: 14px 32px;
  background: #22c55e;
  color: #fff;
  font-size: 16px;
  font-weight: 700;
  border-radius: 10px;
  text-decoration: none;
  transition: background 0.15s;
}

.calc-cta-btn:hover {
  background: #16a34a;
  color: #fff;
  text-decoration: none;
}

/* Breakdown Table */
.calc-breakdown {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 28px;
}

.calc-breakdown h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 16px;
  color: #111827;
}

.calc-breakdown-row {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid #e5e7eb;
  font-size: 14px;
}

.calc-breakdown-row:last-child {
  border-bottom: none;
}

.calc-breakdown-label {
  color: #6b7280;
}

.calc-breakdown-value {
  font-weight: 600;
  color: #1f2937;
}

.calc-disclaimer {
  font-size: 13px;
  color: #9ca3af;
  line-height: 1.5;
  margin-top: 24px;
}

/* ===== Mobile ===== */
@media (max-width: 640px) {
  .calc-grid {
    grid-template-columns: 1fr;
  }
  .calc-compare {
    grid-template-columns: 1fr;
  }
  .calc-savings-amount {
    font-size: 36px;
  }
  .calc-inputs {
    padding: 20px;
  }
  .calc-card {
    padding: 20px;
  }
}
</style>

# Traffic Ticket True Cost Calculator

<div class="calc-container">
  <div class="calc-intro">
    <p>A traffic ticket costs far more than the fine. Calculate your real 3-year cost including insurance increases, and see how much traffic school can save you.</p>
  </div>

  <!-- Inputs -->
  <div class="calc-inputs">
    <h2>Enter Your Ticket Details</h2>
    <div class="calc-grid">

      <div class="calc-field">
        <label class="calc-label" for="calcState">State</label>
        <select class="calc-select" id="calcState">
          <option value="">Select your state...</option>
        </select>
      </div>

      <div class="calc-field">
        <label class="calc-label" for="calcViolation">Violation Type</label>
        <select class="calc-select" id="calcViolation">
          <option value="">Select violation...</option>
          <option value="speeding">Speeding</option>
          <option value="red_light">Red Light / Stop Signal</option>
          <option value="stop_sign">Stop Sign</option>
          <option value="cell_phone">Cell Phone / Distracted Driving</option>
          <option value="other">Other Moving Violation</option>
        </select>
      </div>

      <div class="calc-field" id="speedField">
        <label class="calc-label" for="calcSpeed">Speed Over Limit <span class="calc-label-hint">(mph)</span></label>
        <div class="calc-slider-wrap">
          <input type="range" class="calc-slider" id="calcSpeed" min="1" max="50" value="12">
          <div class="calc-slider-value" id="calcSpeedDisplay">12 mph</div>
        </div>
      </div>

      <div class="calc-field">
        <label class="calc-label" for="calcPremium">Annual Insurance Premium <span class="calc-label-hint">(current)</span></label>
        <input type="text" class="calc-input" id="calcPremium" value="1,800" inputmode="numeric" placeholder="1,800">
      </div>

    </div>
  </div>

  <!-- Results -->
  <div class="calc-results" id="calcResults">

    <!-- Savings Banner -->
    <div class="calc-savings-banner">
      <div class="calc-savings-label">Estimated 3-Year Savings with Traffic School</div>
      <div class="calc-savings-amount" id="calcSavingsAmount">$0</div>
      <div class="calc-savings-sub">compared to paying the ticket and accepting points</div>
    </div>

    <!-- Side-by-side Comparison -->
    <div class="calc-compare">

      <!-- Without Traffic School -->
      <div class="calc-card calc-card-bad">
        <div class="calc-card-header">
          <div class="calc-card-icon">X</div>
          <div class="calc-card-title">Without Traffic School</div>
        </div>
        <div class="calc-line">
          <span class="calc-line-label">Base fine</span>
          <span class="calc-line-value" id="rFine">$0</span>
        </div>
        <div class="calc-line">
          <span class="calc-line-label">Court fees &amp; surcharges</span>
          <span class="calc-line-value" id="rCourtFees">$0</span>
        </div>
        <div class="calc-line">
          <span class="calc-line-label">Insurance increase (3 yr)</span>
          <span class="calc-line-value" id="rInsurance">$0</span>
        </div>
        <div class="calc-line">
          <span class="calc-line-label">Points on license</span>
          <span class="calc-line-value" id="rPoints">0</span>
        </div>
        <div class="calc-line calc-line-total">
          <span class="calc-line-label">Total 3-Year Cost</span>
          <span class="calc-line-value" id="rTotalBad">$0</span>
        </div>
      </div>

      <!-- With Traffic School -->
      <div class="calc-card calc-card-good">
        <div class="calc-card-header">
          <div class="calc-card-icon">&#10003;</div>
          <div class="calc-card-title">With Traffic School</div>
        </div>
        <div class="calc-line">
          <span class="calc-line-label">Course fee</span>
          <span class="calc-line-value" id="rCourseFee">$0</span>
        </div>
        <div class="calc-line">
          <span class="calc-line-label">Court admin fee</span>
          <span class="calc-line-value" id="rAdminFee">$0</span>
        </div>
        <div class="calc-line">
          <span class="calc-line-label">Ticket fine</span>
          <span class="calc-line-value" id="rTsFine">$0</span>
        </div>
        <div class="calc-line">
          <span class="calc-line-label">Insurance increase (3 yr)</span>
          <span class="calc-line-value" id="rTsInsurance">$0</span>
        </div>
        <div class="calc-line">
          <span class="calc-line-label">Points on license</span>
          <span class="calc-line-value" id="rTsPoints">0</span>
        </div>
        <div class="calc-line calc-line-total">
          <span class="calc-line-label">Total 3-Year Cost</span>
          <span class="calc-line-value" id="rTotalGood">$0</span>
        </div>
      </div>

    </div>

    <!-- CTA -->
    <div class="calc-cta-section" id="calcCtaSection">
      <p><strong>Traffic school dismisses your ticket, prevents points, and keeps your insurance rates down.</strong> Most online courses take 4-8 hours and cost under $50.</p>
      <a class="calc-cta-btn" href="/traffic-school/">Find an Approved Traffic School Course</a>
    </div>

    <!-- Insurance Breakdown -->
    <div class="calc-breakdown" id="calcBreakdown">
      <h3>Insurance Impact Breakdown</h3>
      <div id="insuranceRows"></div>
    </div>

    <p class="calc-disclaimer">
      Estimates are based on average fine ranges and a national average insurance increase of 24% for moving violations. Actual costs vary by county, judge, insurance provider, driving history, and other factors. This calculator provides general estimates for informational purposes only.
    </p>

  </div>
</div>

<script>
(function() {
  'use strict';

  /* ===== State List ===== */
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

  /* ===== State Fine & Fee Data (10 supported states) ===== */
  /* Each state: base fines by violation and speed tier, court fees, insurance multiplier, points, traffic school info */
  var STATE_DATA = {
    'California': {
      fines: {
        speeding: [35, 70, 100, 200],   /* tiers: 1-10, 11-20, 21-30, 31+ over */
        red_light: [100, 100, 100, 100],
        stop_sign: [35, 35, 35, 35],
        cell_phone: [20, 50, 50, 50],   /* first/subsequent */
        other: [35, 70, 100, 100]
      },
      courtFees: 235,         /* CA penalty assessments roughly triple the base */
      feeMultiplier: 4.0,     /* Total = base * feeMultiplier (includes fees) */
      insurancePct: 0.24,
      points: { speeding: [1,1,2,2], red_light: 1, stop_sign: 1, cell_phone: 1, other: 1 },
      tsCourseFee: 30,
      tsAdminFee: 65,
      tsFineOwed: true,       /* CA: you still pay the full fine even with traffic school */
      tsPointReductionOnly: false
    },
    'Texas': {
      fines: {
        speeding: [150, 200, 250, 300],
        red_light: [200, 200, 200, 200],
        stop_sign: [150, 150, 150, 150],
        cell_phone: [100, 200, 200, 200],
        other: [150, 200, 200, 200]
      },
      courtFees: 105,
      feeMultiplier: 1.0,     /* TX fines are inclusive */
      insurancePct: 0.22,
      points: { speeding: [2,2,3,3], red_light: 2, stop_sign: 2, cell_phone: 2, other: 2 },
      tsCourseFee: 25,
      tsAdminFee: 10,
      tsFineOwed: false,      /* TX: fine dismissed, pay small court cost */
      tsPointReductionOnly: false
    },
    'Florida': {
      fines: {
        speeding: [129, 204, 254, 379],
        red_light: [158, 158, 158, 158],
        stop_sign: [129, 129, 129, 129],
        cell_phone: [129, 179, 179, 179],
        other: [129, 154, 154, 154]
      },
      courtFees: 0,           /* FL fines include court costs */
      feeMultiplier: 1.0,
      insurancePct: 0.25,
      points: { speeding: [3,3,4,4], red_light: 3, stop_sign: 3, cell_phone: 3, other: 3 },
      tsCourseFee: 25,
      tsAdminFee: 0,
      tsFineOwed: true,       /* FL: fine owed even with elect-traffic-school */
      tsPointReductionOnly: false
    },
    'New York': {
      fines: {
        speeding: [150, 300, 600, 600],
        red_light: [225, 225, 225, 225],
        stop_sign: [150, 150, 150, 150],
        cell_phone: [200, 250, 250, 250],
        other: [150, 200, 200, 200]
      },
      courtFees: 93,
      feeMultiplier: 1.0,
      insurancePct: 0.28,
      points: { speeding: [3,4,6,8], red_light: 3, stop_sign: 3, cell_phone: 5, other: 3 },
      tsCourseFee: 35,
      tsAdminFee: 0,
      tsFineOwed: true,       /* NY: fine still owed, course reduces points by up to 4 */
      tsPointReductionOnly: true
    },
    'Georgia': {
      fines: {
        speeding: [150, 250, 500, 750],
        red_light: [200, 200, 200, 200],
        stop_sign: [150, 150, 150, 150],
        cell_phone: [50, 100, 100, 100],
        other: [150, 200, 200, 200]
      },
      courtFees: 60,
      feeMultiplier: 1.0,
      insurancePct: 0.22,
      points: { speeding: [2,3,4,6], red_light: 3, stop_sign: 3, cell_phone: 1, other: 2 },
      tsCourseFee: 30,
      tsAdminFee: 50,
      tsFineOwed: false,
      tsPointReductionOnly: false
    },
    'Ohio': {
      fines: {
        speeding: [150, 200, 250, 300],
        red_light: [150, 150, 150, 150],
        stop_sign: [150, 150, 150, 150],
        cell_phone: [150, 150, 150, 150],
        other: [150, 150, 150, 150]
      },
      courtFees: 110,
      feeMultiplier: 1.0,
      insurancePct: 0.20,
      points: { speeding: [2,2,4,4], red_light: 2, stop_sign: 2, cell_phone: 2, other: 2 },
      tsCourseFee: 30,
      tsAdminFee: 25,
      tsFineOwed: false,
      tsPointReductionOnly: false
    },
    'Virginia': {
      fines: {
        speeding: [100, 200, 350, 500],
        red_light: [200, 200, 200, 200],
        stop_sign: [100, 100, 100, 100],
        cell_phone: [125, 250, 250, 250],
        other: [100, 150, 150, 150]
      },
      courtFees: 91,
      feeMultiplier: 1.0,
      insurancePct: 0.23,
      points: { speeding: [3,4,6,6], red_light: 4, stop_sign: 3, cell_phone: 3, other: 3 },
      tsCourseFee: 35,
      tsAdminFee: 30,
      tsFineOwed: false,
      tsPointReductionOnly: false
    },
    'Illinois': {
      fines: {
        speeding: [120, 140, 160, 250],
        red_light: [100, 100, 100, 100],
        stop_sign: [120, 120, 120, 120],
        cell_phone: [75, 100, 100, 100],
        other: [120, 120, 120, 120]
      },
      courtFees: 80,
      feeMultiplier: 1.0,
      insurancePct: 0.21,
      points: { speeding: [5,15,20,50], red_light: 20, stop_sign: 5, cell_phone: 20, other: 5 },
      tsCourseFee: 25,
      tsAdminFee: 25,
      tsFineOwed: false,
      tsPointReductionOnly: false
    },
    'North Carolina': {
      fines: {
        speeding: [100, 180, 250, 350],
        red_light: [150, 150, 150, 150],
        stop_sign: [100, 100, 100, 100],
        cell_phone: [100, 100, 100, 100],
        other: [100, 150, 150, 150]
      },
      courtFees: 190,
      feeMultiplier: 1.0,
      insurancePct: 0.25,
      points: { speeding: [2,3,4,4], red_light: 3, stop_sign: 3, cell_phone: 3, other: 2 },
      tsCourseFee: 25,
      tsAdminFee: 50,
      tsFineOwed: false,
      tsPointReductionOnly: false
    },
    'Pennsylvania': {
      fines: {
        speeding: [45, 100, 135, 200],
        red_light: [100, 100, 100, 100],
        stop_sign: [25, 25, 25, 25],
        cell_phone: [50, 50, 50, 50],
        other: [25, 50, 50, 50]
      },
      courtFees: 130,
      feeMultiplier: 1.0,
      insurancePct: 0.22,
      points: { speeding: [2,3,4,5], red_light: 3, stop_sign: 3, cell_phone: 0, other: 2 },
      tsCourseFee: 0,       /* PA does not have standard traffic school dismissal */
      tsAdminFee: 0,
      tsFineOwed: true,
      tsPointReductionOnly: true,
      noTrafficSchool: true
    }
  };

  /* Fallback for states without specific data */
  var DEFAULT_DATA = {
    fines: {
      speeding: [130, 200, 275, 400],
      red_light: [175, 175, 175, 175],
      stop_sign: [130, 130, 130, 130],
      cell_phone: [100, 150, 150, 150],
      other: [130, 175, 175, 175]
    },
    courtFees: 100,
    feeMultiplier: 1.0,
    insurancePct: 0.24,
    points: { speeding: [2,3,4,4], red_light: 3, stop_sign: 3, cell_phone: 2, other: 2 },
    tsCourseFee: 30,
    tsAdminFee: 40,
    tsFineOwed: false,
    tsPointReductionOnly: false
  };

  /* ===== DOM References ===== */
  var stateSelect = document.getElementById('calcState');
  var violationSelect = document.getElementById('calcViolation');
  var speedSlider = document.getElementById('calcSpeed');
  var speedDisplay = document.getElementById('calcSpeedDisplay');
  var premiumInput = document.getElementById('calcPremium');
  var resultsDiv = document.getElementById('calcResults');
  var speedField = document.getElementById('speedField');

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

  /* ===== Speed Tier Mapping ===== */
  function getSpeedTier(mph) {
    if (mph <= 0) { return 0; }
    if (mph <= 10) { return 0; }
    if (mph <= 20) { return 1; }
    if (mph <= 30) { return 2; }
    return 3;
  }

  /* ===== Parse Currency Input ===== */
  function parseCurrency(str) {
    if (!str) { return 0; }
    var cleaned = str.replace(/[^0-9.]/g, '');
    var val = parseFloat(cleaned);
    if (isNaN(val) || val < 0) { return 0; }
    if (val > 100000) { return 100000; } /* bound */
    return val;
  }

  /* ===== Format Currency ===== */
  function formatCurrency(num) {
    if (typeof num !== 'number' || isNaN(num)) { return '$0'; }
    var rounded = Math.round(num);
    return '$' + rounded.toLocaleString('en-US');
  }

  /* ===== Get Points (handles array or scalar) ===== */
  function getPoints(pointsData, violation, speedTier) {
    if (!pointsData) { return 2; }
    var val = pointsData[violation];
    if (val === undefined || val === null) { val = pointsData['other'] || 2; }
    if (Array.isArray(val)) {
      var idx = Math.min(speedTier, val.length - 1);
      return val[idx] || 0;
    }
    return val || 0;
  }

  /* ===== Get Fine ===== */
  function getFine(fineData, violation, speedTier) {
    if (!fineData) { return 150; }
    var fines = fineData[violation];
    if (!fines) { fines = fineData['other'] || [150, 200, 250, 300]; }
    var idx = Math.min(speedTier, fines.length - 1);
    return fines[idx] || 150;
  }

  /* ===== Compute Severity Multiplier ===== */
  function getSeverityMultiplier(violation, tier) {
    if (violation !== 'speeding') { return 1.0; }
    if (tier === 1) { return 1.15; }
    if (tier === 2) { return 1.40; }
    if (tier >= 3) { return 1.75; }
    return 1.0;
  }

  /* ===== Compute Ticket Costs ===== */
  function computeCosts(data, violation, tier, premium) {
    var baseFine = getFine(data.fines, violation, tier);
    var totalFine = baseFine;
    if (data.feeMultiplier && data.feeMultiplier > 1) {
      totalFine = Math.round(baseFine * data.feeMultiplier);
    }
    var courtFees = (data.feeMultiplier > 1) ? 0 : (data.courtFees || 0);
    var points = getPoints(data.points, violation, tier);
    var insurancePct = data.insurancePct || 0.24;
    var sevMult = getSeverityMultiplier(violation, tier);
    var annualIncrease = premium * insurancePct * sevMult;
    var insurance3yr = Math.round(annualIncrease * 3);
    var totalBad = totalFine + courtFees + insurance3yr;

    /* Traffic school costs */
    var courseFee = data.tsCourseFee || 30;
    var adminFee = data.tsAdminFee || 0;
    var tsFine = data.tsFineOwed ? totalFine : 0;
    var tsInsurance = data.tsPointReductionOnly ? Math.round(insurance3yr * 0.4) : 0;
    var totalGood = courseFee + adminFee + tsFine + tsInsurance;
    var savings = Math.max(totalBad - totalGood, 0);

    return {
      totalFine: totalFine, courtFees: courtFees, points: points,
      insurance3yr: insurance3yr, totalBad: totalBad,
      courseFee: courseFee, adminFee: adminFee, tsFine: tsFine,
      tsInsurance: tsInsurance, totalGood: totalGood, savings: savings,
      annualIncrease: annualIncrease, insurancePct: insurancePct, sevMult: sevMult
    };
  }

  /* ===== Render Computed Results ===== */
  function renderResults(c, data, premium) {
    setText('calcSavingsAmount', formatCurrency(c.savings));
    setText('rFine', formatCurrency(c.totalFine));
    setText('rCourtFees', formatCurrency(c.courtFees));
    setText('rInsurance', formatCurrency(c.insurance3yr));
    setText('rPoints', c.points + (c.points === 1 ? ' point' : ' points'));
    setText('rTotalBad', formatCurrency(c.totalBad));

    setText('rCourseFee', formatCurrency(c.courseFee));
    setText('rAdminFee', formatCurrency(c.adminFee));
    setText('rTsFine', c.tsFine > 0 ? formatCurrency(c.tsFine) : '$0 (waived)');
    setText('rTsInsurance', formatCurrency(c.tsInsurance));
    setText('rTsPoints', data.tsPointReductionOnly ? 'Reduced' : '0 points');
    setText('rTotalGood', formatCurrency(c.totalGood));

    renderInsuranceBreakdown(premium, c.annualIncrease, c.insurancePct, c.sevMult);

    var ctaSection = document.getElementById('calcCtaSection');
    if (ctaSection) {
      if (data.noTrafficSchool) {
        ctaSection.innerHTML = '<p><strong>Pennsylvania does not offer standard traffic school for ticket dismissal.</strong> Consider fighting the ticket in court or consulting a traffic ticket attorney to reduce charges and minimize insurance impact.</p>';
      } else {
        ctaSection.innerHTML = '<p><strong>Traffic school dismisses your ticket, prevents points, and keeps your insurance rates down.</strong> Most online courses take 4-8 hours and cost under $50.</p><a class="calc-cta-btn" href="/traffic-school/">Find an Approved Traffic School Course</a>';
      }
    }
  }

  /* ===== Calculate (orchestrator) ===== */
  function calculate() {
    var state = stateSelect ? stateSelect.value : '';
    var violation = violationSelect ? violationSelect.value : '';
    var speedMph = speedSlider ? parseInt(speedSlider.value, 10) : 12;
    var premium = parseCurrency(premiumInput ? premiumInput.value : '1800');

    if (!state || !violation) {
      if (resultsDiv) { resultsDiv.classList.remove('visible'); }
      return;
    }

    var data = STATE_DATA[state] || DEFAULT_DATA;
    var tier = (violation === 'speeding') ? getSpeedTier(speedMph) : 0;
    var costs = computeCosts(data, violation, tier, premium);

    renderResults(costs, data, premium);
    if (resultsDiv) { resultsDiv.classList.add('visible'); }
  }

  function renderInsuranceBreakdown(premium, annualIncrease, basePct, sevMult) {
    var container = document.getElementById('insuranceRows');
    if (!container) { return; }

    var effectivePct = Math.round(basePct * sevMult * 100);
    var rows = [
      ['Current annual premium', formatCurrency(premium)],
      ['Estimated rate increase', effectivePct + '%'],
      ['Annual increase amount', formatCurrency(Math.round(annualIncrease))],
      ['Duration of increase', '3 years (industry standard)'],
      ['Total 3-year insurance cost', formatCurrency(Math.round(annualIncrease * 3))]
    ];

    container.innerHTML = '';
    for (var i = 0; i < rows.length; i++) {
      var row = document.createElement('div');
      row.className = 'calc-breakdown-row';
      row.innerHTML = '<span class="calc-breakdown-label">' + escHtml(rows[i][0]) + '</span><span class="calc-breakdown-value">' + escHtml(rows[i][1]) + '</span>';
      container.appendChild(row);
    }
  }

  /* ===== Utility ===== */
  function setText(id, text) {
    var el = document.getElementById(id);
    if (el) { el.textContent = text; }
  }

  function escHtml(str) {
    if (!str) { return ''; }
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }

  /* ===== Debounce ===== */
  function debounce(fn, delay) {
    var timer = null;
    return function() {
      if (timer !== null) { clearTimeout(timer); }
      timer = setTimeout(function() {
        timer = null;
        fn();
      }, delay);
    };
  }

  /* ===== Speed Field Visibility ===== */
  function updateSpeedFieldVisibility() {
    if (!speedField || !violationSelect) { return; }
    if (violationSelect.value === 'speeding') {
      speedField.style.display = '';
    } else {
      speedField.style.display = 'none';
    }
  }

  /* ===== Premium Input Formatting ===== */
  function formatPremiumInput() {
    if (!premiumInput) { return; }
    var val = parseCurrency(premiumInput.value);
    if (val > 0) {
      premiumInput.value = val.toLocaleString('en-US');
    }
  }

  /* ===== Event Binding ===== */
  function init() {
    populateStates();

    var debouncedCalc = debounce(calculate, 150);

    if (stateSelect) {
      stateSelect.addEventListener('change', calculate);
    }

    if (violationSelect) {
      violationSelect.addEventListener('change', function() {
        updateSpeedFieldVisibility();
        calculate();
      });
    }

    if (speedSlider) {
      speedSlider.addEventListener('input', function() {
        if (speedDisplay) {
          speedDisplay.textContent = speedSlider.value + ' mph';
        }
        debouncedCalc();
      });
    }

    if (premiumInput) {
      premiumInput.addEventListener('input', debouncedCalc);
      premiumInput.addEventListener('blur', function() {
        formatPremiumInput();
        calculate();
      });
    }

    /* Initial state */
    updateSpeedFieldVisibility();
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

## How This Calculator Works

This calculator estimates the **true 3-year cost** of a traffic ticket by accounting for three cost categories most people overlook:

### 1. The Fine Is Just the Beginning

The base fine on your ticket is typically the smallest part of the total cost. Court fees, surcharges, and penalty assessments can double or triple the amount you actually owe.

### 2. Insurance Increases Are the Real Cost

A single moving violation raises your insurance premium by **20-30% for 3 years** on average. On a $1,800/year policy, that is $1,296 to $1,944 in extra premiums -- far more than the fine itself.

Insurance increases are higher for:
- Speeding violations (especially 20+ mph over)
- Multiple violations within 3 years
- Younger drivers (under 25)
- Drivers with prior claims

### 3. Traffic School Prevents the Insurance Hit

When you complete traffic school, your ticket is dismissed (or adjudication is withheld). Your insurance company never sees the violation, so your rates stay the same. The course typically costs $15-50 and takes 4-8 hours.

**Data sources:** Fine amounts are based on published state fee schedules and court records. Insurance increase percentages are based on national averages from insurance industry studies. Actual costs vary by county, court, and insurance provider.

---

*This calculator provides estimates for informational purposes only. Actual fines, fees, and insurance impacts vary by jurisdiction and individual circumstances. Consult your court and insurance provider for exact amounts.*
