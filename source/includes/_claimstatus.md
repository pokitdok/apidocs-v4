## Claims Status
> Example claim status request when the patient is also the subscriber on the insurance policy:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    },
    "service_date": "2014-01-25",
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/claims/status
```

```python
client.claims_status({
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    },
    "service_date": "2014-01-25",
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
client.claimsStatus(
			new Dictionary<string, object> {
				{"patient", new Dictionary<string, object> {
						{"id", "W000000000"},
						{"birth_date", "1970-01-25"},
						{"first_name", "Jane"},
						{"last_name", "Doe"}
					}},
				{"provider", new Dictionary<string, object> {
						{"npi", "1234567893"},
						{"last_name", "BLACKWELL"},
						{"first_name", "ELIZABETH"}
					}},
				{"service_date", "2014-01-25"},
				{"trading_partner_id", "MOCKPAYER"}
			});
```

```ruby
client.claims_status({
    patient: {
        birth_date: "1970-01-25",
        first_name: "JANE",
        last_name: "DOE",
        id: "1234567890"
    },
    provider: {
        first_name: "Elizabeth",
        last_name: "Blackwell",
        npi: "1234567893"
    },
    service_date: "2014-01-25",
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"patient\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"JANE\",");
buf.append("        \"last_name\": \"DOE\",");
buf.append("        \"id\": \"1234567890\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"Elizabeth\",");
buf.append("        \"last_name\": \"Blackwell\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"service_date\": \"2014-01-25\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claimsStatus(query);
```

```swift
let data = [
    "patient": [
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    ],
    "provider": [
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    ],
    "service_date": "2014-01-25",
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.claimsStatus(params: data)
```

> Example claim status request when the patient is not the subscriber on the insurance policy:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "patient": {
        "birth_date": "2000-01-25",
        "first_name": "JOHN",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    },
    "service_date": "2014-01-25",
    "subscriber": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/claims/status
```

```python
client.claims_status({
    "patient": {
        "birth_date": "2000-01-25",
        "first_name": "JOHN",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    },
    "service_date": "2014-01-25",
    "subscriber": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
client.claimsStatus(new Dictionary<string, object> {
    {"patient", new Dictionary<string, string> {
        {"birth_date", "2000-01-25"},
        {"first_name", "JOHN"},
        {"last_name", "DOE"},
        {"id", "1234567890"}
    }},
    {"provider", new Dictionary<string, string> {
        {"first_name", "Elizabeth"},
        {"last_name", "Blackwell"},
        {"npi", "1234567893"}
    }},
    {"service_date", "2014-01-25"},
    {"subscriber", new Dictionary<string, string> {
        {"birth_date", "1970-01-25"},
        {"first_name", "JANE"},
        {"last_name", "DOE"},
        {"id", "1234567890"}
    }},
    {"trading_partner_id", "MOCKPAYER"}
});
```


```ruby
client.claims_status({
    patient: {
        birth_date: "2000-01-25",
        first_name: "JOHN",
        last_name: "DOE",
        id: "1234567890"
    },
    provider: {
        first_name: "Elizabeth",
        last_name: "Blackwell",
        npi: "1234567893"
    },
    service_date: "2014-01-25",
    subscriber: {
        birth_date: "1970-01-25",
        first_name: "JANE",
        last_name: "DOE",
        id: "1234567890"
    },
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"patient\": {");
buf.append("        \"birth_date\": \"2000-01-25\",");
buf.append("        \"first_name\": \"JOHN\",");
buf.append("        \"last_name\": \"DOE\",");
buf.append("        \"id\": \"1234567890\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"Elizabeth\",");
buf.append("        \"last_name\": \"Blackwell\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"service_date\": \"2014-01-25\",");
buf.append("    \"subscriber\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"JANE\",");
buf.append("        \"last_name\": \"DOE\",");
buf.append("        \"id\": \"1234567890\"");
buf.append("    },");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claimsStatus(query);
```

```swift
let data = [
    "patient": [
        "birth_date": "2000-01-25",
        "first_name": "JOHN",
        "last_name": "DOE",
        "id": "1234567890"
    ],
    "provider": [
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    ],
    "service_date": "2014-01-25",
    "subscriber": [
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    ],
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.claimsStatus(params: data)
```

> Example claim status request when the claim service period covers several days:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    },
    "service_date": "2014-01-25",
    "service_end_date": "2014-01-25",
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/claims/status
```

```python
client.claims_status({
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    },
    "service_date": "2014-01-25",
    "service_end_date": "2014-01-25",
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
client.claimsStatus(new Dictionary<string, object> {
    {"patient", new Dictionary<string, string> {
        {"birth_date", "1970-01-25"},
        {"first_name", "JANE"},
        {"last_name", "DOE"},
        {"id", "1234567890"}
    }},
        {"provider", new Dictionary<string, string> {
        {"first_name", "Elizabeth"},
        {"last_name", "Blackwell"},
        {"npi", "1234567893"}
    }},
    {"service_date", "2014-01-25"},
    {"service_end_date", "2014-01-25"},
    {"trading_partner_id", "MOCKPAYER"}
});
```

```ruby
client.claims_status({
    patient: {
        birth_date: "1970-01-25",
        first_name: "JANE",
        last_name: "DOE",
        id: "1234567890"
    },
    provider: {
        first_name: "Elizabeth",
        last_name: "Blackwell",
        npi: "1234567893"
    },
    service_date: "2014-01-25",
    service_end_date: "2014-01-25",
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"patient\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"JANE\",");
buf.append("        \"last_name\": \"DOE\",");
buf.append("        \"id\": \"1234567890\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"Elizabeth\",");
buf.append("        \"last_name\": \"Blackwell\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"service_date\": \"2014-01-25\",");
buf.append("    \"service_end_date\": \"2014-01-25\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claimsStatus(query);
```

```swift
let data = [
    "patient": [
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    ],
    "provider": [
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    ],
    "service_date": "2014-01-25",
    "service_end_date": "2014-01-25",
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.claimsStatus(params: data)
```

> Example claim status request using a claim tracking id to refine the search:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    },
    "service_date": "2014-01-25",
    "tracking_id": "ABC12345",
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/claims/status
```

```python
client.claims_status({
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    },
    "service_date": "2014-01-25",
    "tracking_id": "ABC12345",
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
client.claimsStatus(new Dictionary<string, object> {
    {"patient", new Dictionary<string, string> {
        {"birth_date", "1970-01-25"},
        {"first_name", "JANE"},
        {"last_name", "DOE"},
        {"id", "1234567890"}
    }},
    {"provider", new Dictionary<string, string> {
        {"first_name", "Elizabeth"},
        {"last_name", "Blackwell"},
        {"npi", "1234567893"}
    }},
    {"service_date", "2014-01-25"},
    {"tracking_id", "ABC12345"},
    {"trading_partner_id", "MOCKPAYER"}
});
```

```ruby
client.claims_status({
    patient: {
        birth_date: "1970-01-25",
        first_name: "JANE",
        last_name: "DOE",
        id: "1234567890"
    },
    provider: {
        first_name: "Elizabeth",
        last_name: "Blackwell",
        npi: "1234567893"
    },
    service_date: "2014-01-25",
    tracking_id: "ABC12345",
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"patient\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"JANE\",");
buf.append("        \"last_name\": \"DOE\",");
buf.append("        \"id\": \"1234567890\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"Elizabeth\",");
buf.append("        \"last_name\": \"Blackwell\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"service_date\": \"2014-01-25\",");
buf.append("    \"tracking_id\": \"ABC12345\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claimsStatus(query);
```

```swift
let data = [
    "patient": [
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    ],
    "provider": [
        "first_name": "Elizabeth",
        "last_name": "Blackwell",
        "npi": "1234567893"
    ],
    "service_date": "2014-01-25",
    "tracking_id": "ABC12345",
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.claimsStatus(params: data)
```

> Example claims status response when the trading partner is unable to locate
any matching claims:

```json
{
    "client_id": "<client_id>",
    "patient": {
        "claims": [
            {
                "applied_to_deductible": false,
                "claim_control_number": "NOT APPLICABLE",
                "claim_payment_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "service_date": "2014-01-25",
                "service_end_date": "2014-01-25",
                "statuses": [
                    {
                        "claim_payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "status_category": "Acknowledgement/Not Found-The claim/encounter can not be found in the adjudication system.",
                        "status_category_code": "A4",
                        "status_code": "Claim/encounter not found.",
                        "status_code_value": "35",
                        "status_effective_date": "2014-07-25",
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
            "first_name": "Elizabeth",
            "last_name": "Blackwell",
            "npi": "1234567893"
        }
    ],
    "submitter": {
        "first_name": "Elizabeth",
        "id": "1234567893",
        "last_name": "Blackwell"
    },
    "trading_partner_id": "MOCKPAYER"
}
```
> Example claims status response when there is an error in the formatting of the provider's NPI or
name, and they are unable to find a match:

```json
{  
    "client_id": "<client_id>",
    "payer":{  
        "name":"MOCKPAYER",
        "id":"MOCKPAYER"
    },
    "providers":[  
        {  
            "trace_number":"0",
            "first_name":"Elizabeth",
            "last_name":"Blackwell",
            "npi":"123456789",
            "statuses":[  
                {  
                    "status_code":"Entity's National Provider Identifier (NPI).",
                    "status_code_value": "562",
                    "status_category":"Data Search Unsuccessful - The payer is unable to return status on the requested claim(s) based on the submitted search criteria.",
                    "status_category_code":"D0",
                    "status_effective_date":"2015-09-25"
                }
            ]
        }
    ],
    "correlation_id":"37045a41-634a-4439-a555-d8d6cbb445ce",
    "trading_partner_id":"MOCKPAYER",
    "submitter":{  
        "first_name":"Elizabeth",
        "last_name":"Aye-Ay",
        "id":"MOCKPAYER"
    }
}
```

> Example claims status response when adjudication is finalized and the claim
has been paid:

```json
{
    "client_id": "<client_id>",
    "patient": {
        "claims": [
            {
                "adjudication_finalized_date": "2014-06-25",
                "applied_to_deductible": false,
                "check_number": "08608-000000000",
                "claim_control_number": "EV30000WY00",
                "claim_payment_amount": {
                    "amount": "156",
                    "currency": "USD"
                },
                "remittance_date": "2014-06-25",
                "service_date": "2014-06-25",
                "service_end_date": "2014-06-25",
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
                        "service_date": "2014-06-25",
                        "service_end_date": "2014-06-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_code_value": "107",
                                "status_category_code": "F2",
                                "status_effective_date": "2014-07-25"
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
                        "service_date": "2014-06-25",
                        "service_end_date": "2014-06-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Payment-The claim/line has been paid.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_code_value": "107",
                                "status_category_code": "F1",
                                "status_effective_date": "2014-07-25"
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
                        "service_date": "2014-06-25",
                        "service_end_date": "2014-06-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_code_value": "107",
                                "status_category_code": "F2",
                                "status_effective_date": "2014-07-25"
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
                        "service_date": "2014-06-25",
                        "service_end_date": "2014-06-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Payment-The claim/line has been paid.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_code_value": "107",
                                "status_category_code": "F1",
                                "status_effective_date": "2014-07-25"
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
                        "service_date": "2014-06-25",
                        "service_end_date": "2014-06-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Payment-The claim/line has been paid.",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_code_value": "107",
                                "status_category_code": "F1",
                                "status_effective_date": "2014-07-25"
                            }
                        ]
                    }
                ],
                "statuses": [
                    {
                        "adjudication_finalized_date": "2014-06-25",
                        "check_number": "08608-000000000",
                        "claim_payment_amount": {
                            "amount": "156",
                            "currency": "USD"
                        },
                        "remittance_date": "2014-06-25",
                        "status_category": "Finalized/Payment-The claim/line has been paid.",
                        "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                        "status_code_value": "107",
                        "status_category_code": "F1",
                        "status_effective_date": "2014-07-25",
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

```json
{
    "client_id": "<client_id>",
    "patient": {
        "claims": [
            {
                "adjudication_finalized_date": "2013-07-25",
                "applied_to_deductible": false,
                "claim_control_number": "EM000000000",
                "claim_payment_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "remittance_date": "2013-07-25",
                "service_date": "2013-07-25",
                "service_end_date": "2013-07-25",
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
                        "service_date": "2013-07-25",
                        "service_end_date": "2013-07-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_category_code": "F2",
                                "status_code": "Subscriber and subscriber id not found.",                                                                     
                                "status_code_value": "33",
                                "status_effective_date": "2014-07-25"
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
                        "service_date": "2013-07-25",
                        "service_end_date": "2013-07-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_category_code": "F2",
                                "status_code": "Subscriber and subscriber id not found.",
			                    "status_code_value": "33",
                                "status_effective_date": "2014-07-25"
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
                        "service_date": "2013-07-25",
                        "service_end_date": "2013-07-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",                                
                                "status_category_code": "F2",
                                "status_code": "Subscriber and subscriber id not found.",
                                "status_code_value": "33",
                                "status_effective_date": "2014-07-25"
                            }
                        ]
                    }
                ],
                "statuses": [
                    {
                        "adjudication_finalized_date": "2013-07-25",
                        "claim_payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "remittance_date": "2013-07-25",
                        "status_category": "Finalized/Denial-The claim/line has been denied.",
                        "status_category_code": "F2",
                        "status_code": "Subscriber and subscriber id not found.",
                        "status_code_value": "33",                        
                        "status_effective_date": "2014-07-25",
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
                "adjudication_finalized_date": "2013-08-25",
                "applied_to_deductible": false,
                "claim_control_number": "EH000000000",
                "claim_payment_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "remittance_date": "2013-08-25",
                "service_date": "2013-07-25",
                "service_end_date": "2013-07-25",
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
                        "service_date": "2013-07-25",
                        "service_end_date": "2013-07-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_category_code": "F2",
                                "status_code": "Subscriber and subscriber id not found.",    
                                "status_code_value": "33",
                                "status_effective_date": "2014-07-25"
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
                        "service_date": "2013-07-25",
                        "service_end_date": "2013-07-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_category_code": "F2",
                                "status_code": "Subscriber and subscriber id not found.",
                                 "status_code_value": "33",
                                "status_effective_date": "2014-07-25"
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
                        "service_date": "2013-07-25",
                        "service_end_date": "2013-07-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_category_code": "F2",
                                "status_code": "Subscriber and subscriber id not found.",
                                "status_code_value": "33",
                                "status_effective_date": "2014-07-25"
                            }
                        ]
                    }
                ],
                "statuses": [
                    {
                        "adjudication_finalized_date": "2013-08-25",
                        "claim_payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "remittance_date": "2013-08-25",
                        "status_category": "Finalized/Denial-The claim/line has been denied.",                        
                        "status_category_code": "F2",
                        "status_code": "Subscriber and subscriber id not found.",
                        "status_code_value": "33",
                        "status_effective_date": "2014-07-25",
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

```json
{
    "client_id": "<client_id>",
    "patient": {
        "claims": [
            {
                "adjudication_finalized_date": "2014-04-25",
                "applied_to_deductible": true,
                "check_number": "814000000000000",
                "claim_control_number": "E6Y0C7NQG00",
                "claim_payment_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "remittance_date": "2014-04-25",
                "service_date": "2014-03-25",
                "service_end_date": "2014-03-25",
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
                        "service_date": "2014-03-25",
                        "service_end_date": "2014-03-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_category_code": "F1",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_code_value": "107",
                                "status_effective_date": "2014-07-25"
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
                        "service_date": "2014-03-25",
                        "service_end_date": "2014-03-25",
                        "statuses": [
                            {
                                "status_category": "Finalized/Denial-The claim/line has been denied.",
                                "status_category_code": "F1",
                                "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                                "status_code_value": "107",
                                "status_effective_date": "2014-07-25"
                            }
                        ]
                    }
                ],
                "statuses": [
                    {
                        "adjudication_finalized_date": "2014-04-25",
                        "check_number": "814000000000000",
                        "claim_payment_amount": {
                            "amount": "0",
                            "currency": "USD"
                        },
                        "remittance_date": "2014-04-25",
                        "status_category": "Finalized/Denial-The claim/line has been denied.",
                        "status_category_code": "F1",
                        "status_code": "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
                        "status_code_value": "107",
                        "status_effective_date": "2014-07-25",
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

*Available modes of operation: batch/async or real-time*

The claims status endpoint allows an application to request information from a trading partner about previously submitted claims.  You may send a request to a trading partner to determine where the claim is in their adjudication system and the status of the claim. The Claims Status endpoint can be used to query the status of multiple claims. The claims status endpoint can be used to check the status of claims in the trading partners' system regardless of the submitter or means of submission. Claims status DOES NOT offer insight into where a claim is in PokitDok's system (for more info on monitoring PokitDok's processing of your claims, please see our [activities endpoint](#activities) and [callback url](#api-callbacks)).

The speed at which a claim is adjudicated is dependent on the trading partner. On average it takes 5-7 days for a claim to enter a payer's adjudication system, thus it is recommended to wait at least a week after submitting a claim to check its status.

To understand how the [Claims](#claims) and [Claims Status](#claims_status) Endpoints work together,
see the [claims API workflow](https://pokitdok.com/developers/api/#api-claims-status).

See the [errors](#errors) section of the documentation for details on Trading Partner specific request processing errors
that may occur with this API for some request/partner combinations.

### Endpoint Description


<!--- beginning of table -->

| Endpoint       | HTTP Method | Description                                                     |
|:---------------|:------------|:----------------------------------------------------------------|
| /claims/status | POST        | Submit a claim status request to the specified trading partner. |

<!--- end of table -->

### Parameters

The `/claims/status` endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter                                | Description                                                                                                                                                                                                                                                                                          |
|:-----------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| claims_activity_id                       | Optional: The [activity_id](#the-meta-and-data-sections) of the original Claim submitted via PokitDok.  Providing this parameter will append the Claims Status response to the response history on the original Claim.                                                                               |   
| claim_charge_amount                      | Total claim charge amount.
| patient                                  | The patient associated with the claim. Uses the member [object](#claims_status_member_object).                                                                                                                                                                                                       |
| provider.first_name                      | The provider’s first name when the provider is an individual.                                                                                                                                                                                                                                        |
| provider.middle_name                     | The provider’s middle name when the provider is an individual.                                                                                                                                                                                                                                       |
| provider.last_name                       | The provider’s last name when the provider is an individual.                                                                                                                                                                                                                                         |
| provider.suffix                          | The provider’s suffix when the provider is an individual.                                                                                                                                                                                                                                            |
| provider.tax_id                          | The provider’s tax identifier.                                                                                                                                                                                                                                                                       |
| provider.npi                             | The NPI for the billing provider.                                                                                                                                                                                                                                                                    |
| provider.organization_name               | The provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                                                                                                                                 |
| provider.service_provider_number         | May be used when no Tax ID or NPI are available, and Service Provider ID has been assigned by the Trading Partner who is receiving the request.                                                                                                                                                                                           												 |
| service_date                             | The date services were performed or started for the claim service period. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                            |
| service_end_date                         | Optional: The date services ended for the claim service period. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                      |
| subscriber                               | Optional: The subscriber associated with the claim. Specify when the patient is not the subscriber. Uses the member [object](#claims_status_member_object).                                                                                                                                          |
| tracking_id                              | Optional: The payer's claim tracking id. Specify this value to refine the search criteria for a claim. If a payer claim control number was returned on the claim submission, this number should be used in the tracking id field for the greatest chance of returning valid claim status information.|
| trading_partner_id                       | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) Endpoint.                                                                                                                                                                                      |
| payer                                    | Information associated with the payer of the claim.                                                                                                                                                                                                                                                  |
| payer.organization_name                  | The organization name of the payer.                                                                                                                                                                                                                                                                  |
| payer.id                                 | The unique identifier of the payer.                                                                                                                                                                                                                                                                  |
| receiver                                 | Information associated with the submitter of the claim status request.                                                                                                                                                                                                                               |
| receiver                                 | Information associated with the submitter of the claim status request.                                                                                                                                                                                                                               |
| receiver.first_name                      | The receiver’s first name when the receiver is an individual.                                                                                                                                                                                                                                        |
| receiver.middle_name                     | The receiver’s middle name when the receiver is an individual.                                                                                                                                                                                                                                       |
| receiver.last_name                       | The receiver’s last name when the receiver is an individual.                                                                                                                                                                                                                                         |
| receiver.id                              | The unique identifier of the receiver.                                                                                                                                                                                                                                                               |
| receiver.organization_name               | The receiver’s name when the receiver is an organization. first_name and last_name should be omitted when sending organization_name.                                                                                                                                                                 |
| pharmacy_prescription_number             | The pharmacy prescription number associated with the claim                                                                                                                                                                                                                                           |

<!--- end of table -->

### Response

The `/claim/status` response contains the following fields:

<!--- beginning of table -->

| Field                                                 | Description                                                                                                                                                                                                                                                                                                                                        |
|:------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| client_id                                             | The unique identifier associated with the client making the claims status request.                                                                                                                                                                                                                                                                   |
| trading_partner_id                                    | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.                                                                                                                                                                                                                                    |
| payer                                                 | Information associated with the payer of the claim.                                                                                                                                                                                                                                                                                                |
| payer.name                                            | The name of the payer                                                                                                                                                                                                                                                                                                                              |
| payer.id                                              | The unique identifier of the payer.                                                                                                                                                                                                                                                                                                                  |
| submitter                                             | Information associated with the submitter of the claim status request.                                                                                                                                                                                                                                                                             |
| submitter.first_name                                  | The submitter’s first name when the submitter is an individual.                                                                                                                                                                                                                                                                                    |
| submitter.middle_name                                 | The submitter’s middle name when the submitter is an individual.                                                                                                                                                                                                                                                                                   |
| submitter.last_name                                   | The submitter’s last name when the submitter is an individual.                                                                                                                                                                                                                                                                                     |
| submitter.id                                          | The unique identifier of the submitter.                                                                                                                                                                                                                                                                                                            |
| submitter.organization_name                           | The submitter’s name when the submitter is an organization.                                                                                                                                                                                                                                                                                        |
| submitter.tracking_id                                 | The tracking identifier associated with the submitter.                                                                                                                                                                                                                                                                                             |
| submitter.statuses                                    | A list of statuses associated with the submitter. Uses the status information [object](#claims_status_status_information).                                                                                                                                                                                                                         |
| submitter.accepted_quantity                           | # of units being accepted.                                                                                                                                                                                                                                                                                                                         |
| submitter.rejected_quantity                           | # of units being rejected.                                                                                                                                                                                                                                                                                                                         |
| submitter.amount_in_process                           | The monetary amount of claims currently in process. Uses the monetary amount [object](#claims-status-monetary-amount).                                                                                                                                                                                                                             |
| submitter.amount_returned                             | The monetary amount returned based on claims. Uses the monetary amount [object](#claims-status-monetary-amount).                                                                                                                                                                                                                                   |
| providers                                             | List of providers associated with the claim status request.                                                                                                                                                                                                                                                                                        |
| providers.first_name                                  | The provider’s first name when the provider is an individual.                                                                                                                                                                                                                                                                                      |
| providers.middle_name                                 | The provider’s middle name when the provider is an individual.                                                                                                                                                                                                                                                                                     |
| providers.last_name                                   | The provider’s last name when the provider is an individual.                                                                                                                                                                                                                                                                                       |
| providers.suffix                                      | The provider’s suffix when the provider is an individual.                                                                                                                                                                                                                                                                                          |
| providers.tax_id                                      | The unique tax identifier of the provider.                                                                                                                                                                                                                                                                                                         |
| providers.npi                                         | The provider's NPI.                                                                                                                                                                                                                                                                                                                                |
| providers.service_provider_number                     | The service provider number assigned by the trading partner.                                                                                                                                                                                                                                                                                       |
| providers.trace_number                                | The trace number associated with the provider.                                                                                                                                                                                                                                                                                                     |
| providers.secondary_id                                | Secondary identifiers for the provider.                                                                                                                                                                                                                                                                                                            |
| providers.secondary_id.id_qualifier                   | Qualifier associated with the provider's secondary identifier.                                                                                                                                                                                                                                                                                     |
| providers.secondary_id.id                             | The actual id associated with the provider's secondary identifier.                                                                                                                                                                                                                                                                                 |
| providers.organization_name                           | The provider’s name when the providers is an organization.                                                                                                                                                                                                                                                                                         |
| providers.statuses                                    | A list of statuses associated with the provider. Uses the status information [object](#claims_status_status_information).                                                                                                                                                                                                                          |
| providers.accepted_quantity                           | # of units being accepted.                                                                                                                                                                                                                                                                                                                         |
| providers.rejected_quantity                           | # of units being rejected.                                                                                                                                                                                                                                                                                                                         |
| providers.amount_in_process                           | The monetary amount of claims currently in process. Uses the monetary amount [object](#claims-status-monetary-amount).                                                                                                                                                                                                                             |
| providers.amount_returned                             | The monetary amount returned based on claims. Uses the monetary amount [object](#claims-status-monetary-amount).                                                                                                                                                                                                                                   |
| patient                                               | Information about a patient including any matching claims.                                                                                                                                                                                                                                                                                         |
| patient.claims                                        | A list of matching claims returned by the trading partner for a claims status request.                                                                                                                                                                                                                                                             |
| patient.claims.adjudication_finalized_date            | The date adjudication was finalized for the claim. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                 |
| patient.claims.applied_to_deductible                  | Boolean that indicates whether or not claim charges are applied to the deductible.                                                                                                                                                                                                                                                                 |
| patient.claims.patient_control_number                 | The control number associated with a patient. This number is assigned by the payer.                                                                                                                                                                                                                                                                |
| patient.claims.claim_id_number                        | The id number associated with a claim.                                                                                                                                                                                                                                                                                                             |
| patient.claims.bill_type_id                           | The bill type id associated with a claim.                                                                                                                                                                                                                                                                                                          |
| patient.claims.pharmacy_prescription_number           | The pharmacy prescription number associated with a claim.                                                                                                                                                                                                                                                                                          |
| patient.claims.tracking_id                            | The patient's claim tracking id.                                                                                                                                                                                                                                                                                                                   |
| patient.claims.status_code                            | Indicates the status of the service on the claim.                                                                                                                                                                                                                                                                                                  |
| patient.claims.check_number                           | The check or EFT trace number for a claim payment.                                                                                                                                                                                                                                                                                                 |
| patient.claims.claim_control_number                   | The Payer's Claim Control Number.                                                                                                                                                                                                                                                                                                                  |
| patient.claims.claim_payment_amount                   | The amount that's been paid on the claim. Uses the monetary amount [object](#claims-status-monetary-amount).                                                                                                                                                                                                                                       |
| patient.claims.remittance_date                        | The date the check was issued or EFT funds became available. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                       |
| patient.claims.service_date                           | The date services were performed or started for the claim service period. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                          |
| patient.claims.service_end_date                       | The date services ended for the claim service period. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                              |
| patient.claims.services                               | A list of services linked to the claim.                                                                                                                                                                                                                                                                                                            |
| patient.claims.services.charge_amount                 | The amount charged for a particular service on the claim. Uses the monetary amount [object](#claims-status-monetary-amount).                                                                                                                                                                                                                       |
| patient.claims.services.cpt_code                      | The CPT code indicating the type of service that was performed.                                                                                                                                                                                                                                                                                    |
| patient.claims.services.payment_amount                | The amount paid for a particular service on the claim. Uses the monetary amount [object](#claims-status-monetary-amount).                                                                                                                                                                                                                          |
| patient.claims.services.service_date                  | The date the service was performed or started for the claim service period. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                        |
| patient.claims.services.service_end_date              | The date the service ended for the claim service period. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                           |
| patient.claims.services.statuses                      | A listing of status information for the claim. Uses the status information [object](#claims_status_status_information).                                                                                                                                                                                                                            |
| patient.claims.services.line_item_control_number      | The line item control number associated with a patient's service.                                                                                                                                                                                                                                                                                  |
| patient.claims.services.pharmacy_prescription_number  | The pharmacy prescription number associated with a service.                                                                                                                                                                                                                                                                                        |
| patient.claims.statuses                               | A listing of status information for the claim. Uses the status information [object](#claims_status_status_information).                                                                                                                                                                                                                            |
| patient.claims.total_claim_amount                     | The total charges submitted for the claim. Uses the monetary amount [object](#claims-status-monetary-amount).                                                                                                                                                                                                                                      |
| patient.first_name                                    | The patient’s first name as specified on their policy.                                                                                                                                                                                                                                                                                             |
| patient.middle_name                                   | The patient’s middle name as specified on their policy.                                                                                                                                                                                                                                                                                            |
| patient.id                                            | The patient’s member identifier.                                                                                                                                                                                                                                                                                                                   |
| patient.last_name                                     | The patient’s last name as specified on their policy.                                                                                                                                                                                                                                                                                              |
| patient.suffix                                        | The patient’s suffix.                                                                                                                                                                                                                                                                                                                              |

<!--- end of table -->

### Additional Object Tables

<a name="claims_status_member_object"></a>
Member object:

<!--- beginning of table -->

| Field                             | Description                                                                                           |
|:----------------------------------|:------------------------------------------------------------------------------------------------------|
| birth_date                        | The members’s birth date as specified on their policy. In ISO8601 format (YYYY-MM-DD).                |
| gender                            | The member's gender (Male, Female, Unknown)                                                           |
| last_name                         | The member’s last name as specified on their policy.                                                  |
| first_name                        | The member’s first name as specified on their policy.                                                 |
| middle_name                       | The member’s middle name as specified on their policy.                                                |
| suffix                            | The suffix for the member                                                                             |
| id                                | The member identifier.                                                                                |

<!--- end of table -->

<a name="claims_status_status_information"></a>
Status Information object:

<!--- beginning of table -->

| Field                             | Description                                                                                                                                                                                                                                                                                                                                        |
|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| status_category                   | A verbose message about the general category of the claim's status (e.g. accepted, rejected, etc.). This value is suitable for display to users of a system utilizing the claims status API. A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).            |
| status_category_code              | The code indicating the general category of the claim's status. The status category code is more appropriate for use by the software using the claims status API to categorize the information. A full listing of codes can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).                   |
| status_effective_date             | The effective date associated with a claim's status. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                               |
| secondary_status_category         | A verbose message about the general category of the claim's status (e.g. accepted, rejected, etc.). This value is suitable for display to users of a system utilizing the claims status API. A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).            |
| secondary_status_category_code    | The code indicating the general category of the claim's status. The status category code is more appropriate for use by the software using the claims status API to categorize the information. A full listing of codes can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).                   |
| secondary_status_code             | Indicates the status of the claim. This status code provides more detail to support the status category. This value is suitable for display to users of a system utilizing the claims status API. A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).       |
| tertiary_status_category          | A verbose message about the general category of the claim's status (e.g. accepted, rejected, etc.). This value is suitable for display to users of a system utilizing the claims status API. A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).            |
| tertiary_status_category_code     | The code indicating the general category of the claim's status. The status category code is more appropriate for use by the software using the claims status API to categorize the information. A full listing of codes can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).                   |
| tertiary_status_code              | Indicates the status of the claim. This status code provides more detail to support the status category. This value is suitable for display to users of a system utilizing the claims status API. A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/).       |
| adjudication_finalized_date       | Date that the claim is paid or declined. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                           |
| remittance_date                   | The date the check was issued or EFT funds became available. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                       |
| status_code                       | Indicates the status of the claim. This status code provides more detail to support the status category. This value is suitable for display to users of a system utilizing the claims status API. A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-codes/).                |
| status_code_value                 | Indicates the raw status code value returned in the X12 277 claim status response. This value may be helpful to API clients that previously worked with X12 277 data directly and wish to continue to operate on the status code value while using the claims status API's JSON response format.  A full listing of possible values can be found [here](http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-codes/). |
| total_claim_amount                | The total monetary amount of the claim. Uses the monetary amount [object](#claims-status-monetary-amount).                                                                                                                                                                                                                                         |
| claim_payment_amount              | The amount that's been paid on the claim. Uses the monetary amount [object](#claims-status-monetary-amount).                                                                                                                                                                                                                                       |
| check_number                      | The check or EFT trace number for a claim payment.                                                                                                                                                                                                                                                                                                 |

<!--- end of table -->

<a name="claims-status-monetary-amount"></a>
Monetary amount object:

<!--- beginning of table -->

| Field                                 | Description                                                                                                                                                                               |
|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| amount                                | The value amount for this item.                                                                                                                                                           |
| currency                              | The currency used in the amount.                                                                                                                                                          |

<!--- end of table -->
