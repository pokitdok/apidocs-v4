## Claims Convert
> Example claims convert request using a local X12 837 test file

```shell
cat test_claim.837
ISA*00*          *00*          *01*9012345720000  *01*9088877320000  *151004*2235*U*00501*000000007*0*T*:~GS*HC*901234572000*908887732000*20151004*2235*7*X*005010X222~ST*837*0001~BHT*0019*00*2KYXDRE61GU20TFMBPA*20151004*2231*CH~NM1*41*2*Pokitdok, Inc.*****46*12345~PER*IC**EM*x12info@pokitdok.com~NM1*40*2*MOCKPAYER*****46*12345~HL*1**20*1~PRV*BI*PXC*207Q00000X~NM1*85*1*Blackwell*Elizabeth****XX*1234567893~N3*8311 WARREN H ABERNATHY HWY~N4*SPARTANBURG*SC*293010000~REF*EI*123456789~HL*2*1*22*0~SBR*P*18*******ZZ~NM1*IL*1*Doe*Jane****MI*W000000000~N3*123 N MAIN ST~N4*SPARTANBURG*SC*29301~DMG*D8*19700101*F~NM1*PR*2*MOCKPAYER*****PI*12345~CLM*0f17b46dd39a4bb0add152e99633adbc*60***11:B:1*Y*A*Y*I~HI*BK:4871~LX*1~SV1*HC:99213*60*UN*1.0***1~DTP*472*D8*20140601~SE*24*0001~GE*1*905~IEA*1*000000905~
```

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -XPOST -F file=@test_claim.837 https://platform.pokitdok.com/api/v4/claims/convert
```

```python
client.claims_convert('test_claim.837')
```

```ruby
client.claims_convert('test_claim.837')
```

```csharp
client.claimsConvert('test_claim.837')
```

```java
client.claimsConvert("test_claim.837");
```

```swift
try client.claimsCovert(x12ClaimsFilePath: "test_claim.837")
```

> Example claims convert response when a single claim is included in the uploaded X12 837 file

```json
{
    "claims_request": {
        "billing_provider": {
            "address": {
                "address_lines": [
                    "8311 WARREN H ABERNATHY HWY"
                ],
                "city": "SPARTANBURG",
                "state": "SC",
                "zipcode": "293010000"
            },
            "first_name": "Elizabeth",
            "last_name": "Blackwell",
            "npi": "1234567893",
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
                    "charge_amount": "60",
                    "diagnosis_codes": [
                        "J101"
                    ],
                    "procedure_code": "99213",
                    "service_date": "2014-06-25",
                    "unit_count": "1.0",
                    "unit_type": "units"
                }
            ],
            "total_charge_amount": "60.0"
        },
        "payer": {
            "id": "12345",
            "organization_name": "MOCKPAYER"
        },
        "receiver": {
            "id": "12345",
            "organization_name": "MOCKPAYER"
        },
        "submitter": {
            "email": "x12info@pokitdok.com",
            "id": "12345",
            "organization_name": "Pokitdok, Inc."
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
            "claim_filing_code": "mutually_defined",
            "first_name": "Jane",
            "gender": "female",
            "last_name": "Doe",
            "member_id": "W000000000",
            "payer_responsibility": "primary"
        },
        "trading_partner_id": "MOCKPAYER",
        "transaction_code": "chargeable"
    },
    "converted_edi": "ISA*00*          *00*          *01*9012345720000  *01*9088877320000  *151004*2237*U*00501*000000007*0*T*:~GS*HC*901234572000*908887732000*20151004*2237*7*X*005010X222~ST*837*0001*005010X222~BHT*0019*00*2KYXEO9NJXIZOWBF8WB*20151004*2237*CH~NM1*41*2*Pokitdok, Inc.*****46*12345~PER*IC**EM*x12info@pokitdok.com~NM1*40*2*MOCKPAYER*****46*12345~HL*1**20*1~PRV*BI*PXC*207Q00000X~NM1*85*1*Blackwell*Elizabeth****XX*1234567893~N3*8311 WARREN H ABERNATHY HWY~N4*SPARTANBURG*SC*293010000~REF*EI*123456789~HL*2*1*22*0~SBR*P*18*******ZZ~NM1*IL*1*Doe*Jane****MI*W000000000~N3*123 N MAIN ST~N4*SPARTANBURG*SC*29301~DMG*D8*19700101*F~NM1*PR*2*MOCKPAYER*****PI*12345~CLM*6edff387-bb86-458d-a4a0-1cac77785c21*60***11:B:1*Y*A*Y*I~HI*ABK:J101~LX*1~SV1*HC:99213*60*UN*1.0***1~DTP*472*D8*20140601~SE*24*0001~GE*1*7~IEA*1*000000007~",
    "diagnosis_mappings": [
        {
            "approximate": true,
            "combination": false,
            "destination_scenarios": [
                {
                    "choice_lists": [
                        [
                            {
                                "description": "Influenza due to other identified influenza virus with other respiratory manifestations",
                                "system": "icd10",
                                "value": "J101"
                            },
                            {
                                "description": "Influenza due to unidentified influenza virus with other respiratory manifestations",
                                "system": "icd10",
                                "value": "J111"
                            }
                        ]
                    ]
                }
            ],
            "source_code": {
                "description": "Influenza with other respiratory manifestations",
                "system": "icd9",
                "value": "4871"
            }
        }
    ]
}
```

*Available modes of operation: real-time and batch/async*

The Claims Convert endpoint allows a client application to easily convert a X12 837 claims file
into claims request models.  When a claims file is submitted with ICD-9 diagnosis codes,
those claims will be mapped to corresponding ICD-10 codes. If multiple mappings are possible for the ICD-9 code,
the first matching ICD-10 code is used in the converted claim.  The mapping information that was used during the claim
conversion is also returned in the response so that the mapping may be reviewed prior to submitting converted claims
to a trading partner.  This endpoint operates in a real-time mode when the supplied claims file only includes a single claim.
If the claims file includes multiple claims, the endpoint will operate in a batch mode.
When multiple claims are detected, a platform activity will be returned to the client application so that
it may use the activities endpoint to track the claims conversion process.  For each claim detected in the file, a
child activity will be created that may be used to track the conversion of individual claims within the file.
The activity result for a converted claim will contain a claims_request value that is suitable for submission
to the claims endpoint.  The activity result will also contain a converted_edi string value that
represents the converted X12 837 transaction for that claim.  A list of diagnosis_mappings is also
included so that the client application may review the scenarios and choices that were utilized to
map ICD-9 to ICD-10.


### Endpoint Description

<!--- beginning of table -->

| Endpoint        | HTTP Method | Description                          |
|:----------------|:------------|:-------------------------------------|
| /claims/convert | POST        | Submit a X12 837 file for conversion |

<!--- end of table -->


### Parameters

The `/claims/convert` endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter | Description    |
|:----------|:---------------|
| file      | a X12 837 file |

<!--- end of table -->

### Response

The `/claims/convert` response contains the following fields:

<!--- beginning of table -->

| Field                                                              | Description                                                                                                                                                         |
|:-------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| claims_request                                                     | a JSON object representing the converted claims data that's suitable for use with the claims endpoint                                                               |
| converted_edi                                                      | a string representing a converted X12 837 transaction with ICD-9 mapped to ICD-10.  The X12 envelope (ISA and GS segments) is preserved from the original X12 file. |
| diagnosis_mappings                                                 | a list of diagnosis mapping information that was used to convert ICD-9 to ICD-10 for this claim                                                                     |
| diagnosis_mappings.destination_scenarios                           | a list of mapping scenarios that apply for the matched ICD-9 code                                                                                                   |
| diagnosis_mappings.destination_scenarios.choice_lists              | a list of codes that represent a destination scenario for diagnosis mapping                                                                                         |
| diagnosis_mappings.destination_scenarios.choice_lists.description  | a string representing a description of the source ICD-9 code                                                                                                        |
| diagnosis_mappings.destination_scenarios.choice_lists.value        | a string containing the ICD-9 code value                                                                                                                            |
| diagnosis_mappings.destination_scenarios.choice_lists.system       | a string representing the code system (icd9)                                                                                                                        |
| diagnosis_mappings.source_code.description                         | a string representing a description of the source ICD-9 code                                                                                                        |
| diagnosis_mappings.source_code.system                              | a string representing the code system (icd9)                                                                                                                        |
| diagnosis_mappings.source_code.value                               | a string containing the ICD-9 code value                                                                                                                            |
| diagnosis_mappings.approximate                                     | a boolean of whether or not the mapping from ICD-9 to ICD-10 was direct or more of an approximation.                                                                |
| diagnosis_mappings.combination                                     | a boolean of whether or not multiple ICD-9 values were combined and mapped to fewer ICD-10 values.                                                                                                  |

<!--- end of table -->
