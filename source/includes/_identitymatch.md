## Identity Match
> Example: list all of the MatchConfigs owned by a production app.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match_config/
```

```python
client.get("/identity/match_config/")
```

```csharp
client.request("/identity/match_config/", "GET")
```

```ruby
client.request("/identity/match_config/", "GET")
```

```java
client.get("/identity/match_config/")
```

```swift
let path = "/identity/match_config/"
try client.request(path: path, method: "GET")
```

> Example response showing all MatchConfigs owned by a production app.

```json
{
    "data": [
        {
            "input_topic": "test_name_and_birth_year_source_ids",
            "algorithm_id": "test_name_and_birth_year"
        },
        {
            "input_topic": "test_name_and_strong_id_source_ids",
            "algorithm_id": "test_name_and_strong_id"
        },
        {
            "input_topic": "test_name_and_zipcode_source_ids",
            "algorithm_id": "test_name_and_zipcode"
        }
    ],
    "meta": {
        "...": "..."
    }
}

```

> Example: Retrieves a single MatchConfig by uuid or algorithm_id

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match_config/test_name_and_strong_id
```

```python
client.get("/identity/match_config/test_name_and_strong_id")
```

```csharp
client.request("/identity/match_config/test_name_and_strong_id", "GET")
```

```ruby
client.request("/identity/match_config/test_name_and_strong_id", "GET")
```

```java
client.get("/identity/match_config/test_name_and_strong_id")
```

```swift
let path = "/identity/match_config/test_name_and_strong_id"
try client.request(path: path, method: "GET")
```

> Example response showing a single MatchConfigs owned by a production app.

```json
{
    "data": {
        "_type": "IdentityMatchConfig",
        "insert_dt": "Fri Feb 10 02:11:01 2017",
        "update_dt": "Fri Feb 10 02:11:01 2017",
        "deleted": false,
        "_uuid": "2b1822c8-ef36-11e6-89b8-08002778b074",
        "input_topic": "test_name_and_strong_id_source_ids",
        "algorithm_id": "test_name_and_strong_id",
        "_id": "589d21350640fd45d593ae64",
        "owner_id": "9P10N4H2F7ZbaAU6RYct"
    },
    "meta": {
        "...": "..."
    }
}
```


> Example request to retrieve the _canonical_ identity (the representative identity for a set of matching source identity).

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match/algorithm_id/source/source_id/canonical
```

```python
client.get("/identity/match/algorithm_id/source/source_id/canonical")
```

```csharp
client.request("/identity/match/algorithm_id/source/source_id/canonical", "GET")
```

```ruby
client.request("/identity/match/algorithm_id/source/source_id/canonical", "GET")
```

```java
client.get("/identity/match/algorithm_id/source/source_id/canonical")
```

```swift
let path = "/identity/match/algorithm_id/source/source_id/canonical"
try client.request(path: path, method: "GET")
```

> Example response of a document representing the canonical identity 

```json
{
    "data": [
        {
            "data": {
                "first_name": "Siena",
                "last_name": "Hermann",
                "middle_name": "Madalynn",
                "phone": "1365465555",
                "prefix": "Ms",
                "ssn": "432900000",
                "address": {
                    "city": "Aileenshire",
                    "street2": "Apt. 108",
                    "postal_code": "36672",
                    "state_or_province": "ND",
                    "street1": "765 Osa Tunnel "
                },
                "birth_date": {
                    "month": 5,
                    "day": 13,
                    "year": 1988
                }
            },
            "last_updated": "2017-02-08T21:02:06Z",
            "record_id": "d92a6984-ee41-11e6-8973-82d1feccb5b2",
            "sources": [
                "d8fa22d8-ee41-11e6-9b4e-02cfa09edce7"
            ]
        }
    ],
    "meta": {
        "...": "..."
    }
}
```


```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match/algorithm_id/canonical_id
```

```python
client.get("/identity/match/algorithm_id/canonical_id")
```

```csharp
client.request("/identity/match/algorithm_id/canonical_id", "GET")
```

```ruby
client.request("/identity/match/algorithm_id/canonical_id", "GET")
```

```java
client.get("/identity/match/algorithm_id/canonical_id")
```

```swift
let path = "/identity/match/algorithm_id/canonical_id"
try client.request(path: path, method: "GET")
```

> Example response of a document representing the identity found at canonical_id

```json
{
    "data": {
        "record_id": "d92a6984-ee41-11e6-8973-82d1feccb5b2",
        "sources": [
            "d8fa22d8-ee41-11e6-9b4e-02cfa09edce7"
        ],
        "last_updated": "2017-02-08T21:02:06Z",
        "data": {
            "first_name": "Siena",
            "last_name": "Hermann",
            "middle_name": "Madalynn",
            "phone": "1365465555",
            "prefix": "Ms",
            "ssn": "432900000",
            "address": {
                "city": "Aileenshire",
                "street2": "Apt. 108",
                "postal_code": "36672",
                "state_or_province": "ND",
                "street1": "765 Osa Tunnel "
            },
            "birth_date": {
                "month": 5,
                "day": 13,
                "year": 1988
            },
            "email": "Siena.Hermann@hotmail.com"
        }
    },
    "meta": {
        "...": "..."
    }
}
```

> Example request of the source_id documents associated with a specified canonical_id document within the given MatchConfig, using a direct uuid lookups. The response will contain full documents, not just the source\_ids' uuids. If an array of uuids is desired then look no further than the `canonical_id.sources` attribute.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/identity/match/algorithm_id/canonical_id/sources"
```

```python
client.get("/identity/match/algorithm_id/canonical_id/sources")
```

```csharp
client.request("/identity/match/algorithm_id/canonical_id/sources", "GET")
```

```ruby
client.request("/identity/match/algorithm_id/canonical_id/sources", "GET")
```

```java
client.get("/identity/match/algorithm_id/canonical_id/sources")
```

```swift
let path = "/identity/match/algorithm_id/canonical_id/sources"
try client.request(path: path, method: "GET")
```

> Example response of a document representing the identity found at canonical_id

```json
{
    "data": [
        {
            "_source_id": "d8fa22d8-ee41-11e6-9b4e-02cfa09edce7",
            "data": {
                "first_name": "Siena",
                "last_name": "Hermann",
                "middle_name": "Madalynn",
                "phone": "1365465555",
                "prefix": "Ms",
                "ssn": "432900000",
                "address": {
                    "city": "Aileenshire",
                    "street2": "Apt. 108",
                    "postal_code": "36672",
                    "state_or_province": "ND",
                    "street1": "765 Osa Tunnel "
                },
                "birth_date": {
                    "month": 5,
                    "day": 13,
                    "year": 1988
                },
                "email": "Siena.Hermann@hotmail.com"
            }
        },
        {
            "_source_id": "0283885e-ef6b-11e6-8304-92b49a60ff89",
            "data": {"...": "..."}
        }, "...": "..."
    ],
    "meta": {
        "...": "..."
    }
}
```

The identity match is an identity validation service that serves to collect source identity documents (`source_ids`) into canonical identities (`canonical_ids`). Ideally, a `canonical_id` is a unique digital representation of an individual.

### Endpoint Descriptions

Users interact with the identity match system through an interface called a `match configuration`, which consists of a matching algorithm (designed and deployed by PokitDok) and an input topic, which defines a collection of identity documents that incoming requests will be written to. It's possible, and expected, for different `MatchConfigs` to share an input topic, as this allows the same raw data to be processed according to a variety of matching schemes in parallel.

<!--- beginning of table -->

| Endpoint                                    | HTTP Method | Description                                           |
|:--------------------------------------------|:------------|:------------------------------------------------------|
| /identity/match_config/                     | GET         | List all of the MatchConfigs                          |
| /identity/match_config/uuid_or_algorithm_id | GET         | Retrieve a single MatchConfig by uuid or algorithm_id |

<!--- end of table -->

The matching endpoints are how MatchConfig operations are exposed to the end user. Each matching endpoint starts with `/identity/match/<algorithm_id>`, designating which of MatchConfig will process the requests. Many of the match operations pass all of their parameters as part of the url; those that don't all accept a standardized document called an `IdentityMatchRequest`.

<!--- beginning of table -->

| Endpoint                                                | HTTP Method | Description                                                                                                                                        |
|:--------------------------------------------------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| /identity/match/algorithm_id/canonical_id               | GET         | Request for a specific canonical_id document from the MatchConfig specified by `<algorithm_id>`                                                    |
| /identity/match/algorithm_id/canonical_id/sources       | GET         | Requests the `source_id` documents associated with a specified `canonical_id` document within the given MatchConfig, using a direct `uuid` lookups |
| /identity/match/algorithm_id/source/source_id           | GET         | Retrieves a source id by uuid                                                                                                                      |
| /identity/match/algorithm_id/source/source_id/canonical | GET         | Retrieves the canonical\_ids which the source\_id has been associated with by the specified MatchConfig                                            |

<!--- end of table -->

### Parameters

Each `MatchConfig` endpoint accepts two fields:

<!--- beginning of table -->

| Parameter    | Type   | Description                                                                    | Unique | Required |
|:-------------|:-------|:-------------------------------------------------------------------------------|:-------|:---------|
| algorithm_id | string | The name of the PokitDok match algorithm to be applied.                        | Yes    | Yes      |
| input_topic  | string | The collection of identity data that the match algorithm should be applied to. | No     | Yes      |

<!--- end of table -->


### Response Payloads

The `source_id` endpoints are the `source_id` equivalents of the above `canonical_id` endpoints. The former retrieves a source id by `uuid`, and the latter retrieves the `canonical_id`s which the `source_id` has been associated with by the specified `MatchConfig`. It's worth mentioning that the `/<algorithm_id>/source/<source_id>/canonical [GET]` endpoint will return a list of documents, (usually just a single document), not just a list of `uuid`s.
