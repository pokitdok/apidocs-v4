## Claims Status
> Example claim status request when the patient is also the subscriber on the insurance policy:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "patient": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003"
    },
    "service_date": "2014-01-01",
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/claims/status
```

```python
pd.claims_status({
    "patient": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003"
    },
    "service_date": "2014-01-01",
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
client.claimsStatus(
			new Dictionary<string, object> {
				{"patient", new Dictionary<string, object> {
						{"id", "W000000000"},
						{"birth_date", "1970-01-01"},
						{"first_name", "Jane"},
						{"last_name", "Doe"}
					}},
				{"provider", new Dictionary<string, object> {
						{"npi", "1467560003"},
						{"last_name", "AYA-AY"},
						{"first_name", "JEROME"}
					}},
				{"service_date", "2014-01-01"},
				{"trading_partner_id", "MOCKPAYER"}
			});
```

> Example claim status request when the patient is not the subscriber on the insurance policy:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "patient": {
        "birth_date": "2000-01-01",
        "first_name": "JOHN",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003"
    },
    "service_date": "2014-01-01",
    "subscriber": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/claims/status
```
```python
pd.claims_status({
    "patient": {
        "birth_date": "2000-01-01",
        "first_name": "JOHN",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003"
    },
    "service_date": "2014-01-01",
    "subscriber": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

> Example claim status request when the claim service period covers several days:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "patient": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003"
    },
    "service_date": "2014-01-01",
    "service_end_date": "2014-01-04",
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/claims/status
```

```python
pd.claims_status({
    "patient": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003"
    },
    "service_date": "2014-01-01",
    "service_end_date": "2014-01-04",
    "trading_partner_id": "MOCKPAYER"
})
```

> Example claim status request using a claim tracking id to refine the search:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "patient": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003"
    },
    "service_date": "2014-01-01",
    "tracking_id": "ABC12345",
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/claims/status
```

```python
pd.claims_status({
    "patient": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003"
    },
    "service_date": "2014-01-01",
    "tracking_id": "ABC12345",
    "trading_partner_id": "MOCKPAYER"
})
```

> Example claims status response when the trading partner is unable to locate
any matching claims:

```
{
    "patient": {
        "claims": [
            {
                "applied_to_deductible": false,
                "claim_control_number": "NOT APPLICABLE",
                "claim_payment_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "service_date": "2014-01-01",
                "service_end_date": "2014-01-01",
                "statuses": [
                    {
                        "claim_payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "status_category": "Acknowledgement/Not Found-The claim/encounter can not be found in the adjudication system.",
                        "status_code": "Claim/encounter not found.",
                        "status_effective_date": "2014-07-29",
                        "total_claim_amount": {
                            "amount": "0",
                            "currency": "USD"
                        }
                    }
                ],
                "total_claim_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "tracking_id": "47635D71-B08B-47D9-9C11-4630F5"
            }
        ],
        "first_name": "JANE",
        "id": "W100000000",
        "last_name": "DOE"
    },
    "payer": {
        "id": "MOCKPAYER",
        "name": "MOCKPAYER"
    },
    "providers": [
        {
            "first_name": "Jerome",
            "last_name": "Aya-Ay",
            "npi": "1467560003"
        }
    ],
    "submitter": {
        "first_name": "Jerome",
        "id": "1467560003",
        "last_name": "Aya-Ay"
    },
    "trading_partner_id": "MOCKPAYER"
}
```
> Example claims status response when there is an error in the formatting of the provider's NPI or
name, and they are unable to find a match:

```
{  
    "client_id":"fFFgqPeK5GETjZkC3JPB",
    "payer":{  
        "name":"MOCKPAYER",
        "id":"MOCKPAYER"
    },
    "providers":[  
        {  
            "trace_number":"0",
            "first_name":"Jerome",
            "last_name":"Aya-Ay",
            "npi":"123456789",
            "statuses":[  
                {  
                    "status_code":"Entity's National Provider Identifier (NPI).",
                    "status_category":"Data Search Unsuccessful - The payer is unable to return status on the requested claim(s) based on the submitted search criteria.",
                    "status_effective_date":"2015-09-01",
                    "status_category_code":"D0"
                }
            ]
        }
    ],
    "correlation_id":"37045a41-634a-4439-a555-d8d6cbb445ce",
    "trading_partner_id":"MOCKPAYER",
    "submitter":{  
        "first_name":"Jerome",
        "last_name":"Aye-Ay",
        "id":"MOCKPAYER"
    }
}
```

> Example claims status response when adjudication is finalized and the claim
has been paid:

```
{
    "patient": {
        "claims": [
            {
                "adjudication_finalized_date": "2014-06-20",
                "applied_to_deductible": false,
                "check_number": "08608-000000000",
                "claim_control_number": "EV30000WY00",
                "claim_payment_amount": {
                    "amount": "156",
                    "currency": "USD"
                },
                "remittance_date": "2014-06-24",
                "service_date": "2014-06-17",
                "service_end_date": "2014-06-17",
                "services": [
                    {
                        "charge_amount": {
                            "amount": "20",
                            "currency": "USD"
                        },
                        "cpt_code": "D1206",
                        "payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "service_date": "2014-06-17",
                        "service_end_date": "2014-06-17",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    },
                    {
                        "charge_amount": {
                            "amount": "72",
                            "currency": "USD"
                        },
                        "cpt_code": "D1110",
                        "payment_amount": {
                            "amount": "72",
                            "currency": "USD"
                        },
                        "service_date": "2014-06-17",
                        "service_end_date": "2014-06-17",
                        "statuses": [
                            {
                                "status_category": "Finalized/Payment-The claim/line has been paid.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    },
                    {
                        "charge_amount": {
                            "amount": "29",
                            "currency": "USD"
                        },
                        "cpt_code": "D0431",
                        "payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "service_date": "2014-06-17",
                        "service_end_date": "2014-06-17",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    },
                    {
                        "charge_amount": {
                            "amount": "52",
                            "currency": "USD"
                        },
                        "cpt_code": "D0274",
                        "payment_amount": {
                            "amount": "48",
                            "currency": "USD"
                        },
                        "service_date": "2014-06-17",
                        "service_end_date": "2014-06-17",
                        "statuses": [
                            {
                                "status_category": "Finalized/Payment-The claim/line has been paid.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    },
                    {
                        "charge_amount": {
                            "amount": "41",
                            "currency": "USD"
                        },
                        "cpt_code": "D0120",
                        "payment_amount": {
                            "amount": "36",
                            "currency": "USD"
                        },
                        "service_date": "2014-06-17",
                        "service_end_date": "2014-06-17",
                        "statuses": [
                            {
                                "status_category": "Finalized/Payment-The claim/line has been paid.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    }
                ],
                "statuses": [
                    {
                        "adjudication_finalized_date": "2014-06-20",
                        "check_number": "08608-000000000",
                        "claim_payment_amount": {
                            "amount": "156",
                            "currency": "USD"
                        },
                        "remittance_date": "2014-06-24",
                        "status_category": "Finalized/Payment-The claim/line has been paid.",
                        "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                        "status_effective_date": "2014-07-29",
                        "total_claim_amount": {
                            "amount": "214",
                            "currency": "USD"
                        }
                    }
                ],
                "total_claim_amount": {
                    "amount": "214",
                    "currency": "USD"
                },
                "tracking_id": "B82A26AE-984A-480B-9B20-81DD3E"
            }
        ],
        "first_name": "JANE",
        "id": "W199000000",
        "last_name": "DOE"
    },
    "payer": {
        "id": "MOCKPAYER",
        "name": "MOCKPAYER"
    },
    "providers": [
        {
            "first_name": "ADAM",
            "last_name": "SMITH",
            "npi": "1320000000"
        }
    ],
    "submitter": {
        "first_name": "ADAM",
        "id": "1326000000",
        "last_name": "SMITH"
    },
    "trading_partner_id": "MOCKPAYER"
}
```

> Example claims status response when adjudication is finalized and the claim has been denied:

```
{
    "patient": {
        "claims": [
            {
                "adjudication_finalized_date": "2013-07-24",
                "applied_to_deductible": false,
                "claim_control_number": "EM000000000",
                "claim_payment_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "remittance_date": "2013-07-30",
                "service_date": "2013-07-15",
                "service_end_date": "2013-07-15",
                "services": [
                    {
                        "charge_amount": {
                            "amount": "375",
                            "currency": "USD"
                        },
                        "cpt_code": "D9220",
                        "payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "service_date": "2013-07-15",
                        "service_end_date": "2013-07-15",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    },
                    {
                        "charge_amount": {
                            "amount": "460",
                            "currency": "USD"
                        },
                        "cpt_code": "D7240",
                        "payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "service_date": "2013-07-15",
                        "service_end_date": "2013-07-15",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    },
                    {
                        "charge_amount": {
                            "amount": "140",
                            "currency": "USD"
                        },
                        "cpt_code": "D7140",
                        "payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "service_date": "2013-07-15",
                        "service_end_date": "2013-07-15",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    }
                ],
                "statuses": [
                    {
                        "adjudication_finalized_date": "2013-07-24",
                        "claim_payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "remittance_date": "2013-07-30",
                        "status_category": "Finalized/Denial-The claim/line has been denied.",
                        "status_effective_date": "2014-07-29",
                        "total_claim_amount": {
                            "amount": "975",
                            "currency": "USD"
                        }
                    }
                ],
                "total_claim_amount": {
                    "amount": "975",
                    "currency": "USD"
                },
                "tracking_id": "D92BD44D-9F9F-4DE1-890B-61EF86"
            },
            {
                "adjudication_finalized_date": "2013-08-23",
                "applied_to_deductible": false,
                "claim_control_number": "EH000000000",
                "claim_payment_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "remittance_date": "2013-08-27",
                "service_date": "2013-07-15",
                "service_end_date": "2013-07-15",
                "services": [
                    {
                        "charge_amount": {
                            "amount": "375",
                            "currency": "USD"
                        },
                        "cpt_code": "D9220",
                        "payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "service_date": "2013-07-15",
                        "service_end_date": "2013-07-15",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    },
                    {
                        "charge_amount": {
                            "amount": "460",
                            "currency": "USD"
                        },
                        "cpt_code": "D7240",
                        "payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "service_date": "2013-07-15",
                        "service_end_date": "2013-07-15",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    },
                    {
                        "charge_amount": {
                            "amount": "140",
                            "currency": "USD"
                        },
                        "cpt_code": "D7140",
                        "payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "service_date": "2013-07-15",
                        "service_end_date": "2013-07-15",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    }
                ],
                "statuses": [
                    {
                        "adjudication_finalized_date": "2013-08-23",
                        "claim_payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "remittance_date": "2013-08-27",
                        "status_category": "Finalized/Denial-The claim/line has been denied.",
                        "status_effective_date": "2014-07-29",
                        "total_claim_amount": {
                            "amount": "975",
                            "currency": "USD"
                        }
                    }
                ],
                "total_claim_amount": {
                    "amount": "975",
                    "currency": "USD"
                },
                "tracking_id": "D92BD44D-9F9F-4DE1-890B-61EF86"
            }
        ],
        "first_name": "JANE",
        "id": "W100000000",
        "last_name": "SMITH"
    },
    "payer": {
        "id": "MOCKPAYER",
        "name": "MOCKPAYER"
    },
    "providers": [
        {
            "first_name": "JOHN",
            "last_name": "DOE",
            "npi": "1234567890"
        }
    ],
    "submitter": {
        "first_name": "JOHN",
        "id": "1234567890",
        "last_name": "DOE"
    },
    "trading_partner_id": "MOCKPAYER"
}
```

> Example claims status response when adjudication is finalized, the claim has
been denied (not paid) and the charges are applied to the deductible:

```
{
    "patient": {
        "claims": [
            {
                "adjudication_finalized_date": "2014-04-04",
                "applied_to_deductible": true,
                "check_number": "814000000000000",
                "claim_control_number": "E6Y0C7NQG00",
                "claim_payment_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "remittance_date": "2014-04-14",
                "service_date": "2014-03-26",
                "service_end_date": "2014-03-26",
                "services": [
                    {
                        "charge_amount": {
                            "amount": "137",
                            "currency": "USD"
                        },
                        "cpt_code": "99213",
                        "payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "service_date": "2014-03-26",
                        "service_end_date": "2014-03-26",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    },
                    {
                        "charge_amount": {
                            "amount": "290",
                            "currency": "USD"
                        },
                        "cpt_code": "76830",
                        "payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "service_date": "2014-03-26",
                        "service_end_date": "2014-03-26",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_effective_date": "2014-07-29"
                            }
                        ]
                    }
                ],
                "statuses": [
                    {
                        "adjudication_finalized_date": "2014-04-04",
                        "check_number": "814000000000000",
                        "claim_payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "remittance_date": "2014-04-14",
                        "status_category": "Finalized/Denial-The claim/line has been denied.",
                        "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                        "status_effective_date": "2014-07-29",
                        "total_claim_amount": {
                            "amount": "427",
                            "currency": "USD"
                        }
                    }
                ],
                "total_claim_amount": {
                    "amount": "427",
                    "currency": "USD"
                },
                "tracking_id": "4AAA5F0D-986E-4C69-A428-67DA60"
            }
        ],
        "first_name": "JANE",
        "last_name": "DOE"
    },
    "payer": {
        "id": "MOCKPAYER",
        "name": "MOCKPAYER"
    },
    "providers": [
        {
            "first_name": "JOHN",
            "last_name": "DOE",
            "npi": "1700000000"
        }
    ],
    "submitter": {
        "first_name": "JOHN",
        "id": "1700000000",
        "last_name": "DOE"
    },
    "trading_partner_id": "MOCKPAYER"
}
```

*Available modes of operation: real-time*

The Claims Status Endpoint allows an application to request information about
previously submitted claims. You can send a request to a payer to determine
where the claim is in their adjudication system and the status of the claim.

The PokitDok Claims Status Endpoint can be used to query the status of multiple
claims. To learn how to form such a request and understand how the
[Claims](#claims) and [Claims Status](#claims_status) Endpoints work together,
see [claims API workflow](https://platform.pokitdok.com/claim-processing).

Please note that on average it takes 5-7 days for a claim to enter a payer’s
adjudication system, thus it recommended to wait at least a week after
submitting a claim to check its status.  


| Endpoint       | HTTP Method | Description                                                     |
|:---------------|:------------|:----------------------------------------------------------------|
| /claims/status | POST        | Submit a claim status request to the specified trading partner. |


The /claims/status endpoint accepts the following parameters:

| Parameter                  | Description                                                                                                                          |
|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| patient.birth_date         | The patient’s birth date as specified on their policy.                                                                               |
| patient.id                 | The patient’s member identifier.                                                                                                     |
| patient.first_name         | The patient’s first name as specified on their policy.                                                                               |
| patient.last_name          | The patient’s last name as specified on their policy.                                                                                |
| provider.first_name        | The provider’s first name when the provider is an individual.                                                                        |
| provider.last_name         | The provider’s last name when the provider is an individual.                                                                         |
| provider.npi               | The NPI for the provider.                                                                                                            |
| provider.organization_name | The provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name. |
| service_date               | The date services were performed or started for the claim service period.                                                            |
| service_end_date           | Optional: The date services ended for the claim service period.                                                                      |
| subscriber.birth_date      | Optional: The subscriber’s birth date as specified on their policy. Specify when the patient is not the subscriber.                  |
| subscriber.first_name      | Optional: The subscriber’s first name as specified on their policy. Specify when the patient is not the subscriber.                  |
| subscriber.id              | Optional: The subscriber’s member identifier. Specify when the patient is not the subscriber.                                        |
| subscriber.last_name       | Optional: The subscriber’s last name as specified on their policy. Specify when the patient is not the subscriber.                   |
| tracking_id                | Optional: The payer's claim tracking id. Specify a tracking id to refine the search criteria for a specific claim.                   |
| trading_partner_id         | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) Endpoint.                      |


The /claim/status response contains the following parameters:

| Parameter                                             | Description                                                                                                                                                                                                                                                                                                                                        |
|:------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| patient                                               | Information about a patient including any matching claims.                                                                                                                                                                                                                                                                                         |
| patient.claims                                        | A list of matching claims returned by the trading partner for a claims status request.                                                                                                                                                                                                                                                             |
| patient.claims.adjudication_finalized_date            | The date adjudication was finalized for the claim.                                                                                                                                                                                                                                                                                                 |
| patient.claims.applied_to_deductible                  | Boolean that indicates whether or not claim charges are applied to the deductible.                                                                                                                                                                                                                                                                 |
| patient.claims.check_number                           | The check or EFT trace number for a claim payment.                                                                                                                                                                                                                                                                                                 |
| patient.claims.claim_control_number                   | The Payer's Claim Control Number.                                                                                                                                                                                                                                                                                                                  |
| patient.claims.claim_payment_amount                   | The amount that's been paid on the claim.                                                                                                                                                                                                                                                                                                          |
| patient.claims.remittance_date                        | The date the check was issued or EFT funds became available.                                                                                                                                                                                                                                                                                       |
| patient.claims.service_date                           | The date services were performed or started for the claim service period.                                                                                                                                                                                                                                                                          |
| patient.claims.service_end_date                       | The date services ended for the claim service period.                                                                                                                                                                                                                                                                                              |
| patient.claims.services                               | A list of services linked to the claim.                                                                                                                                                                                                                                                                                                            |
| patient.claims.services.charge_amount                 | The amount charged for a particular service on the claim.                                                                                                                                                                                                                                                                                          |
| patient.claims.services.cpt_code                      | The CPT code indicating the type of service that was performed.                                                                                                                                                                                                                                                                                    |
| patient.claims.services.payment_amount                | The amount paid for a particular service on the claim.                                                                                                                                                                                                                                                                                             |
| patient.claims.services.service_date                  | The date the service was performed or started for the claim service period.                                                                                                                                                                                                                                                                        |
| patient.claims.services.service_end_date              | The date the service ended for the claim service period.                                                                                                                                                                                                                                                                                           |
| patient.claims.services.statuses                      | A listing of status information for the claim.                                                                                                                                                                                                                                                                                                     |
| patient.claims.services.statuses.status_category      | A verbose message about the general category of the service's claim status (e.g. accepted, rejected, etc.). This value is suitable for display to users of a system utilizing the claims status API. A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).    |
| patient.claims.services.statuses.status_category_code | The code indicating the general category of the service's claim status. The status category code is more appropriate for use by the software using the claims status API to categorize the information. A full listing of codes can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).           |
| patient.claims.services.statuses.status_code          | Indicates the status of the service on the claim. This status code provides more detail to support the status category. This value is suitable for display to users of a system utilizing the claims status API. A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-codes/). |
| patient.claims.statuses                               | A listing of status information for the claim.                                                                                                                                                                                                                                                                                                     |
| patient.claims.statuses.status_category               | A verbose message about the general category of the claim's status (e.g. accepted, rejected, etc.). This value is suitable for display to users of a system utilizing the claims status API. A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).            |
| patient.claims.statuses.status_category_code          | The code indicating the general category of the claim's status. The status category code is more appropriate for use by the software using the claims status API to categorize the information. A full listing of codes can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).                   |
| patient.claims.statuses.status_code                   | Indicates the status of the claim. This status code provides more detail to support the status category. This value is suitable for display to users of a system utilizing the claims status API. A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).       |
| patient.claims.total_claim_amount                     | The total charges submitted for the claim.                                                                                                                                                                                                                                                                                                         |
| patient.first_name                                    | The patient’s first name as specified on their policy.                                                                                                                                                                                                                                                                                             |
| patient.id                                            | The patient’s member identifier.                                                                                                                                                                                                                                                                                                                   |
| patient.last_name                                     | The patient’s last name as specified on their policy.                                                                                                                                                                                                                                                                                              |
