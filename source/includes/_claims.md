## Claims
> Sample Claims request:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "J10.1"
                ],
                "service_date": "2016-01-25"
            }
        ]
    }
}` https://platform.pokitdok.com/api/v4/claims/
```

```python
client.claims({
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "J10.1"
                ],
                "service_date": "2016-01-25"
            }
        ]
    }
})
```

```ruby
client.claims({
    transaction_code: "chargeable",
    trading_partner_id: "MOCKPAYER",
    billing_provider: {
        taxonomy_code: "207Q00000X",
        first_name: "Jerome",
        last_name: "Aya-Ay",
        npi: "1467560003",
        address: {
            address_lines: [
                "8311 WARREN H ABERNATHY HWY"
            ],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        tax_id: "123456789"
    },
    subscriber: {
        first_name: "Jane",
        last_name: "Doe",
        member_id: "W000000000",
        address: {
            address_lines: ["123 N MAIN ST"],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        birth_date: "1970-01-25",
        gender: "female"
    },
    claim: {
        total_charge_amount: 60.0,
        service_lines: [
            {
                procedure_code: "99213",
                charge_amount: 60.0,
                unit_count: 1.0,
                diagnosis_codes: [
                    "J10.1"
                ],
                service_date: "2016-01-25"
            }
        ]
    }
});
```

```csharp
client.claims(
    new Dictionary<string, object> {
        {"transaction_code", "chargeable"},
        {"trading_partner_id", "MOCKPAYER"},
        {"billing_provider", new Dictionary<string, object> {
            {"taxonomy_code", "207Q00000X"},
            {"first_name", "Jerome"},
            {"last_name", "Aya-Ay"},
            {"npi", "1467560003"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"8311 WARREN H ABERNATHY HWY"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"tax_id", "123456789"}
        }},
        {"subscriber", new Dictionary<string, object> {
            {"first_name", "Jane"},
            {"last_name", "Doe"},
            {"member_id", "W000000000"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"123 N MAIN ST"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"birth_date", "1970-01-25"},
            {"gender", "female"}
        }},
        {"claim", new Dictionary<string, object> {
            {"total_charge_amount", 60.0},
            {"service_lines", new Object[] {
                new Dictionary<string, object> {
                    {"procedure_code", "99213"},
                    {"charge_amount", 60.0},
                    {"unit_count", 1.0},
                    {"diagnosis_codes", new string[] {"J10.1"}},
                    {"service_date", "2016-01-25"}
        }}}}}
    });
```

```java
StringBuffer buf = new StringBuffer();
buf.append("{");
buf.append("    \"transaction_code\": \"chargeable\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\",");
buf.append("    \"billing_provider\": {");
buf.append("        \"taxonomy_code\": \"207Q00000X\",");
buf.append("        \"first_name\": \"Jerome\",");
buf.append("        \"last_name\": \"Aya-Ay\",");
buf.append("        \"npi\": \"1467560003\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [");
buf.append("                \"8311 WARREN H ABERNATHY HWY\"");
buf.append("            ],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"tax_id\": \"123456789\"");
buf.append("    },");
buf.append("    \"subscriber\": {");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"member_id\": \"W000000000\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [\"123 N MAIN ST\"],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"gender\": \"female\"");
buf.append("    },");
buf.append("    \"claim\": {");
buf.append("        \"total_charge_amount\": 60.0,");
buf.append("        \"service_lines\": [");
buf.append("            {");
buf.append("                \"procedure_code\": \"99213\",");
buf.append("                \"charge_amount\": 60.0,");
buf.append("                \"unit_count\": 1.0,");
buf.append("                \"diagnosis_codes\": [");
buf.append("                    \"J10.1\"");
buf.append("                ],");
buf.append("                \"service_date\": \"2016-01-25\"");
buf.append("            }");
buf.append("        ]");
buf.append("    }");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claims(query);
```

```swift
let data = [
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": [
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": [
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "tax_id": "123456789"
    ],
    "subscriber": [
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": [
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "birth_date": "1970-01-25",
        "gender": "female"
    ],
    "claim": [
        "total_charge_amount": 60.0,
        "service_lines": [
            [
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "J10.1"
                ],
                "service_date": "2016-01-25"
            ]
        ]
    ]
] as [String:Any]
try client.claims(params: data)
```

> Sample PokitDok response to initial claim submission that passes validation checks:

```json
{
  "_type": "PlatformActivityModel",
  "_uuid": "baaf7704-9719-4f7e-92cd-f489b5fd0679",
  "history": [
    {
      "name": "init",
      "record_dt": "2016-06-25T13:42:07.834940",
      "title": "Initializing"
    }
  ],
  "id": "575037af0640fd518fe64c36",
  "name": "claims",
  "parameters": {
    "async": false,
    "billing_provider": {
      "address": {
        "address_lines": [
          "8311 WARREN H ABERNATHY HWY"
        ],
        "city": "SPARTANBURG",
        "state": "SC",
        "zipcode": "29301"
      },
      "first_name": "Jerome",
      "last_name": "Aya-Ay",
      "npi": "1467560003",
      "tax_id": "123456789",
      "taxonomy_code": "207Q00000X"
    },
    "claim": {
      "claim_frequency": "original",
      "direct_payment": "y",
      "information_release": "informed_consent",
      "place_of_service": "office",
      "plan_participation": "assigned",
      "provider_signature": true,
      "service_lines": [
        {
          "charge_amount": "60.0",
          "diagnosis_codes": [
            "J10.1"
          ],
          "procedure_code": "99213",
          "service_date": "2016-01-25",
          "unit_count": "1.0",
          "unit_type": "units"
        }
      ],
      "total_charge_amount": "60.0"
    },
    "correlation_id": "0e6ade93-5672-4abd-8d36-ba23cda627bd",
    "generate_pdf": false,
    "payer": {
      "id": "MOCKPAYER",
      "organization_name": "MOCKPAYER"
    },
    "receiver": {
      "id": "MOCKRECEIVER",
      "organization_name": "MOCKRECEIVER"
    },
    "submitter": {
      "email": "support@pokitdok.com",
      "id": "POKITDOKTEST",
      "organization_name": "POKITDOK TESTING"
    },
    "subscriber": {
      "address": {
        "address_lines": [
          "123 N MAIN ST"
        ],
        "city": "SPARTANBURG",
        "state": "SC",
        "zipcode": "29301"
      },
      "birth_date": "1970-01-25",
      "first_name": "Jane",
      "gender": "female",
      "last_name": "Doe",
      "member_id": "W000000000",
      "payer_responsibility": "primary"
    },
    "trading_partner_id": "MOCKPAYER",
    "transaction_code": "chargeable"
  },
  "remaining_transitions": [
    "generate",
    "store",
    "transmit",
    "wait",
    "receive",
    "process",
    "complete"
  ],
  "state": {
    "name": "scheduled",
    "title": "Scheduled for next available transmission to Trading Partner"
  },
  "trading_partner_id": "MOCKPAYER",
  "transition_path": [
    "schedule",
    "generate",
    "store",
    "transmit",
    "wait",
    "receive",
    "process",
    "complete"
  ],
  "units_of_work": 1
}
```

> Sample trading partner response for claim acknowledgement (this response will complete a claims activity):

```json
{
    "client_id": "ASDFBOI87234CSDEAR",
    "correlation_id": "575037af0640fd518fe64c36",
    "trading_partner_id": "MOCKPAYER",
    "clearinghouse": {
        "name": "MOCK CLEARINGHOUSE",
        "transmitter_id": "12345678",
        "date_received": "2016-12-05",
        "date_processed": "2016-12-05"
    },
    "submitter": {
        "organization_name": "POKITDOK TESTING",
        "id": "1234567890",
        "tracking_id": "20161205123456789",
        "statuses": [
            {
                "action": "accept",
                "status_category": "Acknowledgement/Receipt-The claim/encounter has been received. This does not mean that the claim has been accepted for adjudication.",
                "status_category_code": "A1",
                "status_effective_date": "2016-12-05",
                "status_code": "Accepted for processing.",
                "total_claim_amount": {
                    "amount": "60.0",
                    "currency": "USD"
                }
            }
        ],
        "accepted_quantity": "1",
        "amount_in_process": {
            "amount": "60.0",
            "currency": "USD"
        }
    },
    "providers": [
        {
             "first_name": "Jerome",
             "last_name": "Aya-Ay",
             "npi": "1467560003",
             "tax_id": "123456789",
             "trace_number": "0",
             "accepted_quantity": "1",
             "amount_in_process": {
                "amount": "60.0",
                "currency": "USD"
            }
        }
    ],
    "patient": {
        "last_name": "DOE",
        "first_name": "JANE",
        "id": "W000000000",
        "claim_level_info": {
            "statuses": [
                {
                    "action": "accept",
                    "status_category": "Acknowledgement/Receipt-The claim/encounter has been received. This does not mean that the claim has been accepted for adjudication.",
                    "status_category_code": "A1",
                    "status_effective_date": "2016-12-05",
                    "status_code": "Accepted for processing.",
                    "total_claim_amount": {
                        "amount": "60.0",
                        "currency": "USD"
                    }
                }
            ],
            "claim_id_number": "NA",
            "service_date": "2016-11-01",
            "service_end_date": "2016-11-02",
            "tracking_id": "ASDFBOI87234CSDEAR"
        }
    }
}
```

> Sample trading partner response for claim payment (835):

```json
{
    "claim_payments": [
        {
            "assigned_number": 654654,
            "control_number": "20161205123456789",
            "facility_type": "hospital_inpatient_part_a",
            "claim_frequency": "original",
            "filing_indicator": "health_maintenance_organization",
            "patient_control_number": "20161205123456789",
            "payment_amount": {
                "amount": "0",
                "currency": "USD"
            },
            "patient_responsibility_amount": {
                "amount": "0",
                "currency": "USD"
            },
            "services": [
                {
                    "adjustments": [
                        {
                            "amount": {
                                "amount": "60.0",
                                "currency": "USD"
                            },
                            "group": "contractual_obligations",
                            "reason": "Exact duplicate claim/service",
                            "reason_code": "18"
                        }
                    ],
                    "adjudicated_procedure_code": "26740",
                    "adjudicated_procedure_code_qualifier": "health_care",
                    "adjudicated_procedure_modifier_codes": [
                                "GT"
                            ],
                    "charge_amount": {
                        "amount": "60.0",
                        "currency": "USD"
                    },
                    "provider_payment_amount": {
                        "amount": "0",
                        "currency": "USD"
                    },
                    "service_units_paid": 1,
                    "service_units_submitted": 1,
                    "service_date": "2016-11-01",
                    "control_number": "20161205123456789",
                    "remarks": [
                       {
                          "description": "Service denied because payment already made for same/similar procedure within set time frame.",
                          "code": "M86"
                        }
                    ]
                }
            ],
            "status": "processed_as_primary",
            "total_charge_amount": {
                "amount": "60.0",
                "currency": "USD"
            }
        }
    ],
    "financial_information": {
        "check_eft_trace_number": "EFT2016120798749874",
        "transaction_type": "credit",
        "effective_date": "2016-12-05",
        "originating_company_id": "121212123",
        "payment_amount": {
            "amount": "3210.10",
            "currency": "USD"
        },
        "payment_method": "automated_clearing_house",
        "transaction_handling": "remittance_information_only"
    },
    "payee": {
        "name": "POKITDOK INC",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "npi": "1234567890",
        "tax_id": "987654321"
    },
    "payer": {
        "name": "MOCKPAYER",
        "address": {
            "address_lines": [
                "P.O. BOX 12345"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "294011234"
        },
        "contacts": [
            {
                "function": "business",
                "contact_methods": [
                    {
                        "type": "phone",
                        "value": "8431111111"
                    },
                    {
                        "type": "phone",
                        "value": "8001111111"
                    }
                ]
            },
            {
                "function": "technical",
                "contact_methods": [
                    {
                        "type": "url",
                        "value": "WWW.HELP.COM"
                    }
                ]
            }
        ]
    },
    "patient": {
        "last_name": "DOE",
        "first_name": "JANE",
        "id": "W000000000"
    },
    "production_date": "2016-12-05",
    "transaction_type": "remittance_information_only",
    "meta": {
       "transaction_created_date": "2016-12-08"
    }
}
```

> Sample Claims request where the patient is not the subscriber:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
"transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "patient": {
        "first_name": "John",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1971-01-25",
        "gender": "male",
        "relationship" : "child"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 100.0,
        "service_lines": [
            {
                "procedure_code": "99201",
                "procedure_modifier_codes": ["GT"],
                "charge_amount": 100.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "J10.1"
                ],
                "service_date": "2016-01-25"
            }
        ]
    }
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
client.claims({
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "patient": {
        "first_name": "John",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1971-01-25",
        "gender": "male",
        "relationship": "child"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 100.0,
        "service_lines": [
            {
                "procedure_code": "99201",
                "procedure_modifier_codes": ["GT"],
                "charge_amount": 100.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "J10.1"
                ],
                "service_date": "2016-01-25"
            }
        ]
    }
})
```

```ruby
client.claims({
    transaction_code: "chargeable",
    trading_partner_id: "MOCKPAYER",
    billing_provider: {
        taxonomy_code: "207Q00000X",
        first_name: "Jerome",
        last_name: "Aya-Ay",
        npi: "1467560003",
        address: {
            address_lines: [
                "8311 WARREN H ABERNATHY HWY"
            ],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        tax_id: "123456789"
    },
    patient: {
        first_name: "John",
        last_name: "Doe",
        member_id: "W000000000",
        address: {
            address_lines: ["123 N MAIN ST"],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        birth_date: "1971-01-25",
        gender: "male",
        relationship: "child"
    },
    subscriber: {
        first_name: "Jane",
        last_name: "Doe",
        member_id: "W000000000",
        address: {
            address_lines: ["123 N MAIN ST"],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        birth_date: "1970-01-25",
        gender: "female"
    },
    claim: {
        total_charge_amount: 100.0,
        service_lines: [
            {
                procedure_code: "99201",
                procedure_modifier_codes: ["GT"],
                charge_amount: 100.0,
                unit_count: 1.0,
                diagnosis_codes: [
                    "J10.1"
                ],
                service_date: "2016-01-25"
            }
        ]
    }
})
```

```csharp
client.claims(
    new Dictionary<string, object> {
        {"transaction_code", "chargeable"},
        {"trading_partner_id", "MOCKPAYER"},
        {"billing_provider", new Dictionary<string, object> {
            {"taxonomy_code", "207Q00000X"},
            {"first_name", "Jerome"},
            {"last_name", "Aya-Ay"},
            {"npi", "1467560003"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"8311 WARREN H ABERNATHY HWY"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"tax_id", "123456789"}
        }},
        {"patient", new Dictionary<string, object> {
            {"first_name", "John"},
            {"last_name", "Doe"},
            {"member_id", "W000000000"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"123 N MAIN ST"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"birth_date", "1971-01-25"},
            {"gender", "male"},
            {"relationship" , "child"}
        }},
        {"subscriber", new Dictionary<string, object> {
            {"first_name", "Jane"},
            {"last_name", "Doe"},
            {"member_id", "W000000000"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"123 N MAIN ST"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"birth_date", "1970-01-25"},
            {"gender", "female"}
        }},
        {"claim", new Dictionary<string, object> {
            {"total_charge_amount", 100.0},
            {"service_lines", new Object[] {new Dictionary<string, object> {
                {"procedure_code", "99201"},
                {"procedure_modifier_codes", new string[] {"GT"}},
                {"charge_amount", 100.0},
                {"unit_count", 1.0},
                {"diagnosis_codes", new string[] {"J10.1"}},
                {"service_date", "2016-01-25"}
        }}}}}
    });
```

```java
StringBuffer buf = new StringBuffer();
buf.append("{");
buf.append("\"transaction_code\": \"chargeable\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\",");
buf.append("    \"billing_provider\": {");
buf.append("        \"taxonomy_code\": \"207Q00000X\",");
buf.append("        \"first_name\": \"Jerome\",");
buf.append("        \"last_name\": \"Aya-Ay\",");
buf.append("        \"npi\": \"1467560003\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [");
buf.append("                \"8311 WARREN H ABERNATHY HWY\"");
buf.append("            ],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"tax_id\": \"123456789\"");
buf.append("    },");
buf.append("    \"patient\": {");
buf.append("        \"first_name\": \"John\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"member_id\": \"W000000000\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [\"123 N MAIN ST\"],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"birth_date\": \"1971-01-25\",");
buf.append("        \"gender\": \"male\",");
buf.append("        \"relationship\": \"child\"");
buf.append("    },");
buf.append("    \"subscriber\": {");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"member_id\": \"W000000000\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [\"123 N MAIN ST\"],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"gender\": \"female\"");
buf.append("    },");
buf.append("    \"claim\": {");
buf.append("        \"total_charge_amount\": 100.0,");
buf.append("        \"service_lines\": [");
buf.append("            {");
buf.append("                \"procedure_code\": \"99201\",");
buf.append("                \"procedure_modifier_codes\": [\"GT\"],");
buf.append("                \"charge_amount\": 100.0,");
buf.append("                \"unit_count\": 1.0,");
buf.append("                \"diagnosis_codes\": [");
buf.append("                    \"J10.1\"");
buf.append("                ],");
buf.append("                \"service_date\": \"2016-01-25\"");
buf.append("            }");
buf.append("        ]");
buf.append("    }");
buf.append("");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claims(query);
```

```swift
let data = [
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": [
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": [
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "tax_id": "123456789"
    ],
    "patient": [
        "first_name": "John",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": [
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "birth_date": "1971-01-25",
        "gender": "male",
        "relationship": "child"
    ],
    "subscriber": [
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": [
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "birth_date": "1970-01-25",
        "gender": "female"
    ],
    "claim": [
        "total_charge_amount": 100.0,
        "service_lines": [
            [
                "procedure_code": "99201",
                "procedure_modifier_codes": ["GT"],
                "charge_amount": 100.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "J10.1"
                ],
                "service_date": "2016-01-25"
            ]
        ]
    ]
] as [String:Any]
try client.claims(params: data)
```

> Sample Claims request that includes custom application data for easy handling
of asynchronous responses:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "application_data": {
        "patient_id": "ABC1234XYZ",
        "location_id": 123,
        "transaction_uuid": "93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf"
    },
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "293010000"
        },
       "payment_address": {
            "address_lines": [
                "123 ABC LANE"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "294010000"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "J10.1"
                ],
                "service_date": "2016-01-25"
            }
        ]
    }
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
client.claims({
    "application_data": {
        "patient_id": "ABC1234XYZ",
        "location_id": 123,
        "transaction_uuid": "93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf"
    },
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "payment_address": {
            "address_lines": [
                "123 ABC LANE"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "294010000"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "J10.1"
                ],
                "service_date": "2016-01-25"
            }
        ]
    }
})
```

```ruby
client.claims({
    application_data: {
        patient_id: "ABC1234XYZ",
        location_id: 123,
        transaction_uuid: "93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf"
    },
    transaction_code: "chargeable",
    trading_partner_id: "MOCKPAYER",
    billing_provider: {
        taxonomy_code: "207Q00000X",
        first_name: "Jerome",
        last_name: "Aya-Ay",
        npi: "1467560003",
        address: {
            address_lines: [
                "8311 WARREN H ABERNATHY HWY"
            ],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        tax_id: "123456789"
    },
    subscriber: {
        first_name: "Jane",
        last_name: "Doe",
        member_id: "W000000000",
        address: {
            address_lines: ["123 N MAIN ST"],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        birth_date: "1970-01-25",
        gender: "female"
    },
    claim: {
        total_charge_amount: 60.0,
        service_lines: [
            {
                procedure_code: "99213",
                charge_amount: 60.0,
                unit_count: 1.0,
                diagnosis_codes: [
                    "J10.1"
                ],
                service_date: "2016-01-25"
            }
        ]
    }
})
```

```csharp
client.claims(
    new Dictionary<string, object> {
        {"application_data", new Dictionary<string, object> {
            {"patient_id", "ABC1234XYZ"},
            {"location_id", 123},
            {"transaction_uuid", "93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf"}
        }},
        {"transaction_code", "chargeable"},
        {"trading_partner_id", "MOCKPAYER"},
        {"billing_provider", new Dictionary<string, object> {
            {"taxonomy_code", "207Q00000X"},
            {"first_name", "Jerome"},
            {"last_name", "Aya-Ay"},
            {"npi", "1467560003"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"8311 WARREN H ABERNATHY HWY"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"tax_id", "123456789"}
        }},
        {"subscriber", new Dictionary<string, object> {
            {"first_name", "Jane"},
            {"last_name", "Doe"},
            {"member_id", "W000000000"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"123 N MAIN ST"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"birth_date", "1970-01-25"},
            {"gender", "female"}
        }},
        {"claim", new Dictionary<string, object> {
            {"total_charge_amount", 60.0},
            {"service_lines", new Object[] {new Dictionary<string, object> {
                {"procedure_code", "99213"},
                {"charge_amount", 60.0},
                {"unit_count", 1.0},
                {"diagnosis_codes", new string[] {"J10.1"}},
                {"service_date", "2016-01-25"}
        }}}}}
    });
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"application_data\": {");
buf.append("        \"patient_id\": \"ABC1234XYZ\",");
buf.append("        \"location_id\": 123,");
buf.append("        \"transaction_uuid\": \"93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf\"");
buf.append("    },");
buf.append("    \"transaction_code\": \"chargeable\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\",");
buf.append("    \"billing_provider\": {");
buf.append("        \"taxonomy_code\": \"207Q00000X\",");
buf.append("        \"first_name\": \"Jerome\",");
buf.append("        \"last_name\": \"Aya-Ay\",");
buf.append("        \"npi\": \"1467560003\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [");
buf.append("                \"8311 WARREN H ABERNATHY HWY\"");
buf.append("            ],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"tax_id\": \"123456789\"");
buf.append("    },");
buf.append("    \"subscriber\": {");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"member_id\": \"W000000000\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [\"123 N MAIN ST\"],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"gender\": \"female\"");
buf.append("    },");
buf.append("    \"claim\": {");
buf.append("        \"total_charge_amount\": 60.0,");
buf.append("        \"service_lines\": [");
buf.append("            {");
buf.append("                \"procedure_code\": \"99213\",");
buf.append("                \"charge_amount\": 60.0,");
buf.append("                \"unit_count\": 1.0,");
buf.append("                \"diagnosis_codes\": [");
buf.append("                    \"J10.1\"");
buf.append("                ],");
buf.append("                \"service_date\": \"2016-01-25\"");
buf.append("            }");
buf.append("        ]");
buf.append("    }");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claims(query);
```

```swift
let data = [
    "application_data": [
        "patient_id": "ABC1234XYZ",
        "location_id": 123,
        "transaction_uuid": "93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf"
    ],
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": [
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": [
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "tax_id": "123456789"
    ],
    "subscriber": [
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": [
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "birth_date": "1970-01-25",
        "gender": "female"
    ],
    "claim": [
        "total_charge_amount": 60.0,
        "service_lines": [
            [
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "J10.1"
                ],
                "service_date": "2016-01-25"
            ]
        ]
    ]
] as [String:Any]
try client.claims(params: data)
```

> Sample Claims Request using the patient paid amount to report a cash payment
encounter for contributing toward a member's deductible:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "JEROME",
        "last_name": "AYA-AY",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "1703 John B White Blvd, Unit A"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "JOHN",
        "last_name": "DOE",
        "member_id": "W199000000",
        "address": {
            "address_lines": ["123 MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "male"
    },
    "claim": {
        "place_of_service": "office",
        "total_charge_amount": 150.0,
        "patient_paid_amount": 150.0,
        "service_lines": [
            {
                "procedure_code": "11100",
                "charge_amount": 150.00,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "L90.9"
                ],
                "service_date": "2016-03-25"
            }
        ]
    }
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
client.claims({
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "JEROME",
        "last_name": "AYA-AY",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "1703 John B White Blvd, Unit A"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "JOHN",
        "last_name": "DOE",
        "member_id": "W199000000",
        "address": {
            "address_lines": ["123 MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "male"
    },
    "claim": {
        "place_of_service": "office",
        "total_charge_amount": 150.0,
        "patient_paid_amount": 150.0,
        "service_lines": [
            {
                "procedure_code": "11100",
                "charge_amount": 150.00,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "L90.9"
                ],
                "service_date": "2016-03-25"
            }
        ]
    }
})
```

```ruby
client.claims({
    transaction_code: "chargeable",
    trading_partner_id: "MOCKPAYER",
    billing_provider: {
        taxonomy_code: "207Q00000X",
        first_name: "JEROME",
        last_name: "AYA-AY",
        npi: "1467560003",
        address: {
            address_lines: [
                "1703 John B White Blvd, Unit A"
            ],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        tax_id: "123456789"
    },
    subscriber: {
        first_name: "JOHN",
        last_name: "DOE",
        member_id: "W199000000",
        address: {
            address_lines: ["123 MAIN ST"],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        birth_date: "1970-01-25",
        gender: "male"
    },
    claim: {
        place_of_service: "office",
        total_charge_amount: 150.0,
        patient_paid_amount: 150.0,
        service_lines: [
            {
                procedure_code: "11100",
                charge_amount: 150.00,
                unit_count: 1.0,
                diagnosis_codes: [
                    "L90.9"
                ],
                service_date: "2016-03-25"
            }
        ]
    }
})
```

```csharp
client.claims(
    new Dictionary<string, object> {
        {"transaction_code", "chargeable"},
        {"trading_partner_id", "MOCKPAYER"},
        {"billing_provider", new Dictionary<string, object> {
            {"taxonomy_code", "207Q00000X"},
            {"first_name", "JEROME"},
            {"last_name", "AYA-AY"},
            {"npi", "1467560003"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"1703 John B White Blvd, Unit A"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
        }},
        {"tax_id", "123456789"}
    }},
    {"subscriber", new Dictionary<string, object> {
        {"first_name", "JOHN"},
        {"last_name", "DOE"},
        {"member_id", "W199000000"},
        {"address", new Dictionary<string, object> {
            {"address_lines", new string[] {"123 MAIN ST"}},
            {"city", "SPARTANBURG"},
            {"state", "SC"},
            {"zipcode", "29301"}
        }},
        {"birth_date", "1970-01-25"},
        {"gender", "male"}
    }},
    {"claim", new Dictionary<string, object> {
        {"place_of_service", "office"},
        {"total_charge_amount", 150.0},
        {"patient_paid_amount", 150.0},
        {"service_lines", new Object[] {new Dictionary<string, object> {
            {"procedure_code", "11100"},
            {"charge_amount", 150.0},
            {"unit_count", 1.0},
            {"diagnosis_codes", new string[] {"L90.9"}},
            {"service_date", "2016-03-25"}
        }}}}}
    });
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"transaction_code\": \"chargeable\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\",");
buf.append("    \"billing_provider\": {");
buf.append("        \"taxonomy_code\": \"207Q00000X\",");
buf.append("        \"first_name\": \"JEROME\",");
buf.append("        \"last_name\": \"AYA-AY\",");
buf.append("        \"npi\": \"1467560003\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [");
buf.append("                \"1703 John B White Blvd, Unit A\"");
buf.append("            ],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"tax_id\": \"123456789\"");
buf.append("    },");
buf.append("    \"subscriber\": {");
buf.append("        \"first_name\": \"JOHN\",");
buf.append("        \"last_name\": \"DOE\",");
buf.append("        \"member_id\": \"W199000000\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [\"123 MAIN ST\"],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"gender\": \"male\"");
buf.append("    },");
buf.append("    \"claim\": {");
buf.append("        \"place_of_service\": \"office\",");
buf.append("        \"total_charge_amount\": 150.0,");
buf.append("        \"patient_paid_amount\": 150.0,");
buf.append("        \"service_lines\": [");
buf.append("            {");
buf.append("                \"procedure_code\": \"11100\",");
buf.append("                \"charge_amount\": 150.00,");
buf.append("                \"unit_count\": 1.0,");
buf.append("                \"diagnosis_codes\": [");
buf.append("                    \"L90.9\"");
buf.append("                ],");
buf.append("                \"service_date\": \"2016-03-25\"");
buf.append("            }");
buf.append("        ]");
buf.append("    }");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claims(query);
```

```swift
let data = [
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": [
        "taxonomy_code": "207Q00000X",
        "first_name": "JEROME",
        "last_name": "AYA-AY",
        "npi": "1467560003",
        "address": [
            "address_lines": [
                "1703 John B White Blvd, Unit A"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "tax_id": "123456789"
    ],
    "subscriber": [
        "first_name": "JOHN",
        "last_name": "DOE",
        "member_id": "W199000000",
        "address": [
            "address_lines": ["123 MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "birth_date": "1970-01-25",
        "gender": "male"
    ],
    "claim": [
        "place_of_service": "office",
        "total_charge_amount": 150.0,
        "patient_paid_amount": 150.0,
        "service_lines": [
            [
                "procedure_code": "11100",
                "charge_amount": 150.00,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "L90.9"
                ],
                "service_date": "2016-03-25"
            ]
        ]
    ]
] as [String:Any]
try client.claims(params: data)
```

> Sample Claims request when using procedure modifier codes. This example uses
the "GT" modifier ("via interactive audio and video telecommunications
systems") which would be suitable for telehealth applications:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 100.0,
        "service_lines": [
            {
                "procedure_code": "99201",
                "procedure_modifier_codes": ["GT"],
                "charge_amount": 100.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "W51.XXXA"
                ],
                "service_date": "2016-05-25"
            }
        ]
    }
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
client.claims({
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 100.0,
        "service_lines": [
            {
                "procedure_code": "99201",
                "procedure_modifier_codes": ["GT"],
                "charge_amount": 100.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "W51.XXXA"
                ],
                "service_date": "2016-05-25"
            }
        ]
    }
})
```

```ruby
client.claims({
    transaction_code: "chargeable",
    trading_partner_id: "MOCKPAYER",
    billing_provider: {
        taxonomy_code: "207Q00000X",
        first_name: "Jerome",
        last_name: "Aya-Ay",
        npi: "1467560003",
        address: {
            address_lines: [
                "8311 WARREN H ABERNATHY HWY"
            ],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        tax_id: "123456789"
    },
    subscriber: {
        first_name: "Jane",
        last_name: "Doe",
        member_id: "W000000000",
        address: {
            address_lines: ["123 N MAIN ST"],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        birth_date: "1970-01-25",
        gender: "female"
    },
    claim: {
        total_charge_amount: 100.0,
        service_lines: [
            {
                procedure_code: "99201",
                procedure_modifier_codes: ["GT"],
                charge_amount: 100.0,
                unit_count: 1.0,
                diagnosis_codes: [
                    "W51.XXXA"
                ],
                service_date: "2016-05-25"
            }
        ]
    }
})
```

```csharp
client.claims(
    new Dictionary<string, object> {
        {"transaction_code", "chargeable"},
        {"trading_partner_id", "MOCKPAYER"},
        {"billing_provider", new Dictionary<string, object> {
            {"taxonomy_code", "207Q00000X"},
            {"first_name", "Jerome"},
            {"last_name", "Aya-Ay"},
            {"npi", "1467560003"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"8311 WARREN H ABERNATHY HWY"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"tax_id", "123456789"}
        }},
        {"subscriber", new Dictionary<string, object> {
            {"first_name", "Jane"},
            {"last_name", "Doe"},
            {"member_id", "W000000000"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"123 N MAIN ST"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"birth_date", "1970-01-25"},
            {"gender", "female"}
        }},
        {"claim", new Dictionary<string, object> {
            {"total_charge_amount", 100.0},
            {"service_lines", new Object[] {new Dictionary<string, object> {
                {"procedure_code", "99201"},
                {"procedure_modifier_codes", new string[] {"GT"}},
                {"charge_amount", 100.0},
                {"unit_count", 1.0},
                {"diagnosis_codes", new string[] {"W51.XXXA"}},
                {"service_date", "2016-05-25"}
        }}}}}
    });
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"transaction_code\": \"chargeable\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\",");
buf.append("    \"billing_provider\": {");
buf.append("        \"taxonomy_code\": \"207Q00000X\",");
buf.append("        \"first_name\": \"Jerome\",");
buf.append("        \"last_name\": \"Aya-Ay\",");
buf.append("        \"npi\": \"1467560003\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [");
buf.append("                \"8311 WARREN H ABERNATHY HWY\"");
buf.append("            ],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"tax_id\": \"123456789\"");
buf.append("    },");
buf.append("    \"subscriber\": {");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"member_id\": \"W000000000\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [\"123 N MAIN ST\"],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"gender\": \"female\"");
buf.append("    },");
buf.append("    \"claim\": {");
buf.append("        \"total_charge_amount\": 100.0,");
buf.append("        \"service_lines\": [");
buf.append("            {");
buf.append("                \"procedure_code\": \"99201\",");
buf.append("                \"procedure_modifier_codes\": [\"GT\"],");
buf.append("                \"charge_amount\": 100.0,");
buf.append("                \"unit_count\": 1.0,");
buf.append("                \"diagnosis_codes\": [");
buf.append("                    \"W51.XXXA\"");
buf.append("                ],");
buf.append("                \"service_date\": \"2016-05-25\"");
buf.append("            }");
buf.append("        ]");
buf.append("    }");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claims(query);
```

```swift
let data = [
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": [
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": [
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "tax_id": "123456789"
    ],
    "subscriber": [
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": [
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "birth_date": "1970-01-25",
        "gender": "female"
    ],
    "claim": [
        "total_charge_amount": 100.0,
        "service_lines": [
            [
                "procedure_code": "99201",
                "procedure_modifier_codes": ["GT"],
                "charge_amount": 100.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "W51.XXXA"
                ],
                "service_date": "2016-05-25"
            ]
        ]
    ]
] as [String:Any]
try client.claims(params: data)
```

> Sample Claims request submitting a claim with an application's callback_url specified:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "callback_url": "https://yourapp.com/claims/status",
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "W53.21XA"
                ],
                "service_date": "2016-05-25"
            }
        ]
    }
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
client.claims({
    "callback_url": "https://yourapp.com/claims/status",
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "W53.21XA"
                ],
                "service_date": "2016-05-25"
            }
        ]
    }
})
```

```ruby
client.claims({
    callback_url: "https://yourapp.com/claims/status",
    transaction_code: "chargeable",
    trading_partner_id: "MOCKPAYER",
    billing_provider: {
        taxonomy_code: "207Q00000X",
        first_name: "Jerome",
        last_name: "Aya-Ay",
        npi: "1467560003",
        address: {
            address_lines: [
                "8311 WARREN H ABERNATHY HWY"
            ],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        tax_id: "123456789"
    },
    subscriber: {
        first_name: "Jane",
        last_name: "Doe",
        member_id: "W000000000",
        address: {
            address_lines: ["123 N MAIN ST"],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        birth_date: "1970-01-25",
        gender: "female"
    },
    claim: {
        total_charge_amount: 60.0,
        service_lines: [
            {
                procedure_code: "99213",
                charge_amount: 60.0,
                unit_count: 1.0,
                diagnosis_codes: [
                    "W53.21XA"
                ],
                service_date: "2016-05-25"
            }
        ]
    }
})
```

```csharp
client.claims(
    new Dictionary<string, object> {
        {"callback_url", "https://yourapp.com/claims/status"},
        {"transaction_code", "chargeable"},
        {"trading_partner_id", "MOCKPAYER"},
        {"billing_provider", new Dictionary<string, object> {
            {"taxonomy_code", "207Q00000X"},
            {"first_name", "Jerome"},
            {"last_name", "Aya-Ay"},
            {"npi", "1467560003"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"8311 WARREN H ABERNATHY HWY"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"tax_id", "123456789"}
        }},
        {"subscriber", new Dictionary<string, object> {
            {"first_name", "Jane"},
            {"last_name", "Doe"},
            {"member_id", "W000000000"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"123 N MAIN ST"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"birth_date", "1970-01-25"},
            {"gender", "female"}
        }},
        {"claim", new Dictionary<string, object> {
            {"total_charge_amount", 60.0},
            {"service_lines", new Object[] {new Dictionary<string, object> {
                {"procedure_code", "99213"},
                {"charge_amount", 60.0},
                {"unit_count", 1.0},
                {"diagnosis_codes", new string[] {"W53.21XA"}},
                {"service_date", "2016-05-25"}
        }}}}}
    });
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"callback_url\": \"https://yourapp.com/claims/status\",");
buf.append("    \"transaction_code\": \"chargeable\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\",");
buf.append("    \"billing_provider\": {");
buf.append("        \"taxonomy_code\": \"207Q00000X\",");
buf.append("        \"first_name\": \"Jerome\",");
buf.append("        \"last_name\": \"Aya-Ay\",");
buf.append("        \"npi\": \"1467560003\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [");
buf.append("                \"8311 WARREN H ABERNATHY HWY\"");
buf.append("            ],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"tax_id\": \"123456789\"");
buf.append("    },");
buf.append("    \"subscriber\": {");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"member_id\": \"W000000000\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [\"123 N MAIN ST\"],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"gender\": \"female\"");
buf.append("    },");
buf.append("    \"claim\": {");
buf.append("        \"total_charge_amount\": 60.0,");
buf.append("        \"service_lines\": [");
buf.append("            {");
buf.append("                \"procedure_code\": \"99213\",");
buf.append("                \"charge_amount\": 60.0,");
buf.append("                \"unit_count\": 1.0,");
buf.append("                \"diagnosis_codes\": [");
buf.append("                    \"W53.21XA\"");
buf.append("                ],");
buf.append("                \"service_date\": \"2016-05-25\"");
buf.append("            }");
buf.append("        ]");
buf.append("    }");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claims(query);
```

```swift
let data = [
    "callback_url": "https://yourapp.com/claims/status",
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": [
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": [
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "tax_id": "123456789"
    ],
    "subscriber": [
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": [
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "birth_date": "1970-01-25",
        "gender": "female"
    ],
    "claim": [
        "total_charge_amount": 60.0,
        "service_lines": [
            [
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "W53.21XA"
                ],
                "service_date": "2016-05-25"
            ]
        ]
    ]
] as [String:Any]
try client.claims(params: data)
```


> Claims request registering a callback_url and requesting a mock claim payment callback.
Your application will receive two callbacks.  The first will contain a claims acknowledgement result.
The second will contain a mock claim payment where 85% of the charged amount is paid, 5% is adjusted
due to contractual obligations and 10% is left to be paid by the patient.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "callback_url": "https://your-application.com/callback/1234",
    "application_data": {
        "mock_claim_payment": true
    },
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "W56.22XA"
                ],
                "service_date": "2016-05-25"
            }
        ]
    }
}` https://platform.pokitdok.com/api/v4/claims/
```

```python
client.claims({
    "callback_url": "https://your-application.com/callback/1234",
    "application_data": {
        "mock_claim_payment": True
    },
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "W56.22XA"
                ],
                "service_date": "2016-05-25"
            }
        ]
    }
})
```

```ruby
client.claims({
    callback_url: "https://your-application.com/callback/1234",
    application_data: {
        mock_claim_payment: true
    },
    transaction_code: "chargeable",
    trading_partner_id: "MOCKPAYER",
    billing_provider: {
        taxonomy_code: "207Q00000X",
        first_name: "Jerome",
        last_name: "Aya-Ay",
        npi: "1467560003",
        address: {
            address_lines: [
                "8311 WARREN H ABERNATHY HWY"
            ],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        tax_id: "123456789"
    },
    subscriber: {
        first_name: "Jane",
        last_name: "Doe",
        member_id: "W000000000",
        address: {
            address_lines: ["123 N MAIN ST"],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        birth_date: "1970-01-25",
        gender: "female"
    },
    claim: {
        total_charge_amount: 60.0,
        service_lines: [
            {
                procedure_code: "99213",
                charge_amount: 60.0,
                unit_count: 1.0,
                diagnosis_codes: [
                    "W56.22XA"
                ],
                service_date: "2016-05-25"
            }
        ]
    }
})
```

```csharp
client.claims(
    new Dictionary<string, object> {
        {"callback_url", "https://your-application.com/callback/1234"},
        {"application_data", new Dictionary<string, object> {
            {"mock_claim_payment", True}
        }},
        {"transaction_code", "chargeable"},
        {"trading_partner_id", "MOCKPAYER"},
        {"billing_provider", new Dictionary<string, object> {
            {"taxonomy_code", "207Q00000X"},
            {"first_name", "Jerome"},
            {"last_name", "Aya-Ay"},
            {"npi", "1467560003"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"8311 WARREN H ABERNATHY HWY"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"tax_id", "123456789"}
        }},
        {"subscriber", new Dictionary<string, object> {
            {"first_name", "Jane"},
            {"last_name", "Doe"},
            {"member_id", "W000000000"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"123 N MAIN ST"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"birth_date", "1970-01-25"},
            {"gender", "female"}
        }},
        {"claim", new Dictionary<string, object> {
            {"total_charge_amount", 60.0},
            {"service_lines", new Object[] {new Dictionary<string, object> {
                {"procedure_code", "99213"},
                {"charge_amount", 60.0},
                {"unit_count", 1.0},
                {"diagnosis_codes", new string[] {"W56.22XA"}},
                {"service_date", "2016-05-25"}
        }}}}}
    });
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"callback_url\": \"https://your-application.com/callback/1234\",");
buf.append("    \"application_data\": {");
buf.append("        \"mock_claim_payment\": true");
buf.append("    },");
buf.append("    \"transaction_code\": \"chargeable\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\",");
buf.append("    \"billing_provider\": {");
buf.append("        \"taxonomy_code\": \"207Q00000X\",");
buf.append("        \"first_name\": \"Jerome\",");
buf.append("        \"last_name\": \"Aya-Ay\",");
buf.append("        \"npi\": \"1467560003\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [");
buf.append("                \"8311 WARREN H ABERNATHY HWY\"");
buf.append("            ],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"tax_id\": \"123456789\"");
buf.append("    },");
buf.append("    \"subscriber\": {");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"member_id\": \"W000000000\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [\"123 N MAIN ST\"],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"gender\": \"female\"");
buf.append("    },");
buf.append("    \"claim\": {");
buf.append("        \"total_charge_amount\": 60.0,");
buf.append("        \"service_lines\": [");
buf.append("            {");
buf.append("                \"procedure_code\": \"99213\",");
buf.append("                \"charge_amount\": 60.0,");
buf.append("                \"unit_count\": 1.0,");
buf.append("                \"diagnosis_codes\": [");
buf.append("                    \"W56.22XA\"");
buf.append("                ],");
buf.append("                \"service_date\": \"2016-05-25\"");
buf.append("            }");
buf.append("        ]");
buf.append("    }");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claims(query);
```

```swift
let data = [
    "callback_url": "https://your-application.com/callback/1234",
    "application_data": [
        "mock_claim_payment": True
    ],
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": [
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": [
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "tax_id": "123456789"
    ],
    "subscriber": [
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": [
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "birth_date": "1970-01-25",
        "gender": "female"
    ],
    "claim": [
        "total_charge_amount": 60.0,
        "service_lines": [
            [
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "W56.22XA"
                ],
                "service_date": "2016-05-25"
            ]
        ]
    ]
] as [String:Any]
try client.claims(params: data)
```

> Claims request containing information for rendering provider.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "rendering_provider": {
              "npi": "1467560003",
              "first_name": "JANE",
              "last_name": "DOE",
              "taxonomy_code": "207N00000X"

 },
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "V91.35"
                ],
                "service_date": "2016-05-25"
            }
        ]
    }
}` https://platform.pokitdok.com/api/v4/claims/
```

```python
client.claims({
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "rendering_provider": {
              "npi": "1467560003",
              "first_name": "JANE",
              "last_name": "DOE",
              "taxonomy_code": "207N00000X"

 },
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "V91.35"
                ],
                "service_date": "2016-05-25"
            }
        ]
    }
})
```

```ruby
client.claims({
    transaction_code: "chargeable",
    trading_partner_id: "MOCKPAYER",
    billing_provider: {
        taxonomy_code: "207Q00000X",
        first_name: "Jerome",
        last_name: "Aya-Ay",
        npi: "1467560003",
        address: {
            address_lines: [
                "8311 WARREN H ABERNATHY HWY"
            ],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        tax_id: "123456789"
    },
    subscriber: {
        first_name: "Jane",
        last_name: "Doe",
        member_id: "W000000000",
        address: {
            address_lines: ["123 N MAIN ST"],
            city: "SPARTANBURG",
            state: "SC",
            zipcode: "29301"
        },
        birth_date: "1970-01-25",
        gender: "female"
    },
    claim: {
        total_charge_amount: 60.0,
        rendering_provider: {
              npi: "1467560003",
              first_name: "JANE",
              last_name: "DOE",
              taxonomy_code: "207N00000X"

 },
        service_lines: [
            {
                procedure_code: "99213",
                charge_amount: 60.0,
                unit_count: 1.0,
                diagnosis_codes: [
                    "V91.35"
                ],
                service_date: "2016-05-25"
            }
        ]
    }
})
```

```csharp
client.claims(
    new Dictionary<string, object> {
        {"transaction_code", "chargeable"},
        {"trading_partner_id", "MOCKPAYER"},
        {"billing_provider", new Dictionary<string, object> {
            {"taxonomy_code", "207Q00000X"},
            {"first_name", "Jerome"},
            {"last_name", "Aya-Ay"},
            {"npi", "1467560003"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"8311 WARREN H ABERNATHY HWY"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"tax_id", "123456789"}
        }},
        {"subscriber", new Dictionary<string, object> {
            {"first_name", "Jane"},
            {"last_name", "Doe"},
            {"member_id", "W000000000"},
            {"address", new Dictionary<string, object> {
                {"address_lines", new string[] {"123 N MAIN ST"}},
                {"city", "SPARTANBURG"},
                {"state", "SC"},
                {"zipcode", "29301"}
            }},
            {"birth_date", "1970-01-25"},
            {"gender", "female"}
        }},
        {"claim", new Dictionary<string, object> {
            {"total_charge_amount", 60.0},
            {"rendering_provider", new Dictionary<string, string> {
                {"npi", "1467560003"},
                {"first_name", "JANE"},
                {"last_name", "DOE"},
                {"taxonomy_code", "207N00000X"}
            }},
            {"service_lines", new Object[] {new Dictionary<string, object> {
                {"procedure_code", "99213"},
                {"charge_amount", 60.0},
                {"unit_count", 1.0},
                {"diagnosis_codes", new string[] {"V91.35"}},
                {"service_date", "2016-05-25"}
        }}}}}
    });
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"transaction_code\": \"chargeable\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\",");
buf.append("    \"billing_provider\": {");
buf.append("        \"taxonomy_code\": \"207Q00000X\",");
buf.append("        \"first_name\": \"Jerome\",");
buf.append("        \"last_name\": \"Aya-Ay\",");
buf.append("        \"npi\": \"1467560003\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [");
buf.append("                \"8311 WARREN H ABERNATHY HWY\"");
buf.append("            ],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"tax_id\": \"123456789\"");
buf.append("    },");
buf.append("    \"subscriber\": {");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"member_id\": \"W000000000\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [\"123 N MAIN ST\"],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"gender\": \"female\"");
buf.append("    },");
buf.append("    \"claim\": {");
buf.append("        \"total_charge_amount\": 60.0,");
buf.append("        \"rendering_provider\": {");
buf.append("              \"npi\": \"1467560003\",");
buf.append("              \"first_name\": \"JANE\",");
buf.append("              \"last_name\": \"DOE\",");
buf.append("              \"taxonomy_code\": \"207N00000X\"");
buf.append("");
buf.append(" },");
buf.append("        \"service_lines\": [");
buf.append("            {");
buf.append("                \"procedure_code\": \"99213\",");
buf.append("                \"charge_amount\": 60.0,");
buf.append("                \"unit_count\": 1.0,");
buf.append("                \"diagnosis_codes\": [");
buf.append("                    \"V91.35\"");
buf.append("                ],");
buf.append("                \"service_date\": \"2016-05-25\"");
buf.append("            }");
buf.append("        ]");
buf.append("    }");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claims(query);
```

```swift
let data = [
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": [
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": [
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "tax_id": "123456789"
    ],
    "subscriber": [
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": [
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        ],
        "birth_date": "1970-01-25",
        "gender": "female"
    ],
    "claim": [
        "total_charge_amount": 60.0,
        "rendering_provider": [
              "npi": "1467560003",
              "first_name": "JANE",
              "last_name": "DOE",
              "taxonomy_code": "207N00000X"

        ],
        "service_lines": [
            [
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "V91.35"
                ],
                "service_date": "2016-05-25"
            ]
        ]
    ]
] as [String:Any]
try client.claims(params: data)
```

> Sample Claims request for sending service date range, using service date and service end date with a claim note:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "taxonomy_code": "207Q00000X",
        "first_name": "Jerome",
        "last_name": "Aya-Ay",
        "npi": "1467560003",
        "address": {
            "address_lines": [
                "8311 WARREN H ABERNATHY HWY"
            ],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "tax_id": "123456789"
    },
    "subscriber": {
        "first_name": "Jane",
        "last_name": "Doe",
        "member_id": "W000000000",
        "address": {
            "address_lines": ["123 N MAIN ST"],
            "city": "SPARTANBURG",
            "state": "SC",
            "zipcode": "29301"
        },
        "birth_date": "1970-01-25",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
	"note": {
            "reference_code": "additional_information",
            "note": "this is a note"
            },
        "service_lines": [
            {
                "procedure_code": "99213",
                "charge_amount": 60.0,
                "unit_count": 1.0,
                "diagnosis_codes": [
                    "X35.XXXD"
                ],
                "test_results": [
                     {
                        "measurement": "height",
                        "reference_id": "test_results",
                        "value": "61"
                      }
               ], 
                "service_date": "2016-04-25",
                "service_end_date": "2016-05-25"
            }
        ]
    }
}` https://platform.pokitdok.com/api/v4/claims/
```

```python
client.claims({
  "transaction_code": "chargeable",
  "trading_partner_id": "MOCKPAYER",
  "billing_provider": {
    "taxonomy_code": "207Q00000X",
    "first_name": "Jerome",
    "last_name": "Aya-Ay",
    "npi": "1467560003",
    "address": {
      "address_lines": [
        "8311 WARREN H ABERNATHY HWY"
      ],
      "city": "SPARTANBURG",
      "state": "SC",
      "zipcode": "29301"
    },
    "tax_id": "123456789"
  },
  "subscriber": {
    "first_name": "Jane",
    "last_name": "Doe",
    "member_id": "W000000000",
    "address": {
      "address_lines": [
        "123 N MAIN ST"
      ],
      "city": "SPARTANBURG",
      "state": "SC",
      "zipcode": "29301"
    },
    "birth_date": "1970-01-25",
    "gender": "female"
  },
  "claim": {
    "total_charge_amount": 60.0,
    "service_lines": [
      {
        "procedure_code": "99213",
        "charge_amount": 60.0,
        "unit_count": 1.0,
        "diagnosis_codes": [
          "X35.XXXD"
        ],
        "test_results": [
           {
             "measurement": "height",
             "reference_id": "test_results",
             "value": "61"
            }
        ], 
        "service_date": "2016-04-25",
        "service_end_date": "2016-05-25"
      }
    ]
  }
})
```

```ruby
client.claims({
  transaction_code: "chargeable",
  trading_partner_id: "MOCKPAYER",
  billing_provider: {
    taxonomy_code: "207Q00000X",
    first_name: "Jerome",
    last_name: "Aya-Ay",
    npi: "1467560003",
    address: {
      address_lines: [
        "8311 WARREN H ABERNATHY HWY"
      ],
      city: "SPARTANBURG",
      state: "SC",
      zipcode: "29301"
    },
    tax_id: "123456789"
  },
  subscriber: {
    first_name: "Jane",
    last_name: "Doe",
    member_id: "W000000000",
    address: {
      address_lines: [
        "123 N MAIN ST"
      ],
      city: "SPARTANBURG",
      state: "SC",
      zipcode: "29301"
    },
    birth_date: "1970-01-25",
    gender: "female"
  },
  claim: {
    total_charge_amount: 60.0,
    service_lines: [
      {
        procedure_code: "99213",
        charge_amount: 60.0,
        unit_count: 1.0,
        diagnosis_codes: [
          "X35.XXXD"
        ],
        service_date: "2016-04-25",
        service_end_date: "2016-05-25"
      }
    ]
  }
})
```

```csharp
client.claims(
    new Dictionary<string, object> {
        {"transaction_code", "chargeable"},
        {"trading_partner_id", "MOCKPAYER"},
        {"billing_provider", new Dictionary<string, object> {
                {"taxonomy_code", "207Q00000X"},
                {"first_name", "Jerome"},
                {"last_name", "Aya-Ay"},
                {"npi", "1467560003"},
                {"address", new Dictionary<string, object> {
                        {"address_lines", new string[] {"8311 WARREN H ABERNATHY HWY"}},
                        {"city", "SPARTANBURG"},
                        {"state", "SC"},
                        {"zipcode", "29301"}
                    }},
                {"tax_id", "123456789"}
            }},
        {"subscriber", new Dictionary<string, object> {
                {"first_name", "Jane"},
                {"last_name", "Doe"},
                {"member_id", "W000000000"},
                {"address", new Dictionary<string, object> {
                        {"address_lines", new string[] {"123 N MAIN ST"}},
                        {"city", "SPARTANBURG"},
                        {"state", "SC"},
                        {"zipcode", "29301"}
                    }},
                {"birth_date", "1970-01-25"},
                {"gender", "female"}
            }},
        {"claim", new Dictionary<string, object> {
                {"total_charge_amount", 60.0},
                {"service_lines", new Object[] {new Dictionary<string, object> {
                            {"procedure_code", "99213"},
                            {"charge_amount", 60.0},
                            {"unit_count", 1.0},
                            {"diagnosis_codes", new string[] {"X35.XXXD"}},
                            {"service_date", "2016-04-25"},
                            {"service_end_date", "2016-05-25"}
                        }}}
            }}
    }
);
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"transaction_code\": \"chargeable\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\",");
buf.append("    \"billing_provider\": {");
buf.append("        \"taxonomy_code\": \"207Q00000X\",");
buf.append("        \"first_name\": \"Jerome\",");
buf.append("        \"last_name\": \"Aya-Ay\",");
buf.append("        \"npi\": \"1467560003\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [");
buf.append("                \"8311 WARREN H ABERNATHY HWY\"");
buf.append("            ],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"tax_id\": \"123456789\"");
buf.append("    },");
buf.append("    \"subscriber\": {");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"member_id\": \"W000000000\",");
buf.append("        \"address\": {");
buf.append("            \"address_lines\": [\"123 N MAIN ST\"],");
buf.append("            \"city\": \"SPARTANBURG\",");
buf.append("            \"state\": \"SC\",");
buf.append("            \"zipcode\": \"29301\"");
buf.append("        },");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"gender\": \"female\"");
buf.append("    },");
buf.append("    \"claim\": {");
buf.append("        \"total_charge_amount\": 60.0,");
buf.append("        \"service_lines\": [");
buf.append("            {");
buf.append("                \"procedure_code\": \"99213\",");
buf.append("                \"charge_amount\": 60.0,");
buf.append("                \"unit_count\": 1.0,");
buf.append("                \"diagnosis_codes\": [");
buf.append("                    \"X35.XXXD\"");
buf.append("                ],");
buf.append("                \"service_date\": \"2016-04-25\",");
buf.append("                \"service_end_date\": \"2016-05-25\"");
buf.append("            }");
buf.append("        ]");
buf.append("    }");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.claims(query);
```

```swift
let data = [
  "transaction_code": "chargeable",
  "trading_partner_id": "MOCKPAYER",
  "billing_provider": [
    "taxonomy_code": "207Q00000X",
    "first_name": "Jerome",
    "last_name": "Aya-Ay",
    "npi": "1467560003",
    "address": [
      "address_lines": [
        "8311 WARREN H ABERNATHY HWY"
      ],
      "city": "SPARTANBURG",
      "state": "SC",
      "zipcode": "29301"
    ],
    "tax_id": "123456789"
  ],
  "subscriber": [
    "first_name": "Jane",
    "last_name": "Doe",
    "member_id": "W000000000",
    "address": [
      "address_lines": [
        "123 N MAIN ST"
      ],
      "city": "SPARTANBURG",
      "state": "SC",
      "zipcode": "29301"
    ],
    "birth_date": "1970-01-25",
    "gender": "female"
  ],
  "claim": [
    "total_charge_amount": 60.0,
    "service_lines": [
      [
        "procedure_code": "99213",
        "charge_amount": 60.0,
        "unit_count": 1.0,
        "diagnosis_codes": [
          "X35.XXXD"
        ],
        "service_date": "2016-04-25",
        "service_end_date": "2016-05-25"
      ]
    ]
  ]
] as [String:Any]
try client.claims(params: data)
```


> Sample Coordination of Benefits Claim Request (example includes 2 payers, with COB as a dict).

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "correlation_id": "CLAIM1158654",
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "address": {
            "address_lines": [
                "25 RAINBOW ROW"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29407"
        },
        "npi": "1487640231",
        "organization_name": "MEDCO MEDICAL INC",
        "payment_address": {
            "address_lines": [
                "PO BOX 123"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29401"
        },
        "tax_id": "123456789",
        "taxonomy_code": "777B12345X"
    },
    "claim": {
        "claim_frequency": "original",
        "direct_payment": "y",
        "information_release": "signed_statement",
        "place_of_service": "home",
        "plan_participation": "assigned",
        "prior_authorization_number": "P00171408ABCDEF",
        "provider_signature": true,
        "service_facility": {
            "address": {
                "address_lines": [
                    "300 RIVERS AVE"
                ],
                "city": "CHARLESTON",
                "state": "SC",
                "zipcode": "29412"
            },
            "organization_name": "MEDCITY"
        },
        "service_lines": [
            {
                "adjudication": {
                    "adjustments": [
                        {
                            "amount": "28.22",
                            "group": "patient_responsibility",
                            "reason": "2"
                        },
                        {
                            "amount": "26.79",
                            "group": "contractual_obligations",
                            "reason": "45"
                        }
                    ],
                    "amount": "40.66",
                    "amount_owed": "0",
                    "claim_paid_date": "2017-04-04",
                    "payer_id": "62308",
                    "procedure_code": "T4529",
                    "procedure_qualifier": "HC",
                    "quantity": "246"
                },
                "charge_amount": "95.67",
                "diagnosis_codes": [
                    "N184"
                ],
                "is_emergency": false,
                "ordering_provider": {
                    "first_name": "STEVEN",
                    "last_name": "DOE",
                    "npi": "1912301953",
                    "state_license_number": "SC12345"
                },
                "procedure_code": "T4529",
                "provider_control_number": "900001",
                "service_date": "2017-03-20",
                "unit_count": "246",
                "unit_type": "units"
            },
            {
                "adjudication": {
                    "adjustments": [
                        {
                            "amount": "72",
                            "group": "other_adjustments",
                            "reason": "96"
                        }
                    ],
                    "amount": "0",
                    "amount_owed": "0",
                    "claim_paid_date": "2017-04-04",
                    "payer_id": "62308",
                    "procedure_code": "A4554",
                    "procedure_qualifier": "HC",
                    "quantity": "120"
                },
                "charge_amount": "72",
                "diagnosis_codes": [
                    "N184"
                ],
                "is_emergency": false,
                "ordering_provider": {
                    "first_name": "STEVEN",
                    "last_name": "DOE",
                    "npi": "1912301953",
                    "state_license_number": "SC12345"
                },
                "procedure_code": "A4554",
                "provider_control_number": "900002",
                "service_date": "2017-03-20",
                "unit_count": "120",
                "unit_type": "units"
            }
        ],
        "total_charge_amount": "167.67"
    },
    "coordination_of_benefits": {
        "payer": {
            "id": "777654",
            "organization_name": "BCBSSC"
        },
        "payer_amount_paid": "40.66",
        "subscriber": {
            "address": {
                "address_lines": [
                    "100 CALHOUN"
                ],
                "city": "CHARLESTON",
                "state": "SC",
                "zipcode": "29407"
            },
            "authorize_payment_to_billing_provider": "yes",
            "claim_filing_code": "commercial_insurance_co",
            "first_name": "EMMIE",
            "group_number": "888754",
            "last_name": "DOE",
            "member_id": "987654321",
            "payer_responsibility": "primary",
            "relationship": "self",
            "release_of_information_code": "signed_statement"
        }
    },
    "payer": {
        "address": {
            "address_lines": [
                "PO BOX 301404"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29407"
        },
        "id": "12345",
        "organization_name": "CHARLESTON HEALTH PLAN"
    },
    "receiver": {
        "id": "EMPORIUM",
        "organization_name": "X12 FLAT FILE EMPORIUM"
    },
    "submitter": {
        "contacts": [
            {
                "contact_methods": [
                    {
                        "type": "phone",
                        "value": "8431114444"
                    }
                ],
                "name": "BOB DOE"
            }
        ],
        "id": "55512",
        "organization_name": "MEDCO MEDICAL INC"
    },
    "subscriber": {
        "address": {
            "address_lines": [
                "100 CALHOUN"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29407"
        },
        "birth_date": "2015-01-05",
        "claim_filing_code": "commercial_insurance_co",
        "first_name": "EMMIE",
        "gender": "female",
        "last_name": "DOE",
        "member_id": "987654321",
        "payer_responsibility": "secondary"
    }
}' https://platform.pokitdok.com/api/v4/claims/

```

```python
client.claims({
    "correlation_id": "CLAIM1158654",
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "address": {
            "address_lines": [
                "25 RAINBOW ROW"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29407"
        },
        "npi": "1487640231",
        "organization_name": "MEDCO MEDICAL INC",
        "payment_address": {
            "address_lines": [
                "PO BOX 123"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29401"
        },
        "tax_id": "123456789",
        "taxonomy_code": "777B12345X"
    },
    "claim": {
        "claim_frequency": "original",
        "direct_payment": "y",
        "information_release": "signed_statement",
        "place_of_service": "home",
        "plan_participation": "assigned",
        "prior_authorization_number": "P00171408ABCDEF",
        "provider_signature": True,
        "service_facility": {
            "address": {
                "address_lines": [
                    "300 RIVERS AVE"
                ],
                "city": "CHARLESTON",
                "state": "SC",
                "zipcode": "29412"
            },
            "organization_name": "MEDCITY"
        },
        "service_lines": [
            {
                "adjudication": {
                    "adjustments": [
                        {
                            "amount": "28.22",
                            "group": "patient_responsibility",
                            "reason": "2"
                        },
                        {
                            "amount": "26.79",
                            "group": "contractual_obligations",
                            "reason": "45"
                        }
                    ],
                    "amount": "40.66",
                    "amount_owed": "0",
                    "claim_paid_date": "2017-04-04",
                    "payer_id": "62308",
                    "procedure_code": "T4529",
                    "procedure_qualifier": "HC",
                    "quantity": "246"
                },
                "charge_amount": "95.67",
                "diagnosis_codes": [
                    "N184"
                ],
                "is_emergency": False,
                "ordering_provider": {
                    "first_name": "STEVEN",
                    "last_name": "DOE",
                    "npi": "1912301953",
                    "state_license_number": "SC12345"
                },
                "procedure_code": "T4529",
                "provider_control_number": "900001",
                "service_date": "2017-03-20",
                "unit_count": "246",
                "unit_type": "units"
            },
            {
                "adjudication": {
                    "adjustments": [
                        {
                            "amount": "72",
                            "group": "other_adjustments",
                            "reason": "96"
                        }
                    ],
                    "amount": "0",
                    "amount_owed": "0",
                    "claim_paid_date": "2017-04-04",
                    "payer_id": "62308",
                    "procedure_code": "A4554",
                    "procedure_qualifier": "HC",
                    "quantity": "120"
                },
                "charge_amount": "72",
                "diagnosis_codes": [
                    "N184"
                ],
                "is_emergency": False,
                "ordering_provider": {
                    "first_name": "STEVEN",
                    "last_name": "DOE",
                    "npi": "1912301953",
                    "state_license_number": "SC12345"
                },
                "procedure_code": "A4554",
                "provider_control_number": "900002",
                "service_date": "2017-03-20",
                "unit_count": "120",
                "unit_type": "units"
            }
        ],
        "total_charge_amount": "167.67"
    },
    "coordination_of_benefits": {
        "payer": {
            "id": "777654",
            "organization_name": "BCBSSC"
        },
        "payer_amount_paid": "40.66",
        "subscriber": {
            "address": {
                "address_lines": [
                    "100 CALHOUN"
                ],
                "city": "CHARLESTON",
                "state": "SC",
                "zipcode": "29407"
            },
            "authorize_payment_to_billing_provider": "yes",
            "claim_filing_code": "commercial_insurance_co",
            "first_name": "EMMIE",
            "group_number": "888754",
            "last_name": "DOE",
            "member_id": "987654321",
            "payer_responsibility": "primary",
            "relationship": "self",
            "release_of_information_code": "signed_statement"
        }
    },
    "payer": {
        "address": {
            "address_lines": [
                "PO BOX 301404"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29407"
        },
        "id": "12345",
        "organization_name": "CHARLESTON HEALTH PLAN"
    },
    "receiver": {
        "id": "EMPORIUM",
        "organization_name": "X12 FLAT FILE EMPORIUM"
    },
    "submitter": {
        "contacts": [
            {
                "contact_methods": [
                    {
                        "type": "phone",
                        "value": "8431114444"
                    }
                ],
                "name": "BOB DOE"
            }
        ],
        "id": "55512",
        "organization_name": "MEDCO MEDICAL INC"
    },
    "subscriber": {
        "address": {
            "address_lines": [
                "100 CALHOUN"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29407"
        },
        "birth_date": "2015-01-05",
        "claim_filing_code": "commercial_insurance_co",
        "first_name": "EMMIE",
        "gender": "female",
        "last_name": "DOE",
        "member_id": "987654321",
        "payer_responsibility": "secondary"
    }
})
```

```ruby
client.claims({
    "correlation_id": "CLAIM1158654",
    "transaction_code": "chargeable",
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "address": {
            "address_lines": [
                "25 RAINBOW ROW"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29407"
        },
        "npi": "1487640231",
        "organization_name": "MEDCO MEDICAL INC",
        "payment_address": {
            "address_lines": [
                "PO BOX 123"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29401"
        },
        "tax_id": "123456789",
        "taxonomy_code": "777B12345X"
    },
    "claim": {
        "claim_frequency": "original",
        "direct_payment": "y",
        "information_release": "signed_statement",
        "place_of_service": "home",
        "plan_participation": "assigned",
        "prior_authorization_number": "P00171408ABCDEF",
        "provider_signature": true,
        "service_facility": {
            "address": {
                "address_lines": [
                    "300 RIVERS AVE"
                ],
                "city": "CHARLESTON",
                "state": "SC",
                "zipcode": "29412"
            },
            "organization_name": "MEDCITY"
        },
        "service_lines": [
            {
                "adjudication": {
                    "adjustments": [
                        {
                            "amount": "28.22",
                            "group": "patient_responsibility",
                            "reason": "2"
                        },
                        {
                            "amount": "26.79",
                            "group": "contractual_obligations",
                            "reason": "45"
                        }
                    ],
                    "amount": "40.66",
                    "amount_owed": "0",
                    "claim_paid_date": "2017-04-04",
                    "payer_id": "62308",
                    "procedure_code": "T4529",
                    "procedure_qualifier": "HC",
                    "quantity": "246"
                },
                "charge_amount": "95.67",
                "diagnosis_codes": [
                    "N184"
                ],
                "is_emergency": false,
                "ordering_provider": {
                    "first_name": "STEVEN",
                    "last_name": "DOE",
                    "npi": "1912301953",
                    "state_license_number": "SC12345"
                },
                "procedure_code": "T4529",
                "provider_control_number": "900001",
                "service_date": "2017-03-20",
                "unit_count": "246",
                "unit_type": "units"
            },
            {
                "adjudication": {
                    "adjustments": [
                        {
                            "amount": "72",
                            "group": "other_adjustments",
                            "reason": "96"
                        }
                    ],
                    "amount": "0",
                    "amount_owed": "0",
                    "claim_paid_date": "2017-04-04",
                    "payer_id": "62308",
                    "procedure_code": "A4554",
                    "procedure_qualifier": "HC",
                    "quantity": "120"
                },
                "charge_amount": "72",
                "diagnosis_codes": [
                    "N184"
                ],
                "is_emergency": false,
                "ordering_provider": {
                    "first_name": "STEVEN",
                    "last_name": "DOE",
                    "npi": "1912301953",
                    "state_license_number": "SC12345"
                },
                "procedure_code": "A4554",
                "provider_control_number": "900002",
                "service_date": "2017-03-20",
                "unit_count": "120",
                "unit_type": "units"
            }
        ],
        "total_charge_amount": "167.67"
    },
    "coordination_of_benefits": {
        "payer": {
            "id": "777654",
            "organization_name": "BCBSSC"
        },
        "payer_amount_paid": "40.66",
        "subscriber": {
            "address": {
                "address_lines": [
                    "100 CALHOUN"
                ],
                "city": "CHARLESTON",
                "state": "SC",
                "zipcode": "29407"
            },
            "authorize_payment_to_billing_provider": "yes",
            "claim_filing_code": "commercial_insurance_co",
            "first_name": "EMMIE",
            "group_number": "888754",
            "last_name": "DOE",
            "member_id": "987654321",
            "payer_responsibility": "primary",
            "relationship": "self",
            "release_of_information_code": "signed_statement"
        }
    },
    "payer": {
        "address": {
            "address_lines": [
                "PO BOX 301404"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29407"
        },
        "id": "12345",
        "organization_name": "CHARLESTON HEALTH PLAN"
    },
    "receiver": {
        "id": "EMPORIUM",
        "organization_name": "X12 FLAT FILE EMPORIUM"
    },
    "submitter": {
        "contacts": [
            {
                "contact_methods": [
                    {
                        "type": "phone",
                        "value": "8431114444"
                    }
                ],
                "name": "BOB DOE"
            }
        ],
        "id": "55512",
        "organization_name": "MEDCO MEDICAL INC"
    },
    "subscriber": {
        "address": {
            "address_lines": [
                "100 CALHOUN"
            ],
            "city": "CHARLESTON",
            "state": "SC",
            "zipcode": "29407"
        },
        "birth_date": "2015-01-05",
        "claim_filing_code": "commercial_insurance_co",
        "first_name": "EMMIE",
        "gender": "female",
        "last_name": "DOE",
        "member_id": "987654321",
        "payer_responsibility": "secondary"
    }})
```

```csharp
		var cobClaimRequest = new Dictionary<string, object>();
		cobClaimRequest.Add("correlation_id", "CLAIM1158654");
		cobClaimRequest.Add("transaction_code", "chargeable");
		cobClaimRequest.Add("trading_partner_id", "MOCKPAYER");

		cobClaimRequest.Add("billing_provider", new Dictionary<string, object> {
			{"address", new Dictionary<string, object> {
				{"address_lines", new object[] {"25 RAINBOW ROW"}},
        {"city", "CHARLESTON"},
        {"state", "SC"},
        {"zipcode", "29407"}}},
        {"npi", "1487640231"},
        {"organization_name", "MEDCO MEDICAL INC"},
        {"payment_address", new Dictionary<string, object>{
            {"address_lines", new object[] {"PO BOX 123"}},
            {"city", "CHARLESTON"},
            {"state", "SC"},
            {"zipcode", "29401"}}},
        {"tax_id", "123456789"},
        {"taxonomy_code", "777B12345X"}});

      cobClaimRequest.Add("claim", new Dictionary<string, object> {
        {"claim_frequency", "original"},
        {"direct_payment", "y"},
        {"information_release", "signed_statement"},
        {"place_of_service", "home"},
        {"plan_participation", "assigned"},
        {"prior_authorization_number", "P00171408ABCDEF"},
        {"provider_signature", true},
        {"total_charge_amount", "167.67"}});

      cobClaimRequest["service_facility"] = new Dictionary<string, object> {
        {"address", new Dictionary<string, object>{
			{"address_lines", new object[] {"300 RIVERS AVE"}},
            {"city", "CHARLESTON"},
            {"state", "SC"},
            {"zipcode", "29412"}}},
          {"organization_name", "MEDCITY"}};

     cobClaimRequest["service_lines"] = new object[] {
         new Dictionary<string, object>{
                {"charge_amount", "95.67"},
                {"diagnosis_codes", new string[] {"N184"}},
                {"is_emergency", false},
                {"ordering_provider", new Dictionary<string, object>{
                    {"first_name", "STEVEN"},
                    {"last_name", "DOE"},
                    {"npi", "1912301953"},
                    {"state_license_number", "SC12345"}}},
                {"procedure_code", "T4529"},
                {"provider_control_number", "900001"},
                {"service_date", "2017-03-20"},
                {"unit_count", "246"},
                {"unit_type", "units"},
                {"adjudication", new Dictionary<string, object>{
                    {"amount", "40.66"},
                    {"amount_owed", "0"},
                    {"claim_paid_date", "2017-04-04"},
                    {"payer_id", "62308"},
                    {"procedure_code", "T4529"},
                    {"procedure_qualifier", "HC"},
                    {"quantity", "246"},
                    {"adjustments", new object[]{
                        new Dictionary<string, object>{
                            {"amount", "28.22"},
                            {"group", "patient_responsibility"},
                            {"reason", "2"}},
                        new Dictionary<string, object>{
                        {"amount", "28.22"},
                        {"group", "patient_responsibility"},
                        {"reason", "2"}}
                    }}
                }}
            },
            new Dictionary<string, object>{
                {"charge_amount", "72"},
                {"diagnosis_codes", new string[] {"N184"}},
                {"is_emergency", false},
                {"ordering_provider", new Dictionary<string, object>{
                    {"first_name", "STEVEN"},
                    {"last_name", "DOE"},
                    {"npi", "1912301953"},
                    {"state_license_number", "SC12345"}}},
                {"procedure_code", "A4554"},
                {"provider_control_number", "900002"},
                {"service_date", "2017-03-20"},
                {"unit_count", "120"},
                {"unit_type", "units"},
                {"adjudication", new Dictionary<string, object>{
                    {"amount", "0"},
                    {"amount_owed", "0"},
                    {"claim_paid_date", "2017-04-04"},
                    {"payer_id", "62308"},
                    {"procedure_code", "A4554"},
                    {"procedure_qualifier", "HC"},
                    {"quantity", "120"},
                    {"adjustments", new object[]{
                        new Dictionary<string, object>{
                            {"amount", "72"},
                            {"group", "other_adjustments"},
                            {"reason", "96"}}
                    }}
                }}
            }
         };

    cobClaimRequest.Add("coordination_of_benefits",  new Dictionary<string, object>{
        {"payer_amount_paid", "40.66"},
        {"authorize_payment_to_billing_provider", "yes"},
        {"claim_filing_code", "commercial_insurance_co"},
        {"first_name", "EMMIE"},
        {"group_number", "888754"},
        {"last_name", "DOE"},
        {"member_id", "987654321"},
        {"payer_responsibility", "primary"},
        {"relationship", "self"},
        {"release_of_information_code", "signed_statement"},
        {"payer", new Dictionary<string, object>{
            {"id", "777654"},
            {"organization_name", "BCBSSC"}
        }},
        {"subscriber", new Dictionary<string, object>{
            {"address", new Dictionary<string, object>{
                {"address_lines", new string[] {"100 CALHOUN"}},
                {"city", "CHARLESTON"},
                {"state", "SC"},
                {"zipcode", "29407"}
            }}
        }}
    });

    cobClaimRequest.Add("payer", new Dictionary<string, object>{
        {"id", "12345"},
        {"organization_name", "CHARLESTON HEALTH PLAN"},
        {"address", new Dictionary<string, object>{
            {"address_lines", new string[] {"PO BOX 301404"}},
            {"city", "CHARLESTON"},
            {"state", "SC"},
            {"zipcode", "29407"}
        }}
    });

    cobClaimRequest.Add("receiver", new Dictionary<string, object>{
        {"id", "EMPORIUM"},
        {"organization_name", "X12 FLAT FILE EMPORIUM"}
    });

    cobClaimRequest.Add("submitter", new Dictionary<string, object>{
        {"id", "55512"},
        {"organization_name", "MEDCO MEDICAL INC"},
        {"contacts", new object[] {new Dictionary<string, object>{{"name", "BOB DOE"}}}}
    });

    cobClaimRequest.Add("subscriber", new Dictionary<string, object>{
        {"birth_date", "2015-01-05"},
        {"claim_filing_code", "commercial_insurance_co"},
        {"first_name", "EMMIE"},
        {"gender", "female"},
        {"last_name", "DOE"},
        {"member_id", "987654321"},
        {"payer_responsibility", "secondary"},
        {"address", new Dictionary<string, object>{
            {"address_lines", new string[] {"100 CALHOUN"}},
            {"city", "CHARLESTON"},
            {"state", "SC"},
            {"zipcode", "29407"}}}
    });

client.claims(cobClaimRequest);
```

```swift
let data = [
  "correlation_id": "CLAIM1158654",
  "transaction_code": "chargeable",
  "trading_partner_id": "MOCKPAYER"
  "billing_provider": [
      "address": [
          "address_lines": [
              "25 RAINBOW ROW"
          ],
          "city": "CHARLESTON",
          "state": "SC",
          "zipcode": "29407"
      ],
      "npi": "1487640231",
      "organization_name": "MEDCO MEDICAL INC",
      "payment_address": [
          "address_lines": [
              "PO BOX 123"
          ],
          "city": "CHARLESTON",
          "state": "SC",
          "zipcode": "29401"
      ],
      "tax_id": "123456789",
      "taxonomy_code": "777B12345X"
  ],
  "claim": [
      "claim_frequency": "original",
      "direct_payment": "y",
      "information_release": "signed_statement",
      "place_of_service": "home",
      "plan_participation": "assigned",
      "prior_authorization_number": "P00171408ABCDEF",
      "provider_signature": true,
      "service_facility": [
          "address": [
              "address_lines": [
                  "300 RIVERS AVE"
              ],
              "city": "CHARLESTON",
              "state": "SC",
              "zipcode": "29412"
          ],
          "organization_name": "MEDCITY"
      ],
      "service_lines": [
          [
              "adjudication": [
                  "adjustments": [
                      [
                          "amount": "28.22",
                          "group": "patient_responsibility",
                          "reason": "2"
                      ],
                      [
                          "amount": "26.79",
                          "group": "contractual_obligations",
                          "reason": "45"
                      ]
                  ],
                  "amount": "40.66",
                  "amount_owed": "0",
                  "claim_paid_date": "2017-04-04",
                  "payer_id": "62308",
                  "procedure_code": "T4529",
                  "procedure_qualifier": "HC",
                  "quantity": "246"
              ],
              "charge_amount": "95.67",
              "diagnosis_codes": [
                  "N184"
              ],
              "is_emergency": false,
              "ordering_provider": [
                  "first_name": "STEVEN",
                  "last_name": "DOE",
                  "npi": "1912301953",
                  "state_license_number": "SC12345"
              ],
              "procedure_code": "T4529",
              "provider_control_number": "900001",
              "service_date": "2017-03-20",
              "unit_count": "246",
              "unit_type": "units"
          ],
          [
              "adjudication": [
                  "adjustments": [
                      [
                          "amount": "72",
                          "group": "other_adjustments",
                          "reason": "96"
                      ]
                  ],
                  "amount": "0",
                  "amount_owed": "0",
                  "claim_paid_date": "2017-04-04",
                  "payer_id": "62308",
                  "procedure_code": "A4554",
                  "procedure_qualifier": "HC",
                  "quantity": "120"
              ],
              "charge_amount": "72",
              "diagnosis_codes": [
                  "N184"
              ],
              "is_emergency": false,
              "ordering_provider": [
                  "first_name": "STEVEN",
                  "last_name": "DOE",
                  "npi": "1912301953",
                  "state_license_number": "SC12345"
              ],
              "procedure_code": "A4554",
              "provider_control_number": "900002",
              "service_date": "2017-03-20",
              "unit_count": "120",
              "unit_type": "units"
          ]
      ],
      "total_charge_amount": "167.67"
  ],
  "coordination_of_benefits": [
      "payer": [
          "id": "777654",
          "organization_name": "BCBSSC"
      ],
      "payer_amount_paid": "40.66",
      "subscriber": [
          "address": [
              "address_lines": [
                  "100 CALHOUN"
              ],
              "city": "CHARLESTON",
              "state": "SC",
              "zipcode": "29407"
          ],
          "authorize_payment_to_billing_provider": "yes",
          "claim_filing_code": "commercial_insurance_co",
          "first_name": "EMMIE",
          "group_number": "888754",
          "last_name": "DOE",
          "member_id": "987654321",
          "payer_responsibility": "primary",
          "relationship": "self",
          "release_of_information_code": "signed_statement"
      ]
  ],
  "payer": [
      "address": [
          "address_lines": [
              "PO BOX 301404"
          ],
          "city": "CHARLESTON",
          "state": "SC",
          "zipcode": "29407"
      ],
      "id": "12345",
      "organization_name": "CHARLESTON HEALTH PLAN"
  ],
  "receiver": [
      "id": "EMPORIUM",
      "organization_name": "X12 FLAT FILE EMPORIUM"
  ],
  "submitter": [
      "contacts": [
          [
              "contact_methods": [
                  [
                      "type": "phone",
                      "value": "8431114444"
                  ]
              ],
              "name": "BOB DOE"
          ]
      ],
      "id": "55512",
      "organization_name": "MEDCO MEDICAL INC"
  ],
  "subscriber": [
      "address": [
          "address_lines": [
              "100 CALHOUN"
          ],
          "city": "CHARLESTON",
          "state": "SC",
          "zipcode": "29407"
      ],
      "birth_date": "2015-01-05",
      "claim_filing_code": "commercial_insurance_co",
      "first_name": "EMMIE",
      "gender": "female",
      "last_name": "DOE",
      "member_id": "987654321",
      "payer_responsibility": "secondary"
  ]
] as [String:Any]
try client.claims(params: data)
```


> Sample Coordination of Benefits Claim Request (example includes 3 payers, with COB as a list).

```python
client.claims({
    "trading_partner_id": "MOCKPAYER",
    "billing_provider": {
        "address": {
            "address_lines": [
                "25 RAINBOW ROW"
            ], 
            "city": "CHARLESTON", 
            "state": "SC", 
            "zipcode": "29407"
        }, 
        "npi": "1487640231", 
        "organization_name": "MEDICO MEDICAL INC", 
        "payment_address": {
            "address_lines": [
                "PO BOX 123"
            ], 
            "city": "CHARLESTON", 
            "state": "SC", 
            "zipcode": "29401"
        }, 
        "tax_id": "123456789", 
        "taxonomy_code": "777B12345X"
    }, 
    "claim": {
        "claim_frequency": "original", 
        "direct_payment": "y", 
        "information_release": "signed_statement", 
        "place_of_service": "home", 
        "plan_participation": "assigned", 
        "provider_signature": true, 
        "service_lines": [
            {
                "charge_amount": "570", 
                "diagnosis_codes": [
                    "Z930"
                ], 
                "is_emergency": false, 
                "ordering_provider": {
                    "first_name": "STEVEN", 
                    "last_name": "DOE", 
                    "npi": "1912301953"
                }, 
                "procedure_code": "A4605", 
                "provider_control_number": "992443", 
                "service_date": "2017-01-24", 
                "unit_count": "30", 
                "unit_type": "units"
            }
        ], 
        "total_charge_amount": "570"
    }, 
    "coordination_of_benefits": [
        {
            "payer": {
                "id": "123456", 
                "organization_name": "AETNA HEALTH PLANS"
            }, 
            "subscriber": {
                "address": {
                    "address_lines": [
                        "100 Calhoun Street"
                    ], 
	
                    "city": "CHARLESTON", 
                    "state": "SC", 
                    "zipcode": "29407"
                }, 
                "authorize_payment_to_billing_provider": "yes", 
                "claim_filing_code": "commercial_insurance_co", 
                "first_name": "EMMIE", 
                "group_number": "47672912001", 
                "last_name": "DOE", 
                "member_id": "W128675309", 
                "payer_responsibility": "secondary", 
                "relationship": "self", 
                "release_of_information_code": "signed_statement"
            }
        }, 
        {
            "payer": {
                "id": "MCAIDSC", 
                "organization_name": "MEDICAID SC"
            }, 
            "subscriber": {
                "address": {
                    "address_lines": [
                        "100 Calhoun Street"
                    ], 
                    "city": "CHARLESTON", 
                    "state": "SC", 
                    "zipcode": "29407"
                }, 
                "authorize_payment_to_billing_provider": "yes", 
                "claim_filing_code": "medicaid", 
                "first_name": "EMMIE", 
                "last_name": "DOE", 
                "member_id": "519108745", 
                "payer_responsibility": "tertiary", 
                "relationship": "self", 
                "release_of_information_code": "signed_statement"
            }
        }
    ], 
    "correlation_id": "C0200000000001150965", 
    "payer": {
        "address": {
            "address_lines": [
                "PO BOX 301404"
            ], 
            "city": "CHARLESTON", 
            "state": "SC", 
            "zipcode": "29407"
        }, 
        "id": "12345", 
        "organization_name": "CHARLESTON MEDICARE PLAN"
    }, 
    "receiver": {
        "id": "EMPORIUM", 
        "organization_name": "X12 FLAT FILE EMPORIUM"
    }, 
    "submitter": {
        "contacts": [
            {
                "contact_methods": [
                    {
                        "type": "phone", 
                        "value": "8431114444"
                    }
                ]
            }
        ], 
        "id": "55512", 
        "organization_name": "MEDICO MEDICAL INC"
    }, 
    "subscriber": {
        "address": {
            "address_lines": [
                "100 Calhoun Street"
            ], 
            "city": "CHARLESTON", 
            "state": "SC", 
            "zipcode": "29403"
        }, 
        "birth_date": "1930-11-26", 
        "claim_filing_code": "medicare_part_b", 
        "first_name": "EMMIE", 
        "gender": "male", 
        "last_name": "DOE", 
        "member_id": "86753090020", 
        "payer_responsibility": "primary"
    }, 
    "transaction_code": "chargeable"
})
```



*Available modes of operation: batch/async*

Following the standard X12 837 format, the Claims endpoint allows applications to easily submit claims to designated trading partners. A Claim is submitted to the trading partner to report services completed and request compensation.  To understand how the Claims endpoint works, reference our <a href="https://pokitdok.com/developers/api/#api-claim-submission">Claims workflow</a>.

The Claims endpoint gives clients the ability to submit Professional (837P) claims. Professional format claims are submitted using the CMS-1500 parameters by physicians, suppliers and other non-institutional providers. To review which trading partners support claim transactions, visit our <a href="https://platform.pokitdok.com/tradingpartners#/">trading partners list</a>.

Once a claim has been submitted, status can be tracked through PokitDok's system using the Activities endpoint.  There is also an option to supply a callback_url in the claim request which indicates that your application should be notified when the asynchronous processing is complete and a claim acknowledgement has been received from the trading partner.  In order to track status in the trading partner's adjudication system, please utilize the Claim Status endpoint.

A trading partner's first response lets you know if the request has been accepted (or rejected) by their claims validation system. Once your claim submission is accepted by the trading partner, it will enter their adjudication system. A tracking id or claim control number will be assigned after passing the validation stage, which can then be used in claims status requests to track the claim. A claim can be monitored via a Claims Status request once the claim has been accepted in the trading partner’s adjudication system. The speed at which a claim is adjudicated is dependent on the trading partner. On average it takes 5-7 days for a claim to enter a payer’s adjudication system, thus it is recommended to wait at least a week after submitting a claim to check its status. Once adjudication is complete, the trading partner will return an electronic remittance advice or ERA (if registered to receive ERAs), otherwise a paper remittance advice is sent with final adjudication information.  Review our [claim payments reference](claim_payments.html) for additional information.

A special `trading_partner_id` called `MOCKPAYER` is available for use to test different claims scenarios.
See [MOCKPAYER claims testing](#mockpayer-claims-testing) for details.

The [Payments](#payments) endpoints may be used as a companion to the Claims endpoint to search and retrieve 
claim payment information including the raw X12 835 data.  Individual claim payment objects will be assigned 
to the matching claims activity's result.  The Payments endpoints are useful when the application has a need 
to review a summary of payment information or match deposits back up with the claims activities that were 
bundled in a single payment.

### Endpoint Description

<!--- beginning of table -->

| Endpoint | HTTP Method | Description                                      |
|:---------|:------------|:-------------------------------------------------|
| /claims/ | POST        | Submit a claim to the specified trading partner. |

<!--- end of table -->

### Parameters

The `/claims/` endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter                                     | Description                                                                                                                                                                                                                                                                           | CMS 1500                                           |
|:----------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------|
| billing_provider                              | Required: A dictionary of information for the provider that is billing for services. Uses the provider object [below](#claims-provider-object).                                                                                                                                       | 33: Billing Provider Info                          |
| claim                                         | Dictionary of information representing a claim for services that have been performed by a health care provider for the patient.                                                                                                                                                       |                                                    |
| claim.claim_frequency                         | Used to identify if a claim is original, corrected or canceled. Defaults to original. A full list of possible values can be found [below](#claim-frequency).  If submitting a corrected claim, claim.original_reference_number is required.      					                                                                                                                   |                                                    |
| claim.provider_signature                      | Whether a provider signature is associated with the claim. Defaults to true.                                                                                                                                                                                                          |                                                    |
| claim.plan_participation                      | Whether there is plan participation associated with the claim. Defaults to assigned. Possible values are assigned, lab, and n/a.                                                                                                                                                      |                                                    |
| claim.direct_payment                          | Whether the claim was a direct payment to the provider. Possible values are y, n, and n/a. Selecting y indicates patient signature included on CMS 1500 form box 13 and payment sent to provider.                                                                                                                                                                                                           |                                                    |
| claim.information_release                     | Information release informatin associated with the claim. Possible values are informed_consent and signed_statement.                                                                                                                                                                  |                                                    |
| claim.medical_record_number                   | The patient's medical record number.                                                                                                                                                                                                                                                  |     
| claim.clinical_laboratory_improvement_amendment_number | The Clinical Laboratory Improvement Amendment (CLIA) number for the facility.
                                                                         |    
| claim.onset_date                              | Optional: the date of first symptoms for the illness. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                 | 14: Date of current illness OR injury OR pregnancy |
| claim.place_of_service                        | The location where services were performed (e.g. office). A full list of possible values is included [below](#place-of-service).                                                                                                                                                      | 24b: Place of service                              |
| claim.patient_paid_amount                     | Optional: The amount the patient has already paid the provider for the services listed in the claim. When reporting cash payment encounters for the purpose of contributing those amounts toward the member's deductible, the patient_paid_amount will equal the total_charge_amount. | 29: Amount Paid                                    |
| claim.patient_signature_on_file               | Boolean indicator for whether or not a patient's signature is on file to authorize the release of medical records. Defaults to true if not specified.                                                                                                                                 | 12: Patient's or authorized person's signature     |
| claim.statement_date                          | The (start) date of this statement. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                   |                                                    |
| claim.statement_end_date                      | The end date of this statement. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                       |                                                    |
| claim.note                                    | Claim Note object.                                                                                                                                                                                                                                                       |                                                    |
| claim.note.reference_code                     | Reference codes associated with claim note. Possibilities are additional_information (ADD), goals_rehab_discharge (DCP), certification_narrative (CER), diagnosis_description (DGN), third_party_organization_notes (TPO).                                                            |                                                    |
| claim.note.note                 		| Message text for claim note.                                                            |                                                    |                                                                         |                                                    |
| claim.service_lines                           | List of services that were performed as part of this claim.                                                                                                                                                                                                                           |                                                    |
| claim.service_lines.charge_amount             | The amount charged for this specific service. (e.g. 100.00)                                                                                                                                                                                                                           | 24f: Charges                                       |
| claim.service_lines.diagnosis_codes           | A list of diagnosis codes related to this service. (e.g. 487.1)                                                                                                                                                                                                                       | 21: Diagnosis or nature of illness or injury       |
| claim.service_lines.procedure_code            | The CPT code for the service that was performed                                                                                                                                                                                                                                       | 24d: Procedures, Services, or Supplies             |
| claim.service_lines.procedure_modifier_codes  | Optional: List of modifier codes for the specified procedure. (e.g. ["GT"])  Some trading partners may require explicit placement of specific modifier codes within this list.  When a partner mandates this, you may use `""` to advance to the next slot in the list.  (e.g. `["", "GT"]` when the partner indicates `GT` must be sent as the second modifier and no other modifiers are to be included.)                                                                               | 24d: Procedures, Services, or Supplies             |
| claim.service_lines.provider_control_number   | The provider's control number.                                                                                                                                                                                                                                                        |                                                    |
| claim.service_lines.note              | Service Line Note object.                                                                                                                                                                                                              							     |						  |
| claim.service_lines.note.reference_code              | Reference codes associated with service line note. Possibilities are additional_information (ADD) and goals_rehab_discharge (DCP).                                                                                                                                                                                                      |                     |
| claim.service_lines.note.note              | Message text for service line note.				                                                                                                  | 				                     |
| claim.service_lines.service_date              | The date the service was performed. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                   | 24a: Date(s) of service (from)                     |
| claim.service_lines.service_end_date          | Optional: The end date for the service. Use this to utilize a date range for the service date. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                        | 24a: Date(s) of service (to)                       |
| claim.service_lines.unit_count                | Number of units of this service. (e.g. 1.0)                                                                                                                                                                                                                                           | 24g: Days or Units                                 |
| claim.service_lines.unit_type                 | The type of unit being described for this particular service's unit count. Possible values include: units, days                                                                                                                                                                       |                                                    |
| claim.service_lines.procedure_description     | The procedure description of the service.                                                                                                                                                                                                                                             |                                                    |
| claim.service_lines.sales_tax                 | The sales tax of a service.                                                                                                                                                                                                                                                           |                                                    |
| claim.service_lines.is_emergency              | Boolean of whether the service is an emergency.                                                                                                                                                                                                                                       |                                                    |
| claim.service_lines.begin_therapy_date        | The start date of therapy associated to a service. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                    |                                                    |
| claim.service_lines.certification_revision_date| Date of revision for Durable Medical Equipment Certification. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                        |                                                    |
| claim.service_lines.last_certification_date   | Date of last certification for Durable Medical Equipment. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                             |                                                    |
| claim.service_lines.ambulance_patient_count   | The ambulance patient count associated with the service. Required if more than one patient is transported in the same vehicle.                                                                                                                                                        |                                                    |
| claim.service_lines.test_results                      | Used to communicate measurements or counts for tests.                                                                                                                                                                                                                      |                                                    |
| claim.service_lines.test_results.reference_id                   | Code which identifies the category for the measurement. Available options are original or test_results.                                                                                                                                                          |                                                    |
| claim.service_lines.test_results.measurement                   | Qualifier for the type of measurement.  Available options are height, hemoglobin, hematocrit, epoetin_starting_dosage, and creatinine.                                                                                                                                                                                                                                                |                                                    |
| claim.service_lines.test_results.value                   | Numerical value associated with the measurement.                                                                                                                                                                                                                        |                                                    |
| claim.service_lines.rendering_provider        | Rendering provider associated with the service. Used if the claim's billing provider is not the health care provider that provided this particular service. Uses the provider object [below](#claims-provider-object).                                                      |                                                    |
| claim.service_lines.purchased_service_provider| Provider associated with the purchased service. Used if the service reported in the service line item is a purchased service. Uses certain parameters available in the provider object [below](#claims-provider-object).  Tax id, taxonomy code and address are not to be submitted for a purchased service provider.                                                                                       |                                                    |
| claim.service_lines.supervising_provider      | The supervising provider associated with this claim.  Used if the claim's rendering provider is supervised by a physician.  The supervising provider must be an individual, not an organization. Uses certain parameters available in the provider object [below](#claims-provider-object).  Tax id, taxonomy code and address are not to be submitted for a supervising provider.                                                                                                                                                         |                                                    |
| claim.service_lines.ordering_provider         | Ordering provider associated with the service. Used if the claim's ordering provider is different than the rendering provider for this service line.  The ordering provider must be an individual, not an organization. Uses certain parameters available in the provider object [below](#claims-provider-object).  Tax id, taxonomy code are not to be submitted for an ordering provider.                                                                                                                             |                                                    |
| claim.service_lines.referring_provider        | Referring provider associated with the service. Used if the claim involves a referral.  The referring provider must be an individual, not an organization. Uses certain parameters available in the provider object [below](#claims-provider-object).  Tax id, taxonomy code and address are not to be submitted for a referring provider.                                                             |                                                    |
| claim.service_lines.drug                      | Information regarding the drug associated with a service.                                                                                                                                                                                                                             |                                                    |
| claim.service_lines.drug.code_type            | The code type associated to the drug.                                                                                                                                                                                                                                                 |                                                    |
| claim.service_lines.drug.code                 | The code associated to the drug.                                                                                                                                                                                                                                                      |                                                    |
| claim.service_lines.drug.unit_type            | The unit or system used to measure the drug. A full list of possible values can be found [below](#drug-unit).                                                                                                                                                                         |                                                    |
| claim.service_lines.drug.quantity             | The quantity associated with the drug.                                                                                                                                                                                                                                                |                                                    |
| claim.service_lines.drug.precription_number   | The prescription number associated to the drug.                                                                                                                                                                                                                                       |                                                    |
| claim.service_lines.dme_certification         | Information regarding the durable medical equipment certification.                                                                                                                                                                                                                    |                                                    |
| claim.service_lines.dme_certification.type    | The type of certification associated with the DME. Possible values are initial, renewal, revised.                                                                                                                                                                                     |                                                    |
| claim.service_lines.dme_certification.months  | Number of months associated with the durable medical equipment certification.                                                                                                                                                                                                         |                                                    |
| claim.service_lines.paperwork                 | Supplemental claim information (paperwork traveling separate from the claim transaction).                                                                                                                                                                                             |                                                    |
| claim.service_lines.paperwork.report_type     | The report type associated with the paperwork.                                                                                                                                                                                                                                        |                                                    |
| claim.service_lines.paperwork.transmission_method| The transmission method of the paperwork (e.g. email, fax).                                                                                                                                                                                                                        |                                                    |
| claim.service_lines.paperwork.control_number  | The control number associated with the paperwork.                                                                                                                                                                                                                                     |                                                    |
| claim.service_lines.forms                     | Supporting documentation associated with a service.                                                                                                                                                                                                                                   |                                                    |
| claim.service_lines.forms.form_type           | Type associated with a form. Possible values are form_type_code and cms_dmerc_cmn.                                                                                                                                                                                                    |                                                    |
| claim.service_lines.forms.identifier          | The form identifier.                                                                                                                                                                                                                                                                  |                                                    |
| claim.service_lines.forms.questions.question_number| The question number.                                                                                                                                                                                                                                                             |                                                    |
| claim.service_lines.forms.questions.yes_no_response| The yes or no response to the question                                                                                                                                                                                                                                           |                                                    |
| claim.service_lines.forms.questions.text_response  | The text response to the question                                                                                                                                                                                                                                                |                                                    |
| claim.service_lines.forms.questions.date_response  | The date response to the question                                                                                                                                                                                                                                                |                                                    |
| claim.service_lines.forms.questions.percent_decimal_response| The percent decimal response to the question                                                                                                                                                                                                                            |                                                    |
| claim.service_lines.referral_number           | The referral number for the service line claim                    |                                                    |
| claim.service_line.adjudication               | Provides previous payer adjudication information for the claim service line. [below](#claim-adjudication) |
| claim.paperwork                               | Supplemental claim information (paperwork traveling separate from the claim transaction).                                                                                                                                                                                             |                                                    |
| claim.paperwork.report_type                   | The report type associated with the paperwork.                                                                                                                                                                                                                                        |                                                    |
| claim.paperwork.transmission_method           | The transmission method of the paperwork (e.g. email, fax).                                                                                                                                                                                                                           |                                                    |
| claim.paperwork.control_number                | The control number associated with the paperwork.                                                                                                                                                                                                                                     |                                                    |
| claim.total_charge_amount                     | The total amount charged/billed for the claim. (e.g. 100.00)                                                                                                                                                                                                                          | 28: Total Charge                                   |
| claim.initial_treatment_date                  | The initial treatment date of this claim. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                             |                                                    |
| claim.acute_manifestation_date                | The acute manifestation date of this claim. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                           |                                                    |
| claim.last_x_ray_date                         | The last x-ray date associated with this claim. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                       |                                                    |
| claim.accident_date                           | The accident date associated with this claim. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                         |                                                    |
| claim.referring_provider                      | Referring provider associated with the service. Used if the claim involves a referral.  The referring provider must be an individual, not an organization. Uses certain parameters available in the provider object [below](#claims-provider-object).  Tax id, taxonomy code and address are not to be submitted for a referring provider.                                                               |                                                    |
| claim.rendering_provider                      | The rendering provider associated with this claim. Used if the top level billing provider is not the health care provider that provided services. Uses the provider object [below](#claims-provider-object).                                                                          |                                                    |
| claim.supervising_provider                    | The supervising provider associated with this claim.  Used if the claim's rendering provider is supervised by a physician.  The supervising provider must be an individual, not an organization. Uses certain parameters available in the provider object [below](#claims-provider-object).  Tax id, taxonomy code and address are not to be submitted for a supervising provider.                                                                                                                                                          |                                                    |
| claim.related_causes_code                     | Codes specifying a cause associated with the claim. Possibilities are auto_accident (AA), employment (EM), and other_accident (OA). Used if the top level billing provider is not the health care provider that provided services.                                                    |                                                    |
| claim.original_reference_number               | The original reference number of the claim. Required if claim.claim_frequency is "corrected".                                                                                                                                            |                                                    |
| claim.ambulance                               | Ambulance information associated with the claim.                                                                                                                                                                                                                                      |                                                    |
| claim.patient_weight                          | The weight of the patient.                                                                                                                                                                                                                                                             |                                                    |                                          
| claim.ambulance.reason_code                   | The reason for ambulance transportation. Possibilities can be seen [below](#ambulance-reason-codes).                                                                                                                                                                                  |                                                    |
| claim.ambulance.transport_distance            | The distance the patient was transported in the ambulance.                                                                                                                                                                                                                            |                                                    |
| claim.ambulance.round_trip_purpose_description| The purpose description for a round trip.                                                                                                                                                                                                                                             |                                                    |
| claim.ambulance.stretcher_purpose_description | The purpose description for stretcher use.                                                                                                                                                                                                                                            |                                                    |
| claim.ambulance.applicable_conditions         | Conditions associated with reasons for ambulance transport. Possibilities can be seen [below](#ambulance-applicable-conditions).                                                                                                                                                      |                                                    |
| claim.ambulance.not_applicable_conditions     | Conditions associated with reason not for ambulance transport. Possibilities can be seen [below](#ambulance-applicable-conditions).                                                                                                                                                   |                                                    |
| claim.ambulance.pickup_location               | The pickup location for the ambulance. Uses an address [object](#claims-address).                                                                                                                                                                                                     |                                                    |
| claim.ambulance.dropoff_location              | The dropoff location for the ambulance. Uses an address [object](#claims-address).                                                                                                                                                                                                    |                                                    |
| claim.chiropractic                            | Chiropractic information associated with the claim.                                                                                                                                                                                                                                   |                                                    |
| claim.chiropractic.spinal_condition           | Chiropractic condition associated with the claim. Possibilities can be seen [below](#chiropractic-conditions).                                                                                                                                                                        |                                                    |
| claim.chiropractic.description                | Description of the chiropractic information associcated with the claim.                                                                                                                                                                                                               |                                                    |
| claim.service_facility                        | Service facility associated with the claim.                                                                                                                                                                                                                                           |                                                    |
| claim.service_facility.organization_name      | Organization name of the service facility.                                                                                                                                                                                                                                            |                                                    |
| claim.service_facility.npi                    | NPI of the service facility.                                                                                                                                                                                                                                                          |                                                    |
| claim.service_facility.address                | Address of the service facility. Uses an address [object](#claims-address).                                                                                                                                                                                                           |                                                    |
| claim.prior_authorization_number               | Prior authorization number associated with the claim. This value is assigned by the payor.                                                                                                                                                                                                               |                                                    |                                                                                      
| claim.referral_number                         | The referral number for the claim                                                                                                                               |                                                    |
| patient                                       | Information about the patient that received services outlined in the claim. Patient information is only required when the patient is not the insurance subscriber.                                                                                                                    |                                                    |
| patient.address                               | Required: The patient’s address information. Uses the address [object](#claims-address).                                                                                                                                                                                              | 5: Patient's address                               |
| patient.birth_date                            | The patient’s birth date as specified on their policy. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                | 3: Patients Birth Date                             |
| patient.first_name                            | Required: The patient’s first name.                                                                                                                                                                                                                                                   | 2: Patient's Name                                  |
| patient.gender                                | The patient’s gender.                                                                                                                                                                                                                                                                 | 3: The patient's sex                               |
| patient.death_date                            | The patient’s date of death. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                          |                                                    |
| patient.suffix                                | The suffix of the patient.                                                                                                                                                                                                                                                            |                                                    |
| patient.phone                                 | The patient’s phone number.                                                                                                                                                                                                                                                           |                                                    |
| patient.ssn                                   | The patient’s ssn.                                                                                                                                                                                                                                                                    |                                                    |
| patient.member_id                             | Required: The patient’s member identifier.                                                                                                                                                                                                                                            |                                                    |
| patient.middle_name                           | Optional: The patient’s middle name.                                                                                                                                                                                                                                                  |                                                    |
| patient.last_name                             | Required: The patient’s last name.                                                                                                                                                                                                                                                    | 2: Patient's Name                                  |
| patient.pregnant                              | Patient pregnancy indicator. Defaults to false.                                                                                                                                                                                                                                       |                                                    |
| patient.relationship                          | Required: The patient’s relationship to the subscriber. A full list of possible values is included [below](#relationships).                                                                                                                                                           | 6: Patient's relationship to the insured           |
| subscriber                                    | Information about the insurance subscriber as it appears on their policy. Uses the subscriber [object](#claims-subscriber-object).                                                                                                                                                    |                                                    |
| trading_partner_id                            | Required: Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.                                                                                                                                                             |                                                    |
| transaction_code                              | Required: The type of claim transaction that is being submitted (e.g. "chargeable"). A full list of possible values is included [below](#transaction-code).                                                                                                                           |                                                    |
| coordination_of_benefits                      | Required for Secondary Claims: Information related to the coordination of benefits for additional payers. [object](#claims-coordination-of-benefits-object) |

<!--- end of table -->

A claim goes through an entire lifecycle after its transmission to a payer.
For details on this process, and how the [Claims Status](#claims-status)
Endpoint ties in, see our [claims API workflow](https://pokitdok.com/developers/api/#api-claim-submission).

### Response

The `/claims/` response contains an activity and thus returns the same object as the activity endpoint. This object can be seen under the activities endpoint documentation [above](#activities_response). The only difference between the activities and claims response is the data returned via the 'parameters' field. The following objects/fields are attached internally and can be accessed via the parameters object:

<!--- beginning of table -->

| Field                                           | Description                                                                                                       |
|:------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| submitter                                       | The submitter of the claims request.                                                                              |
| submitter.first_name                            | The first name of the submitter.                                                                                  |
| submitter.middle_name                           | The middle name of the submitter.                                                                                 |
| submitter.last_name                             | The last name of the submitter.                                                                                   |
| submitter.organization_name                     | The organization name of the submitter.                                                                           |
| submitter.id                                    | The unique id of the submitter.                                                                                   |
| submitter.email                                 | The email of the submitter.                                                                                       |
| submitter.contacts                              | A list of contacts associated with submitter.                                                                     |
| submitter.contacts.name                         | The name of the contact.                                                                                          |                                                    
| submitter.contacts.contact_methods              | A list of contact methods assoicated with the contact.                                                            |                                                    
| submitter.contacts.contact_methods.type         | The type of contact method. Possibilities are email, fax, phone, phone_extensions, and url.                       |                                                    
| submitter.contacts.contact_methods.value        | The value assoicated with a contact type (e.g. a phone number).                                                   |                                                    
| receiver                                        | The receiver of the claims request.                                                                               |
| receiver.id                                     | The unique id of the receiver.                                                                                    |
| receiver.organization_name                      | The organization name of the receiver.                                                                            |
| receiver.email                                  | The email of the receiver.                                                                                        |

<!--- end of table -->

### Additional Object Tables

<a name="claims-subscriber-object"></a>
Subscriber object:

<!--- beginning of table -->

| Field                              | Description                                                                                                                                                                                                                                                                           | CMS 1500                                           |
|:---------------------------------- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| address                            | The subscriber’s address information as specified on their policy. Uses an address [object](#claims-address).                                                                                                                                                                         | 7: Insured's address                               |
| birth_date                         | The subscriber’s birth date as specified on their policy. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                             | 11a: Insured's date of birth                       |
| claim_filing_code                  | Indicates the type of payment for the claim. It is an optional field and when left blank or not passed in the request, defaults to "mutually_defined". A full list of possible values is included [below](#filing).                                                                   |                                                    |
| first_name                         | Required: The subscriber’s first name as specified on their policy.                                                                                                                                                                                                                   |                                                                             
| suffix                             | The suffix if any used by the subscriber.                                                                                                                                                                                                                                             |                                                    
| middle_name                        | The subscriber’s middle name as specified on their policy.                                                                                                                                                                                                                            |                                                    |
| phone                              | The subscriber's phone number.                                                                                                                                                                                                                                                        |                                                    |
| gender                             | The subscriber’s gender as specified on their policy.                                                                                                                                                                                                                                 | 11a: Insured's sex                                 |
| group_number                       | Optional: The subscriber’s group or policy number as specified on their policy.                                                                                                                                                                                                       | 11:      Employer's policy number or group number  |
| group_name                         | Optional: The subscriber’s group name as specified on their policy.                                                                                                                                                                                                                   | 11b: Employer's name or school name                |
| member_id                          | Required: The subscriber’s member identifier.                                                                                                                                                                                                                                         | 1a: Insured's ID number                            |
| last_name                          | Required: The subscriber’s last name as specified on their policy.                                                                                                                                                                                                                    | 4: Insured's name                                  |
| ssn                                | The subscriber’s ssn name as specified on their policy.                                                                                                                                                                                                                               |                                                    |
| payer_responsibility               | Determines the position of the payer with regards to coordination of benefits. Defaults to primary. List of possibilities can be seen [below](#payer-responsibility).                                                                                                                 |                                                    |
| relationship                       | Used for coordination of benefits subscriber only. The patient’s relationship to the subscriber. A full list of possible values is included [below](#relationships).                                                                                                                  | 6: Patient's relationship to the insured           |
| authorize_payment_to_billing_provider | Used for coordination of benefits subscriber only. Values: [no, default: yes] |
| patient_signature_source           | Used for coordination of benefits subscriber only. Values: [other, default: patient] |
| release_of_information_code        | Used for coordination of benefits subscriber only. Values: [signed_statement, default: informed_consent] |

<!--- end of table -->

<a name="claims-provider-object"></a>
Provider object:

<!--- beginning of table -->

| Field                             | Description                                                                                                                                                                     | CMS 1500                                           |
|:----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| taxonomy_code                     | The taxonomy code for the provider. (e.g. "207Q00000X")                                                                                                                         | 24i: ID Qualifier                                  |
| first_name                        | The first name of the provider. Required when the provider is an individual.                                                                                                    |                                                    |
| middle_name                       | The middle name of the provider. Required when the provider is an individual.                                                                                                   |                                                    |
| last_name                         | The last name of the provider. Required when the provider is an individual.                                                                                                     |                                                    |
| suffix                            | The suffix of the provider.                                                                                                                                                     |                                                    |
| organization_name                 | The provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                            |                                                    |
| npi                               | The National Provider Identifier for the provider.                                                                                                                              | 33a: Billing Provider NPI                          |
| state_license_number              | The state license number for the provider.                                                                                                                                      | 33a: Billing Provider NPI                          |
| tax_id                            | The federal tax id for the provider. For individual providers, this may be the tax id of the medical practice or organization where a provider works.                           | 25: Federal tax ID Number (SSN EIN)                |
| provider_commercial_number        | A proprietary number assigned to a provider by the destination payer.                                                                                                            |                                                    |
| upin                              | A unique physician identification number which was replaced by the use of NPI.                                                                                                  |                                                    |
| location_number                   | A location number assigned to a provider.                                                                                                                                        |                                                    |
| address                           | The provider's address. Uses an address [object](#claims-address).                                                                                                               |                                                    |
| payment_address                   | The provider's payment address to be used when the address for payment is different than that of the billing provider.  Parameter is placed under the billing provider and uses an address [object](#claims-address).                                                                                                      |                                                    |
|contacts                          | A list of contacts associated with the provider.                                                                                                                                |                                                    |
| contacts.name                     | The name of the contact.                                                                                                                                                        |                                                    |
| contacts.contact_methods          | A list of contact methods associated with the contact.                                                                                                                          |                                                    |
| contacts.contact_methods.type     | The type of contact method. Possibilities are email, fax, phone, phone_extensions, and url.                                                                                     |                                                    |
| contacts.contact_methods.value    | The value assoicated with a contact type (e.g. a phone number).                                                                                                                 |                                                    |

<!--- end of table -->


<a name="claims-address"></a>
Address object:

<!--- beginning of table -->

| Field                                 | Description                                                                                                       |
|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| address_lines                         | List of strings representing the street address. (e.g. ["123 MAIN ST.", "Suite 4"])                               |
| city                                  | The city component of a address. (e.g. "SAN MATEO")                                                               |
| state                                 | The state component of a address. (e.g. "CA")                                                                     |
| zipcode                               | The zip/postal code. (e.g. "94401")                                                                               |
| country                               | The country component of a address.                                                                               |

<!--- end of table -->

<a name="claims-coordination-of-benefits-object"></a>
Coordination of Benefits object:
The coordination of benefits object can be either a list or a dict. If two payers are included in the claim (one payer in COB), COB will be a dict. If three or more payers are included (two+ payers in COB), COB will be a list.

<!--- beginning of table -->

| Field                                 | Description                                                                                                       |
|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| subscriber                            | Required: The subscriber of the policy for the additional payer(s). May be the same as the original payer with some additional field requirements. Uses the Subscriber [object](#claims-subscriber-object). |
| adjustments                           | List of claim adjustments (maximum of five). Support varies by trading partner. Uses the adjustment [below](#claim-adjustment). |
| payer_amount_paid                | Amount paid on the claim after claim has been adjudicated by the primary payer. |
| amount_owed                | Remaining liability amount to be paid after adjudication by the primary payer. |
| payer                | Required: The payer information to communicate to the top level payer for coordination of benefits.  Uses the payer [object](#claim-adjustment). |

<!--- end of table -->

<a name="claim-adjustment"></a>
Claim Adjustment object:
Adjustments are used to balance the original submitted billing amounts, monetary and service units, against the primary payer, secondary payer, and patient's payment amounts and responsibility.

<!--- beginning of table -->

| Field                              | Description                                                              |
| :----------------------------------|:-------------------------------------------------------------------------|
| group                              | Required: The adjustment group code. Identifies the payment adjustment category. [object](#claim-adjustment-group-codes) |
| reason                             | Required: The adjustment reason code as defined in HCFA CPCS 139 (Claim Adjustment Reason Codes). Identifies the reason the adjustment was made. |
| amount                             | Required: Adjusts a claim total or service line monetary amount. |
| quantity                           | Adjusts the number of service units used in the claim or on within a specific service line. |

<!--- end of table -->

<a name="claim-adjustment-group-codes"></a>
Full list of possible values that can be used in the `adjustment.group` field:

<!--- beginning of table -->

| adjustment.group Values                       |
|:---------------------------------- |
| 'contractual_obligations' |
| 'other_adjustments' |
| 'payor_initiated_reductions' |
| 'patient_responsibility' |
| 'corrections_and_reversals' |

<!--- end of table -->

<a name="claim-adjudication"></a>
Claim Adjudication object:
Tracks previous payments and adjustments made to a service line within a Coordination of Benefits transaction.

<!--- beginning of table -->

| Field                              | Description                                                              |
| :----------------------------------|:-------------------------------------------------------------------------|
| amount                             | Required: The amount paid for the service line.                          |
| procedure_code                     | Required: The service line  procedure code (HCPCS/CPT).                              |
| procedure_modifiers                | List of modifier codes for the service line procedure (maximum of 4)     |
| quantity                           | The service line quantity                                                |
| adjustments                        | List of claim service line adjustments (maximum of 5). Uses the adjustment [object](#claim-adjustment) |
| claim_paid_date                    | Required: The date the service line was paid. In ISO8601 format (YYYY-MM-DD). |
| amount_owed                        | The remaining patient liability amount for the service line. |

<!--- end of table -->

<a name="coordination-of-benefits-payer"></a>
Payer object:

<!--- beginning of table -->

| Field                              | Description                                                                                                                                                                                                                                                                           |
|:---------------------------------- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| organization_name               | Required: Name information for the coordination of benefits payer. |
| id                              | Required: Numerical payer id value associated with coordination of benefits payer. |
| address                         | Address information for the coordination of benefits payer.  Uses an address [object](#claims-address).  |

<!--- end of table -->


<a name="claim-frequency"></a>
Full list of possible values that can be used in the `claim.claim_frequency` parameter on the claim:

<!--- beginning of table -->

| claim_frequency Values             |                           |
|:-----------------------------------|:--------------------------|
| nonpayment                         | original                  |
| interim_first_claim                | interim_continuing_claims |
| interim_last_claim                 | late_charges              |
| adjustment                         | corrected                 |
| cancel                             | final_claim_home_health   |

<!--- end of table -->

<a name="drug-units"></a>
Full list of possible values that can be used in the `claim.service_lines.drug.unit_type` parameter on the claim:

<!--- beginning of table -->

| unit_type Values                   |                           |
|:-----------------------------------|:--------------------------|
| international                      | gram                      |
| milligram                          | milliliter                |
| unit                               |                           |

<!--- end of table -->

<a name="ambulance-reason-codes"></a>
Full list of possible values that can be used in the `claim.ambulance.reason_code` parameter on the claim:

<!--- beginning of table -->

| reason_code Values                 |                           |
|:-----------------------------------|:--------------------------|
| nearest_or_residential_facility (A)| preferred_physician (B)   |
| family_proximity (C)               | specialist (D)            |
| rehab_facility (E)                 |                           |

<!--- end of table -->

<a name="ambulance-applicable-conditions"></a>
Full list of possible values that can be used in the `claim.ambulance.applicable_conditions` and `claim.ambulance.not_applicable_conditions` parameter on the claim:

<!--- beginning of table -->

| condition Values                   |                           |
|:-----------------------------------|:--------------------------|
| admitted_to_hospital               | moved_by_stretcher        |
| unconscious_in_shock               | emergency_transport       |
| physically_restrained              | visible_hemorrhaging      |
| ambulance_medically_necessary      | patient_confined_bed_chair|

<!--- end of table -->

<a name="chiropractic-conditions"></a>
Full list of possible values that can be used in the `claim.chiropractic.spinal_condition` parameter on the claim:

<!--- beginning of table -->

| spinal_condition Values              |                           |
|:-------------------------------------|:--------------------------|
| acute_condition                      | chronic_condition         |
| non_acute                            | non_life_threatening      |
| routine                              | symptomatic               |
| acute_manifestation_chronic_condition|                           |                    

<!--- end of table -->


<a name="place-of-service"></a>
Full list of possible values that can be used in the `claim.place_of_service` parameter on the claim:

<!--- beginning of table -->

| place_of_service Values   |                               |
|:--------------------------|:------------------------------|
| ambulance_air_or_water    | nursing	                    |
| ambulance_land            | off_campus_outpatient_hospital|
| ambulatory_substance_abuse| office			    |
| assisted_living	    | other                         |
| birthing_center           | outpatient_hospital           |
| custodial                 | outpatient_rehab              |
| end_stage_renal           | pharmacy                      |
| er_hospital               | prison                        |
| federal_qualified         | psych_partial_hospital        |
| group_home                | psych_residential             |
| home                      | public_clinic                 |
| hospice                   | residential_substance_abuse   |
| ihs_freestanding          | rural_clinic                  |
| ihs_provider              | school                        |
| immunization              | shelter                       |
| independent_clinic        | skilled_nursing               |
| independent_lab           | surgical_center               |
| inpatient_hospital        | telehealth                    |
| inpatient_psych           | temp_lodging     		    |
| inpatient_rehab           | tribal_638_freestanding       |
| mental_health_center      | tribal_638_provider           |
| mentally_retarded         | urgent_care                   |
| military                  | walkin_clinic                 |
| mobile_unit		    | worksite			    |
<!--- end of table -->


<a name="relationships"></a>
Full list of possible values that can be used in the `patient.relationships` parameter on the claim:

<!--- beginning of table -->

| relationship Values |                    |
|:--------------------|:-------------------|
| cadaver_donor       | organ_donor        |
| child               | other_relationship |
| employee            | spouse             |
| life_partner        | unknown            |

<!--- end of table -->


<a name="filing"></a>
Full list of possible values that can be used in the `subscriber.filing_code` parameter on the claim:

<!--- beginning of table -->

| filing_code Values              |                                   |
|:--------------------------------|:----------------------------------|
| automobile_medical              | medicaid                          |
| blue_cross_blue_shield          | medicare_part_a                   |
| champus                         | medicare_part_b                   |
| commercial_insurance_co         | mutualy_defined                   |
| dental_maintenance_organization | other_federal_program             |
| disability                      | other_non_federal_program         |
| epo                             | pos                               |
| federal_employee_program        | ppo                               |
| hmo                             | title_v                           |
| hmo_medicare_risk               | veterans_affairs_plan             |
| indemnity_insurance             | workers_compensation_health_claim |
| liability_medical               |                                   |

<!--- end of table -->


<a name="transaction-code"></a>
Full list of possible values that can be used in the `transaction_code` parameter on the claim:

<!--- beginning of table -->

| transaction_code Values |
|:------------------------|
| subrogation_demand      |
| chargeable              |
| reporting               |

<!--- end of table -->


<a name="admitsource"></a>
Full list of possible values that can be used in the `claim.admission_source` parameter on the claim:

<!--- beginning of table -->

| admission_source Values |                         |
|:------------------------|:------------------------|
| clinic                  | immediate_care_facility |
| emergency_room          | law_enforcement         |
| health_care_facility    | not_available           |
| hospice_transfer        | physician_referral      |
| hospital_transfer       | surgery_center          |

<!--- end of table -->


<a name="admittype"></a>
Full list of possible values that can be used in the `claim.admission_type` parameter on the claim:

<!--- beginning of table -->

| admission_type Values     |               |
|:--------------------------|:--------------|
| elective                  | newborn       |
| emergency                 | trauma_center |
| information_not_available | urgent        |

<!--- end of table -->


<a name="faciltype"></a>
Full list of possible values that can be used in the `claim.facility_type` parameter on the claim:

<!--- beginning of table -->

| facility_type Values              |                                  |
|:----------------------------------|:---------------------------------|
| clinic_corf                       | hospital_inpatient_part_b        |
| clinic_ersd                       | hospital_other_part_b            |
| clinic_opt                        | hospital_outpatient_asc          |
| clinic_rural_health               | hospital_outpatient              |
| community_mental_health_center    | hospital_swing_bed               |
| critical_access_hospital          | nonhospital_based_hospice        |
| federally_qualified_health_center | religious_nonmedical_institution |
| home_health_part_b                | skilled_nursing_inpatient_part_b |
| home_health                       | skilled_nursing_inpatient        |
| hospital_based_hospice            | skilled_nursing_outpatient       |
| hospital_inpatient_part_a         | skilled_nursing_swing_bed        |

<!--- end of table -->


<a name="patstatus"></a>
Full list of possible values that can be used in the `claim.patient_status` parameter on the claim:

<!--- beginning of table -->

| patient_status Values                        |                                                        |
|:---------------------------------------------|:-------------------------------------------------------|
| expired_at_home                              | transferred_to_hospice_at_home                         |
| expired_in_medical_facility                  | transferred_to_hospice_medical_facility                |
| expired_place_unknown                        | transferred_to_inpatient_rehab                         |
| expired                                      | transferred_to_intermediate_care_facility              |
| inpatient_at_this_hospital                   | transferred_to_long_term_care_hospital                 |
| left_against_medical_advice                  | transferred_to_nursing_facility_not_medicare_certified |
| routine_discharge                            | transferred_to_other_health_care_institution           |
| still_patient                                | transferred_to_psychiatric_hospital                    |
| transferred_to_cancer_center                 | transferred_to_short_term_hospital                     |
| transferred_to_critical_access_hospital      | transferred_to_skilled_nursing_facility                |
| transferred_to_federal_hospital              | transferred_to_swing_bed                               |
| transferred_to_home_with_home_health_service |                                                        |

<!--- end of table -->


<a name="occtype"></a>
Full list of possible values that can be used in the `claim.occurrence_information.occurrence_type` parameter on the claim:

<!--- beginning of table -->

| occurrence_type Values                               |                                                             |
|:-----------------------------------------------------|:------------------------------------------------------------|
| accident_employment_related                          | guarantee_of_payment                                        |
| accident_medical_coverage                            | home_iv_therapy_started                                     |
| accident_no_medical_coverage                         | hospice_certification                                       |
| accident_tort_liability                              | inpatient_hospital_discharge_non_covered_transplant_patient |
| active_care_ended                                    | inpatient_hospital_discharge_transplant_patient             |
| admission_scheduled                                  | insurance_denied                                            |
| beneficiary_notified_of_intent_to_bill_accomodations | last_menstrual_period                                       |
| beneficiary_notified_of_intent_to_bill_procedures    | last_therapy                                                |
| benefits_exhausted_payer_a                           | no_fault_insurance_involved                                 |
| benefits_exhausted_payer_b                           | occupational_therapy_started                                |
| benefits_exhausted_payer_c                           | onset_for_chronically_dependent_individual                  |
| benefits_terminated_primary_payer                    | onset_of_symptoms                                           |
| birth_date_insured_a                                 | outpatient_occupational_therapy_plan_reviewed               |
| birth_date_insured_b                                 | outpatient_physical_therapy_plan_reviewed                   |
| birth_date_insured_c                                 | outpatient_speech_pathology_plan_reviewed                   |
| canceled_surgery_scheduled                           | physical_therapy_started                                    |
| cardiac_rehab_started                                | pre_admission_testing                                       |
| comprehensive_outpatient_rehab_plan_reviewed         | retirement_spouse                                           |
| cost_outlier_status_begins                           | retirement                                                  |
| crime_victim                                         | snf_bed_became_available                                    |
| discharge                                            | speech_therapy_started                                      |
| discharged_on_continuous_course_iv_therapy           | split_bill_date                                             |
| effective_date_insured_a                             | start_coordination_period_for_esrd_beneficiaries            |
| effective_date_insured_b                             | start_infertility_treatement_cycle                          |
| effective_date_insured_c                             | ur_notice_received                                          |
| election_of_extended_care_facilities                 |                                                             |

<!--- end of table -->


<a name="valuecode"></a>
Full list of possible values that can be used in the `claim.value_information.value_type` parameter on the claim:

<!--- beginning of table -->

| value_information.value_type                                  |                                                      |
|:--------------------------------------------------------------|:-----------------------------------------------------|
| accident_hour                                                 | medicare_blood_deductible                            |
| any_liability_insurance                                       | medicare_coinsurance_amount_first_year               |
| arterial_blood_gas                                            | medicare_coinsurance_amount_second_year              |
| black_lung                                                    | medicare_lifetime_reserve_amount_first_year          |
| blood_deductible_pints                                        | medicare_lifetime_reserve_amount_second_year         |
| blood_pints_furnished                                         | medicare_new_technology_add_on_payment               |
| blood_pints_replaced                                          | medicare_spend_down_amount                           |
| cardiac_rehab_visits                                          | most_common_semi_private_rate                        |
| catastrophic                                                  | multiple_patient_ambulance_transport                 |
| chiropractic_services_offset_patient_payment_amount           | new_coverage_not_implemented_by_managed_care_plan    |
| coinsurance_days                                              | newborn_birth_weight                                 |
| coinsurance_payer_a                                           | no_fault_insurance                                   |
| coinsurance_payer_b                                           | non_covered_days                                     |
| coinsurance_payer_c                                           | occupational_therapy_visits                          |
| conventional_provider_payment_amount_non_demonstration_claims | operating_disproportionate_share_amount              |
| copayment_payer_a                                             | operating_indirect_medical_education_amount          |
| copayment_payer_b                                             | operating_outlier_amount                             |
| copayment_payer_c                                             | other_assessments_payer_a                            |
| covered_days                                                  | other_assessments_payer_b                            |
| covered_self_administrable_drugs_diagnostic_study             | other_assessments_payer_c                            |
| covered_self_administrable_drugs_emergency                    | other_medical_services_offset_patient_payment_amount |
| covered_self_administrable_drugs_not_self_administrable       | oxygen_saturation                                    |
| deductible_payer_a                                            | part_a_demonstration_payment                         |
| deductible_payer_b                                            | part_b_coinsurance                                   |
| deductible_payer_c                                            | part_b_demonstration_payment                         |
| dental_services_offset_patient_payment_amount                 | patient_estimated_responsibility                     |
| disabled_beneficiary_under_65_with_lghp                       | patient_height                                       |
| eligibility_threshold_charity_care                            | patient_liability_amount                             |
| epo_units_provided                                            | patient_weight                                       |
| esrd_beneficiary_in_medicare_coordination_period_with_eghp    | peritoneal_dialysis                                  |
| esrd_network_funding                                          | phs                                                  |
| estimated_responsibility_payer_a                              | physical_therapy_visits                              |
| estimated_responsibility_payer_b                              | podiatric_services_offset_patient_payment_amount     |
| estimated_responsibility_payer_c                              | prescription_drugs_offset_patient_payment_amount     |
| flat_rate_surgery_charge                                      | professional_charges_included_and_billed_separately  |
| grace_days                                                    | provider_amount_agreed_to_accept_primary_payer       |
| health_insurance_premiums_offset_patient_payment_amount       | providers_interim_rate                               |
| hearing_ear_services_offset_patient_payment_amount            | recurring_monthly_income                             |
| hematocrit_reading                                            | regulatory_surcharges_payer_a                        |
| hemoglobin_reading                                            | regulatory_surcharges_payer_b                        |
| hh_reimbursements_part_a                                      | regulatory_surcharges_payer_c                        |
| hh_reimbursements_part_b                                      | service_furnished_location_number                    |
| hh_visits_part_a                                              | skilled_nurse_home_visit_hours                       |
| hh_visits_part_b                                              | special_zip_code_reporting                           |
| hha_branch_msa                                                | speech_therapy_visits                                |
| home_health_aide_home_visit_hours                             | state_charity_care_percent                           |
| hospital_no_semi_private_rooms                                | surplus                                              |
| inpatient_professional_charges_combined_billed                | veterans_affairs                                     |
| interest_amount                                               | vision_eye_services_offset_patient_payment_amount    |
| lifetime_reserve_days                                         | workers_compensation                                 |
| medicaid_rate_code                                            | working_age_beneficiary_spouse_with_eghp             |
| medicaid_rate_code                                            | working_age_beneficiary_spouse_with_eghp             |

<!--- end of table -->

<a name="payer-responsibility"></a>
Full list of possible values that can be returned in the `subscriber.payer_responsibility` field on the claim:

<!--- beginning of table -->

| payer_responsibility Values |                    |
|:----------------------------|:-------------------|
| four                        | five               |
| six                         | seven              |
| eight                       | nine               |
| ten                         | eleven             |
| primary                     | secondary          |
| tertiary                    | unknown            |

<!--- end of table -->

<a name="mockpayer-claims-testing"></a>
### MOCKPAYER Additional Details

The `MOCKPAYER` trading partner id supports a couple different testing scenarios to help API client applications
verify their handling of different `claims` activity results.  Similar to some payment processors, special
member id values may be used in a MOCKPAYER claims API request to simulate a rejection for that claim.

The `00001234` member id value may be used to simulate a claim being rejected due to an invalid date of service.
This will often happen when a claim is submitted for a date of service prior to the date that member became
active for coverage.

The `00009999` member id value may be used to simulate a claim being rejected due to an invalid date of birth
for the subscriber/patient.  This can often happen if the eligiblity API is not utilized prior to submitting
a claims API request to verify the member's information with the trading partner.

When `MOCKPAYER` claims requests are submitted for processing, they'll enter a `scheduled` state if they're
valid claims requests.   About 5 minutes or so after submission, those `MOCKPAYER` claims will be processed.
If any of the above values are included in the claims request data, it will be rejected.   Otherwise, it
will be accepted for further processing.
