## Pharmacy Drug Cost

The Pharmacy Drug Cost Endpoint allows a deep dive into the cost for a member’s 
medication. It returns details about a medication’s out of pocket cost, total cost, 
and insurance payment.

| Endpoint    | HTTP Method | Description                                   |
|:------------|:------------|:----------------------------------------------|
| /pharmacy/drugcost        | GET          | Determine drug cost for member |

To use the Pharmacy Drug Cost Endpoint with a medicare member, use the Eligibility Endpoint
to submit an eligibility request for a member using medicare_national trading partner id.
Medicare members with Part D coverage will have pharmacy.is_eligible set to true and the 
pharmacy.plan_number will contain the member’s Medicare Part D plan_number. This number can be
used to access the member’s benefits.
 
A medication for which coverage is being determined will need to be specified. This can be done 
using the drug name or NDC. A drug name can include the name of the medication, strength, and form.
For example, SIMVASTATIN 10 MG TABLET. Simvastatin is the drug name, the brand name of simvastatin 
is Zocor,10 MG is the strength. Medications can come in different strengths. Available strengths of 
simvastatin are 5mg, 10mg, 20mg, 40mg, and 80mg. The form of this medication is tablet. Some drugs 
will come in multiple forms. Other examples are capsule, solution, suspension, lotion, cream, etc.
 
Access benefits for a specific medication by searching by complete name of the medication. For example, 
SIMVASTATIN 10 MG TABLET will return coverage information for just that medication. For general results,
search “simvastatin” and all of the coverage information for all strengths and forms of the drug will be 
returned.
 
The Pharmacy Drug Cost Endpoint also accepts national drug code number (NDC). The NDC is a unique 11-digit,
3-segment number used to identify a specific drug product. The segments identify the manufacturer (first 5 numbers), 
product (middle 4 numbers), and package (last 2 numbers). An alternative way to lookup drug coverage is by using 
the NDC. One medication can have multiple NDC numbers. For example, simvastatin 10 mg tablets can be supplied
to the pharmacy in a 100 count and 1000 count bottle. Both of these will have different NDC numbers even 
though the same drug is in each of the bottles. If simvastatin comes is bought from two different generic
manufacturers, they will have different NDC numbers.

Out of pocket costs for medications are based on 30 day supply at retail or 90 day supply at mail order
pharmacies. Some medication isn’t taken continuously, ex. antibiotics. For those medications, the member
would just pay one 30 day supply copay. 

In some cases, the member’s copay will be more than the total cost of the drug. In these situations, the
actual amount the member will pay will depend on the pharmacy where they fill the prescription. For example,
if the member’s copay is $10 and the drug only costs $4, the pharmacy could decide to charge the member the 
full $10, or the actual drug price of $4. 

If the drug is not covered, only estimated total cost data will be returned for drug. 
 
The /pharmacy/drugcost endpoint accepts the following parameters:

| Field              | Type     | Description                                                                                       |
|:-------------------|:---------|:--------------------------------------------------------------------------------------------------|
| trading_partner_id | {string} | Unique id for the intended trading partner, as specified by the [Trading Partners](https://platform.pokitdok.com/documentation/v4/#trading-partners) endpoint.                   |
| plan_number        | {string} | Member’s plan identification number. Note: If unknown can use X12 270/271 eligibility             |
| drug               | {string} | Name of medication, strength, and form. Note: Strength and form are optional                      |
| ndc                | {string} | National drug code: a unique 11-digit, 3-segment number used to identify medication               |

Example request to determine drug coverage using full drug name (name + strength + form):

```python
pd.drug_cost(trading_partner_id: “medicare_national”, plan_number: “S5820003”, drug: “simvastatin 10mg tablet”)
```

Example request to determine drug coverage using drug name and strength:

```python
pd.drug_cost(trading_partner_id: “medicare_national”, plan_number: “S5820003”, drug: “simvastatin 10mg”)
```
Example request to determine drug coverage using drug name without strength or form:

```python
pd.drug_cost(trading_partner_id: “medicare_national”, plan_number: “S5820003”, drug: “simvastatin”)
```

Example request to determine drug coverage using NDC:

```python
pd.drug_cost(trading_partner_id: “medicare_national”, plan_number: “S5820003”, ndc: “59310-0574-12”)
```

The /pharmacy/drugcost response contains the following parameters:

| Field                    | Type     | Description                                                                                                                             |
|:-------------------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------|
| label_name               | {string} | The full drug name (name + strength + form)                                                                                             |
| is_covered               | {string} | Is this medication covered on the insurance formulary                                                                                   |
| retail.oop_30_day        | {string} | Out of pocket cost for 30 day supply of drug at a in-network retail pharmacy                                                            |
| retail.total_cost_30_day | {string} | Total cost of drug for 30 day supply of drug at a in-network retail pharmacy (average insurance negotiated rate with pharmacy)          |
| retail.ins_pay_30_day    | {string} | Amount insurance covers for 30 day supply of drug at a in-network retail pharmacy (average insurance negotiated rate with pharmacy)     |
| mail.oop_90_day          | {string} | Out of pocket cost for 90 day supply of drug at a in-network mail order pharmacy                                                        |

| mail.total_cost_90_day   | {string} | Total cost of drug for 90 day supply of drug at a in-network mail order pharmacy (average insurance negotiated rate with pharmacy)      |

| mail.ins_pay_90_day      | {string} | Amount insurance covers for 90 day supply of drug at a in-network mail order pharmacy (average insurance negotiated rate with pharmacy) |

Sample Pharmacy Formulary API response when searching for a medication using the 
complete drug name (SIMVASTATIN 10 MG TABLET) :  

```json
“data” : {
"drugs": {
[
{	
“drug” : “SIMVASTATIN 10 MG TABLET”,
“retail”: {
	“oop_30_day” : {
“amount” : “1.00”,
“currency” : “USD”
        	},
	“total_cost_30_dayl” : {
“amount” : “3.41”,
“currency” : “USD”
        	},
	“ins_pay_30_day” : {
“amount” : “2.41”,
“currency” : “USD”
        	}
},
“mail”: {
          	“oop_90_day” : {
“amount” : “3.00”,
“currency” : “USD”
        	},
           “total_cost_90_day_mail” {
“amount” : “8.27”,
“currency” : “USD”
        	},
	“ins_pay_90_day_mail” : {
“amount” : “5.27”,
“currency” : “USD”
        	}
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
“retail”: {
	“oop_30_day” : {
“amount” : “1.00”,
“currency” : “USD”
        	},
	“total_cost_30_day” : {
“amount” : “3.32”,
“currency” : “USD”
        	},
	“ins_pay_30_day” : {
“amount” : “2.32”,
“currency” : “USD”
        	}
},
“mail”: {
          	“oop_90_day” : {
“amount” : “3.00”,
“currency” : “USD”
        	},
           “total_cost_90_day_mail” {
“amount” : “7.98”,
“currency” : “USD”
        	},
	“ins_pay_90_day_mail” : {
“amount” : “4.98”,
“currency” : “USD”
        	}
}
{	
“drug” : “SIMVASTATIN 10 MG TABLET”,
“retail”: {
	“oop_30_day” : {
“amount” : “1.00”,
“currency” : “USD”
        	},
	“total_cost_30_dayl” : {
“amount” : “3.41”,
“currency” : “USD”
        	},
	“ins_pay_30_day” : {
“amount” : “2.41”,
“currency” : “USD”
        	}
},
“mail”: {
          	“oop_90_day” : {
“amount” : “3.00”,
“currency” : “USD”
        	},
           “total_cost_90_day_mail” {
“amount” : “8.27”,
“currency” : “USD”
        	},
	“ins_pay_90_day_mail” : {
“amount” : “5.27”,
“currency” : “USD”
        	}
}
{	
“drug” : “SIMVASTATIN 20 MG TABLET”,
“retail”: {
	“oop_30_day” : {
“amount” : “1.00”,
“currency” : “USD”
        	},
	“total_cost_30_dayl” : {
“amount” : “3.37”,
“currency” : “USD”
        	},
	“ins_pay_30_day” : {
“amount” : “2.37”,
“currency” : “USD”
        	}
},
“mail”: {
          	“oop_90_day” : {
“amount” : “3.00”,
“currency” : “USD”
        	},
           “total_cost_90_day_mail” {
“amount” : “8.14”,
“currency” : “USD”
        	},
	“ins_pay_90_day_mail” : {
“amount” : “5.14”,
“currency” : “USD”
        	}
}
{	
“drug” : “SIMVASTATIN 40 MG TABLET”,
“retail”: {
	“oop_30_day” : {
“amount” : “1.00”,
“currency” : “USD”
        	},
	“total_cost_30_dayl” : {
“amount” : “3.22”,
“currency” : “USD”
        	},
	“ins_pay_30_day” : {
“amount” : “7.69”,
“currency” : “USD”
        	}
},
“mail”: {
          	“oop_90_day” : {
“amount” : “3.00”,
“currency” : “USD”
        	},
           “total_cost_90_day_mail” {
“amount” : “7.69”,
“currency” : “USD”
        	},
	“ins_pay_90_day_mail” : {
“amount” : “4.69”,
“currency” : “USD”
        	}
}
{	
“drug” : “SIMVASTATIN 80 MG TABLET”,
“retail”: {
	“oop_30_day” : {
“amount” : “1.00”,
“currency” : “USD”
        	},
	“total_cost_30_dayl” : {
“amount” : “3.44”,
“currency” : “USD”
        	},
	“ins_pay_30_day” : {
“amount” : “2.44”,
“currency” : “USD”
        	}
},
“mail”: {
          	“oop_90_day” : {
“amount” : “3.00”,
“currency” : “USD”
        	},
           “total_cost_90_day_mail” {
“amount” : “8.37”,
“currency” : “USD”
        	},
	“ins_pay_90_day_mail” : {
“amount” : “5.37”,
“currency” : “USD”
        	}
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
“retail”: {
	“oop_30_day” : {
“amount” : “1.00”,
“currency” : “USD”
        	},
	“total_cost_30_dayl” : {
“amount” : “3.41”,
“currency” : “USD”
        	},
	“ins_pay_30_day” : {
“amount” : “2.41”,
“currency” : “USD”
        	}
},
“mail”: {
          	“oop_90_day” : {
“amount” : “3.00”,
“currency” : “USD”
        	},
           “total_cost_90_day_mail” {
“amount” : “8.27”,
“currency” : “USD”
        	},
	“ins_pay_90_day_mail” : {
“amount” : “5.27”,
“currency” : “USD”
        	}
}
]
},
"is_covered": true
}
```

Sample Pharmacy Formulary API response when searching for a medication using the 
complete drug name (TAMIFLU 75MG CAPSULE) and drug is not covered :  

```json
“data” : {
"drugs": {
[
{	
“drug” : “TAMIFLU 75MG CAPSULE”,
}
]
},
"is_covered": false
}
```
