# Travelers Home Insurance — Underwriting Risk Factors Reference

**Audience:** Data analysts supporting Personal Lines underwriting  
**Last reviewed:** Q1 2026  
**Owner:** Home Underwriting Product Team

---

## Purpose

This document describes the property and policyholder characteristics that Travelers uses to assess risk and price home insurance policies. It is intended to help analysts understand what drives premium variation and what factors appear in policy and rating data.

This document covers rating factors only. It does not cover eligibility decisions (whether Travelers will write a policy at all) or claim adjudication decisions. Those are handled under separate guidelines.

---

## Primary Rating Factors

These factors have the largest impact on home insurance premium.

### Location

Location is the single most influential factor in home insurance pricing.

- **Geographic risk score** — a composite score based on proximity to fire stations and hydrants, regional weather patterns (wind, hail, freeze), and catastrophe model output. Stored in policy data as `geo_risk_score`.
- **State and territory** — state-level regulation affects allowable rating factors and rate levels. Rates filed and approved in one state do not apply in another.
- **Coastal proximity** — properties within a defined distance of the coast carry higher wind and storm surge risk. Coastal properties in Florida, the Gulf Coast states, and parts of the Northeast are subject to separate coastal rate schedules or coverage limitations.
- **Wildfire Hazard Score** — applied in California, Colorado, Oregon, and other western states. Properties in high wildfire hazard zones may face coverage restrictions or surcharges. Field name: `wildfire_score`.

### Dwelling Characteristics

- **Year built** — older homes carry higher risk for electrical, plumbing, and roof-related losses. Homes built before 1980 are flagged for additional review of roof age and electrical systems.
- **Construction type** — the primary construction material affects both fire risk and wind resistance. Common codes: `FRAME` (wood frame), `MASONRY` (brick or block), `SUPERIOR` (fire-resistive materials). Masonry and superior construction typically receive a credit.
- **Roof age and material** — roof age is one of the strongest predictors of water intrusion and wind claims. Policies on homes with roofs older than 20 years may be subject to a surcharge or an ACV-only roof settlement clause. Roof materials: asphalt shingle (most common), metal, tile, flat/modified bitumen.
- **Square footage** — larger homes cost more to rebuild. Directly related to the dwelling replacement cost calculation.
- **Number of stories** — affects both rebuilding cost and loss exposure.
- **Presence of a pool or trampoline** — liability surcharge applies; both are considered attractive nuisances.
- **Presence of a wood-burning stove or fireplace** — fire risk factor; may require an inspection in some states.

### Coverage Amount and Structure

- **Dwelling limit (Coverage A)** — higher limits mean higher premiums but also higher claims when losses occur. The relationship is not linear — replacement cost per square foot increases with home quality.
- **Deductible** — higher deductibles reduce premium. The standard all-peril deductible is $500 or $1,000. Separate wind/hail deductibles are common in high-wind states and are expressed as a percentage of the dwelling limit (e.g., 1%, 2%, 5%) rather than a flat dollar amount.
- **Endorsements selected** — each endorsement adds to the premium. Water backup is the most commonly added endorsement and is also the most frequently claimed.

### Policyholder Characteristics

- **Years with Travelers (tenure)** — longer-tenured customers have historically lower claim frequency. Loyalty credits apply at 3, 5, and 10 years.
- **Claims history** — prior claims in the past 3–5 years are a surcharge factor. Claims within the past 12 months have the strongest impact. Claims sourced from CLUE (Comprehensive Loss Underwriting Exchange) reports, which include claims from prior insurers.
- **Home purchase date** — new homebuyers (within 12 months of purchase) are typically better risks; they have recently had the property inspected and are engaged with their coverage. New purchase discount applies in most states.
- **Credit-based insurance score** — used in most states (not California, Hawaii, or Massachusetts where it is prohibited by regulation). Correlated with overall claim frequency. Stored as a banded score, not a raw credit score. Field name: `ins_score_band`.

---

## Secondary Rating Factors

These factors have smaller premium impact but appear in the data and affect risk segmentation.

- **Dog breed** — certain breeds (Rottweilers, Pit Bulls, and others listed in the underwriting guidelines) are excluded from liability coverage or trigger a liability surcharge. Field name: `dog_breed_flag`.
- **Home-based business** — if disclosed, triggers review. Standard personal lines policies do not cover business liability; a business owner's policy endorsement or a separate policy may be required.
- **Rental status** — primary residence, seasonal/secondary home, or tenant-occupied rental property. Each carries different risk profiles and is rated separately. Tenant-occupied rentals are typically written on a different policy form (DP-3, not HO-3).
- **Security features** — central station burglar and fire alarms generate a premium credit. Self-monitored systems do not qualify for the same credit.
- **Protective devices** — automatic water shut-off systems (leak detection devices) are increasingly recognized as a credit factor, particularly in states with high water claim frequency.

---

## Fields Commonly Joined to Policy Data for Analysis

When analyzing underwriting data, the following joins are common:

| Data element | Source table | Join key |
|---|---|---|
| Geographic risk score | `geo_risk_dim` | `zip_code` |
| Wildfire score | `wildfire_risk_dim` | `property_id` |
| Insurance score band | `policyholder_dim` | `customer_id` |
| Prior claims (CLUE) | `clue_history` | `customer_id` |
| Roof inspection results | `inspection_results` | `policy_id` |

---

## What This Document Does Not Cover

- Eligibility rules (which properties Travelers will or will not write) — see Underwriting Eligibility Guidelines
- Claim coverage decisions — see Claims Coverage Reference
- State-specific rate filings — see the Rate Filing Archive
- Pricing model outputs (e.g., GLM or ML model scores) — see Actuarial Pricing Documentation
