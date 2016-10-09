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

>Example Response:

```json
{
  "provider": {
    "birth_date": "1972",
    "degree": "MD",
    "description": "Dr. Jerome Aya-Ay was raised in the small rural town of Grantsville, West Virginia. He graduated from the University of Notre Dame with a bachelor's degree in Biology.  After studying for a Masters in Biomedical Sciences at Marshall University, he continued on to graduate from Marshall University School of Medicine in Huntington, WV with a medical degree. Dr. Aya-Ay completed his residency in Family Medicine at Spartanburg Regional Medical Center where he was awarded the Family Medicine...",
    "education": {
      "graduation_year": 2004,
      "medical_school": "Marshall University School Of Medicine"
    },
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
    "licensures": [
      {
        "expiration_date": "2017-06-25",
        "number": "27210",
        "state": "SC",
        "status": "active",
        "verified": "Y"
      }
    ],
    "locations": [
      {
        "address_lines": [
          "1703 John B White SR Blvd Ste A"
        ],
        "city": "Spartanburg",
        "geo_location": [
          -81.98184,
          34.92287
        ],
        "phone": "8646417229",
        "role": [
          "practice"
        ],
        "state": "SC",
        "zipcode": "29301"
      },
      {
        "address_lines": [
          "1120 N Pleasantburg Dr Ste 301"
        ],
        "city": "Greenville",
        "geo_location": [
          -82.36932,
          34.80968
        ],
        "phone": "8642524808",
        "role": [
          "practice"
        ],
        "state": "SC",
        "zipcode": "29607"
      }
    ],
    "middle_name": "Benitez",
    "npi": "1467560003",
    "phone": "8645625100",
    "prefix": "DR",
    "residencies": [
      {
        "institution_name": "Spartanburg Regional Healthcare System",
        "type": "Residency"
      },
      {
        "institution_name": "Marshall University School Of Medicine",
        "to_year": 2004,
        "type": "Medical School"
      }
    ],
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
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" "https://platform.pokitdok.com/api/v4/providers/?zipcode=29307&specialty=rheumatology&radius=3mi"
```

```python
client.providers(zipcode='29307', specialty='rheumatology', radius='3mi')
```

```csharp
 client.providers(
			new Dictionary<string, string> {
				{ "zipcode", "29307" },
				{ "specialty", "rheumatology" },
				{ "radius", "3mi" }
		});
```

```ruby
client.providers({zipcode: '29307', specialty: 'rheumatology', radius: '3mi'})
```

```java
HashMap<String, String> query = new HashMap<String, String>();
query.put("zipcode", "29307");
query.put("specialty", "rheumatology");
query.put("radius", "3mi");

client.providers(query)
```

>Example response:

```json
[
  {
    "distance": 2.0202967583329134,
    "provider": {
      "entity_type": "organization",
      "fax": "8645821269",
      "locations": [
        {
          "address_lines": [
            "1770 Skylyn Dr"
          ],
          "city": "Spartanburg",
          "county": "Spartanburg",
          "fax": "8645821269",
          "geo_location": [
            -81.892414,
            34.980127
          ],
          "phone": "8645827892",
          "state": "SC",
          "zipcode": "29307"
        }
      ],
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
      "birth_date": "1971",
      "degree": "MD",
      "education": {
        "graduation_year": 1997,
        "medical_school": "Sri Devaraj Urs Medical College"
      },
      "entity_type": "individual",
      "facilities": [
        {
          "npi": "1669425963",
          "organization_name": "Mary Black Memorial Hospital"
        }
      ],
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
      "licensures": [
        {
          "expiration_date": "2017-06-30",
          "number": "28487",
          "state": "SC",
          "status": "active",
          "verified": "Y"
        }
      ],
      "locations": [
        {
          "address_lines": [
            "1770 Skylyn Dr"
          ],
          "city": "Spartanburg",
          "county": "Spartanburg",
          "fax": "8645821582",
          "geo_location": [
            -81.892414,
            34.980127
          ],
          "phone": "8645827892",
          "state": "SC",
          "zipcode": "29307"
        },
        {
          "address_lines": [
            "1650 Skylyn Dr",
            "Suite 220"
          ],
          "city": "Spartanburg",
          "county": "Spartanburg",
          "geo_location": [
            -81.894438,
            34.977198
          ],
          "state": "SC",
          "suite": "220",
          "zipcode": "29307"
        }
      ],
      "middle_name": "J",
      "npi": "1699725986",
      "phone": "8645827892",
      "residencies": [
        {
          "institution_name": "University Mo Columbia School Medicine",
          "type": "Residency"
        },
        {
          "institution_name": "Sri Devaraj Urs Medical College",
          "to_year": 1997,
          "type": "Medical School"
        }
      ],
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
      "locations": [
        {
          "address_lines": [
            "PO Box 277827"
          ],
          "city": "Atlanta",
          "country": "US",
          "geo_location": [
            -84.47405,
            33.844371
          ],
          "phone": "8642538080",
          "role": [
            "mailing"
          ],
          "state": "GA",
          "zipcode": "30384"
        },
        {
          "address_lines": [
            "1770 Skylyn Dr"
          ],
          "city": "Spartanburg",
          "country": "US",
          "fax": "8645821582",
          "geo_location": [
            -81.89268,
            34.97982
          ],
          "phone": "8645827892",
          "role": [
            "practice"
          ],
          "state": "SC",
          "zipcode": "29307"
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
education, credential, and license information. For a complete reference to all possible 
provider specialties, see our [provider specialties reference](provider_specialties.html).

Available Provider Endpoints:

| Endpoint        | HTTP Method | Description                                                              |
|:----------------|:------------|:-------------------------------------------------------------------------|
| /providers/     | GET         | Get a list of providers meeting certain search criteria                  |
| /providers/{id} | GET         | Retrieve the data for a specified provider; the ID is the provider's NPI |

The /providers/ endpoint accepts the following search parameters:

| Parameter         | Type     | Description                                                                                                                                         |
|:------------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| address_lines     | {string} | Any or all of number, street name, apartment, suite number                                                                                          |
| city              | {string} | Name of city in which to search for providers (e.g. "San Mateo" or "Charleston")                                                                    |
| first_name        | {string} | The provider's first name                                                                                                                           |
| middle_name       | {string} | The provider's middle name                                                                                                                          |
| last_name         | {string} | The provider's last name                                                                                                                            |
| gender            | {string} | The provider's gender                                                                                                                               |
| organization_name | {string} | The business practice name                                                                                                                          |
| name              | {string} | Queries against the provider's full name (first, middle, last) for individuals, organization and other organization names for organizations. For best results individual name properties and organization name should be omitted when passing this parameter.|
| radius            | {string} | Search distance from geographic centerpoint, with unit (e.g. "1mi")                                                                                 |
| specialty         | {string} | The provider's specialty name (e.g. "rheumatology").  Partial name-prefixes may be specified (e.g. "rheum")                                         |
| state             | {string} | Name of U.S. state in which to search for providers (e.g. "CA" or "SC")                                                                             |
| zipcode           | {string} | Geographic center point in which to search for providers (e.g. "94401")                                                                             |
| sort              | {string} | Accepted values include 'distance' (default) or 'rank'.  'distance' sort requires city & state or zipcode parameters otherwise sort will be 'rank'. |
| entity_types      | {string} | The desired provider entity type(s), as a comma-separated string.  Possibilities are 'individual', 'organization', and 'individual,organization'.   |
| facility_names    | {string} | Name(s) of provider facilities.  Providers having facilities.organization_name matching this name will be boosted in the results.  Only facility_names or facility_npis may be specified not both. |
| facility_npis     | {string} | NPIs of provider facilities.  Providers having facilities.npi matching these NPIs will be boosted in the results.  The string argument should be a comma-separated list of NPIs.  Only facility_name or facility_npis may be specified not both. |

The response from the /providers/ endpoints contain the following fields:

| Field                                 | Type      | Description                                                                                                    | Presence |
|:--------------------------------------|:----------|:---------------------------------------------------------------------------------------------------------------|:------------------|
| provider.birth_date                   | {string}  | The provider's birth year. In ISO8601 format (YYYY-MM-DD).                                                     | Optional (when entity_type is 'individual') |
| provider.board_certifications         | {array}   | The provider's board certifications                                                                            | Optional (when entity_type is 'individual') |
| provider.degree                       | {string}  | The provider's degree ("MD" or "DO")                                                                           | Optional (when entity_type is 'individual') |
| provider.description                  | {string}  | Provider description                                                                                           | Optional |
| provider.education                    | {dict}    | The provider's medical school information                                                                      | Optional (when entity_type is 'individual') |
| provider.education.medical_school     | {string}  | Provider's medical school                                                                                      | Required |
| provider.education.graduation_year    | {string}  | Provider's graduation year                                                                                     | Optional |
| provider.entity_type                  | {string}  | The entity type of the provider. Possibilities are 'individual') and 'organization')                           | Required |
| provider.facilities                   | {array}   | Providers' affiliated facilities                                                                               | Optional |
| provider.facilities.organization_name | {string}  | Facility organization name                                                                                     | Required |
| provider.facilities.npi               | {string}  | Facility NPI                                                                                                   | Optional |
| provider.fax                          | {string}  | The provider's fax number                                                                                      | Optional |
| provider.first_name                   | {string}  | The provider's first name                                                                                      | Required (when entity_type is 'individual') |
| provider.gender                       | {string}  | The provider's gender                                                                                          | Optional |
| provider.last_name                    | {string}  | The provider's last name                                                                                       | Required (when entity_type is 'individual') |
| provider.licenses                     | {array}   | CMS-NPI license information                                                                                    | Optional |
| provider.licenses.number              | {string}  | License number                                                                                                 | Optional |
| provider.licenses.state               | {string}  | License state                                                                                                  | Optional |
| provider.licensures                   | {array}   | State licensure information                                                                                    | Optional |
| provider.licensures.as_of_date        | {string}  | Licensure as of date. In ISO8601 format (YYYY-MM-DD).                                                          | Optional |
| provider.licensures.expiration_date   | {string}  | Licensure expiration date. In ISO8601 format (YYYY-MM-DD).                                                     | Optional |
| provider.licensures.number            | {string}  | Licensure number                                                                                               | Optional |
| provider.licensures.status            | {string}  | Licensure status ('active', 'inactive')                                                                        | Optional |
| provider.licensures.state             | {string}  | Licensure state                                                                                                | Optional |
| provider.licensures.verified          | {string}  | Licensure verification status ('Y' or 'N')                                                                     | Optional |
| provider.locations                    | {array}   | List of locations associated with the provider                                                                 | Optional |
| provider.locations.address_lines      | {array}   | Address lines                                                                                                  | Optional |
| provider.locations.city               | {string}  | City                                                                                                           | Required |
| provider.locations.country            | {string}  | Country                                                                                                        | Optional |
| provider.locations.fax                | {string}  | Fax number                                                                                                     | Optional |
| provider.locations.geo_location       | {array}   | GeoJSON array of \[longitude, latitude\]                                                                       | Optional |
| provider.locations.phone              | {string}  | Phone number                                                                                                   | Optional |
| provider.locations.state              | {string}  | State                                                                                                          | Required |
| provider.locations.zipcode            | {string}  | Zip code                                                                                                       | Required |
| provider.locations.county             | {string}  | County                                                                                                         | Optional |
| provider.locations.role               | {list}    | Address role(s). One or both of: ('mailing' or 'practice').  When missing the address is the practice address. | Optional |
| provider.locations.suite              | {string}  | Address suite																								     | Optional |
| provider.middle_name                  | {string}  | The provider's middle name or initial                                                                          | Optional |
| provider.npi                          | {string}  | The provider's NPI                                                                                             | Optional |
| provider.organization_name            | {string}  | The business practice name                                                                                     | Required (when entity_type is 'organization') |
| provider.other_organization_name      | {string}  | The business practice's other name                                                                             | Optional (when entity_type is 'organization') |
| provider.phone                        | {string}  | The provider's phone number                                                                                    | Optional |
| provider.prefix                       | {string}  | The provider's prefix (Mr., Mrs., Dr., etc)                                                                    | Optional |
| provider.residencies                  | {array}   | Provider residency and education information                                                                   | Optional (when entity_type is 'individual') |
| provider.residencies.institution_name | {string}  | Institution name                                                                                               | Required |
| provider.residencies.type             | {string}  | Education type.  One of: ('Medical School', 'Residency','Internship', 'Fellowship', 'College Attended')        | Required |
| provider.residencies.to_year          | {string}  | Graduation year                                                                                                | Optional |
| provider.specialty                    | {array}   | List of specialties from the specialty taxonomy associated with the provider                                   | Required |
| provider.specialty_primary            | {array}   | List of provider's primary specialties                                                                         | Required |
| provider.specialty_secondary          | {array}   | List of provider's secondary specialties                                                                       | Required |
| provider.suffix                       | {string}  | The provider's suffix (MD, Jr., etc)                                                                           | Optional |
| provider.uuid                         | {uuid}    | The provider's unique PokitDok Platform identifier                                                             | Required |
| provider.website_url                  | {string}  | (verified providers only) Provider website URL                                                                 | Optional (when entity_type is 'organization') |
| distance                              | {string}  | When sort is 'distance' (default) this is the distance from the city & state or zipcode centroid               | Optional (when sort is 'distance') |

