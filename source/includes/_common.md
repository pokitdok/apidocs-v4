# Common To All Endpoints

## Client generic request handlers
To guarantee clients have reliable access to the newest PokitDok endpoints,
a generic request handler is built into most clients. This allows for the sending
of files and JSON payloads to any PokitDok endpoint for any given CRUD operation.

> Example calls using the generic request handler


```csharp
client.request("/eligibility/", "POST", ExampleRequests.EligibilityRequest);
```

```csharp
client.request("/identity/4d04d8dc-3d0b-4ea1-8add-4dbc9619e1ae", "PUT", ExampleRequests.CreateIdentityRequest);
```

> Example call sending a file using the generic request handler

```csharp
 client.request(
            "/enrollment/snapshot",
            "../../tests/files/acme_inc_add_subscriber.834",
            "file",
            "application/EDI-X12",
            postData
            );
```

## Collection Parameters
The below query parameters can be added to collection requests from endpoints
to limit and page through the returned list of results. Singular endpoint
(/endpoint/{id}) requests do not accept these parameters.

Argument | Description
-------- | -----------
async | Whether the API call is asynchronous.  For endpoints that offer both synchronous and asynchronous operation, a boolean can be used for this parameter to specify which mode of operation you desire; if the async parameter is omitted, the synchronous mode will be used. For POST requests, the async parameter should be included along with other JSON data being POSTed. When async is true, the API client has the option of including a callback URL so that it can be notified when the asynchronous processing is complete.
application_data | API client applications may include custom application data in requests to help support scenarios where an application is unable to store the activity id and wishes to include application specific data in their API requests so that the information will be stored on the request's activity and returned to the application in asynchronous callbacks. This can be useful for scenarios where you want to directly associate a PokitDok Platform API request with some identifier(s) in your system so that you can do direct lookups to associate responses with the appropriate information. For example, suppose you wish to fire off a number of eligibility or claims requests and want to include some identifiers specific to your application. By including the identifier(s) you need in the request's application_data section, you can easily do direct lookups using those identifiers when you receive the API response.
limit | The number of objects to return in a list (only for collection requests)
offset | The number of objects to skip when paging through a list (only for collection requests)

## The Meta and Data Sections
The response payload for all endpoints consists of a meta key and a data key.
The meta key contains information regarding rate limiting, linked urls for
convenient paging of lists, record counts, response time and API billing
information. The data key contains either a an object, in the case of singular
endpoints, or an array of objects, in the case of collection or search
endpoints.

The following is a list of values that are contained in the meta block, along
with their types. Credit and rate limiting information is only included in the
meta information for APIs that are billable and/or rate limited. Processing
time is always included in the meta information.

Key | Type | Description
--- | ---- | -----------
activity_id | {uuid} | The id of the activity used to process the API request.
application_mode | {string} | Indicates if the application is configured for test or production use.
credits_billed | {int} | The amount of credits billed for this request
credits_remaining | {int} | The amount of credits remaining on your API account
next | {int} | A url pointing to the next page of results
previous | {int} | A url pointing to the previous page of results
processing_time | {int} | The time to process the request in milliseconds
rate_limit_amount | {int} | The amount of requests made during the current rate limit period
rate_limit_cap | {int} | The amount of requests available per hour
rate_limit_reset | {int} | The time (Unix Timestamp) when the rate limit amount resets

## Errors
> Unauthorized access

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN"
https://platform.pokitdok.com/api/v4/activities/5317f51527a27620f2ec7533
HTTP/1.1 401 UNAUTHORIZED
Server: nginx
Date: Thu, 06 Mar 2014 16:44:07 GMT
Content-Type: application/json
Content-Length: 31
{
    "message": "Unauthorized"
}
```

```python
See cURL example.
```

```ruby
See cURL example.
```

```javascript
See cURL example.
```

```csharp
See cURL example.
```

```java
See cURL example.
```

```haskell
See cURL example.
```

```lua
See cURL example.
```

> Insufficient credits

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/providers/?limit=20
HTTP/1.0 402 PAYMENT REQUIRED
Server: nginx
Date: Tue, 25 Feb 2014 16:15:31 GMT
Content-Type: application/json
Content-Length: 35
{
    "message": "Payment Required"
}
```

```python
See cURL example.
```

```ruby
See cURL example.
```

```javascript
See cURL example.
```

```csharp
See cURL example.
```

```java
See cURL example.
```

```haskell
See cURL example.
```

```lua
See cURL example.
```

> Rate limit exceeded

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN"
https://platform.pokitdok.com/api/v4/activities/5317f51527a27620f2ec7533
HTTP/1.0 403 FORBIDDEN
Server: nginx
Date: Tue, 25 Feb 2014 16:04:50 GMT
Content-Type: application/json
Content-Length: 28
{
    "message": "Forbidden"
}
```

```python
See cURL example.
```

```ruby
See cURL example.
```

```javascript
See cURL example.
```

```csharp
See cURL example.
```

```java
See cURL example.
```

```haskell
See cURL example.
```

```lua
See cURL example.
```

> Required information missing or invalid

```shell
curl -i -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS_TOKEN" -d "{}"
https://platform.pokitdok.com/api/v4/eligibility/
HTTP/1.1 422 UNPROCESSABLE ENTITY
Server: nginx
Date: Thu, 06 Mar 2014 19:50:17 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 510
Connection: keep-alive
mimetype: application/json
charset: utf-8
{
    "meta": {
        "activity_id": "53d9506356c02c67c4070096",
        "application_mode": "production",
        "credits_billed": 1,
        "credits_remaining": 995,
        "processing_time": 3,
        "rate_limit_amount": 2,
        "rate_limit_cap": 1000,
        "rate_limit_reset": 1394138991
    },
    "data": {
        "errors": {
            "validation": {
                "member": [
                    "This field is required."
                ],
                "provider": [
                    "This field is required."
                ],
                "trading_partner_id": [
                    "This field is required."
                ]
            }
        }
    }
}
```

```python
See cURL example.
```

```ruby
See cURL example.
```

```javascript
See cURL example.
```

```csharp
See cURL example.
```

```java
See cURL example.
```

```haskell
See cURL example.
```

```lua
See cURL example.
```

Error information may be returned to an API client. Common error scenarios
include:

* the data that was provided is invalid
* required information is missing
* rate limits have been exceeded
* an API access token is not valid or no longer valid
* insufficient credits are available for billable endpoints

Some examples of these are included to the right.

### Unauthorized access
This may be encountered when an invalid or no longer valid access token is
supplied. Access tokens expire one hour after being acquired. Applications
should handle 401s properly and request a new access token when this is
encountered.

### Insufficient credits
This may be encountered when credits are not available to an application for
a billable endpoint requested in the API call. If this is encountered, the
application owner will need to load more credits on their application or change
their billing tier.

### Rate limit exceeded
This may be encountered when too many API calls are made within a period of
time for a rate limited endpoint. Rate limits are currently enforced on an
hourly basis. If your application receives a 403, you can wait for the rate
limit period to renew and then make the API call again.

### Required information missing or invalid
You may encounter errors like this when required information is omitted from an
API call. Simply supply the appropriate information on the next API call to resolve.

>