## Pharmacy Formulary

> Example request to determine drug coverage using drug name:

```python
pd.pharmacy_formulary(trading_partner_id='medicare_national', plan_number='S0522034', drug='simvastatin')
```

> Example request to determine drug coverage using NDC:

```python
pd.pharmacy_formulary(trading_partner_id='medicare_national', plan_number='S0522034', ndc='00071101968')
```

> Sample Pharmacy Formulary API response when searching for a drug name (SIMVASTATIN) : 

```json
{
    "data": [
        {
            "drug": "SIMVASTATIN 40 MG TABLET", 
            "prior_auth": false, 
            "quantity_limit": false, 
            "step_therapy": false, 
            "tier": 1, 
            "tier_name": "preferred generic"
        }, 
        {
            "drug": "SIMVASTATIN 20 MG TABLET", 
            "prior_auth": false, 
            "quantity_limit": false, 
            "step_therapy": false, 
            "tier": 1, 
            "tier_name": "preferred generic"
        }, 
        {
            "drug": "SIMVASTATIN 5 MG TABLET", 
            "prior_auth": false, 
            "quantity_limit": false, 
            "step_therapy": false, 
            "tier": 1, 
            "tier_name": "preferred generic"
        }, 
        {
            "drug": "SIMVASTATIN 80 MG TABLET", 
            "limit_amount": "30", 
            "limit_days": 30, 
            "prior_auth": false, 
            "quantity_limit": true, 
            "step_therapy": false, 
            "tier": 1, 
            "tier_name": "preferred generic"
        }, 
        {
            "drug": "SIMVASTATIN 10 MG TABLET", 
            "prior_auth": false, 
            "quantity_limit": false, 
            "step_therapy": false, 
            "tier": 1, 
            "tier_name": "preferred generic"
        }
    ]
}

```

> Sample Pharmacy Formulary API response when searching by NDC (00071101968) :

```json
{
    "data": [
        {
            "drug": "LYRICA 225 MG CAPSULE", 
            "limit_amount": "60", 
            "limit_days": 30, 
            "prior_auth": false, 
            "quantity_limit": true, 
            "step_therapy": false, 
            "tier": 3, 
            "tier_name": "preferred brand"
        }
    ]
}
```

The Pharmacy Formulary Endpoint allows a deep dive into the member’s drug benefit. It returns details about what medications are covered in the formulary.  

A formulary is a list of medication that are approved for coverage by an insurance company. Drugs on a formulary are usually grouped into tier levels. The tier that the medication falls in determines the member’s copay. Most plans have between 3 to 5 tiers. The lower the tier, the less expensive the copay. Lower tiers are usually generic medication, middle tiers are brand medications, and the highest tier is usually reserved for specialty medications. 

This endpoint returns tier level and restrictions such as prior authorization, step therapy, and quantity limit. Only Medicare Part C and D plans are currently available.

Medications can also have restrictions on their coverage such as prior authorization, step therapy, and quantity limit.

| Endpoint            | HTTP Method | Description                        |
|:--------------------|:------------|:-----------------------------------|
| /pharmacy/formulary | GET         | Determine drug coverage for member |

To use the Pharmacy Formulary Endpoint with a Medicare member, you will need the plan number. This is the contract ID (ex. S1234) + Plan's Plan Benefit Package (PBP) Number PBP number (ex. 001) concatenated together in that order. There are several ways to get this number. The plan number may be on the member’s insurance card. If not, you can use an NCPDP E1 eligibility check or PokitDok’s Eligibility Endpoint. With the Eligibility Endpoint, Medicare members with Part D coverage will have pharmacy.is_eligible set to true and the pharmacy.plan_number will contain their Medicare Part D plan_number. Note: Your NPI must be registered with Medicare to check eligibility. 
 
A medication for which coverage is being determined will need to be specified. This can be done using the drug name or NDC. A drug name can include the name of the medication, strength, and form. For example, SIMVASTATIN 10 MG TABLET. Simvastatin is the drug name. 10 MG is the strength. Simvastatin can come in other strengths (5mg, 10mg, 20mg, 40mg, and 80mg). The form of this medication is tablet. Some drugs will come in multiple forms. Other examples are capsule, solution, suspension, lotion, cream, etc. The brand name of simvastatin is Zocor. You can search for a drug with just the brand or generic name or any combination of drug +/- strength +/- form.

Access benefits for a specific medication by searching by complete name of the medication. For example, SIMVASTATIN 10 MG TABLET will return coverage information for just that medication. For general results, search “simvastatin” and all of the coverage information for all strengths and forms of the drug will be returned.

The Pharmacy Formulary Endpoint also accepts national drug code number (NDC). The NDC is a unique 11-digit, 3-segment number used to identify a specific drug product. The segments identify the manufacturer (first 5 numbers), product (middle 4 numbers), and package (last 2 numbers). An alternative way to lookup drug coverage is by using the NDC. One medication can have multiple NDC numbers. For example, simvastatin 10 mg tablets can be supplied to the pharmacy in a 100 count and 1000 count bottle. Both of these will have different NDC numbers even though the same drug is in each of the bottles. Simvastatin from different generic manufacturers will have different NDC numbers. 

The /pharmacy/formulary endpoint accepts the following parameters:

| Field              | Type     | Description                                                                                                                                                    |
|:-------------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trading_partner_id | {string} | Unique id for the intended [trading partner](https://platform.pokitdok.com/documentation/v4/#trading-partners), as specified by the Trading Partners endpoint. |
| plan_number        | {string} | Member’s plan identification number. Note: If unknown can use X12 270/271 eligibility                                                                          |
| drug               | {string} | Name of medication, strength, and form. Note: Strength and form are optional                                                                                   |
| ndc                | {string} | National drug code: a unique 11-digit, 3-segment number used to identify medication                                                                            |

The /pharmacy/formulary response contains the following parameters:

| Field                 | Type      | Description                                                                                        |
|:----------------------|:----------|:---------------------------------------------------------------------------------------------------|
| drug                  | {string}  | The full drug name (name + strength + form)                                                        |
| tier                  | {short}   | The level the drug fall under on the formulary                                                     |
| tier_name             | {string}  | The name associated with the tier level                                                            |
| prior_auth            | {boolean} | Does the drug require a prior authorization?                                                       |
| step_therapy          | {boolean} | Does the drug require step therapy?                                                                |
| quantity_limit        | {boolean} | Does this drug have a quantity limit?                                                              |
| limit_amount | {string}  | Quantity limit amount associated with this drug. The unit of measure is specific to the drug type. |
| limit_days   | {integer} | Quantity limit days associated with this drug. E.g. 30                                             |