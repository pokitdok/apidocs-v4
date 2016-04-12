## Pharmacy Plan

The Pharmacy Plans Endpoint returns a member’s pharmacy plan information such
as plan name, premium, deductible, initial coverage limit and copays for each tier 
(initial coverage phase). Only Medicare Part C and D plans are currently available.

Available Pharmacy Plan Endpoints:

| Endpoint          | HTTP Method | Description                             |
|:------------------|:------------|:----------------------------------------|
| /pharmacy/plan   | GET        | Determine pharmacy plan info for member |

To use the Pharmacy Plans Endpoint with a medicare member, use the Eligibility Endpoint
to submit an eligibility request for a member using medicare_national trading partner id.
Medicare members with Part D coverage will have pharmacy.is_eligible set to true and the 
pharmacy.plan_number will contain their Medicare Part D plan_number. You will use this 
number to access the member’s benefits.

The /pharmacy/plan endpoint accepts the following parameters:

| Field               | Type     | Description                                                                               |
|:--------------------|:---------|:------------------------------------------------------------------------------------------|
| trading_partner_id  | {string} | Unique id for the intended trading partner, as specified by the Trading Partners endpoint.|
| plan_number         | {string} | Member’s plan identification number. Note: If unknown can use X12 270/271 eligibility     |

Example request to determine pharmacy plan information:

```python
pd.pharmacy_plan(trading_partner_id = “medicare_national”, plan_number = “S5820003”)
```

The Pharmacy Plan Endpoint allows you to dive into the member’s drug benefit and discover
details about the plan.

Most prescription benefits are included in the medical plan, therefore will not have a separate 
premium or deductible. Medicare Part D plans are purchased separate from medical benefits, 
therefore will have their own premium and deductible. Premium and deductible will only be 
returned for Medicare Part D plans. 

Medicare drug plans have different phases of coverage, including deductible, initial coverage, 
gap coverage, and catastrophic coverage. Each phase has a different out of pocket cost for covered 
medications. The copays included in the Pharmacy Plan Endpoint are coverage during the Initial Coverage Phase.

Medications are grouped into tiers or levels. Plans may have several tiers and the copay for a drug 
depends on which tier the drug is in. Usually the lower tiers contain less expensive medications and 
the higher tiers are reserved for more expensive medications. 

Each tier level will have either a copay or coinsurance associated with it. The copay will be a dollar
amount that the member will be responsible for paying out of pocket. Ex. retail_30_day_tier_1_copay 
The co-insurance will be a percentage of the total cost of the drug that the member will pay out of pocket. 
Ex. retail_30_day_tier_4_coins

To determine in-network pharmacies for the plan, you can use the In-Network Pharmacy Endpoint. To determine 
if a specific drug is located on a tier level, you can use our Pharmacy Formulary Endpoint. You can also
use Eligibility Endpoint to get initial member benefit information including basic pharmacy benefit information.

The /pharmacy/plan response contains the following parameters:

| Field                      | Type     | Description                                                                                                             |
|:---------------------------|:---------|:------------------------------------------------------------------------------------------------------------------------|
| plan_name                  | {string} | Name of prescription drug plan                                                                                          |
| trading_partner_id         | {string} | Unique id for the intended trading partner, as specified by the Trading Partners Endpoint                               |
| premium                    | {string} | Monthly premium - amount member pays per month for coverage                                                             |
| deductible                 | {string} | The amount the member must pay out of pocket before initial coverage begins                                             |
| initial_coverage_limit     | {string} | The total drug cost before the member reaches the donut hole (coverage gap)                                             |
| retail.tier_one_30_day_copay | {string} | Copay ($) for a tier 1 medication for 30-day supply at an in-network retail pharmacy           |
| retail.tier_two_30_day_copay | {string} | Copay ($) for a tier 2 medication for 30-day supply at an in-network retail pharmacy           |
| retail.tier_three_30_day_copay | {string} | Copay ($) for a tier 3 medication for 30-day supply at an in-network retail pharmacy          |
| retail.tier_four_30_day_copayy | {string} | Copay ($) for a tier 4 medication for 30-day supply at an in-network retail pharmacy           |
| retail.tier_five_30_day_copay| {string} | Copay ($) for a tier 5 medication for 30-day supply at an in-network retail pharmacy           |
| retail.tier_one_30_day_coins | {string} | Coinsurance (%) for a tier 1 medication for 30-day supply at an in-network retail pharmacy     |
| retail.tier_two_30_day_coins | {string} | Coinsurance (%) for a tier 2 medication for 30-day supply at an in-network retail pharmacy  |
| retail.tier_three_30_day_coins | {string} | Coinsurance (%) for a tier 3 medication for 30-day supply at an in-network retail pharmacy    |
| retail.tier_four_30_day_coins | {string} | Coinsurance (%) for a tier 4 medication for 30-day supply at an in-network retail pharmacy   |
| retail.tier_five_30_day_coins | {string} | Coinsurance (%) for a tier 5 medication for 30-day supply at an in-network retail pharmacy    |
| mail.tier_one_90_day_copay   | {string} | Copay ($) for a tier 1 medication for 90-day supply at an in-network mail-order pharmacy      |
| mail.tier_two_90_day_copay   | {string} | Copay ($) for a tier 2 medication for 90-day supply at an in-network mail-order pharmacy    |
| mail.tier_three_90_day_copay   | {string} | Copay ($) for a tier 3 medication for 90-day supply at an in-network mail-order pharmacy        |
| mail.tier_four_90_day_copay   | {string} | Copay ($) for a tier 4 medication for 90-day supply at an in-network mail-order pharmacy      |
| mail.tier_five_90_day_copay   | {string} | Copay ($) for a tier 5 medication for 90-day supply at an in-network mail-order pharmacy      |
| mail.tier_one_90_day_coins   | {string} | Coinsurance (%) for a tier 1 medication for 90-day supply at an in-network mail-order pharmacy |
| mail.tier_two_90_day_coins   | {string} | Coinsurance (%) for a tier 2 medication for 90-day supply at an in-network mail-order pharmacy  |
| mail.tier_three_90_day_coins   | {string} | Coinsurance (%) for a tier 3 medication for 90-day supply at an in-network mail-order pharmacy  |
| mail.tier_four_90_day_coins   | {string} | Coinsurance (%) for a tier 4 medication for 90-day supply at an in-network mail-order pharmacy |
| mail.tier_five_90_day_coins   | {string} | Coinsurance (%) for a tier 5 medication for 90-day supply at an in-network mail-order pharmacy |

Example pharmacy plan response for a member with Medicare Part D:

```json
{
  “plan_name” : “Aetna Medicare Rx Saver“,
  “trading_partner_id” : “medicare_national”,
  “premium” : {
    “amount” : “24.00”,
    “currency” : “USD”
  },
  “deductible” : {
    “amount” : “360.00”,
    “currency” : “USD”
  },
  “initial_coverage_limit” : {
    “amount” : “3310.00”,
    “currency” : “USD”
  },
  “retail”: {
	“tier_one_30_day_copay”: {
		“amount”: “1.00”
		“currency”: “USD”
	},
	“tier_two_30_day_copay”: {
		“amount”: “2.00”
		“currency”: “USD”
	},
	“tier_three_30_day_copay”: {
		“amount”: “35.00”
		“currency”: “USD”
	},
	“tier_four_30_day_coins” : “0.4”,
        “tier_five_30_day_coins” : “0.25”
	},
“mail”: {
	“tier_one_90_day_copay”: {
		“amount”: “18.00”
		“currency”: “USD”
	},
	“tier_two_90_day_copay”: {
		“amount”: “21.00”
		“currency”: “USD”
	},
	“tier_three_90_day_copay”: {
		“amount”: “105.00”
		“currency”: “USD”
	},
	“tier_four_90_day_coins” : “0.4”,
	}

}
```
