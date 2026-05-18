# Travelers Home Insurance — Coverage Types Reference

**Audience:** Internal reference for data analysts and customer-facing staff  
**Last reviewed:** Q1 2026  
**Owner:** Personal Lines Product Team

---

## What a Standard Home Policy Covers

A standard Travelers homeowners policy (HO-3) includes six coverage types. Each has its own limit and is tracked separately in our policy data systems.

### Coverage A — Dwelling

Pays to repair or rebuild the physical structure of the home if it is damaged by a covered event. Covered events include fire, wind, hail, lightning, and vandalism. Flooding and earthquakes are not covered under a standard HO-3 — those require separate endorsements or separate policies.

The dwelling limit is set at replacement cost value (RCV), not market value. Replacement cost is what it would cost to rebuild the home at today's labor and material prices. Market value includes the land and reflects buyer demand — it is not the right number for insurance purposes.

**Common data field:** `dwelling_limit` — the Coverage A limit on the policy record.

### Coverage B — Other Structures

Covers detached structures on the property: fences, sheds, detached garages, and similar. The limit defaults to 10% of the Coverage A dwelling limit unless the customer requests a higher amount.

**Common data field:** `other_structures_limit`

### Coverage C — Personal Property

Covers the contents of the home — furniture, clothing, electronics, appliances. The standard limit is 50% of the dwelling limit. High-value items (jewelry, art, musical instruments) may require a scheduled personal property endorsement to be fully covered.

Personal property is typically insured at actual cash value (ACV) unless the customer upgrades to replacement cost coverage. ACV deducts depreciation; replacement cost does not.

**Common data field:** `personal_property_limit`, `personal_property_valuation` (ACV or RCV)

### Coverage D — Loss of Use

If a covered loss makes the home temporarily uninhabitable, Coverage D pays for additional living expenses — hotel stays, restaurant meals above normal food costs, and similar. The limit is typically 20–30% of the dwelling limit and is capped at a maximum dollar amount per occurrence.

**Common data field:** `loss_of_use_limit`

### Coverage E — Personal Liability

Pays if the policyholder is found legally responsible for bodily injury or property damage to someone else — for example, a visitor who is injured on the property. Standard limits are $100,000, $300,000, or $500,000. This coverage also pays legal defense costs.

**Common data field:** `liability_limit`

### Coverage F — Medical Payments to Others

Pays medical bills for guests injured on the property regardless of fault. This is a goodwill coverage — it does not require a liability finding. Standard limit is $1,000 to $5,000 per person.

**Common data field:** `med_pay_limit`

---

## Endorsements Commonly Seen in Our Book

An endorsement (also called a rider) modifies or adds to the standard policy. The most common endorsements in the Travelers home book:

- **Water Backup and Sump Overflow** — covers damage from backed-up drains or a failed sump pump. Not included in the standard HO-3. Very commonly added in the Northeast region.
- **Equipment Breakdown** — covers mechanical or electrical failure of home systems (HVAC, water heater). Separate from the standard policy.
- **Home Systems Protection** — similar to equipment breakdown but broader; covers more appliances.
- **Scheduled Personal Property** — adds specific coverage for high-value items by listing them individually with agreed values.
- **Identity Fraud Expense** — reimburses costs associated with recovering from identity theft.

**Common data field:** `endorsements` — typically a list or flag columns per endorsement type.

---

## What Is Not Covered (Standard Exclusions)

The following are excluded from a standard HO-3 and generate out-of-scope questions that the agent should not attempt to answer from this document alone:

- **Flooding** — requires a separate flood policy (NFIP or private flood)
- **Earthquakes** — requires a separate earthquake endorsement or policy
- **Maintenance and wear** — gradual deterioration, mold from long-term leaks, pest infestation
- **Intentional acts** — damage caused on purpose by the policyholder
- **Business use of the home** — commercial liability arising from a home-based business is not covered under a personal lines policy

---

## Policy Terminology Quick Reference

| Term | Definition |
|------|-----------|
| Premium | The amount the customer pays for coverage, typically annually or in installments |
| Deductible | The amount the customer pays out of pocket before the policy pays on a claim |
| Endorsement | A modification to the standard policy terms |
| Replacement Cost Value (RCV) | What it costs to rebuild or replace at today's prices, without depreciation |
| Actual Cash Value (ACV) | Replacement cost minus depreciation |
| Occurrence | A single event that triggers a claim |
| Named Peril vs. Open Peril | Named peril covers only listed events; open peril (HO-3 standard) covers all events except listed exclusions |
