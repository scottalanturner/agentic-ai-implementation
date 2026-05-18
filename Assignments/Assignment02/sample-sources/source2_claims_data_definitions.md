# Travelers Home Claims — Data Definitions and Key Metrics

**Audience:** Data analysts in Personal Lines  
**Last reviewed:** Q1 2026  
**Owner:** Claims Analytics Team

---

## Overview

This document defines the fields, statuses, and metrics used in Travelers home insurance claims reporting. It is the authoritative reference for claim data questions. Questions about coverage eligibility, underwriting decisions, or policy terms are out of scope for this document — see the Coverage Types Reference.

---

## Claim Lifecycle and Status Codes

A home insurance claim moves through a defined set of statuses from the time it is reported to the time it is closed. The status codes used in our data systems are:

| Status Code | Label | Meaning |
|-------------|-------|---------|
| `OPEN` | Open | Claim has been reported and is being actively worked |
| `PEND` | Pending | Claim is waiting on information from the customer, a vendor, or an inspector |
| `RSRV` | Reserved | An initial reserve has been set; payment has not yet been made |
| `PAID` | Paid | At least one payment has been made; claim may still be open |
| `CLSD` | Closed | All payments made, claim is complete; no further activity expected |
| `VOID` | Void | Claim was entered in error or is a duplicate |
| `DENY` | Denied | Claim was reviewed and determined to be not covered |

A claim can move between OPEN, PEND, and RSRV multiple times before reaching PAID or CLSD. A CLSD claim can be reopened if new information or a supplemental damage assessment is submitted.

---

## Core Claim Data Fields

### Claim Identification

- **`claim_id`** — unique identifier for the claim. Format: TRV-YYYY-XXXXXXXX. Never reused.
- **`policy_id`** — the policy record the claim is filed against. A single policy can have multiple claims.
- **`reported_date`** — the date the claim was first reported to Travelers, regardless of when the loss occurred.
- **`loss_date`** — the date the covered event occurred. For storms, this is the storm date. For theft, it is the date the theft was discovered, not necessarily the date it occurred.

### Loss Categorization

- **`peril_code`** — the primary cause of loss. Common codes in the home book:
  - `WIND` — wind and hail
  - `FIRE` — fire and smoke
  - `WATER_INT` — internal water (burst pipes, appliance leaks, water backup)
  - `WATER_EXT` — external water (surface flooding — note: typically DENIED under standard HO-3)
  - `THEFT` — theft or burglary
  - `LIAB` — liability claim
  - `OTHER` — does not fit a primary category; requires manual review

- **`coverage_triggered`** — which coverage letter was activated (A, B, C, D, E, or F). A single claim can trigger multiple coverages.

### Financial Fields

- **`initial_reserve`** — the first dollar estimate of how much the claim will cost. Set by the adjuster within 24–48 hours of assignment. Not a payment; it is a liability estimate for financial reporting.
- **`total_incurred`** — current total cost of the claim: all payments made plus the remaining open reserve.
- **`total_paid`** — total dollars actually paid out on the claim as of the reporting date.
- **`recovery_amount`** — money recovered through subrogation (suing a third party who caused the loss) or salvage. Reduces net loss.
- **`deductible_applied`** — the deductible amount collected from the customer, which reduces the payment Travelers makes.

### Timing Fields

- **`days_to_first_contact`** — number of days from `reported_date` to the first adjuster contact with the customer. Target is 1 business day.
- **`days_to_close`** — number of days from `reported_date` to `CLSD` status. A key cycle-time metric.
- **`reopen_count`** — number of times the claim was reopened after reaching CLSD status.

---

## Key Performance Metrics Used in Home Claims Reporting

### Loss Ratio

The loss ratio is the core profitability metric for the home line.

**Formula:** Loss Ratio = (Total Incurred Losses + Loss Adjustment Expenses) / Earned Premium

A loss ratio below 60% is generally healthy for home. During catastrophe years (major hurricane or wildfire season), the loss ratio can spike above 100%, meaning we pay out more than we collect in premium.

**Where it appears in data:** calculated at the region, state, and book level. Not stored at the claim level — it requires aggregating across all claims and joining to premium data.

### Severity

Average dollar amount paid per closed claim.

**Formula:** Severity = Total Paid / Number of Closed Claims

Severity varies significantly by peril. Fire claims are typically the highest severity. Liability claims have high variance — most are small, but a severe injury can produce a six-figure payment.

### Frequency

Number of claims per 100 (or 1,000) insured homes over a period.

**Formula:** Frequency = (Claim Count / Earned House Years) × 100

Earned house years = the total number of home-years of coverage in force during the period. A policy in force for a full year = 1.0 house year.

### Cycle Time

Average `days_to_close` across a set of claims. Tracked by region, adjuster team, and peril type. Long cycle times are correlated with lower customer satisfaction scores and higher supplemental claim rates.

---

## Catastrophe (CAT) Claims

Claims tied to a declared catastrophe event are flagged with a **`cat_code`** in the data. CAT claims are handled differently:

- They are assigned to dedicated CAT teams, not standard adjusters.
- Cycle time targets are extended.
- CAT claims are excluded from many standard performance reports to avoid distorting non-CAT metrics.
- CAT codes are assigned by the Claims Operations team using industry-standard definitions (ISO/PCS catastrophe declarations).

If a claim has a `cat_code` value, it should be excluded from frequency, severity, and cycle time comparisons against non-CAT baselines unless the analysis is specifically about catastrophe performance.

---

## Common Data Quality Issues

These issues appear regularly in the home claims dataset and affect analysis results:

1. **`loss_date` after `reported_date`** — data entry error; should be flagged and reviewed.
2. **Zero `initial_reserve` on non-voided claims** — sometimes occurs when the claim was recorded before the adjuster completed the initial review. These are not yet reliable for reserve analysis.
3. **`peril_code = OTHER` at high rates** — if more than 10–15% of claims in a segment show OTHER, it usually indicates a classification issue, not an unusual loss pattern.
4. **Duplicate `claim_id` entries** — rare but occurs after system migrations. One record will have `VOID` status.
