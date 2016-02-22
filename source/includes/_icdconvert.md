## ICD Convert
> Example ICD convert request to map an ICD-9 code to possible ICD-10 codes


```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/icd/convert/250.12
```

```python
pd.icd_convert('250.12')
```

```csharp
client.icdConvert("250.12");
```

> Example ICD convert response

```
{
    "approximate": true,
    "combination": false,
    "destination_scenarios": [
        {
            "choice_lists": [
                [
                    {
                        "description": "Type 2 diabetes mellitus with hyperglycemia",
                        "system": "icd10",
                        "value": "E1165"
                    }
                ],
                [
                    {
                        "description": "Type 2 diabetes mellitus with other specified complication",
                        "system": "icd10",
                        "value": "E1169"
                    },
                    {
                        "description": "Other specified diabetes mellitus with ketoacidosis without coma",
                        "system": "icd10",
                        "value": "E1310"
                    }
                ]
            ]
        }
    ],
    "source_code": {
        "description": "Diabetes with ketoacidosis, type II or unspecified type, uncontrolled",
        "system": "icd9",
        "value": "25012"
    }
}
```

*Available modes of operation: real-time*

The ICD Convert endpoint allows a client application to request ICD-9 to ICD-10 mapping information for the
specified ICD-9 code.


| Endpoint     | HTTP Method | Description                                  |
|:-------------|:------------|:---------------------------------------------|
| /icd/convert | GET         | retrieve ICD-9 to ICD-10 mapping information |


The /icd/convert endpoint accepts the following parameters:

| Parameter | Description |
|:----------|:------------|
| code      | ICD-9 code  |


The /icd/convert response contains the following parameters:

| Parameter                                  | Description                                                                         |
|:-------------------------------------------|:------------------------------------------------------------------------------------|
| diagnosis_mappings                         | a list of diagnosis mapping information that may be used to convert ICD-9 to ICD-10 |
| diagnosis_mappings.destination_scenarios   | a list of ICD-10 mapping scenarios that apply for the matched ICD-9 code            |
| diagnosis_mappings.source_code.description | a string representing a description of the source ICD-9 code                        |
| diagnosis_mappings.source_code.system      | a string representing the code system (icd9)                                        |
| diagnosis_mappings.source_code.value       | a string containing the ICD-9 code value                                            |
