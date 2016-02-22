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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
}` https://platform.pokitdok.com/api/v4/claims/
```

```python
pd.claims({
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
})
```

```csharp
client.claims (
			new Dictionary<string, object> {
				{"transaction_code", "chargeable"},
				{"trading_partner_id", "MOCKPAYER"},
				{"billing_provider", new Dictionary<string, object> {
						{"taxonomy_code", "207Q00000X"},
						{"first_name", "Jerome"},
						{"last_name", "Aya-Ay"},
						{"npi", "1467560003"},
						{"address", new Dictionary<string, object> {
								{"address_lines", new string[] { "8311 WARREN H ABERNATHY HWY" }},
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
								{"address_lines", new string[] { "123 N MAIN ST" }},
								{"city", "SPARTANBURG"},
								{"state", "SC"},
								{"zipcode", "29301"}
							}},
						{"birth_date", "1970-01-01"},
						{"gender", "female"}
					}},
				{"claim", new Dictionary<string, object> {
						{"total_charge_amount", 60.0},
						{"service_lines", new object[] {
								new Dictionary<string, object> {
									{"procedure_code", "99213"},
									{"charge_amount", 60.0},
									{"unit_count", 1.0},
									{"diagnosis_codes", new string[] { "487.1" }},
									{"service_date", "2014-06-01"}
					}}}}}
			});
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
        "birth_date": "1971-01-01",
        "gender": "male"
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
pd.claims({
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
        "birth_date": "1971-01-01",
        "gender": "male"
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
})
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
pd.claims({
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
})
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
        "birth_date": "1970-01-01",
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
                    "701.9"
                ],
                "service_date": "2014-11-24"
            }
        ]
    }
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
pd.claims({
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
        "birth_date": "1970-01-01",
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
                    "701.9"
                ],
                "service_date": "2014-11-24"
            }
        ]
    }
})
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
pd.claims({
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
})
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
pd.claims({
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
})
```

> Sample Institutional claim for continuing/hospice care:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
  "billing_provider": {
    "address": {
      "address_lines": [
        "100 New Street"
      ],
      "city": "New Town",
      "state": "CA",
      "zipcode": "941001001"
    },
    "npi": "1912301953",
    "organization_name": "TEST FACILITY,LLC",
    "taxonomy_code": "251G00000X",
    "tax_id": "123456789"
  },
  "claim": {
    "admission_date": "2011-08-05",
    "statement_date": "2015-03-01",
    "statement_end_date": "2015-03-31",
    "admission_type": "elective",
    "admission_source": "not_available",
    "patient_status": "still_patient",
    "attending_provider": {
      "npi": "1467560003",
      "first_name": "JEAN",
      "last_name": "SMITH",
      "taxonomy_code": "251G00000X"
    },
    "claim_frequency": "interim_continuing_claims",
    "direct_payment": "y",
    "information_release": "informed_consent",
    "medical_record_number": "661",
    "facility_type": "nonhospital_based_hospice",
    "plan_participation": "assigned",
    "occurrence_information": [
      {
        "occurrence_type": "hospice_certification",
        "occurrence_date": "2013-03-27"
      }
    ],
    "value_information": [
      {
        "value_type": "service_furnished_location_number",
        "value": "36420"
      }
    ],
    "service_lines": [
      {
        "charge_amount": "4000",
        "diagnosis_codes": [
          "29411"
        ],
        "procedure_code": "Q5002",
        "revenue_code": "0651",
        "service_date": "2015-03-01",
        "unit_count": "31",
        "unit_type": "days",
        "provider_control_number": "6750000"
      }
    ],
    "total_charge_amount": "4000"
  },
  "subscriber": {
    "address": {
      "address_lines": [
        "1234 MAIN AVE"
      ],
      "city": "NEW TOWN",
      "state": "CA",
      "zipcode": "941001001"
    },
    "birth_date": "1920-07-25",
    "claim_filing_code": "medicare_part_a",
    "first_name": "JOHN",
    "gender": "male",
    "last_name": "SMITH",
    "member_id": "R12345678",
    "payer_responsibility": "primary"
  },
  "trading_partner_id": "MOCKPAYER",
  "transaction_code": "chargeable"
}' https://platform.pokitdok.com/api/v4/claims/
```

```python
pd.claims({
  "billing_provider": {
    "address": {
      "address_lines": [
        "100 New Street"
      ],
      "city": "New Town",
      "state": "CA",
      "zipcode": "941001001"
    },
    "npi": "1912301953",
    "organization_name": "TEST FACILITY,LLC",
    "taxonomy_code": "251G00000X",
    "tax_id": "123456789"
  },
  "claim": {
    "admission_date": "2011-08-05",
    "statement_date": "2015-03-01",
    "statement_end_date": "2015-03-31",
    "admission_type": "elective",
    "admission_source": "not_available",
    "patient_status": "still_patient",
    "attending_provider": {
      "npi": "1467560003",
      "first_name": "JEAN",
      "last_name": "SMITH",
      "taxonomy_code": "251G00000X"
    },
    "claim_frequency": "interim_continuing_claims",
    "direct_payment": "y",
    "information_release": "informed_consent",
    "medical_record_number": "661",
    "facility_type": "nonhospital_based_hospice",
    "plan_participation": "assigned",
    "occurrence_information": [
      {
        "occurrence_type": "hospice_certification",
        "occurrence_date": "2013-03-27"
      }
    ],
    "value_information": [
      {
        "value_type": "service_furnished_location_number",
        "value": "36420"
      }
    ],
    "service_lines": [
      {
        "charge_amount": "4000",
        "diagnosis_codes": [
          "29411"
        ],
        "procedure_code": "Q5002",
        "revenue_code": "0651",
        "service_date": "2015-03-01",
        "unit_count": "31",
        "unit_type": "days",
        "provider_control_number": "6750000"
      }
    ],
    "total_charge_amount": "4000"
  },
  "subscriber": {
    "address": {
      "address_lines": [
        "1234 MAIN AVE"
      ],
      "city": "NEW TOWN",
      "state": "CA",
      "zipcode": "941001001"
    },
    "birth_date": "1920-07-25",
    "claim_filing_code": "medicare_part_a",
    "first_name": "JOHN",
    "gender": "male",
    "last_name": "SMITH",
    "member_id": "R12345678",
    "payer_responsibility": "primary"
  },
  "trading_partner_id": "MOCKPAYER",
  "transaction_code": "chargeable"
})
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
}` https://platform.pokitdok.com/api/v4/claims/
```

```python
pd.claims({
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
        "birth_date": "1970-01-01",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
})
```

> Claims request containing information for rendering provider.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
{
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
        "birth_date": "1970-01-01",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "rendering_provider": {
              "npi": "2228880001",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
})
```

```python
pd.claims({
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
        "birth_date": "1970-01-01",
        "gender": "female"
    },
    "claim": {
        "total_charge_amount": 60.0,
        "rendering_provider": {
              "npi": "2228880001",
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
                    "487.1"
                ],
                "service_date": "2014-06-01"
            }
        ]
    }
})
```

*Available modes of operation: batch/async*

Following the standard X12 837 format, the Claims endpoint allows
applications to easily file claims to designated trading partners.

When using the Claims endpoint, there is an option to supply a callback_url,
which indicates that your application should be notified when the asynchronous
processing is complete and a claim acknowledgement has been received from the
trading partner. The full claims request activity will be POSTed back to the
callback_url. A claim acknowledgement will be returned for each submitted
claims request. Once a claim is adjudicated, an 835 Electronic Remittance
Advice transaction will be returned to applications that are registered to receive them.
If a callback_url was registered on the claims request and claim payment information is received,
the full claims request activity will be POSTed back to the callback_url a second time.  The claim payment information will be
contained in the result section of the claims activity JSON.   The original claims acknowledgement will move to
the result_history section of the claims activity.  For a complete reference to all possible values in a claim payment result,
see our [claim payments reference](claim_payments.html)
If you are interested in receiving 835 files, please <a href="http://pokitdok.com/contact?context=PokitDok">contact us</a>.

The PokitDok Claims endpoint gives clients the ability to submit either professional (837P) or institutional (837I) claims, using the same claims endpoint. If a claims request includes an _Institutional claim specific (837I)_ parameter, then the Claims endpoint will validate the request as an institutional claim and submit it accordingly. If no _Institutional claim specific_ parameter is passed in the request, then the request will be validated and transmitted as a professional claim.
Parameters that are specific to Institutional claims only have (_Insitutional claim specific_) in the Description column in the below endpoint parameter table.

| Endpoint | HTTP Method | Description                                      |
|:---------|:------------|:-------------------------------------------------|
| /claims/ | POST        | Submit a claim to the specified trading partner. |


The /claims/ endpoint accepts the following parameters:

| Parameter                                     | Description                                                                                                                                                                                                                                                                           | CMS 1500                                           |
|:----------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------|
| billing_provider                              | Required: A dictionary of information for the provider that is billing for services.                                                                                                                                                                                                  | 33: Billing Provider Info                          |
| billing_provider.address                      | A dictionary of information for the billing provider's address.                                                                                                                                                                                                                       |                                                    |
| billing_provider.address.address_lines        | List of strings representing the street address for a billing provider. (e.g. ["123 MAIN ST.", "Suite 4"])                                                                                                                                                                            |                                                    |
| billing_provider.address.city                 | The city component of a billing provider's address. (e.g. "SAN MATEO")                                                                                                                                                                                                                |                                                    |
| billing_provider.address.state                | The state component of a billing provider's address. (e.g. "CA")                                                                                                                                                                                                                      |                                                    |
| billing_provider.address.zipcode              | The billing provider's zip/postal code. (e.g. "94401")                                                                                                                                                                                                                                |                                                    |
| billing_provider.first_name                   | The first name of the provider billing for services. Required when the billing provider is an individual.                                                                                                                                                                             |                                                    |
| billing_provider.last_name                    | The last name of the provider billing for services. Required when the billing provider is an individual.                                                                                                                                                                              |                                                    |
| billing_provider.organization_name            | The billing provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                                                                                                          |                                                    |
| billing_provider.npi                          | The National Provider Identifier for the provider billing for services.                                                                                                                                                                                                               | 33a: Billing Provider NPI                          |
| billing_provider.tax_id                       | The federal tax id for the provider billing for services. For individual providers, this may be the tax id of the medical practice or organization where a provider works.                                                                                                            | 25: Federal tax ID Number (SSN EIN)                |
| billing_provider.taxonomy_code                | The taxonomy code for the provider billing for services. (e.g. "207Q00000X")                                                                                                                                                                                                          | 24i: ID Qualifier                                  |
| claim                                         | Dictionary of information representing a claim for services that have been performed by a health care provider for the patient.                                                                                                                                                       |                                                    |
| claim.admission_date                          | (_Institutional claim specific_) The date the patient was admitted. UB-04 field: *12. Admission Date*                                                                                                                                                                                 |                                                    |
| claim.admission_source                        | (_Institutional claim specific_) The source of the patient's admission. A full list of possible values can be found [below](#admitsource). UB-04 field: *15. Admission Source*                                                                                                        |                                                    |
| claim.admission_type                          | (_Institutional claim specific_) The admission/type priority of the patient's admission. A full list of possible values can be found [below](#admittype).  UB-04 field: *14. Priority (Type) of Visit*                                                                                |                                                    |
| claim.facility_type                           | (_Institutional claim specific_) The type of facility where the patient was admitted. A full list of possible values can be found [below](#faciltype).                                                                                                                                |                                                    |
| claim.medical_record_number                   | The patient's medical record number.                                                                                                                                                                                                                                                  |                                                    |
| claim.onset_date                              | Optional: the date of first symptoms for the illness.                                                                                                                                                                                                                                 | 14: Date of current illness OR injury OR pregnancy |
| claim.place_of_service                        | The location where services were performed (e.g. office). A full list of possible values is included [below](#place-of-service).                                                                                                                                                      | 24b: Place of service                              |
| claim.patient_paid_amount                     | Optional: The amount the patient has already paid the provider for the services listed in the claim. When reporting cash payment encounters for the purpose of contributing those amounts toward the member's deductible, the patient_paid_amount will equal the total_charge_amount. | 29: Amount Paid                                    |
| claim.patient_signature_on_file               | Boolean indicator for whether or not a patient's signature is on file to authorize the release of medical records. Defaults to true if not specified.                                                                                                                                 | 12: Patient's or authorized person's signature     |
| claim.patient_status                          | (_Institutional claim specific_) The patient's status as of the dates covered through the statement. A full list of possible values can be found [below](#patstatus).  UB-04 field: *17. Patient Discharge Status*                                                                    |                                                    |
| claim.statement_date                          | The (start) date of this statement.                                                                                                                                                                                                                                                   |                                                    |
| claim.statement_end_date                      | The end date of this statement.                                                                                                                                                                                                                                                       |                                                    |
| claim.value_information                       | (_Institutional claim specific_) The value code that applies to this claim. A full list of possible values can be found [below](#valuecode).                                                                                                                                          |                                                    |
| claim.attending_provider                      | (_Institutional claim specific_) A dictionary of information for the attending provider on this claim.                                                                                                                                                                                |                                                    |
| claim.attending_provider.first_name           | (_Institutional claim specific_) The first name of the attending provider.                                                                                                                                                                                                            |                                                    |
| claim.attending_provider.last_name            | (_Institutional claim specific_) The last name of the attending provider.                                                                                                                                                                                                             |                                                    |
| claim.attending_provider.npi                  | (_Institutional claim specific_) The National Provider Identifier for the attending provider.                                                                                                                                                                                         |                                                    |
| claim.attending_provider.taxonomy_code        | (_Institutional claim specific_) The taxonomy code for the attending provider.                                                                                                                                                                                                        |                                                    |
| claim.occurrence_information                  | (_Institutional claim specific_) A dictionary of information related to the occurrence/frequency of the claim.                                                                                                                                                                        |                                                    |
| claim.occurrence_information.occurrence_type  | (_Institutional claim specific_) The type of claim-related occurrence for specifc dates. A full list of possible values can be found [below](#occtype). UB-04 field: *31. Occurrence Code*                                                                                            |                                                    |
| claim.occurrence_information.occurrence_dates | (_Institutional claim specific_) The specific dates for the claim-related occurrence type. UB-04 field: *31. Occurrence Date*                                                                                                                                                         |                                                    |
|                                               |                                                                                                                                                                                                                                                                                       |                                                    |
| claim.rendering_provider                      | A dictionary of information for the rendering provider on this claim.                                                                                                                                                                                                                 |                                                    |
| claim.rendering_provider.first_name           | The first name of the rendering provider.                                                                                                                                                                                                                                             |                                                    |
| claim.rendering_provider.last_name            | The last name of the rendering provider.                                                                                                                                                                                                                                              |                                                    |
| claim.rendering_provider.npi                  | The National Provider Identifier for the rendering provider.                                                                                                                                                                                                                          |                                                    |
| claim.rendering_provider.taxonomy_code        | The taxonomy code for the rendering provider.                                                                                                                                                                                                                                         |                                                    |
| claim.service_lines                           | List of services that were performed as part of this claim.                                                                                                                                                                                                                           |                                                    |
| claim.service_lines.charge_amount             | The amount charged for this specific service. (e.g. 100.00)                                                                                                                                                                                                                           | 24f: Charges                                       |
| claim.service_lines.diagnosis_codes           | A list of diagnosis codes related to this service. (e.g. 487.1)                                                                                                                                                                                                                       | 21: Diagnosis or nature of illness or injury       |
| claim.service_lines.procedure_code            | The CPT code for the service that was performed                                                                                                                                                                                                                                       | 24d: Procedures, Services, or Supplies             |
| claim.service_lines.procedure_modifier_codes  | Optional: List of modifier codes for the specified procedure. (e.g. ["GT"])                                                                                                                                                                                                           | 24d: Procedures, Services, or Supplies             |
| claim.service_lines.provider_control_number   | The provider's control number.                                                                                                                                                                                                                                                        |                                                    |
| claim.service_lines.revenue_code              | (_Institutional claim specific_) The revenue code related to this service. UB-04 field: *42. Revenue Code*                                                                                                                                                                            |                                                    |
| claim.service_lines.service_date              | The date the service was performed.                                                                                                                                                                                                                                                   | 24a: Date(s) of service (from, to)                 |
| claim.service_lines.unit_count                | Number of units of this service. (e.g. 1.0)                                                                                                                                                                                                                                           | 24g: Days or Units                                 |
| claim.service_lines.unit_type                 | The type of unit being described for this particular service's unit count. Possible values include: units, days                                                                                                                                                                       |                                                    |
| claim.total_charge_amount                     | The total amount charged/billed for the claim. (e.g. 100.00)                                                                                                                                                                                                                          | 28: Total Charge                                   |
| patient                                       | Information about the patient that received services outlined in the claim. Patient information is only required when the patient is not the insurance subscriber.                                                                                                                    |                                                    |
| patient.address                               | Required: The patient’s address information.                                                                                                                                                                                                                                          | 5: Patient's address                               |
| patient.address.address_lines                 | The patient’s street address information. (e.g. ["123 N MAIN ST"])                                                                                                                                                                                                                    |                                                    |
| patient.address.city                          | The patient’s city information. (e.g. "SAN MATEO")                                                                                                                                                                                                                                    |                                                    |
| patient.address.state                         | The patient’s state information. (e.g. "CA")                                                                                                                                                                                                                                          |                                                    |
| patient.address.zipcode                       | The patient’s zip/postal code. (e.g. "94401")                                                                                                                                                                                                                                         |                                                    |
| patient.birth_date                            | The patient’s birth date as specified on their policy.                                                                                                                                                                                                                                | 3: Patients Birth Date                             |
| patient.first_name                            | Required: The patient’s first name.                                                                                                                                                                                                                                                   | 2: Patient's Name                                  |
| patient.gender                                | The patient’s gender.                                                                                                                                                                                                                                                                 | 3: The patient's sex                               |
| patient.member_id                             | Required: The patient’s member identifier.                                                                                                                                                                                                                                            |                                                    |
| patient.middle_name                           | Optional: The patient’s middle name.                                                                                                                                                                                                                                                  | 2: Patient's Name                                  |
| patient.last_name                             | Required: The patient’s last name.                                                                                                                                                                                                                                                    | 2: Patient's Name                                  |
| patient.pregnant                              | Patient pregnancy indicator. Defaults to false.                                                                                                                                                                                                                                       |                                                    |
| patient.relationship                          | Required: The patient’s relationship to the subscriber. A full list of possible values is included [below](#relationships).                                                                                                                                                           | 6: Patient's relationship to the insured           |
| subscriber                                    | Information about the insurance subscriber as it appears on their policy.                                                                                                                                                                                                             |                                                    |
| subscriber.address                            | The subscriber’s address information as specified on their policy.                                                                                                                                                                                                                    | 7: Insured's address                               |
| subscriber.address.address_lines              | The subscriber’s street address information as specified on their policy. (e.g. ["123 N MAIN ST"])                                                                                                                                                                                    |                                                    |
| subscriber.address.city                       | The subscriber’s city information as specified on their policy. (e.g. "SAN MATEO")                                                                                                                                                                                                    |                                                    |
| subscriber.address.state                      | The subscriber’s state information as specified on their policy. (e.g. "CA")                                                                                                                                                                                                          |                                                    |
| subscriber.address.zipcode                    | The subscriber’s zip/postal code as specified on their policy. (e.g. "94401")                                                                                                                                                                                                         |                                                    |
| subscriber.birth_date                         | The subscriber’s birth date as specified on their policy.                                                                                                                                                                                                                             | 11a: Insured's date of birth                       |
| subscriber.claim_filing_code                  | Indicates the type of payment for the claim. It is an optional field and when left blank or not passed in the request, defaults to "mutually_defined". A full list of possible values is included [below](#filing).                                                                   |                                                    |
| subscriber.first_name                         | Required: The subscriber’s first name as specified on their policy.                                                                                                                                                                                                                   | 4: Insured's name                                  |
| subscriber.gender                             | The subscriber’s gender as specified on their policy.                                                                                                                                                                                                                                 | 11a: Insured's sex                                 |
| subscriber.group_number                       | Optional: The subscriber’s group or policy number as specified on their policy.                                                                                                                                                                                                       | 11:      Employer's policy number or group number  |
| subscriber.group_name                         | Optional: The subscriber’s group name as specified on their policy.                                                                                                                                                                                                                   | 11b: Employer's name or school name                |
| subscriber.member_id                          | Required: The subscriber’s member identifier.                                                                                                                                                                                                                                         | 1a: Insured's ID number                            |
| subscriber.last_name                          | Required: The subscriber’s last name as specified on their policy.                                                                                                                                                                                                                    | 4: Insured's name                                  |
| trading_partner_id                            | Required: Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.                                                                                                                                                             |                                                    |
| transaction_code                              | Required: The type of claim transaction that is being submitted (e.g. "chargeable"). A full list of possible values is included [below](#transaction-code).                                                                                                                           |                                                    |

A claim goes through an entire lifecycle after its transmission to a payer.
For details on this process, and how the [Claims Status](#claims-status)
Endpoint ties in, see our [claims API workflow](https://platform.pokitdok.com/claim-processing).

<a name="place-of-service"></a>
Full list of possible values that can be used in the claim.place_of_service parameter on the claim:

| place_of_service Values |                             |
|:------------------------|:----------------------------|
| ambulance_air_or_water  | mobile_unit                 |
| ambulance_land          | nursing                     |
| assisted_living         | office                      |
| birthing_center         | other                       |
| custodial               | outpatient_hospital         |
| end_stage_renal         | outpatient_rehab            |
| er_hospital             | pharmacy                    |
| federal_qualified       | prison                      |
| group_home              | psych_partial_hospital      |
| home                    | public_clinic               |
| hospice                 | residential_substance_abuse |
| ihs_freestanding        | rural_clinic                |
| ihs_provider            | school                      |
| immunization            | shelter                     |
| independent_clinic      | skilled_nursing             |
| independent_lab         | surgical_center             |
| inpatient_hospital      | temp_lodging                |
| inpatient_psych         | tribal_638_freestanding     |
| inpatient_rehab         | tribal_638_provider         |
| mental_health_center    | urgent_care                 |
| mentally_retarded       | walkin_clinic               |
| military                | worksite                    |


<a name="relationships"></a>
Full list of possible values that can be used in the patient.relationships parameter on the claim:

| relationship Values |                    |
|:--------------------|:-------------------|
| cadaver_donor       | organ_donor        |
| child               | other_relationship |
| employee            | spouse             |
| life_partner        | unknown            |


<a name="filing"></a>
Full list of possible values that can be used in the subscriber.filing_code parameter on the claim:

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


<a name="transaction-code"></a>
Full list of possible values that can be used in the transaction_code parameter on the claim:

| transaction_code Values |
|:------------------------|
| subrogation_demand      |
| chargeable              |
| reporting               |


<a name="admitsource"></a>
Full list of possible values that can be used in the claim.admission_source parameter on the claim:

| admission_source Values |                         |
|:------------------------|:------------------------|
| clinic                  | immediate_care_facility |
| emergency_room          | law_enforcement         |
| health_care_facility    | not_available           |
| hospice_transfer        | physician_referral      |
| hospital_transfer       | surgery_center          |


<a name="admittype"></a>
Full list of possible values that can be used in the claim.admission_type parameter on the claim:

| admission_type Values     |               |
|:--------------------------|:--------------|
| elective                  | newborn       |
| emergency                 | trauma_center |
| information_not_available | urgent        |


<a name="faciltype"></a>
Full list of possible values that can be used in the claim.facility_type parameter on the claim:

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


<a name="patstatus"></a>
Full list of possible values that can be used in the claim.patient_status parameter on the claim:

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


<a name="occtype"></a>
Full list of possible values that can be used in the claim.occurrence_information.occurrence_type parameter on the claim:

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


<a name="valuecode"></a>
Full list of possible values that can be used in the claim.value_information parameter on the claim:

| value_information Values                                      |                                                      |
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
