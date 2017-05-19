## Pharmacy Coverage

> Example request to determine pharmacy coverage information:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "pharmacy_npi": "0000000000",
    "prescriber": {
        "npi": "1111111111",
        "last_name": "Jones"
    },
    "member": {
        "gender": "Unknown",
        "last_name": "Smith",
        "date_of_birth": "19000101"
    },
    "insurance": {
        "bin_number": "my_bin",
        "pcn": "my_pcn",
        "cardholder_id": "my_id",
        "group_id": "my_group"
    },
    "drugs": [
        {
            "ndc": "46122006965",
            "quantity_dispensed": 30
        },
        {
            "ndc": "00904598660",
            "quantity_dispensed": 30
        },
        {
            "ndc": "00536478701",
            "quantity_dispensed": 30
        }
    ]
}' https://platform.pokitdok.com/api/v4/pharmacy/coverage/
```

```python
client.post(
    path = "/pharmacy/coverage/",
    data = {
        "pharmacy_npi": "0000000000",
        "prescriber": {
            "npi": "1111111111",
            "last_name": "Jones"
        },
        "member": {
            "gender": "Unknown",
            "last_name": "Smith",
            "date_of_birth": "19000101"
        },
        "insurance": {
            "bin_number": "my_bin",
            "pcn": "my_pcn",
            "cardholder_id": "my_id",
            "group_id": "my_group"
        },
        "drugs": [
            {
                "ndc": "46122006965",
                "quantity_dispensed": 30
            },
            {
                "ndc": "00904598660",
                "quantity_dispensed": 30
            },
            {
                "ndc": "00536478701",
                "quantity_dispensed": 30
            }
        ]
    }
)
```

```ruby
client.post(
        path = "/pharmacy/coverage/",
        {
            pharmacy_npi: "0000000000",
            prescriber: {
                npi: "1111111111",
                last_name: "Jones"
            },
            member: {
                gender: "Unknown",
                last_name: "Smith",
                date_of_birth: "19000101"
            },
            insurance: {
                bin_number: "my_bin",
                pcn: "my_pcn",
                cardholder_id: "my_id",
                group_id: "my_group"
            },
            drugs: [
                {
                    ndc: "46122006965",
                    quantity_dispensed: 30
                },
                {
                    ndc: "00904598660",
                    quantity_dispensed: 30
                },
                {
                    ndc: "00536478701",
                    quantity_dispensed: 30
                }
            ]
        }
    }
)
```

```csharp
client.request(
    "/pharmacy/coverage/",
    "POST",
    new Dictionary<string, object> {
        {"pharmacy_npi", new string[] { "0000000000" }},
        {"prescriber", new Dictionary<string, object> {
            {"npi", "1111111111"},
            {"last_name", "Jones"}
        }},
        {"member", new Dictionary<string, object> {
            {"gender", "Unknown"},
            {"last_name", "Smith"},
            {"date_of_birth", "19000101"}
        }},
        {"insurance", new Dictionary<string, object> {
            {"bin_number", "my_bin"},
            {"pcn", "my_pcn"},
            {"cardholder_id", "my_id"},
            {"group_id", "my_group"}
        }},
        {"drugs", new Object[] { 
            new Dictionary<string, object> {
                {"ndc", "46122006965"},
                {"quantity_dispensed", 30}
            },
            new Dictionary<string, object> {
                {"ndc", "00904598660"},
                {"quantity_dispensed", 30}
            },
            new Dictionary<string, object> {
                {"ndc", "00536478701"},
                {"quantity_dispensed", 30}
            }
        }}
});
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"pharmacy_npi\": \"0000000000\",");
buf.append("    \"prescriber\": {");
buf.append("        \"npi\": \"1111111111\",");
buf.append("        \"last_name\": \"Jones\"");
buf.append("    },");
buf.append("    \"member\": {");
buf.append("        \"gender\": \"Unknown\",");
buf.append("        \"last_name\": \"Smith\",");
buf.append("        \"date_of_birth\": \"19000101\"");
buf.append("    },");
buf.append("    \"insurance\": {");
buf.append("        \"bin_number\": \"my_bin\",");
buf.append("        \"pcn\": \"my_pcn\",");
buf.append("        \"cardholder_id\": \"my_id\",");
buf.append("        \"group_id\": \"my_group\"");
buf.append("    },");
buf.append("    \"drugs\": [");
buf.append("        {");
buf.append("            \"ndc\": \"46122006965\",");
buf.append("            \"quantity_dispensed\": 30");
buf.append("        },");
buf.append("        {");
buf.append("            \"ndc\": \"00904598660\",");
buf.append("            \"quantity_dispensed\": 30");
buf.append("        },");
buf.append("        {");
buf.append("            \"ndc\": \"00536478701\",");
buf.append("            \"quantity_dispensed\": 30");
buf.append("        }");
buf.append("    ]");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
client.post("/pharmacy/coverage/", query)
```

```swift
let path = "/pharmacy/coverage/"
let data = [
    "pharmacy_npi": "0000000000",
    "prescriber": [
        "npi": "1111111111",
        "last_name": "Jones"
    ],
    "member": [
        "gender": "Unknown",
        "last_name": "Smith",
        "date_of_birth": "19000101"
    ],
    "insurance": [
        "bin_number": "my_bin",
        "pcn": "my_pcn",
        "cardholder_id": "my_id",
        "group_id": "my_group"
    ],
    "drugs": [
        [
            "ndc": "46122006965",
            "quantity_dispensed": 30
        ],
        [
            "ndc": "00904598660",
            "quantity_dispensed": 30
        ],
        [
            "ndc": "00536478701",
            "quantity_dispensed": 30
        ]
    ]
] as [String:Any]
try client.request(path: path, method: "POST", params: data)
```

> Example pharmacy coverage response:

```json
{
  "data": {
    "drugs": [
      {
        "ndc": "46122006965",
        "additional_information": [
          {
            "information": "DISCOUNT APPLIED"
          }
        ],
        "patient_pay_amount": {
            "amount": "2.15",
            "currency": "USD",
            "display": "$2.15"
        },
        "amount_of_copay": {
            "amount": "2.15",
            "currency": "USD",
            "display": "$2.15"
        },
        "amount_of_coinsurance": {
            "amount": "2.15",
            "currency": "USD",
            "display": "$2.15"
        }
      },
      {
        "ndc": "00904598660",
        "additional_information": [
          {
            "information": "DISCOUNT APPLIED"
          }
        ],
        "patient_pay_amount": {
            "amount": "2.85",
            "currency": "USD",
            "display": "$2.85"
        },
        "amount_of_copay": {
            "amount": "2.85",
            "currency": "USD",
            "display": "$2.85"
        },
        "amount_of_coinsurance": {
            "amount": "2.85",
            "currency": "USD",
            "display": "$2.85"
        }
      },
      {
        "ndc": "00536478701",
        "additional_information": [
          {
            "information": "DISCOUNT APPLIED"
          }
        ],
        "patient_pay_amount": {
            "amount": "1.74",
            "currency": "USD",
            "display": "$1.74"
        },
        "amount_of_copay": {
            "amount": "1.74",
            "currency": "USD",
            "display": "$1.74"
        },
        "amount_of_coinsurance": {
            "amount": "1.74",
            "currency": "USD",
            "display": "$1.74"
        }
      }
    ]
  }
}
```

The Pharmacy Coverage API returns a members’s medication coverage and an estimated out of pocket cost.

Available Pharmacy Coverage Endpoints:


| Endpoint           | HTTP Method | Description                             |
|:-------------------|:------------|:----------------------------------------|
| /pharmacy/coverage | POST        | Determine medication coverage and an estimated out of pocket cost |

All pharmacy coverage requests must include a valid prescriber NPI and valid pharmacy NPI. 
These NPIs must be registered with PokitDok before using the pharmacy coverage endpoint.

The /pharmacy/coverage endpoint accepts the following parameters:

| Parameter          | Type          | Description                                                                  | Presence |
|:-------------------|:--------------|:-----------------------------------------------------------------------------|:---------|
| pharmacy_npi       | {string}      | NPI of submitting pharmacy                                                   | Required |
| prescriber         | {object}      | The prescribing physician. Uses the prescriber [object](#prescriber_object). | Required |
| member             | {object}      | The patient. Uses the member [object](#member_object).                       | Required |
| insurance          | {object}      | Insurance information. Uses the insurance [object](#insurance_object).       | Required |
| drugs              | {list objects}| List of drug information. Uses the drug [object](#drug_request_object).      | Required |

<a name="prescriber_object"></a>
###Prescriber Object
| Parameter          | Type          | Description                        | Presence |
|:-------------------|:--------------|:-----------------------------------|:---------|
| last_name          | {string}      | Last name of prescribing physician | Required |
| npi                | {string}      | NPI of prescribing physician       | Required |

<a name="member_object"></a>
###Member Object
| Parameter          | Type          | Description                                                    | Presence |
|:-------------------|:--------------|:---------------------------------------------------------------|:---------|
| last_name          | {string}      | Member’s last name                                             | Required |
| date_of_birth      | {string}      | Member’s date of birth, of the form YYYYMMDD                   | Required |
| gender             | {string}      | Member’s gender: Female, Male, or Unknown                      | Required |
| residence          | {string}      | Member’s residence, possible [values](#residence_values) below | Default is Home |

<a name="residence_values"></a>
###Residence Values
| Values |
|:-------|
|Home|
|Residential Substance Abuse Treatment Facility|
|Hospice|
|Psychiatric Residential Treatment Facility|
|Comprehensive Inpatient Rehabilitation Facility|
|Homeless Shelter|
|Correctional Institution|
|Skilled Nursing Facility|
|Nursing Facility|
|Assisted Living Facility|
|Custodial Care Facility|
|Group Home|
|Inpatient Psychiatric Facility|
|Psychiatric Facility|
|Intermediate Care Facility/Mentally Retarded|

<a name="insurance_object"></a>
###Insurance Object
| Parameter            | Type     | Description                      | Presence |
|:---------------------|:---------|:---------------------------------|:---------|
| bin_number           | {string} | BIN number (on member’s card)    | Required |
| pcn                  | {string} | PCN number (on member’s card)    | Required |
| cardholder_id        | {string} | Cardholder ID (on member’s card) | Required |
| group_id             | {string} | Group ID (on member’s card)      | Required |
| patient_relationship | {string} | Patient relationship code (on member’s card), possible [values](#relationship_values) below | Default is Cardholder |

<a name="relationship_values"></a>
###Relationship Values
| Values |
|:-------|
|Not Specified|
|Cardholder|
|Spouse|
|Child|
|Other|
|Student|
|Disabled Dependent|
|Adult Dependent|
|Significant Other|

<a name="drug_request_object"></a>
###Drug Object
| Parameter                 | Type          | Description                                                  | Presence |
|:--------------------------|:--------------|:-------------------------------------------------------------|:---------|
| ndc                       | {string}      | 11-digit NDC of medication                                   | Required |
| quantity_dispensed        | {decimal}     | Quantity of medication dispensed, up to three decimal places | Required |
| days_supply               | {int}         | Day supply of medication                                     | Default is 30 |



The /pharmacy/coverage response contains the following fields:

| Field | Type           | Description                     | Presence |
|:------|:---------------|:--------------------------------|:---------|
| drugs | {list objects} | List of drug objects. Uses the drug [object](#drug_response_object). | Optional |


<a name="drug_request_object"></a>
###Drug Object
| Parameter                 | Type           | Description                                          | Presence |
|:--------------------------|:---------------|:-----------------------------------------------------|:---------|
| ndc                       | {string}       | NDC of medication                                    | Required |
| rejections                | {list string}  | List of rejection reasons, if the claim was rejected | Optional |
| additional_information    | {list objects} | List of additional information objects. Uses the additional information [object](#add_info). | Optional |
| patient_pay_amount        | {object}       | Amount member owes for medication. Uses the monetary [object](#monetary).                    | Optional |
| amount_of_copay           | {object}       | Copay amount. Uses the monetary [object](#monetary).                                         | Optional |
| amount_of_coinsurance     | {object}       | Coinsurance amount. Uses the monetary [object](#monetary).                                   | Optional |
| history                   | {list objects} | List of history objects. Uses the history [object](#history_object).                         | Optional |

<a name="monetary"></a>
###Monetary Object
| Parameter | Type      | Description                                      | Presence |
|:----------|:----------|:-------------------------------------------------|:---------|
| amount    | {decimal} | the monetary amount                              | Optional |
| currency  | {string}  | the currency, such as "USD"                      | Optional |
| display   | {string}  | a display string for the amount, such as "$1.00" | Optional |

<a name="add_info"></a>
###Additional Information Object
| Parameter   | Type     | Description                           | Presence |
|:------------|:---------|:--------------------------------------|:---------|
| code        | {string} | Approval code (if claim was approved) | Optional |
| information | {string} | Free form message for additional info | Optional |

<a name="history_object"></a>
###History Object
| Parameter                 | Type            | Description                          | Presence |
|:--------------------------|:----------------|:-------------------------------------|:---------|
| previous_date_of_fill     | {date YYYYMMDD} | Date of previous fill of medication  | Optional |
| quantity_of_previous_fill | {decimal}       | Quantity of previous fill            | Optional |
| free_text                 | {string}        | Free text of drug utilization review | Optional |
| additional_text           | {string}        | Additional text of DUR               | Optional |
