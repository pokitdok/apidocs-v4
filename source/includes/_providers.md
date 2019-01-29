## Providers
> Example fetching provider information by NPI:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/providers/1467560003"
```

```python
client.providers(npi='1467560003')
```

```csharp
client.providers("1467560003");
```

```ruby
client.providers({npi: '1467560003'})
```

```java
HashMap<String, String> query = new HashMap<String, String>();
query.put("npi", "1467560003");

client.providers(query)
```

```swift
try client.providers(npi: "1467560003")
```

>Example Response:

```json
{
  "provider": {
    "fax": "8645625230",
    "first_name": "JEROME",
    "last_name": "AYA-AY",
    "middle_name": "BENITEZ",
    "uuid": "fc44d0e0-ea7f-492e-90f0-0f9148453019",
    "degree": "MD",
    "entity_type": "individual",
    "gender": "Male",
    "verified": false,
    "locations": [
      {
        "city": "Spartanburg",
        "fax": "8645625230",
        "address_lines": [
          "8311 Warren H Abernathy Hwy"
        ],
        "country": "US",
        "zipcode": "293011249",
        "phone": "8645625100",
        "state": "SC",
        "role": [
          "practice"
        ]
      },
      {
        "city": "Spartanburg",
        "fax": "8645604413",
        "address_lines": [
          "Po Box 2168"
        ],
        "country": "US",
        "zipcode": "293042168",
        "phone": "8645604304",
        "state": "SC",
        "role": [
          "mailing"
        ]
      }
    ],
    "specialty_primary": [
      "Family Practice",
      "Family Medicine"
    ],
    "specialty": [
      "Family Practice",
      "Family Medicine",
      "General & Family Medicine"
    ],
    "phone": "8645625100",
    "prefix": "DR",
    "licenses": [
      {
        "state": "SC",
        "number": "27210"
      }
    ],
    "npi": "1467560003",
    "specialty_secondary": [
      "General & Family Medicine"
    ]
  }
}
```

> Example searching providers by zipcode and specialty:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/providers/?zipcode=29307&specialty=rheumatology"
```

```python
client.providers(zipcode='29307', specialty='rheumatology')
```

```csharp
 client.providers(
			new Dictionary<string, string> {
				{ "zipcode", "29307" },
				{ "specialty", "rheumatology" }
		});
```

```ruby
client.providers({zipcode: '29307', specialty: 'rheumatology'})
```

```java
HashMap<String, String> query = new HashMap<String, String>();
query.put("zipcode", "29307");
query.put("specialty", "rheumatology");

client.providers(query)
```

```swift
let data = [
    "zipcode": "29307",
    "specialty": "rheumatology"
] as [String: Any]
try client.providers(params: data)
```

>Example response:

```json
[
  {
    "provider": {
      "fax": "8645910007",
      "first_name": "MARGARET",
      "last_name": "CURRAN",
      "middle_name": "YAP",
      "uuid": "94f13987-6430-4962-87a4-6122c70db6f0",
      "degree": "MD",
      "entity_type": "individual",
      "gender": "Female",
      "verified": false,
      "locations": [
        {
          "city": "Spartanburg",
          "fax": "8645910007",
          "address_lines": [
            "1455 E Main St Ste 103"
          ],
          "country": "US",
          "zipcode": "293072243",
          "phone": "8645911700",
          "state": "SC",
          "role": [
            "mailing"
          ]
        },
        {
          "city": "Spartanburg",
          "fax": "8645910007",
          "address_lines": [
            "1455 E Main St Ste 103"
          ],
          "country": "US",
          "zipcode": "29307",
          "phone": "8645911700",
          "state": "SC",
          "role": [
            "practice"
          ]
        }
      ],
      "specialty_primary": [
        "Specialist",
        "Rheumatology"
      ],
      "specialty": [
        "Rheumatology",
        "Specialist",
        "Internal Medicine"
      ],
      "phone": "8645911700",
      "prefix": "DR",
      "licenses": [
        {
          "state": "SC",
          "number": "21157"
        },
        {
          "state": "SC",
          "number": "21157"
        }
      ],
      "npi": "1629149364",
      "specialty_secondary": [
        "Internal Medicine"
      ]
    }
  }
]
```

*Available modes of operation: real-time only*

The Providers endpoints provide access to PokitDok's provider directory.
The Providers endpoints can be used to search for Providers, view biographical,
credential, and license information. For a complete reference to all possible 
provider specialties, see our [provider specialties reference](provider_specialties.html).

### Endpoint Description

Available Provider Endpoints:

<!--- beginning of table -->

| Endpoint        | HTTP Method | Description                                                              |
|:----------------|:------------|:-------------------------------------------------------------------------|
| /providers/     | GET         | Get a list of providers meeting certain search criteria                  |
| /providers/{id} | GET         | Retrieve the data for a specified provider; the ID is the provider's NPI |

<!--- end of table -->

### Parameters

The `/providers/` endpoint accepts the following search parameters:

<!--- beginning of table -->

| Parameter         | Type     | Description                                                                                                                                         |
|:------------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| address_lines     | {string} | Any or all of number, street name, apartment, suite number                                                                                          |
| city              | {string} | Name of city in which to search for providers (e.g. "San Mateo" or "Charleston")                                                                    |
| first_name        | {string} | The provider's first name                                                                                                                           |
| middle_name       | {string} | The provider's middle name                                                                                                                          |
| last_name         | {string} | The provider's last name                                                                                                                            |
| lat_lon           | {string} | Latitude and longitude, as a comma-separated string (e.g. "37.563546, -122.325181").  When lat_lon is provided results will be sorted from this location. |
| gender            | {string} | The provider's gender                                                                                                                               |
| organization_name | {string} | The business practice name                                                                                                                          |
| name              | {string} | Queries against the provider's full name (first, middle, last) for individuals, organization and other organization names for organizations. For best results, do not pass individual name properties (first, middle, last names and organization_name) when using this field.  The name field also uses fuzzy matching and may not return exact matches.|
| specialty         | {string} | The provider's specialty name (e.g. "rheumatology").  Partial name-prefixes may be specified (e.g. "rheum")                                         |
| state             | {string} | The provider's U.S. state code (e.g. "CA")                                                                                                          |
| zipcode           | {string} | The provider's zip or postal code (e.g. "94401")                                                                                                    |
| sort              | {string} | Accepted values include 'distance' (default) or 'rank'.  'distance' sort requires lat_lon, city & state, or zipcode parameters otherwise sort will be 'rank'. |
| entity_types      | {string} | The provider's entity type(s), as a comma-separated string.  Possibilities are 'individual', 'organization', and 'individual,organization'.   |

<!--- end of table -->

### Response

The response from the `/providers/` endpoints contain the following fields:

<!--- beginning of table -->

| Field                                 | Type      | Description                                                                                                    | Presence |
|:--------------------------------------|:----------|:---------------------------------------------------------------------------------------------------------------|:------------------|
| provider.degree                       | {string}  | The provider's degree ("MD" or "DO")                                                                           | Optional (when entity_type is 'individual') |
| provider.description                  | {string}  | Provider description                                                                                           | Optional |
| provider.entity_type                  | {string}  | The entity type of the provider. Possibilities are 'individual') and 'organization')                           | Required |
| provider.fax                          | {string}  | The provider's fax number                                                                                      | Optional |
| provider.first_name                   | {string}  | The provider's first name                                                                                      | Required (when entity_type is 'individual') |
| provider.gender                       | {string}  | The provider's gender                                                                                          | Optional |
| provider.last_name                    | {string}  | The provider's last name                                                                                       | Required (when entity_type is 'individual') |
| provider.licenses                     | {array}   | CMS-NPI license information                                                                                    | Optional |
| provider.licenses.number              | {string}  | License number                                                                                                 | Optional |
| provider.licenses.state               | {string}  | License state                                                                                                  | Optional |
| provider.locations                    | {array}   | List of locations associated with the provider                                                                 | Optional |
| provider.locations.address_lines      | {array}   | Address lines                                                                                                  | Optional |
| provider.locations.city               | {string}  | City                                                                                                           | Required |
| provider.locations.country            | {string}  | Country                                                                                                        | Optional |
| provider.locations.fax                | {string}  | Fax number                                                                                                     | Optional |
| provider.locations.phone              | {string}  | Phone number                                                                                                   | Optional |
| provider.locations.state              | {string}  | State                                                                                                          | Required |
| provider.locations.zipcode            | {string}  | Zip code; length is between 5 and 10 alphanumeric characters                                                                                                      | Required |
| provider.locations.county             | {string}  | County                                                                                                         | Optional |
| provider.locations.role               | {list}    | Address role(s). One or both of: ('mailing' or 'practice').  When missing the address is the practice address. | Optional |
| provider.locations.suite              | {string}  | Address suite																								     | Optional |
| provider.middle_name                  | {string}  | The provider's middle name or initial                                                                          | Optional |
| provider.npi                          | {string}  | The provider's NPI                                                                                             | Optional |
| provider.organization_name            | {string}  | The business practice name                                                                                     | Required (when entity_type is 'organization') |
| provider.other_organization_name      | {string}  | The business practice's other name                                                                             | Optional (when entity_type is 'organization') |
| provider.phone                        | {string}  | The provider's phone number                                                                                    | Optional |
| provider.prefix                       | {string}  | The provider's prefix (Mr., Mrs., Dr., etc)                                                                    | Optional |
| provider.specialty                    | {array}   | List of specialties from the specialty taxonomy associated with the provider                                   | Required |
| provider.specialty_primary            | {array}   | List of provider's primary specialties                                                                         | Required |
| provider.specialty_secondary          | {array}   | List of provider's secondary specialties                                                                       | Required |
| provider.suffix                       | {string}  | The provider's suffix (MD, Jr., etc)                                                                           | Optional |
| provider.uuid                         | {uuid}    | The provider's unique PokitDok Platform identifier                                                             | Required |
| distance                              | {string}  | When sort is 'distance' (default) this is the distance from the city & state or zipcode centroid               | Optional (when sort is 'distance') |

<!--- end of table -->

