## Trading Partners
> Example fetching trading partner information:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/tradingpartners/
```

```python
client.trading_partners()
```

```csharp
client.tradingPartners();
```

```ruby
client.trading_partners
```

```java
client.tradingPartners();
```

```swift
try client.tradingPartners()
```

>Example response (for a more complete response please use the test application):

```json
[
  {
    "enrollment_required": [],
    "id": "aetna",
    "is_enabled": true,
    "name": "Aetna",
    "supported_transactions": [
      "276",
      "270",
      "278",
      "837"
    ]
  },
  {
    "enrollment_required": [],
    "id": "aetna_affordable_health_src",
    "is_enabled": true,
    "name": "Aetna Affordable Health Choices SM SRC",
    "supported_transactions": [
      "837"
    ]
  },
  {
    "enrollment_required": [],
    "id": "aetna_better_health",
    "is_enabled": true,
    "name": "Aetna Better Health",
    "supported_transactions": [
      "276",
      "837",
      "270"
    ]
  }
]
```

> Example fetching information for a specific trading partner:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/tradingpartners/aetna
```

```python
client.trading_partners('aetna')
```

```csharp
client.tradingPartners("MOCKPAYER");
```

```ruby
client.trading_partners('aetna')
```

```java
client.trading_partners({ trading_partner_id: 'aetna' })
```

```swift
try client.tradingPartners(tradingPartnerId: "aetna")
```

> Example response:

```json
{
  "id": "aetna",
  "is_enabled": true,
  "name": "Aetna",
  "enrollment_required": [],
  "provider_enrollment_required": false,
  "provider_enrollment_setup": {
    "client_action_required": false,
    "internal_action_required": false,
    "internal_action_initiates": false
  },
  "provider_enrollment_required_transaction_types": [],
  "provider_enrollment_setup_transaction_types": {
    "client_action_required": [],
    "internal_action_required": [],
    "internal_action_initiates": []
  },
  "metrics": {
    "real_time_response_average": 1450.6305211848169,
    "real_time_response_percentiles": {
      "50": 1205.7390631791739,
      "75": 1573.4728916585882,
      "95": 2470.0921487230594
    }
  },
  "monitoring": {
    "claims": {
      "last_updated": "2016-09-29T13:45:03.750000",
      "status": "available"
    },
    "eligibility": {
      "last_updated": "2016-12-06T16:50:25.146000",
      "status": "available"
    },
    "referrals": {
      "last_updated": "2015-09-03T20:52:05.077000",
      "status": "available"
    }
  },
  "pass_through_fees": {
    "270": {
      "amount": "0.0",
      "currency": "USD"
    },
    "276": {
      "amount": "0.0",
      "currency": "USD"
    },
    "278": {
      "amount": "0.0",
      "currency": "USD"
    },
    "837": {
      "amount": "0.0",
      "currency": "USD"
    }
  },
  "restricted_transactions": [
    "837",
    "278"
  ],
  "supported_search_options": [
    "no_id_search",
    "no_first_name_search",
    "no_birth_date_search",
    "no_name_search",
    "primary_search"
  ],
  "supported_transactions": [
    "270",
    "837",
    "276",
    "278"
  ]
}
```

*Available modes of operation: real-time*

The Trading Partners endpoint provides access to the collection of PokitDok's trading
partners. Available Trading Partner endpoints and the descriptions of their request and response parameters are as follows.

### Endpoint Description

<!--- beginning of table -->

| Endpoint              | HTTP Method | Description                                                                                   |
|:----------------------|:------------|:----------------------------------------------------------------------------------------------|
| /tradingpartners/     | GET         | Get a list of trading partners.                                                               |
| /tradingpartners/{id} | GET         | Retrieve the data for a specified trading partner; the ID is the PokitDok trading partner id. |

<!--- end of table -->

### Response

The `/tradingpartners/` response contains the following fields:

<!--- beginning of table -->

| Field                                                                  | Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:-----------------------------------------------------------------------|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                                                                     | {string}   | The "trading_partner_id" used in requests to identify this trading partner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| is_enabled                                                             | {boolean}  | Indicates if the connection to the trading partner is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| name                                                                   | {string}   | Full name for the trading partner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| supported_transactions                                                 | {array}    | Identifies the X12 transaction sets (270, 276, 278, 837, etc.) available for a trading partner. The list of supported transactions indicates the API Endpoints that are enabled for the trading partner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| enrollment_required                                                    | {array}    | Field is no longer in use.  Previously used to identify the X12 transaction sets (270, 276, 278, 837, etc.) that required additional set up before transacting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| provider_enrollment_required                                           | {boolean}  | Specifies whether a provider needs to be enrolled with the trading partner before that provider can be used in an API call sent to the trading partner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| provider_enrollment_required_transaction_types                         | {array}    | Specifies which of the X12 transaction types (270, 276, 278, 837, etc.) require a provider to be enrolled with the trading partner before that provider can be used in an API call sent to the trading partner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| provider_enrollment_setup                                              | {object}   | Describes what steps need to be taken to enroll a provider with the trading partner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| provider_enrollment_setup.client_action_required                       | {boolean}  | Specifies whether client action is required during the provider enrollment process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| provider_enrollment_setup.internal_action_required                     | {boolean}  | Specifies whether internal action is required during the provider enrollment process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| provider_enrollment_setup.internal_action_initiates                    | {boolean}  | Specifies whether internal action initiates the enrollment process (i.e., PokitDok has internal processes to complete before provider enrollment is active).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| provider_enrollment_setup_transaction_types                            | {object}   | Describes what steps need to be taken for which which transaction types to enroll a provider with the trading partner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| provider_enrollment_setup_transaction_types.client_action_required     | {array}    | Specifies which of the X12 transaction types (270, 276, 278, 837, etc.) require client action during the provider enrollment process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| provider_enrollment_setup_transaction_types.internal_action_required   | {array}    | Specifies which of the X12 transaction types (270, 276, 278, 837, etc.) require internal action during the provider enrollment process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| provider_enrollment_setup_transaction_types.internal_action_initiates  | {array}    | Specifies which of the X12 transaction types (270, 276, 278, 837, etc.) require internal action to initiate the enrollment process (i.e., PokitDok has internal processes to complete before provider enrollment is active).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| metrics                                                                | {object}   | When a specific trading partner id is requested and metrics are available, they will be included in the response. Timings are in milliseconds unless otherwise specified. Field returned only for /tradingpartners/{id} request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| metrics.real_time_response_average                                     | {float}    | The average response time (milliseconds) for requests to this trading partner. Field returned only for /tradingpartners/{id} request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| metrics.real_time_response_percentiles                                 | {float}    | Provides a percentile rank of the trading partner's response times, with the following groupings: 50%, 75%, and 95%. Field returned only for /tradingpartners/{id} request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| monitoring                                                             | {object}   | When a specific trading partner id is requested and monitoring data is available, monitoring information will be included in the response. Each key in the monitoring section corresponds to the name of an API where connectivity is enabled (e.g. claims, claim_status, eligibility, etc). Each API name will be associated with a monitoring status value and a timestamp to indicate when the status was last updated. Field returned only for /tradingpartners/{id} request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| monitoring.{api_name}.status                                           | {string}   | The most recent status for the trading partner/API combination as returned by our monitoring system. Possible values include: available, unavailable, delayed, and unknown. A status of "available" indicates that the trading partner is operating normally based successful transactions executing within their average response time range. A status of "unavailable" indicates that the trading partner is unable to respond normally at that time. This may be due to scheduled or unplanned downtime. A status of "delayed" indicates that the trading partner is able to respond successfully to requests but that response times are higher than their average response time. A status of "unknown" will be returned for new trading partners that have just been added to the system and also for cases where the monitoring system encounters an exception and is unable to determine the current status. Field returned only for /tradingpartners/{id} request. |
| monitoring.{api_name}.last_updated                                     | {datetime} | The date the monitoring status was last updated. Field returned only for /tradingpartners/{id} request. In ISO8601 format (YYYY-MM-DDThh:mm:ss.ssssss).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| pass_through_fees                                                      | {object}   | Identifies the X12 transaction sets (270, 278, 837) that have pass through fees associated with transactions. Field returned only for /tradingpartners/{id} request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| pass_through_fees.{transaction_set}.amount                             | {float}    | Identifies the cost of each pass through fee per transaction. Field returned only for /tradingpartners/{id} request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| pass_through_fees.{transaction_set}.currency                           | {string}   | Identifies the currency associated with the pass through fee amount. Field returned only for /tradingpartners/{id} request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| restricted_transactions                                                | {array}    | Identifies the X12 transaction sets (270, 278, 837) that require NPI submission in the client dashboard prior to use. Field returned only for /tradingpartners/{id} request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| supported_search_options                                               | {array}    | A list of member search options that are supported by the trading partner for eligibility requests.  A complete listing of possible [search options](#search-options) is included below. Field returned only for /tradingpartners/{id} request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

<!--- end of table -->

### Additional Object Tables

<a name="search-options"></a>
Full list of possible search options that may be available for use with a trading partner on eligibility requests.
These constants align with Section 1.4.8 (Search Options) of the X12 270/271 specification around the use of available
member information to locate the member in the trading partner's system. Please note that supported search options are subject to change and are dictated by the trading partner. For best results, include as much information as possible and note that primary_search is most effective.

<!--- beginning of table -->

| Search Option                               | Description
|:--------------------------------------------|:----------------|
| primary_search                              | first_name, last_name, id, and birth_date are provided to locate a member.  This is the search option supported by most trading partners. |
| primary_search_gender                       | first_name, last_name, id, birth_date, and gender are provided to locate a member.                |
| no_first_name_search                        | last_name, id, and birth_date are provided to locate a member.                |
| no_birth_date_search                        | first_name, last_name, and id are provided to locate a member.               |
| no_name_search                              | id and birth_date are provided to locate a member.               |
| no_id_search                                | first_name, last_name and birth_date are provided to locate a member.               |

<!--- end of table -->