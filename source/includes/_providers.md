## Providers
> Example fetching provider information by NPI:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/providers/1467560003
```

```python
pd.providers(npi='1467560003')
```

```csharp
client.providers("1467560003");
```

> Example searching providers by zipcode and specialty:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/providers/?zipcode=29307&specialty=rheumatology&radius=20mi
```

```python
pd.providers(zipcode='29307', specialty='rheumatology', radius='20mi')
```

```csharp
 client.providers(
			new Dictionary<string, string> {
				{ "zipcode", "29307" },
				{ "specialty", "rheumatology" },
				{ "radius", "20mi" }
		});
```


*Available modes of operation: real-time only*

The Providers endpoints provide access to PokitDok's provider directory.
The Providers endpoints can be used to search for Providers, view biographical,
education and credential information, and view specialty taxonomies. Any of
the above listed keywords can be used to show additional fields, perform
searches, and page through results.

Available Provider Endpoints:

| Endpoint        | HTTP Method | Description                                                              |
|:----------------|:------------|:-------------------------------------------------------------------------|
| /providers/     | GET         | Get a list of providers meeting certain search criteria                  |
| /providers/{id} | GET         | Retrieve the data for a specified provider; the ID is the provider's NPI |

The /providers/ endpoint accepts the following search parameters:

| Field             | Type     | Description                                                                                                                                         |
|:------------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| address_lines     | {string} | Any or all of number, street name, apartment, suite number                                                                                       |
| city              | {string} | Name of city in which to search for providers (e.g. "San Mateo" or "Charleston")                                                                    |
| first_name        | {string} | The provider's first name                                                                                                                           |
| last_name         | {string} | The provider's last name                                                                                                                            |
| organization_name | {string} | The business practice name                                                                                                                          |
| radius            | {string} | Search distance from geographic centerpoint, with unit (e.g. "1mi")                                                                                 |
| specialty         | {string} | The provider's specialty name (e.g. "RHEUMATOLOGY")                                                                                                 |
| state             | {string} | Name of U.S. state in which to search for providers (e.g. "CA" or "SC")                                                                             |
| zipcode           | {string} | Geographic center point in which to search for providers (e.g. "94401")                                                                             |
| sort              | {string} | Accepted values include 'distance' (default) or 'rank'.  'distance' sort requires city & state or zipcode parameters otherwise sort will be 'rank'. |

For a complete reference to all possible provider specialties,
see our [provider specialties reference](provider_specialties.html).

The response from the /providers/ endpoints contain the following fields:

| Field                                 | Type      | Description                                                                                                              |
|:--------------------------------------|:----------|:-------------------------------------------------------------------------------------------------------------------------|
| provider.birth_date                   | {string}  | Optional: The provider's birth year                                                                                      |
| provider.board_certifications         | {array}   | Optional: The provider's board certifications                                                                            |
| provider.board_subcertifications      | {array}   | Optional/Deprecated: The provider's board sub-certifications                                                             |
| provider.degree                       | {string}  | Optional: The provider's degree ("MD" or "DO")                                                                           |
| provider.description                  | {string}  | Optional: (verified providers only) Provider full-text description                                                       |
| provider.education                    | {dict}    | Optional: The provider's medical school information                                                                      |
| provider.education.medical_school     | {string}  | Optional: Provider's medical school                                                                                      |
| provider.education.graduation_year    | {string}  | Optional: Provider's graduation year                                                                                     |
| provider.fax                          | {string}  | Optional: The provider's fax number                                                                                      |
| provider.first_name                   | {string}  | Optional: The provider's first name                                                                                      |
| provider.gender                       | {string}  | Optional: The provider's gender                                                                                          |
| provider.last_name                    | {string}  | Optional: The provider's last name                                                                                       |
| provider.licenses                     | {array}   | Optional: CMS-NPI license information                                                                                    |
| provider.licenses.number              | {string}  | Optional: License number                                                                                                 |
| provider.licenses.state               | {string}  | Optional: License state                                                                                                  |
| provider.licenses.year                | {string}  | Optional: License year                                                                                                   |
| provider.licenses.role                | {string}  | Optional/Deprecated: License role                                                                                        |
| provider.licensures                   | {array}   | Optional: State licensure information                                                                                    |
| provider.licensures.as_of_date        | {string}  | Optional: Licensure as of date (ISO-8601)                                                                                |
| provider.licensures.expiration_date   | {string}  | Optional: Licensure expiration date                                                                                      |
| provider.licensures.number            | {string}  | Optional: Licensure number                                                                                               |
| provider.licensures.status            | {string}  | Optional: Licensure status ('active', 'inactive')                                                                        |
| provider.licensures.state             | {string}  | Optional: Licensure state                                                                                                |
| provider.licensures.verified          | {string}  | Optional: Licensure verification status ('Y' or 'N')                                                                     |
| provider.locations                    | {array}   | Optional: List of locations associated with the provider                                                                 |
| provider.locations.address_lines      | {array}   | Address lines                                                                                                            |
| provider.locations.city               | {string}  | City                                                                                                                     |
| provider.locations.country            | {string}  | Optional: Country                                                                                                        |
| provider.locations.fax                | {string}  | Optional: Fax number                                                                                                     |
| provider.locations.geo_location       | {array}   | GeoJSON array of \[longitude, latitude\]                                                                                 |
| provider.locations.phone              | {string}  | Optional: Phone number                                                                                                   |
| provider.locations.state              | {string}  | State                                                                                                                    |
| provider.locations.zipcode            | {string}  | Zip code                                                                                                                 |
| provider.locations.role               | {list}    | Optional: Address role(s). One or both of: ('mailing' or 'practice').  When missing the address is the practice address. |
| provider.middle_name                  | {string}  | Optional: The provider's middle name or initial                                                                          |
| provider.npi                          | {string}  | The provider's NPI                                                                                                       |
| provider.organization_name            | {string}  | Optional: The business practice name                                                                                     |
| provider.phone                        | {string}  | Optional: The provider's phone number                                                                                    |
| provider.prefix                       | {string}  | Optional: The provider's prefix (Mr., Mrs., Dr., etc)                                                                    |
| provider.residencies                  | {array}   | Optional: Provider residency and education information                                                                   |
| provider.residencies.institution_name | {string}  | Optional: Institution name                                                                                               |
| provider.residencies.type             | {string}  | Optional: Education type.  One of: ('Medical School', 'Residency','Internship', 'Fellowship', 'College Attended')        |
| provider.residencies.to_year          | {string}  | Optional: Graduation year                                                                                                |
| provider.residencies.from_year        | {string}  | Optional/Deprecated: Start year                                                                                          |
| provider.residencies.city             | {string}  | Optional/Deprecated: Residency city                                                                                      |
| provider.residencies.specialty        | {string}  | Optional/Deprecated: Residency specialty                                                                                 |
| provider.specialty                    | {array}   | Optional: List of specialties from the specialty taxonomy associated with the provider                                   |
| provider.specialty_primary            | {array}   | Optional: List of provider's primary specialties                                                                         |
| provider.specialty_secondary          | {array}   | Optional: List of provider's secondary specialties                                                                       |
| provider.suffix                       | {string}  | Optional: The provider's suffix (MD, Jr., etc)                                                                           |
| provider.uuid                         | {uuid}    | The provider's unique PokitDok Platform identifier                                                                       |
| provider.verified                     | {boolean} | Optional: Provider PokitDok verification status                                                                          |
| provider.facebook_url                 | {string}  | Optional: (verified providers only) Provider Facebook URL                                                                |
| provider.small_image_url              | {string}  | Optional: (verified providers only) Provider small image URL                                                             |
| provider.twitter_url                  | {string}  | Optional: (verified providers only) Provider Twitter URL                                                                 |
| provider.website_url                  | {string}  | Optional: (verified providers only) Provider website URL                                                                 |
| distance                              | {string}  | Optional: When sort is 'distance' (default) this is the distance from the city & state or zipcode centroid               |
