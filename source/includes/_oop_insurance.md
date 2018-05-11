## OOP Price Estimate
> Example loading trading partner price for cpt_bundle to /oop/insurance-load-price

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "trading_partner_id": "MOCKPAYER",
    "cpt_bundle":["99385"],
    "price": {
        "amount": "750"
    }
}' https://platform.pokitdok.com/api/v4/oop/insurance-load-price
```

```python
client.request('/oop/insurance-load-price', method='post', data={
    "trading_partner_id": "MOCKPAYER",
    "cpt_bundle":["99385"],
    "price": {
        "amount": "750"
    }
})
```

```csharp
string endpoint = "/oop/insurance-load-price";
string method = "POST";
Dictionary<string, object> data = new Dictionary<string, object> {
                {"price", new Dictionary<string, object>{
                    {"amount", "750"}
                },
                {"cpt_bundle", new string[] { "99385" }},
                {"trading_partner_id", "MOCKPAYER"}
        };
client.request(endpoint, method, data);
```

```ruby
client.request('/oop/insurance-load-price', method='post', params={
    trading_partner_id: "MOCKPAYER",
    cpt_bundle:["99385"],
    price: {
        amount: "750"
    }
})
```

```java
```

```swift
let data = [
    "trading_partner_id": "MOCKPAYER",
    "cpt_bundle":["99385"],
    "price": [
        "amount": "750"
    ]
] as [String:Any]
try client.oopLoadPrice(params: data)
```

> Example Response from /oop/insurance-load-price:

```json
{
     "client_id": "<client_id>",
     "cpt_bundle": ["99385"],
     "price": {"amount": "750", "currency": "USD"},
     "trading_partner_id": "MOCKPAYER"
 }
```

> Example fetching OOP Price Estimate from /oop/insurance-estimate

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "trading_partner_id" :"MOCKPAYER",
    "cpt_bundle":["99385"],
    "zip_code": "29412",
    "eligibility": {
           "provider": {
                "first_name": "ELIZABETH",
                "last_name": "BLACKWELL",
                "npi": "1234567893"
           },
           "member": {
               "birth_date": "1970-01-25",
               "first_name": "Jane",
               "last_name": "Doe",
               "id": "W000000000"
           }
     }
}' https://platform.pokitdok.com/api/v4/oop/insurance-estimate
```

```python
client.request('/oop/insurance-estimate', method='post', data={
    "trading_partner_id" :"MOCKPAYER",
    "cpt_bundle":["99385"],
    "zip_code": "29412",
    "eligibility": {
           "provider": {
                "first_name": "ELIZABETH",
                "last_name": "BLACKWELL",
                "npi": "1234567893"
           },
           "member": {
               "birth_date": "1970-01-25",
               "first_name": "Jane",
               "last_name": "Doe",
               "id": "W000000000"
           }
     }
})
```

```csharp
string endpoint = "/oop/insurance-estimate";
string method = "POST";
Dictionary<string, object> data = new Dictionary<string, object> {
                {"eligibility", new Dictionary<string, object>{
                    {"member", new Dictionary<string, object> {
                        {"id", "W000000000"},
                        {"birth_date", "1970-01-25"},
                        {"first_name", "Jane"},
                        {"last_name", "Doe"}
                        }},
                    {"provider", new Dictionary<string, object> {
                        {"npi", "1234567893"},
                        {"last_name", "BLACKWELL"},
                        {"first_name", "ELIZABETH"}
                        }}
                },
                {"cpt_bundle", new string[] { "99385" }},
                {"trading_partner_id", "MOCKPAYER"},
                {"zip_code", "29412"}
        };
client.request(endpoint, method, data);
```

```ruby
client.request('/oop/insurance-estimate', method='post', params={
    trading_partner_id: "MOCKPAYER",
    cpt_bundle: ["99385"],
    zip_code: "29412",
    eligibility: {
           provider: {
                first_name: "ELIZABETH",
                last_name: "BLACKWELL",
                npi: "1234567893"
           },
           member: {
               birth_date: "1970-01-25",
               first_name: "Jane",
               last_name: "Doe",
               id: "W000000000"
           }
     }
})
```

```java
```

```swift
let data = [
    "trading_partner_id" :"MOCKPAYER",
    "cpt_bundle":["99385"],
    "zip_code": "29412",
    "eligibility": [
           "provider": [
                "first_name": "ELIZABETH",
                "last_name": "BLACKWELL",
                "npi": "1234567893"
           ],
           "member": [
               "birth_date": "1970-01-25",
               "first_name": "Jane",
               "last_name": "Doe",
               "id": "W000000000"
           ]
     ]
] as [String:Any]
try client.oopEstimate(params: data)
```

>Example Response from /oop/insurance-estimate:

```json
{
    "calculation": {
       "coinsurance": ["0.0"],
       "deductible": "2983.57",
       "estimate": ["130"],
       "high_price": {"amount": "244.6", "currency": "USD"},
       "low_price": {"amount": "84.24", "currency": "USD"},
       "lower_estimate": ["84"],
       "max_oop": "2983.57",
       "messages": ["Deductible of 2983.57 has not been met."],
       "price": {"amount": "130.3855", "currency": "USD"},
       "service_type_codes": [["98"]],
       "upper_estimate": ["245"]
    },
    "eligibility": {
        "client_id": "<client_id>",
        "summary": {
             "deductible": {
                 "individual": {
                      "in_network": {
                          "applied": {
                              "currency": "USD",
                              "amount": "16.43"
                         },
                          "limit": {
                              "currency": "USD",
                              "amount": "3000"
                          },
                          "remaining": {
                              "currency": "USD",
                              "amount": "2983.57"
                          }
                        },
                      "out_of_network": {
                           "applied": {
                              "currency": "USD",
                              "amount": "16.43"
                          },
                          "limit": {
                              "currency": "USD",
                              "amount": "6000"
                          },
                          "remaining": {
                              "currency": "USD",
                              "amount": "5983.57"
                          }
                      }
                  },
                  "family": {
                     "in_network": {
                          "applied": {
                              "currency": "USD",
                              "amount": "43.91"
                          },
                          "limit": {
                              "currency": "USD",
                              "amount": "6000"
                          },
                          "remaining": {
                              "currency": "USD",
                              "amount": "5956.09"
                          }
                     },
                      "out_of_network": {
                          "applied": {
                              "currency": "USD",
                              "amount": "43.91"
                          },
                          "limit": {
                              "currency": "USD",
                              "amount": "12000"
                          },
                          "remaining": {
                              "currency": "USD",
                              "amount": "11956.09"
                          }
                      }
                  }
              },
              "out_of_pocket": {
                  "individual": {
                      "in_network": {
                          "applied": {
                              "currency": "USD",
                              "amount": "16.43"
                          },
                          "limit": {
                              "currency": "USD",
                              "amount": "3000"
                          },
                          "remaining": {
                              "currency": "USD",
                              "amount": "2983.57"
                          }
                      },
                      "out_of_network": {
                          "applied": {
                              "currency": "USD",
                              "amount": "16.43"
                          },
                          "limit": {
                              "currency": "USD",
                              "amount": "12500"
                          },
                          "remaining": {
                              "currency": "USD",
                              "amount": "12483.57"
                          }
                      }
                  },
                  "family": {
                      "in_network": {
                          "applied": {
                              "currency": "USD",
                              "amount": "43.91"
                          },
                         "limit": {
                              "currency": "USD",
                              "amount": "6000"
                          },
                          "remaining": {
                              "currency": "USD",
                              "amount": "5956.09"
                          }
                     },
                      "out_of_network": {
                          "applied": {
                              "currency": "USD",
                              "amount": "43.91"
                          },
                          "limit": {
                              "currency": "USD",
                              "amount": "25000"
                          },
                          "remaining": {
                              "currency": "USD",
                              "amount": "24956.09"
                          }
                      }
                  }
              }
          },
        "coverage": {
            "coinsurance": [
                {
                    "benefit_percent": 0.0,
                    "authorization_required": "yes",
                    "coverage_level": "employee_and_spouse",
                    "in_plan_network": "yes",
                    "messages": [],
                    "service_type_codes": [
                        "98"
                    ],
                    "service_types": [
                        "professional_physician_visit_office"
                    ]
                },
                {
                    "benefit_percent": 0.5,
                    "coverage_level": "employee_and_spouse",
                    "in_plan_network": "no",
                    "messages": [],
                    "service_type_codes": [
                        "98"
                    ],
                    "service_types": [
                        "professional_physician_visit_office"
                    ]
                }
            ],
            "copay": [
                {
                    "authorization_required": "yes",
                    "copayment": {
                        "amount": "0",
                        "currency": "USD"
                    },
                    "coverage_level": "employee_and_spouse",
                    "in_plan_network": "yes",
                    "messages": [
                        {
                            "message": "PRIMARY OFFICE"
                        }
                    ],
                    "service_type_codes": [
                        "98"
                    ],
                    "service_types": [
                        "professional_physician_visit_office"
                    ]
                },
                {
                    "copayment": {
                        "amount": "0",
                        "currency": "USD"
                    },
                    "coverage_level": "employee_and_spouse",
                    "in_plan_network": "not_applicable",
                    "messages": [
                        {
                            "message": "GYN OFFICE VS"
                        },
                        {
                            "message": "GYN VISIT"
                        },
                        {
                            "message": "SPEC OFFICE"
                        },
                        {
                            "message": "SPEC VISIT"
                        },
                        {
                            "message": "PRIME CARE VST"
                        },
                        {
                            "message": "Plan Requires PreCert"
                        },
                        {
                            "message": "Commercial"
                        },
                        {
                            "message": "Plan includes NAP"
                        },
                        {
                            "message": "Pre-Existing may apply"
                        }
                    ],
                    "service_type_codes": [
                        "98"
                    ],
                    "service_types": [
                        "professional_physician_visit_office"
                    ]
                }
            ],
            "deductibles": [
                {
                    "benefit_amount": {
                        "amount": "6000",
                        "currency": "USD"
                    },
                    "coverage_level": "family",
                    "eligibility_date": "2013-01-25",
                    "in_plan_network": "yes",
                    "messages": [],
                    "time_period": "calendar_year"
                },
                {
                    "benefit_amount": {
                        "amount": "5956.09",
                        "currency": "USD"
                    },
                    "coverage_level": "family",
                    "in_plan_network": "yes",
                    "messages": [],
                    "time_period": "remaining"
                },
                {
                    "benefit_amount": {
                        "amount": "3000",
                        "currency": "USD"
                    },
                    "coverage_level": "individual",
                    "eligibility_date": "2013-01-25",
                    "in_plan_network": "yes",
                    "messages": [],
                    "time_period": "calendar_year"
                },
                {
                    "benefit_amount": {
                        "amount": "2983.57",
                        "currency": "USD"
                    },
                    "coverage_level": "individual",
                    "in_plan_network": "yes",
                    "messages": [],
                    "time_period": "remaining"
                },
                {
                    "benefit_amount": {
                        "amount": "12000",
                        "currency": "USD"
                    },
                    "coverage_level": "family",
                    "eligibility_date": "2013-01-25",
                    "in_plan_network": "no",
                    "messages": [],
                    "time_period": "calendar_year"
                },
                {
                    "benefit_amount": {
                        "amount": "11956.09",
                        "currency": "USD"
                    },
                    "coverage_level": "family",
                    "in_plan_network": "no",
                    "messages": [],
                    "time_period": "remaining"
                },
                {
                    "benefit_amount": {
                        "amount": "6000",
                        "currency": "USD"
                    },
                    "coverage_level": "individual",
                    "eligibility_date": "2013-01-25",
                    "in_plan_network": "no",
                    "messages": [],
                    "time_period": "calendar_year"
                },
                {
                    "benefit_amount": {
                        "amount": "5983.57",
                        "currency": "USD"
                    },
                    "coverage_level": "individual",
                    "in_plan_network": "no",
                    "messages": [],
                    "time_period": "remaining"
                }
            ],
            "eligibility_begin_date": "2012-02-25",
            "group_description": "MOCK INDIVIDUAL ADVANTAGE PLAN",
            "group_number": "000000000000013",
            "level": "employee_and_spouse",
            "out_of_pocket": [
                {
                    "benefit_amount": {
                        "amount": "3000",
                        "currency": "USD"
                    },
                    "coverage_level": "individual",
                    "in_plan_network": "yes"
                },
                {
                    "benefit_amount": {
                        "amount": "2983.57",
                        "currency": "USD"
                    },
                    "coverage_level": "individual",
                    "in_plan_network": "yes",
                    "time_period": "remaining"
                },
                {
                    "benefit_amount": {
                        "amount": "6000",
                        "currency": "USD"
                    },
                    "coverage_level": "family",
                    "in_plan_network": "yes"
                },
                {
                    "benefit_amount": {
                        "amount": "5956.09",
                        "currency": "USD"
                    },
                    "coverage_level": "family",
                    "in_plan_network": "yes",
                    "time_period": "remaining"
                },
                {
                    "benefit_amount": {
                        "amount": "12500",
                        "currency": "USD"
                    },
                    "coverage_level": "individual",
                    "in_plan_network": "no"
                },
                {
                    "benefit_amount": {
                        "amount": "12483.57",
                        "currency": "USD"
                    },
                    "coverage_level": "individual",
                    "in_plan_network": "no",
                    "time_period": "remaining"
                },
                {
                    "benefit_amount": {
                        "amount": "25000",
                        "currency": "USD"
                    },
                    "coverage_level": "family",
                    "in_plan_network": "no"
                },
                {
                    "benefit_amount": {
                        "amount": "24956.09",
                        "currency": "USD"
                    },
                    "coverage_level": "family",
                    "in_plan_network": "no",
                    "messages": [],
                    "time_period": "remaining"
                }
            ],
            "plan_begin_date": "2013-02-25",
            "plan_number": "0000000",
            "service_date": "2013-08-25",
            "service_type_codes": [
                "98"
            ],
            "service_types": [
                "professional_physician_visit_office"
            ]
        },
        "payer": {
            "id": "MOCKPAYER",
            "name": "MOCK PAYER INC"
        },
        "provider": {
            "first_name": "ELIZABETH",
            "last_name": "BLACKWELL",
            "npi": "1234567893"
        },
        "service_type_codes": [
            "98"
        ],
        "service_types": [
            "professional_physician_visit_office"
        ],
        "subscriber": {
            "address": {
                "address_lines": [
                    "123 MAIN ST"
                ],
                "city": "SAN MATEO",
                "state": "CA",
                "zipcode": "94401"
            },
            "birth_date": "1970-01-25",
            "first_name": "Jane",
            "id": "W000000000",
            "last_name": "Doe"
        },
        "trading_partner_id": "MOCKPAYER",
        "valid_request": true
    }
}
```

*Available modes of operation: real-time*

The Out-of-Pokit (OOP) Insurance Estimate endpoint takes advantage of industry standard calculation methods
and our eligibility endpoint to provide an estimate of what consumers may expect to pay out of pocket for a set of services.

### Endpoint Description

Available OOP Insurance Endpoints:

<!--- beginning of table -->

| Endpoint                                  | HTTP Method | Description                                                                                     |
|:------------------------------------------|:------------|:------------------------------------------------------------------------------------------------|
| /oop/insurance-load-price                 | POST        | Loads procedure prices for a specific trading partner.                                          |
| /oop/insurance-load-price                 | GET         | Returns a list of loaded prices.                                                                |
| /oop/insurance-load-price/{price_uuid}    | GET         | Returns the loaded price with the given UUID.                                                    |
| /oop/insurance-load-price/{price_uuid}    | DELETE      | Removes a previously loaded procedure price from the system.                                    |
| /oop/insurance-estimate                   | POST        | Returns estimated out of pocket cost and eligibility information for a given procedure.         |

<!--- end of table -->

The `/oop/insurance-load-price` POST endpoint is used to load pricing data that is used in the `/oop-insurance-estimate` endpoint's calculations.
The `/oop/insurance-load-price` endpoint may also be used to retrieve pricing data, specific to the client that loaded it.
Sending a request that includes only the trading_partner_id and cpt_bundle parameters will either return the currently loaded price or, if no price has been loaded, return an error response.


### Parameters

The `/oop/insurance-load-price` POST endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter          | Type     | Description                                                                                   | Presence |
|:-------------------|:---------|:----------------------------------------------------------------------------------------------|:------------------|
| trading_partner_id | {string} | Unique id for the intended trading partner, as specified by the Trading Partners endpoint.    | Required |
| cpt_bundle         | {array}  | Collection of {string} CPT codes which would be billed as a bundle with a single price        | Required |
| price.amount       | {string} | The price of the bundle of procedures in the cpt_bundle                                       | Optional (include to load price, do not include to retrieve price) |
| price.currency     | {string} | Optional: The denomination of the currency of the price.amount. Defaults to 'USD'             | Optional (include to load price, do not include to retrieve price) |

<!--- end of table -->

The `/oop/insurance-load-price` POST response contains the aforementioned fields and activity tracking meta data.
The `/oop/insurance-load-price` POST response also contains a "uuid" field that can be passed to the `/oop/insurance-load-price/{price_uuid}` DELETE endpoint as the {price_uuid} in order to remove that loaded pricing data.
The `/oop/insurance-load-price/{price_uuid}` DELETE endpoint may be used to delete previously loaded pricing data.

The `/oop/insurance-estimate` endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter                             | Type     | Description                                                                                                                                                                        | Presence |
|:--------------------------------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| trading_partner_id                    | {string} | Unique id for the intended trading partner, as specified by the Trading Partners endpoint.                                                                                         | Required |
| cpt_bundle                            | {array}  | Collection of {string} CPT codes which would be billed as a bundle with a single price                                                                                             | Required |
| eligibility.provider.npi              | {string} | The NPI for the provider.                                                                                                                                                          | Optional |
| eligibility.provider.organization_name| {string} | The provider’s name when the provider is an organization.                                                                                                                          | Optional |
| eligibility.member.first_name         | {string} | The named insured’s first name as specified on their policy.                                                                                                                       | Optional |
| eligibility.member.last_name          | {string} | The named insured’s last name as specified on their policy.                                                                                                                        | Optional |
| eligibility.member.birth_date         | {string} | The named insured’s birth date as specified on their policy. May be omitted if member.id is provided. In ISO8601 format (YYYY-MM-DD).                                              | Optional |
| eligibility.member.id                 | {string} | The named insured’s member identifier. May be omitted if member.birth_date is provided.                                                                                            | Optional |
| zip_code                              | {string} | Optional: Used as a back up price data source if the trading partner has not loaded data for the chosen cpt_bundle. Hits the Insurance Prices endpoint to get prices based on area | Optional |

<!--- end of table -->

If eligibility information is not provided, generated eligibility data will be used, and a less accurate out of pocket estimate may be generated.

If either `eligibility.member` or `eligibility.provider` data is omitted, 
generic eligibility data will be used, and the generated out 
of pocket estimate will be less accurate. However, by including both 
`eligibility.member` and `eligibility.provider` data on your request you 
enable the Pokitdok API to perform a real-time eligibility check for the 
patient. Always include both fields whenever possible to ensure your 
customers receive the best possible estimate of out of pocket costs.

While the endpoint accepts a five-digit zip code, only the first three digits
are significant. This is because the index is only granular to the first three
digits of the zip code, commonly called a "geozip" or a "ZIP Code Prefix". These
three digits refer to the geographical regions surrounding major cities or
metropolitan areas. There are approximately 900 "geozips" in the United States.

### Response

The `/oop/insurance-estimate` response contains the following fields:

<!--- beginning of table -->

| Field                                                 | Description                                                                                                                                                                     | Presence |
|:------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| calculation.coinsurance                               | Collection of coinsurance values used to calculate estimate. Number of coinsurances returned will depend on eligibility response and will equal number of estimates returned.   | Required |
| calculation.deductible                                | Deductible returned from eligibility response and used in calculation                                                                                                           | Required |
| calculation.estimate                                  | Collection of out of pocket cost estimates based on price.amount                                                                                                                | Required |
| calculation.high_price.amount                         | High end price of cpt bundle returned from either the trading partner loaded prices or the Insurance Prices endpoint based on zip code                                          | Required |
| calculation.high_price.currency                       | The denomination of the currency of the calculation.high_price.amount                                                                                                           | Required |
| calculation.low_price.amount                          | Low end price of cpt bundle returned from either the trading partner loaded prices or the Insurance Prices endpoint based on zip code                                           | Required |
| calculation.low_price.currency                        | The denomination of the currency of the calculation.low_price.amount                                                                                                            | Required |
| calculation.lower_estimate                            | Collection of out of pocket cost estimates based on low_price.amount                                                                                                            | Required |
| calculation.max_oop                                   | Max out of pocket cost returned from eligibility response                                                                                                                       | Required |
| calculation.messages                                  | Collection of messages that describe factors that influenced the estimate calculation                                                                                           | Optional |
| calculation.price.amount                              | Base price of cpt bundle returned from either the trading partner loaded prices or the Insurance Prices endpoint based on zip code                                              | Required |
| calculation.price.currency                            | The denomination of the currency of the calculation.price.amount                                                                                                                | Required |
| calculation.service_type_codes                        | Collection of collections of service type codes that correspond to coinsurance and estimate collections                                                                         | Required |
| calculation.upper_estimate                            | Collection of out of pocket cost estimates based on high_price.amount                                                                                                           | Required |
| eligibility                                           | Full eligibility response from eligibility endpoint. See [eligibility documentation](#eligibility) above for more information                                                                   | Required |


<!--- end of table -->

The `oop/insurance-load-price` response contains the following fields:

<!--- beginning of table -->

| Field  | Type | Description |
| :--- | :--- | :--- |
| uuid | {string} | The UUID of the loaded price. |
| trading_partner_id | {string} | Unique ID for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint. |
| cpt_bundle | {list} | List of string CPT codes. |
| price.amount | {string} | The price of the bundle of procedures in the cpt_bundle. |
| price.currency | {string} | The denomination of the currency of the price.amount. Defaults to 'USD'|


<!--- end of table -->
