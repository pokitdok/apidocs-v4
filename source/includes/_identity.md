Identity Management
-------------------

> Example creating an identity resource

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"
 -XPOST -d '{
    "prefix": "Mr.",
       "first_name": "Oscar",
       "middle_name": "Harold",
       "last_name": "Whitmire",
       "suffix": "IV",
       "birth_date": "2000-05-01",
       "gender": "male",
       "email": "oscar@pokitdok.com",
       "phone": "555-555-5555",
       "secondary_phone": "333-333-4444",
       "address": {
           "address_lines": ["1400 Anyhoo Avenue"],
           "city": "Springfield",
           "state": "IL",
           "zipcode": "90210"
       },
       "identifiers": [
           {
               "location": [-121.93831, 37.53901],
               "provider_uuid": "1917f12b-fb6a-4016-93bc-adeb83204c83",
               "system_uuid": "967d207f-b024-41cc-8cac-89575a1f6fef",
               "value": "W90100-IG-88"

           }
       ]    
    }' https://platform.pokitdok.com/api/v4/identity/
```

```python
pd.create_identity({
    "prefix": "Mr.",
    "first_name": "Oscar",
    "middle_name": "Harold",
    "last_name": "Whitmire",
    "suffix": "IV",
    "birth_date": "2000-05-01",
    "gender": "male",
    "email": "oscar@pokitdok.com",
    "phone": "555-555-5555",
    "secondary_phone": "333-333-4444",
    "address": {
        "address_lines": ["1400 Anyhoo Avenue"],
        "city": "Springfield",
        "state": "IL",
        "zipcode": "90210"
    },
    "identifiers": [
        {
            "location": [-121.93831, 37.53901],
            "provider_uuid": "1917f12b-fb6a-4016-93bc-adeb83204c83",
            "system_uuid": "967d207f-b024-41cc-8cac-89575a1f6fef",
            "value": "W90100-IG-88"

        }
    ]
})
```

> Example updating an identity resource

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"
 -XPUT -d '{
    "prefix": "Mr.",
       "first_name": "Oscar",
       "middle_name": "Harold",
       "last_name": "Whitmire",
       "suffix": "IV",
       "birth_date": "2000-05-01",
       "gender": "male",
       "email": "oscar.whitmire@pokitdok.com",
       "phone": "555-555-5555",
       "secondary_phone": "333-333-4444",
       "address": {
           "address_lines": ["1400 Anyhoo Avenue"],
           "city": "Springfield",
           "state": "IL",
           "zipcode": "90210"
       },
       "identifiers": [
           {
               "location": [-121.93831, 37.53901],
               "provider_uuid": "1917f12b-fb6a-4016-93bc-adeb83204c83",
               "system_uuid": "967d207f-b024-41cc-8cac-89575a1f6fef",
               "value": "W90100-IG-88"

           }
       ]    
    }' "https://platform.pokitdok.com/api/v4/identity/881bc095-2068-43cb-9783-cce630364122"
```

```python
pd.update_identity("881bc095-2068-43cb-9783-cce630364122", {
    "prefix": "Mr.",
    "first_name": "Oscar",
    "middle_name": "Harold",
    "last_name": "Whitmire",
    "suffix": "IV",
    "birth_date": "2000-05-01",
    "gender": "male",
    "email": "oscar.whitmire@pokitdok.com",
    "phone": "555-555-5555",
    "secondary_phone": "333-333-4444",
    "address": {
        "address_lines": ["1400 Anyhoo Avenue"],
        "city": "Springfield",
        "state": "IL",
        "zipcode": "90210"
    },
    "identifiers": [
        {
            "location": [-121.93831, 37.53901],
            "provider_uuid": "1917f12b-fb6a-4016-93bc-adeb83204c83",
            "system_uuid": "967d207f-b024-41cc-8cac-89575a1f6fef",
            "value": "W90100-IG-88"

        }
    ]
})
```

> Query for a single identity resource

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/identity/881bc095-2068-43cb-9783-cce630364122"
```

```python
pd.identity("881bc095-2068-43cb-9783-cce630364122")
```

> Query for one or more identity resources using parameters

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/identity?first_name=Oscar&last_name=Whitmire&gender=male"
```

```python
pd.identity(first_name='Oscar', last_name='Whitmire', gender='male')
```

> Query for identity record history

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/identity/881bc095-2068-43cb-9783-cce630364122/history"
```

```python
pd.identity_history("881bc095-2068-43cb-9783-cce630364122")
```

> Query for a historical identity record

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/identity/881bc095-2068-43cb-9783-cce630364122/history/0"
```

```python
pd.identity_history("881bc095-2068-43cb-9783-cce630364122", 0)
```

**Available modes of operation: real-time**

PokitDok's Identity Management (IdM) API queries an EMPI (Enterprise Master Patient Index) and/or MPI (Master Patient Index), both typically components of an EMR or EHR system, to find a patient identifier and details in the target EMR/EHR system. This helps providers identify the patient through past visits or other records within other EMR/EHR systems.

Available Identity endpoints:

##### Identity
| Endpoint   | HTTP Method | Description                                                            |
|:-----------|:------------|:-----------------------------------------------------------------------|
| /identity/ | POST        | Creates an identity resource. Returns the created resource with a uuid |
| /identity/{uuid} | GET | Returns an identity resource with a given uuid |
| /identity/{uuid} | PUT | Updates an identity with the given uuid | 


The /identity/ endpoint accepts the following parameters:

| Field                 | Type     | Description                                                                                                        |
|:----------------------|:---------|:-------------------------------------------------------------------------------------------------------------------|
| address.address_lines | {array}  | Address lines                                                                                                      |
| address.city          | {string} | Name of city in which to search for identity records (e.g. "San Mateo" or "Charleston")                            |
| address.state         | {string} | Name of U.S. state in which to search for identity records (e.g. "CA" or "SC")                                     |
| address.zipcode       | {string} | Geographic center point in which to search for identity records.                                                   |
| birth_date            | {string} | Birth date in ISO-8601 format. Ex: 1990-01-01                                                                      |
| email                 | {string} | Valid email address including "@" separator and appropriate domain prefix                                          |
| first_name            | {string} | First name                                                                                                         |
| gender                | {string} | Valid values include: male, female, or unknown                                                                     |
| identifiers           | {array}  | List of external identifiers. Each identifier entry is qualified using a system_uuid, provider_uuid, and location. |
| last_name             | {string} | Last name                                                                                                          |
| member_id             | {string} | The primary insurance membership id associated with the identity resource                                          |
| middle_name           | {string} | Middle name                                                                                                        |
| phone                 | {string} | Primary phone number                                                                                               |
| prefix                | {string} | Prefix/Title                                                                                                       |
| secondary_phone       | {string} | Secondary phone number                                                                                             |
| ssn                   | {string} | Social security number                                                                                             |
| suffix                | {string} | Suffix                                                                                                             |
| uuid                  | {uuid}   | Identity resource unique identifier                                                                                |

Each identifier, or identifiers list entry, represents an external system utilized by a provider at a specific location. Fields within an identifier entry include:

| Field         | Type     | Description                                        |
|:--------------|:---------|:---------------------------------------------------|
| location      | {array}  | Optional: GeoJSON array of \[longitude, latitude\] |
| provider_uuid | {uuid}   | The unique identifier for the provider             |
| system_uuid   | {uuid}   | The unique identifier for the system               |
| value         | {string} | The identifier value                               |

The location and provider_uuid values correspond to provider resources accessed through the /providers endpoint. system_uuid values correspond to registered systems under the /schedule/schedulers endpoint.

Supported query string parameters to the /identity endpoint are listed below. Parameters highlighted in ​*bold*​ utilize
a fuzzy matching strategy which finds comparable (or similar) records within a maximum edit distance of two characters.
All other parameters employ an exact matching strategy.

- *first_name*
- *middle_name*
- *last_name*
- gender
- birth_date
- email
- member_id
- *address*
- *city*
- state
- zipcode
- phone
- secondary_phone

External id search is executed using the "id" parameter:
/identity?id={identifier value}

The id parameter, if present, overrides other search parameters.

##### Identity History
| Endpoint   | HTTP Method | Description                                                            |
|:-----------|:------------|:-----------------------------------------------------------------------|
| /identity/{uuid}/history | GET | Returns an identity record's change history including the version date and version id|
| /identity/{uuid}/history/{version id} | GET | Returns a historical identity record | 