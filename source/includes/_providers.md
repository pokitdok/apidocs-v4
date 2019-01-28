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
    "degree": "MD",
    "description": "Dr. Jerome Aya-Ay was raised in the small rural town of Grantsville, West Virginia. He graduated from the University of Notre Dame with a bachelor's degree in Biology.  After studying for a Masters in Biomedical Sciences at Marshall University, he continued on to graduate from Marshall University School of Medicine in Huntington, WV with a medical degree. Dr. Aya-Ay completed his residency in Family Medicine at Spartanburg Regional Medical Center where he was awarded the Family Medicine...",
    "fax": "8645625230",
    "first_name": "Jerome",
    "gender": "Male",
    "last_name": "Aya-Ay",
    "licenses": [
      {
        "number": "27210",
        "state": "SC"
      }
    ],
    "middle_name": "Benitez",
    "npi": "1467560003",
    "phone": "8645625100",
    "prefix": "DR",
    "small_image_url": "https://d2sc6ykmuixlzf.cloudfront.net/pda0233f41447f472dab57393b0cbf5bb7-29ef4cc83c4372854a573b302b259b2c-thumbnail.jpeg",
    "specialty": [
      "General & Family Medicine",
      "Family Practice",
      "Preventive Medicine",
      "General Practitioner"
    ],
    "specialty_primary": [
      "Family Practice"
    ],
    "specialty_secondary": [
      "Physician"
    ],
    "uuid": "fc44d0e0-ea7f-492e-90f0-0f9148453019",
    "verified": true
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
    "distance": 2.0202967583329134,
    "provider": {
      "entity_type": "organization",
      "fax": "8645821269",
      "npi": "1588809198",
      "organization_name": "Mary Black Physicians Group LLC",
      "other_organization_name": "Piedmont Rheumatology",
      "phone": "8645827892",
      "specialty": [
        "Rheumatology",
        "Internal Medicine"
      ],
      "specialty_primary": [
        "Rheumatology"
      ],
      "specialty_secondary": [
        "Allopathic and Osteopathic Physicians (MD/DO)"
      ],
      "uuid": "03d41ad4-4744-425c-882f-4136bf5d5d86",
      "verified": false
    }
  },
  {
    "distance": 2.0202967583329134,
    "provider": {
      "degree": "MD",
      "entity_type": "individual",
      "fax": "8645821582",
      "first_name": "Muthamma",
      "gender": "Female",
      "last_name": "Machimada",
      "licenses": [
        {
          "number": "28487",
          "state": "SC"
        }
      ],
      "middle_name": "J",
      "npi": "1699725986",
      "phone": "8645827892",
      "specialty": [
        "Rheumatology",
        "Internal Medicine"
      ],
      "specialty_primary": [
        "Rheumatology"
      ],
      "specialty_secondary": [
        "Physician"
      ],
      "uuid": "e3f3690d-b49b-458f-b83c-f159b7a18b6e",
      "verified": false
    }
  },
  {
    "distance": 2.037465294795502,
    "provider": {
      "degree": "MD",
      "entity_type": "individual",
      "fax": "8645821582",
      "first_name": "KEVIN",
      "gender": "Male",
      "last_name": "TRACY",
      "licenses": [
        {
          "number": "14815",
          "state": "SC"
        }
      ],
      "middle_name": "PATRICK",
      "npi": "1215993159",
      "phone": "8645827892",
      "prefix": "DR",
      "specialty": [
        "Rheumatology",
        "Internal Medicine"
      ],
      "specialty_primary": [
        "Rheumatology"
      ],
      "specialty_secondary": [
        "Internal Medicine"
      ],
      "uuid": "bd67dda2-51c2-4325-999f-73052b372885",
      "verified": false
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

