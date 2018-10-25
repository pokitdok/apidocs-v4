## In-Network Pharmacies

> Example fetching pharmacy information by NPI:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"  'https://platform.pokitdok.com/api/v4/pharmacy/network/1427382266?trading_partner_id=medicare_national&plan_number=S5820003'
```

```python
client.pharmacy_network(npi='1427382266', trading_partner_id='medicare_national', plan_number='S5820003')
```

```ruby
client.pharmacy_network(npi: '1427382266', trading_partner_id: 'medicare_national', plan_number: 'S5820003')
```

```csharp
client.pharmacyNetwork(
                    "1427382266",
                    new Dictionary<string, string> {
                      {"trading_partner_id", "medicare_national"},
                      {"plan_number", "S5820003"}
                  });
```

```java
Map<String, Object> params = new HashMap<String, Object>();
params.put("trading_partner_id", "medicare_national");
params.put("plan_number", "S5820003");
client.pharmacyNetwork("1427382266", params);
```

```swift
let data = [
    "trading_partner_id": "medicare_national",
    "plan_number": "S5820003"
] as [String:Any]
try client.pharmacyNetwork(npi: "1427382266", params: data)
```

> Example searching for in-network pharmacies by plan and zip code:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"  'https://platform.pokitdok.com/api/v4/pharmacy/network?trading_partner_id=medicare_national&plan_number=S5820003&zipcode=07030&radius=1mi'
```

```python
client.pharmacy_network(trading_partner_id='medicare_national', plan_number='S5820003' , zipcode='07030', radius='1mi')
```

```ruby
client.pharmacy_network(trading_partner_id: 'medicare_national', plan_number: 'S5820003' , zipcode: '07030', radius: '1mi')
```

```csharp
client.pharmacyNetwork(
                    new Dictionary<string, string> {
                      {"trading_partner_id", "medicare_national"},
                      {"plan_number", "S5820003"},
                      {"zipcode", "07030"},
                      {"radius", "1mi"}
                  });
```

```java
Map<String, Object> params = new HashMap<String, Object>();
params.put("trading_partner_id", "medicare_national");
params.put("plan_number", "S5820003");
params.put("zipcode", "07030");
params.put("radius", "1mi");
client.pharmacyNetwork(params);
```

```swift
let data = [
    "trading_partner_id": "medicare_national",
    "plan_number": "S5820003",
    "zipcode": "07030",
    "radius": "1mi"
] as [String:Any]
try client.pharmacyNetwork(params: data)
```

> Sample response for /pharmacy/network/{npi} endpoint :

```
{
    "data": [
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "307 1st St"
                ],
                "city": "Hoboken",
                "country": "US",
                "geo_location": [
                    -74.03467,
                    40.738
                ],
                "phone": "2014207777",
                "state": "NJ",
                "zipcode": "07030"
            },
            "mail": false,
            "npi": "1427382266",
            "pharmacy_name": "HOBOKEN DRUGS",
            "plan_id": "H0755036",
            "retail": true
        }
    ]
}

```

> Sample response for /pharmacy/network endpoint when using zipcode and radius as parameters:

```
{
    "data": [
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "59 Washington St Court St Plz"
                ],
                "city": "Hoboken",
                "geo_location": [
                    -74.032718,
                    40.74409
                ],
                "phone": "2017981889",
                "state": "NJ",
                "zipcode": "07030"
            },
            "mail": false,
            "npi": "1578655056",
            "pharmacy_name": "New Jersey Cvs Pharmacy Llc",
            "plan_id": "H0755035",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "210 14th St"
                ],
                "city": "Hoboken",
                "geo_location": [
                    -74.02829,
                    40.75364
                ],
                "phone": "4017651500",
                "state": "NJ",
                "zipcode": "07030"
            },
            "mail": false,
            "npi": "1801919907",
            "pharmacy_name": "New Jersey Cvs Pharmacy Llc",
            "plan_id": "H0755035",
            "retail": true
        },
        {
            "in_network": true,
            "location": {
                "address_lines": [
                    "1320 Shipyard Ln",
                    "Suite 3-4"
                ],
                "city": "Hoboken",
                "geo_location": [
                    -74.024709,
                    40.751996
                ],
                "phone": "2018760040",
                "state": "NJ",
                "zipcode": "07030"
            },
            "mail": false,
            "npi": "1295845972",
            "pharmacy_name": "Rite Aid Of New Jersey Inc",
            "plan_id": "H0913013",
            "retail": true
        }
    ]
}
```

The In-Network Pharmacy Endpoint returns in-network pharmacies for a plan.

### Endpoint Description

<!--- beginning of table -->

| Endpoint               | HTTP Method | Description                                                              |
|:-----------------------|:------------|:-------------------------------------------------------------------------|
| /pharmacy/network/     | GET         | Get a list of pharmacies meeting certain search criteria                 |
| /pharmacy/network/{id} | GET         | Retrieve the data for a specified pharmacy; the ID is the provider’s NPI |

<!--- end of table -->

To use the In-Network Pharmacy Endpoint with a Medicare member, you will need the plan number. This is the contract ID (ex. S1234) + Plan's Plan Benefit Package (PBP) Number PBP number (ex. 001) concatenated together in that order. There are several ways to get this number. The plan number may be on the member’s insurance card. If not, you can use an NCPDP E1 eligibility check or PokitDok’s Eligibility Endpoint. With the Eligibility Endpoint, Medicare members with Part D coverage will have pharmacy.is_eligible set to true and the pharmacy.plan_number will contain their Medicare Part D plan_number. Note: Your NPI must be registered with Medicare to check eligibility.

A list of pharmacies will be returned for a given location and radius. The in-network pharmacy endpoint defaults to retail pharmacies.

The response will include details about the pharmacy such as name, address, phone number, etc.

### Parameters

The `/pharmacy/network` endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter          | Type     | Description                                                                                                                                                    | Presence |
|:-------------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
| trading_partner_id | {string} | Unique id for the intended trading partner, as specified by the [Trading Partners](https://platform.pokitdok.com/documentation/v4/#trading-partners) endpoint. | Required |
| plan_number        | {string} | Member’s plan identification number. Note: If unknown can use X12 270/271 eligibility                                                                          | Optional |
| zipcode            | {string} | Zip code for location                                                                                                                                          | Optional |
| radius             | {string} | Radius of area (miles)                                                                                                                                         | Optional |
| pharmacy_name      | {string} | Name of pharmacy                                                                                                                                               | Optional |
| state              | {string} | Name of U.S. state in which to search for providers (e.g. “CA” or “SC”)                                                                                        | Optional |
| sort               | {string} | Accepted values include ‘distance’ (default) or 'rank’. 'distance’ sort requires city & state or zipcode parameters otherwise sort will be 'rank’.             | Optional |
| retail             | {boolean} | Return retail pharmacies (default=true)                                                                                                                       | Optional |
| mail               | {boolean} | Return mail order pharmacies (default=false)                                                                                                                  | Optional |

<!--- end of table -->

### Response

The `/pharmacy/network` response contains the following fields:

<!--- beginning of table -->

| Field                            | Type      | Description                            | Presence |
|:---------------------------------|:----------|:---------------------------------------|:---------|
| pharmacy.pharmacy_name           | {string}  | Name of pharmacy                       | Required |
| pharmacy.npi                     | {string}  | NPI of pharmacy                        | Required |
| pharmacy.in_network              | {boolean} | True if pharmacy is in-network         | Required |
| pharmacy.locations.address_lines | {array}   | Address lines                          | Optional |
| pharmacy.locations.city          | {string}  | City                                   | Optional |
| pharmacy.locations.country       | {string}  | Country                                | Optional |
| pharmacy.locations.geo_location  | {array}   | GeoJSON array of [longitude, latitude] | Optional |
| pharmacy.locations.phone         | {string}  | Phone number                           | Optional |
| pharmacy.locations.state         | {string}  | State                                  | Optional |
| pharmacy.locations.zipcode       | {string}  | Zip code                               | Optional |
| pharmacy.mail                    | {boolean} | Is location a mail order pharmacy?     | Optional |
| pharmacy.plan_number             | {string}  | Plan number                            | Required |
| pharmacy.retail                  | {boolean} | Is location a retail order pharmacy?   | Optional |

<!--- end of table -->
