## Pharmacy Plans

> Example request to determine pharmacy plan information:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"  'https://platform.pokitdok.com/api/v4/pharmacy/plans?trading_partner_id=medicare_national&plan_number=S5820003'
```

```python
client.pharmacy_plans(trading_partner_id='medicare_national', plan_number='S5820003')
```

```ruby
client.pharmacy_plans(trading_partner_id:'medicare_national', plan_number:'S5820003')
```

```csharp
client.pharmacyPlans(
                  new Dictionary<string, string> {
                    {"trading_partner_id", "medicare_national"},
                    {"plan_number", "S5820003"}
                });
```

```java
Map<String, Object> params = new HashMap<String, Object>();
params.put("trading_partner_id", "medicare_national");
params.put("plan_number", "S5820003");
client.pharmacyPlans(params);
```

```swift
let data = [
    "trading_partner_id": "medicare_national",
    "plan_number": "S5820003",
] as [String:Any]
try client.pharmacyPlans(params: data)
```

> Example pharmacy plan response for a member with Medicare Part D:

```json
{
    "data": [
        {
            "deductible": {
                "amount": "0.00",
                "currency": "USD"
            },
            "initial_coverage_limit": {
                "amount": "3310.00",
                "currency": "USD"
            },
            "mail": {
                "tier_five_90_day_coins": "0.33",
                "tier_four_90_day_coins": "0.4",
                "tier_one_90_day_copay": {
                    "amount": "0.00",
                    "currency": "USD"
                },
                "tier_three_90_day_copay": {
                    "amount": "90.00",
                    "currency": "USD"
                },
                "tier_two_90_day_copay": {
                    "amount": "0.00",
                    "currency": "USD"
                }
            },
            "plan_name": "AARP MedicareRx Preferred (PDP)",
            "plan_number": "S5820003",
            "premium": {
                "amount": "65.80",
                "currency": "USD"
            },
            "retail": {
                "tier_five_30_day_coins": "0.33",
                "tier_four_30_day_coins": "0.4",
                "tier_one_30_day_copay": {
                    "amount": "4.00",
                    "currency": "USD"
                },
                "tier_three_30_day_copay": {
                    "amount": "35.00",
                    "currency": "USD"
                },
                "tier_two_30_day_copay": {
                    "amount": "8.00",
                    "currency": "USD"
                }
            },
            "trading_partner_id": "medicare_national",
            "zipcodes": [
                "29401",
                "94401"
            ]
        }
    ]
}
```

The Pharmacy Plans Endpoint returns a member’s pharmacy plan information such
as plan name, premium, deductible, initial coverage limit and copays for each tier
(initial coverage phase). Only Medicare Part C and D plans are currently available.

### Endpoint Description

Available Pharmacy Plans Endpoints:

<!--- beginning of table -->

| Endpoint       | HTTP Method | Description                             |
|:---------------|:------------|:----------------------------------------|
| /pharmacy/plans | GET         | Determine pharmacy plan info for member |

<!--- end of table -->

To use the Pharmacy Plans Endpoint with a Medicare member, you will need the plan number. This is the contract ID (ex. S1234) + Plan's Plan Benefit Package (PBP) Number PBP number (ex. 001) concatenated together in that order. There are several ways to get this number. The plan number may be on the member’s insurance card. If not, you can use an NCPDP E1 eligibility check or PokitDok’s Eligibility Endpoint. With the Eligibility Endpoint, Medicare members with Part D coverage will have pharmacy.is_eligible set to true and the pharmacy.plan_number will contain their Medicare Part D plan_number. Note: Your NPI must be registered with Medicare to check eligibility.

### Parameters

The `/pharmacy/plans` endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter          | Type     | Description                                                                                                                                                    | Presence |
|:-------------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| trading_partner_id | {string} | Unique id for the intended trading partner, as specified by the [Trading Partners](https://platform.pokitdok.com/documentation/v4/#trading-partners) endpoint. | Required |
| plan_number        | {string} | Member’s plan identification number. Note: If unknown can use X12 270/271 eligibility                                                                          | Either plan_number or plan_name must be present |
| plan_name          | {string} | Name of prescription drug plan                                                                                                                                 | Either plan_number or plan_name must be present |
| zipcode            | {string} | Zip code where plan is available                                                                                                                               | Optional |

<!--- end of table -->

The Pharmacy Plans Endpoint allows you to dive into the member’s drug benefit and discover details about the plan.

Medicare drug plans have different phases of coverage, including deductible, initial coverage, gap coverage, and catastrophic coverage. Each phase has a different out of pocket cost for covered medications. The copays included in the Pharmacy Plan Endpoint are for the member during the Initial Coverage Phase.
Medications are grouped into tiers or levels. Plans may have several tiers and the copay for a drug depends on which tier the drug is in. Usually the lower tiers contain less expensive medications and the higher tiers are reserved for more expensive medications. Each tier level will have either a copay or coinsurance associated with it. The copay will be a dollar amount that the member will be responsible for paying out of pocket. Ex. retail_30_day_tier_1_copay The co-insurance will be a percentage of the total cost of the drug that the member will pay out of pocket. Ex. retail_30_day_tier_4_coins

### Response

The `/pharmacy/plans` response contains the following fields:

<!--- beginning of table -->

| Field                          | Type     | Description                                                                                    | Presence |
|:-------------------------------|:---------|:-----------------------------------------------------------------------------------------------|:---------|
| plan_name                      | {string} | Name of prescription drug plan                                                                 | Required |
| plan_number                    | {string} | Member’s plan identification number                                                            | Required |
| trading_partner_id             | {string} | Unique id for the intended trading partner, as specified by the Trading Partners Endpoint      | Required |
| zipcodes                       | {array}  | A list of zipcodes (strings) where the plan is available                                       | Optional |
| premium                        | {string} | Monthly premium - amount member pays per month for coverage                                    | Optional |
| deductible                     | {string} | The amount the member must pay out of pocket before initial coverage begins                    | Optional |
| initial_coverage_limit         | {string} | The total drug cost before the member reaches the donut hole (coverage gap)                    | Optional |
| retail.tier_one_30_day_copay   | {string} | Copay ($) for a tier 1 medication for 30-day supply at an in-network retail pharmacy           | Optional |
| retail.tier_two_30_day_copay   | {string} | Copay ($) for a tier 2 medication for 30-day supply at an in-network retail pharmacy           | Optional |
| retail.tier_three_30_day_copay | {string} | Copay ($) for a tier 3 medication for 30-day supply at an in-network retail pharmacy           | Optional |
| retail.tier_four_30_day_copay  | {string} | Copay ($) for a tier 4 medication for 30-day supply at an in-network retail pharmacy           | Optional |
| retail.tier_five_30_day_copay  | {string} | Copay ($) for a tier 5 medication for 30-day supply at an in-network retail pharmacy           | Optional |
| retail.tier_one_30_day_coins   | {string} | Coinsurance (%) for a tier 1 medication for 30-day supply at an in-network retail pharmacy     | Optional |
| retail.tier_two_30_day_coins   | {string} | Coinsurance (%) for a tier 2 medication for 30-day supply at an in-network retail pharmacy     | Optional |
| retail.tier_three_30_day_coins | {string} | Coinsurance (%) for a tier 3 medication for 30-day supply at an in-network retail pharmacy     | Optional |
| retail.tier_four_30_day_coins  | {string} | Coinsurance (%) for a tier 4 medication for 30-day supply at an in-network retail pharmacy     | Optional |
| retail.tier_five_30_day_coins  | {string} | Coinsurance (%) for a tier 5 medication for 30-day supply at an in-network retail pharmacy     | Optional |
| mail.tier_one_90_day_copay     | {string} | Copay ($) for a tier 1 medication for 90-day supply at an in-network mail-order pharmacy       | Optional |
| mail.tier_two_90_day_copay     | {string} | Copay ($) for a tier 2 medication for 90-day supply at an in-network mail-order pharmacy       | Optional |
| mail.tier_three_90_day_copay   | {string} | Copay ($) for a tier 3 medication for 90-day supply at an in-network mail-order pharmacy       | Optional |
| mail.tier_four_90_day_copay    | {string} | Copay ($) for a tier 4 medication for 90-day supply at an in-network mail-order pharmacy       | Optional |
| mail.tier_five_90_day_copay    | {string} | Copay ($) for a tier 5 medication for 90-day supply at an in-network mail-order pharmacy       | Optional |
| mail.tier_one_90_day_coins     | {string} | Coinsurance (%) for a tier 1 medication for 90-day supply at an in-network mail-order pharmacy | Optional |
| mail.tier_two_90_day_coins     | {string} | Coinsurance (%) for a tier 2 medication for 90-day supply at an in-network mail-order pharmacy | Optional |
| mail.tier_three_90_day_coins   | {string} | Coinsurance (%) for a tier 3 medication for 90-day supply at an in-network mail-order pharmacy | Optional |
| mail.tier_four_90_day_coins    | {string} | Coinsurance (%) for a tier 4 medication for 90-day supply at an in-network mail-order pharmacy | Optional |
| mail.tier_five_90_day_coins    | {string} | Coinsurance (%) for a tier 5 medication for 90-day supply at an in-network mail-order pharmacy | Optional |

<!--- end of table -->