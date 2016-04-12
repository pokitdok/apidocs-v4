## Pharmacy Formulary

The Pharmacy Formulary Endpoint allows a deep dive into the member’s drug benefit. It 
returns details about what medications are covered in the formulary.  

A formulary is a list of medication that are approved for coverage by an insurance company.
Drugs on a formulary are usually grouped into tier levels. The tier that the medication falls
in determines the member’s copay. Most plans have between 3 to 5 tiers. The lower the tier, 
the less expensive the copay. Lower tiers are usually generic medication, middle tiers are 
brand medications and the highest tier is usually reserved for specialty medications. 

This includes tier level and restrictions such as prior authorization, step therapy, and 
quantity limit. Only Medicare Part C and D plans are currently available.

Medications can also have restrictions on their coverage such as prior authorization, 
step therapy, and quantity limit.

| Endpoint             | HTTP Method | Description                        |
|:---------------------|:------------|:-----------------------------------|
| /pharmacy/formulary  | GET         | Determine drug coverage for member |

To use the Pharmacy Formulary Endpoint with a medicare member, use the Eligibility
Endpoint to submit an eligibility request for a member using medicare_national trading 
partner id. Medicare members with Part D coverage will have pharmacy.is_eligible set to 
true and the pharmacy.plan_number will contain the member’s Medicare Part D plan_number. 
This number can be used to access the member’s benefits.
 
A medication for which coverage is being determined will need to be specified. This can
be done using the drug name or NDC. A drug name can include the name of the medication, 
strength, and form. For example, SIMVASTATIN 10 MG TABLET. Simvastatin is the drug name, 
the brand name of simvastatin is Zocor,10 MG is the strength. Medications can come in 
different strengths. Available strengths of simvastatin are 5mg, 10mg, 20mg, 40mg, and 80mg.
The form of this medication is tablet. Some drugs will come in multiple forms. Other examples
are capsule, solution, suspension, lotion, cream, etc. 

Access benefits for a specific medication by searching by complete name of the medication. 
For example, SIMVASTATIN 10 MG TABLET will return coverage information for just that medication.
For general results, search “simvastatin” and all of the coverage information for all strengths 
and forms of the drug will be returned. 

The Pharmacy Formulary Endpoint also accepts national drug code number (NDC). The NDC is a 
unique 11-digit, 3-segment number used to identify a specific drug product. The segments 
identify the manufacturer (first 5 numbers), product (middle 4 numbers), and package 
(last 2 numbers). An alternative way to lookup drug coverage is by using the NDC. One medication
can have multiple NDC numbers. For example, simvastatin 10 mg tablets can be supplied to the
pharmacy in a 100 count and 1000 count bottle. Both of these will have different NDC numbers 
even though the same drug is in each of the bottles. If simvastatin comes is bought from two 
different generic manufacturers, they will have different NDC numbers.

The /pharmacy/formulary endpoint accepts the following parameters:

| Field              | Type     | Description                                                                           |
|:-------------------|:---------|:--------------------------------------------------------------------------------------|
| trading_partner_id | {string} | Unique id for the intended [trading partner](https://platform.pokitdok.com/documentation/v4/#trading-partners), as specified by the Trading Partners endpoint. |
| plan_number        | {string} | Member’s plan identification number. Note: If unknown can use X12 270/271 eligibility |
| drug               | {string} | Name of medication, strength, and form. Note: Strength and form are optional          |
| ndc                | {string} | National drug code: a unique 11-digit, 3-segment number used to identify medication   |

Example request to determine drug coverage using full drug name (name + strength + form):

```python
pd.pharmacy_formulary(trading_partner_id: “medicare_national”, plan_number : “S5820003”, drug: “simvastatin 10mg tablet”)
```
Example request to determine drug coverage using drug name and strength:
 
```python
pd.pharmacy_formulary(trading_partner_id: “medicare_national”, plan_number: “S5820003”, drug: “simvastatin 10mg”)
```

Example request to determine drug coverage using drug name without strength or form:

```python
pd.pharmacy_formulary(trading_partner_id: “medicare_national”, plan_number: “S5820003”, drug: “simvastatin”)
```

Example request to determine drug coverage using NDC:

```python
pd.pharmacy_formulary(trading_partner_id: “medicare_national”, plan_number: “S5820003”, ndc: “59310-0574-12”)
```

The /pharmacy/formulary response contains the following parameters:

| Field       | Type     | Description                                                |
|:------------|:---------|:-----------------------------------------------------------|
| drug                  | {string} | The full drug name (name + strength + form)      |
| is_covered            | {string} | Is this medication on the insurance formulary    |
| tier                  | {short} | The level the drug fall under on the formulary    |
| tier_name             | {string} | The name associated with the tier level          |
| prior_auth            | {boolean} | Does the drug require a prior authorization?    |
| step_therapy          | {boolean} | Does the drug require step therapy?             |
| quantity_limit        | {boolean} | Does this drug have a quantity limit?           |
| quantity_limit_amount | {string} | Quantity limit amount associated with this drug. The unit of measure is specific to the drug type. |
| quantity_limit_days   | {integer} | Quantity limit days associated with this drug. E.g. 30  |

Sample Pharmacy Formulary API response when searching for a medication using the complete
drug name (SIMVASTATIN 10 MG TABLET) :  

```json
“data” : {
"drugs": {
[
{	
“drug” : “SIMVASTATIN 10 MG TABLET”,
“tier” : 1,
“tier_name” : “preferred generic”, 
“prior_auth” : false,
“step_therapy” false,
“quantity_limit” : false
}
]
},
"is_covered": true
}
```
Sample pharmacy plan API response when searching for a drug name without strength (SIMVASTATIN) : 

```json
“data” : {
"drugs": {
[
{	
“drug” : “SIMVASTATIN 5 MG TABLET”,
“tier” : 1,
“tier_name” : “preferred generic”, 
“prior_auth” : false,
“step_therapy” false,
“quantity_limit” : false
}
{	
“drug” : “SIMVASTATIN 10 MG TABLET”,
“tier” : 1,
“tier_name” : “preferred generic”, 
“prior_auth” : false,
“step_therapy” false,
“quantity_limit” : false
}
{	
“drug” : “SIMVASTATIN 20 MG TABLET”,
“tier” : 1,
“tier_name” : “preferred generic”, 
“prior_auth” : false,
“step_therapy” false,
“quantity_limit” : false
}
{	
“drug” : “SIMVASTATIN 40 MG TABLET”,
“tier” : 1,
“tier_name” : “preferred generic”, 
“prior_auth” : false,
“step_therapy” false,
“quantity_limit” : false
}
{	
“drug” : “SIMVASTATIN 80 MG TABLET”,
“tier” : 1,
“tier_name” : “preferred generic”, 
“prior_auth” : false,
“step_therapy” false,
“quantity_limit” : false
}
]
},
"is_covered": true
}
```
Sample pharmacy plan API response when searching by NDC (59310-0579-22) :

```json
“data” : {
"drugs": {
[
{	
“drug” : “SIMVASTATIN 10 MG TABLET”,
“tier” : 1,
“tier_name” : “preferred generic”, 
“prior_auth” : false,
“step_therapy” false,
“quantity_limit” : false
}
]
},
"is_covered": true
}
```

Sample Pharmacy Formulary API response when searching for a medication using the complete drug 
name (LYRICA 225 MG CAPSULE) and drug has a quantity limit :  

```json
“data” : {
"drugs": {
[
{	
“drug” : “LYRICA 225 MG CAPSULE”,
“tier” : 4,
“tier_name” : “non-preferred brand” 
“prior_auth” : false,
“step_therapy” false,
“quantity_limit” : true
“quantity_limit_amount” : “60.00”
“quantity_limit_days” : 30
}
]
},
"is_covered": true
}
```
