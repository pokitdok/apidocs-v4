## Identity Proof

> Example: How to start a new KBA request.

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"
 -XPOST -d '{
       "first_name": "Oscar",
       "middle_name": "Harold",
       "last_name": "Whitmire",
       "ssn": "123456789",
       "birth_date": {
           "year": 1989,
           "month": 12,
           "day": 07
           },
       "email": "oscar@pokitdok.com",
       "phone": "555-555-5555",
       "address" : {
            "street1" : "1400 Anyhoo Avenue",
            "street2" : "Apt 15"
            "city" : "Springfield",
            "state_or_province" : "IL",
            "postal_code" : "90210",
            "country_code" : "US"
        }
    }' https://platform.pokitdok.com/api/v4/identity/proof/questions/generate/
```

```python
client.request('/identity/proof/questions/generate/', method='post', data={
       "first_name": "Oscar",
       "middle_name": "Harold",
       "last_name": "Whitmire",
       "ssn": "123456789",
       "birth_date": {
           "year": 1989,
           "month": 12,
           "day": 07
           },
       "email": "oscar@pokitdok.com",
       "phone": "555-555-5555",
       "address" : {
            "street1" : "1400 Anyhoo Avenue",
            "street2" : "Apt 15"
            "city" : "Springfield",
            "state_or_province" : "IL",
            "postal_code" : "90210",
            "country_code" : "US"
        }
    })
```

```csharp
string endpoint = "/identity/proof/questions/generate/";
string method = "POST";
Dictionary<string, object> data = new Dictionary<string, object> {
       {"first_name", new string[] { "Oscar" },
       {"middle_name", new string[] { "Harold" },
       {"last_name", new string[] { "Whitmire" },
       {"ssn", new string[] { "123456789" },
       {"birth_date", new Dictionary<string, int>{
            {"year": 1989},
            {"month": 12},
            {"day": 07}
                }},
       {"email", new string[] { "oscar@pokitdok.com" },
       {"phone", new string[] { "555-555-5555" },
       {"address", new Dictionary<string, string>{
            {"street1": "1400 Anyhoo Avenue"},
            {"street2": "Apt 15"},
            {"city": "Springfield"},
            {"state_or_province": "IL"},
            {"postal_code": "90210"},
            {"country_code": "US"}
                }}
    };
client.request(endpoint, method, data);
```

```ruby
client.request('/identity/proof/questions/generate/', method='post', params={
       first_name: "Oscar",
       middle_name: "Harold",
       last_name: "Whitmire",
       ssn: "123456789",
       birth_date: {
           year: 1989,
           month: 12,
           day: 07
           },
       email: "oscar@pokitdok.com",
       phone: "555-555-5555",
       address: {
            street1: "1400 Anyhoo Avenue",
            street2: "Apt 15"
            city: "Springfield",
            state_or_province: "IL",
            postal_code: "90210",
            country_code: "US"
        }
    })
```

```java
```

```swift
let data = [
   "first_name": "Oscar",
   "middle_name": "Harold",
   "last_name": "Whitmire",
   "ssn": "123456789",
   "birth_date": [
        "year": 1989,
        "month": 12,
        "day": 07
   ],
   "email": "oscar@pokitdok.com",
   "phone": "555-555-5555",
   "address" : [
        "street1" : "1400 Anyhoo Avenue",
        "street2" : "Apt 15",
        "city" : "Springfield",
        "state_or_province" : "IL",
        "postal_code" : "90210",
        "country_code" : "US"
   ]
] as [String:Any]
try client.request(path: "/identity/proof/questions/generate/", method: "POST", params: data)
```
> Example: Submitting a user response.

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"
 -XPOST -d '{
        "questionnaire_id": "a9ec1381-5ad6-499b-a3a6-644ece186363",
        "question_id": 1,
        "answer": 2
    }' https://platform.pokitdok.com/api/v4/identity/proof/questions/score/
```

```python
client.request('/identity/proof/questions/score/', method='post', data={
        "questionnaire_id": "a9ec1381-5ad6-499b-a3a6-644ece186363",
        "question_id": 1,
        "answer": 2
    })
```

```csharp
string endpoint = "/identity/proof/questions/score/";
string method = "POST";
Dictionary<string, object> data = new Dictionary<string, object> {
       {"questionnaire_id", new string[] { "a9ec1381-5ad6-499b-a3a6-644ece186363" },
       {"question_id", new int[] { 1 },
       {"answer", new int[] { 2 }
    };
client.request(endpoint, method, data);
```

```ruby
client.request('/identity/proof/questions/score/', method='post', params={
       questionnaire_id: "a9ec1381-5ad6-499b-a3a6-644ece186363",
       question_id: 1,
       answer: 2
    })
```

```java
```

```swift
let data = [
    "questionnaire_id": "a9ec1381-5ad6-499b-a3a6-644ece186363",
    "question_id": 1,
    "answer": 2
] as [String:Any]
try client.request(path: "/identity/proof/questions/score/", method: "POST", params: data)
```

> VALID response data:

```
{
	"is_verifiable": false,
	"is_valid": true
}
```
> INVALID response data:

```
{
	"is_verifiable": false,
	"is_valid": false
}
```

> OK response data:

```
{
	"is_verifiable": true,
	"is_valid": true,
	"question": {"answers": [{"answer": "49557", "id": 1},
                             {"answer": "49511", "id": 2},
                             {"answer": "49728", "id": 3},
                             {"answer": "49230", "id": 4},
                             {"answer": "None Of The Above", "id": 5}],
                "id": 1,
                "text": "Which one of the following zip codes is associated with you?"}
}
```

PokitDok's Identity Proof API allows providers to validate and verify patient provided information against identity
records maintained by government agencies, credit bureaus, and insurance companies.

Validation is the process of determining whether an identity matching the request is present in our system. By
validating patient information, providers can prevent erroneous records from being created due to data entry mistakes.

Verification is the process of determining whether the given identity belongs to the customer who made the request;
ensuring that the patient is who they say they are. To accomplish this, our Identity Proof API produces security
questions for the patient to answer in order to prove their authenticity in a process called KBA (Knowledge Based
Authentication). When used during account creation, or password recovery, KBA ensures that patients' privacy is
protected while still allowing them convenient access to their own healthcare information.

### Endpoint Description

<!--- beginning of table -->

| Endpoint                            | HTTP Method | Description                                             |
|-------------------------------------|-------------|---------------------------------------------------------|
| /identity/proof/questions/generate/ | POST        | Generates a new KBA questionnaire.                      |
| /identity/proof/questions/score/    | POST        | Scores the patient's response to a KBA question.        |
| /identity/proof/valid/              | POST        | Validate's the identity fields provided by the patient. |
| /identity/proof/report              | GET         | Generate report on prior KBA questionnaire activities. |


<!--- end of table -->

### Parameters

The `/identity/proof/questions/generate/` and `/identity/proof/valid/` endpoints both accept the same Identity Proof
Request (IPR) json document defined below.

<!--- beginning of table -->

| Parameter                 | Type     | Description                                                                       | Required |
|---------------------------|----------|-----------------------------------------------------------------------------------|----------|
| first_name                | {string} | Person's legal first name.                                                        | Yes      |
| middle_name               | {string} | Person's legal middle name.                                                       | No       |
| last_name                 | {string} | Person's legal surname.                                                           | Yes      |
| ssn                       | {string} | Person's social security number. (Full or last 4 digits)                          | Depends  |
| drivers_license_number    | {string} | Person's driver's license number.                                                 | Depends  |
| birth_date.year           | {string} | The year the person was born. (ISO 4-digit form, e.g. 1987)                       | Yes      |
| birth_date.month          | {string} | The month the person was born. (Unpadded numeric form, e.g. 1)                    | Yes      |
| birth_date.day            | {string} | The day of the month the person was born (Unpadded numeric form, e.g. 1)          | Yes      |
| address.street1           | {string} | The first line of the person's street address.                                    | No       |
| address.street2           | {string} | The second line of the person's street address.                                   | No       |
| address.city              | {string} | The city/town of the person's street address.                                     | No       |
| address.state_or_province | {string} | The two-letter state abbreviation code of the person's street address. (e.g. SC)  | No       |
| address.postal_code       | {string} | The zip or postal code of the person's address. (e.g. 29414)                      | No       |
| address.country_code      | {string} | The country code of the person's address. (e.g. US)                               | No       |
| phone_number              | {string} | The person's phone number.                                                        | No       |
| email                     | {string} | The person's email address.                                                       | No       |
| ip_address                | {string} | The ip address the person is using to connect to the provider system.             | No       |

<!--- end of table -->

One of ssn or drivers_license_number is required. If using drivers_license_number then ideally address fields are 
also provided but not required.

It is worth noting that validation will always be run as part of verification, so providers do not need to hit the
`/identity/proof/valid/` endpoint prior to a `/identity/proof/questions/generate/` call.

The `/identity/proof/questions/score` endpoint handles the scoring of the questionnaires generated by the
`/identity/proof/questions/generate` endpoint. Requests submitted to `/identity/proof/questions/score` should have
the following parameters:

<!--- beginning of table -->

| Parameter        | Type     | Description                                    |
|------------------|----------|------------------------------------------------|
| questionnaire_id | {string} | The KBA Questionnaire's uuid.                  |
| question_id      | {string} | The question id.                               |
| answer           | {string} | The answer_id of the choice the user selected. |

<!--- end of table -->

The `/identity/proof/report` endpoint generates reports on prior KBA questionnaire activities, with a record for each call to `/identity/proof/questions/generate` and the subsequent calls to `/identity/proof/questions/score`.
If no parameters are given to `/identity/proof/report` it will return a JSON-formatted report for all questionnaires that were initiated in the previous 24 hours.
CSV-formatted reports are also available, but the JSON report includes more details about the activities that comprise questionnaires.
The endpoint accepts the following `GET` request parameters:


<!--- end of table -->

| Parameter       |  Type     |  Description
|-----------------|-------------|------------------------------------------------|
|start_dt          |  {datetime} |  ISO8601 date or datetime string for the start of a time-range report; defaults to (end_dt - 24hrs).|
|end_dt            |  {datetime} |  ISO8601 date or datetime string for the end of a time-range report; defaults to now.|
|questionnaire_id  |  {string}   |  Generate report for a specific questionnaire_id; start_dt and end_dt are ignored.|
|activity_id       |  {string}   |  Generate report for a specific questionnaire involving the activity_id (where the activity_id was assigned to any `generate` or `score` call); `start_dt` and `end_dt` are ignored.|
|csv               |  {boolean}  |  Generate a CSV-formatted response instead of JSON; defaults to false.|

<!--- end of table -->

### Response


The `/identity/proof/questions/generate/` endpoint can return several types of responses. Only a VERIFIABLE response will include the first
question of a KBA questionnaire; allowing the patient to begin the KBA process. To protect the integrity of the KBA
process, KBA questionnaires expire after 25 minutes. Additionally, identities will be locked for 12 hours following
the creation of a KBA questionnaire in order to guard against brute force attacks.

<!--- beginning of table -->

| Type | Code | Reason |
| :--- | :---: | --- |
| BAD REQUEST | 400 | Required fields were missing or invalid.
| FORBIDDEN | 403 | The requested Identity has been temporarily locked following successful questionnaire generation, or following the detection of suspicious activity.
| INVALID | 200 | The request was valid, but an identity matching the request could not be found.
| VALID | 200 | The request was valid, and a matching identity was found, but there was insufficient data with which to generate questions.
| VERIFIABLE | 200 | questionnaire was successfully generated.

<!--- end of table -->


Provided the request parameters were valid, the `/identity/proof/questions/score` endpoint will produce one of three
types of response:


The `/identity/proof/report` endpoint can return a JSON or CSV report.
The JSON report will have richer data concerning the individual activities that comprise KBA questionnaires, including the `activity_id`, timestamp and response status code for each.
The CSV report lacks those complete details but does return the `activity_id` and status code for the originating call to `/identity/proof/questions/generate`.

The JSON report is a list of objects, one for each KBA questionnaire covered. The following fields may be present in each object:

|Field                |  Type       |  Description |
|---------------------|-------------|--------------|
| start_dt             |  {datetime} |  Timestamp questionnaire was initiated.|
| end_dt               |  {datetime} |  Timestamp questionnaire was completed; not present if questionnaire was not completed.|
| questionnaire_id     |  {string}   |  Questionnaire's ID.|
| verification_result  |  {string}   |  Verification result, if questionnaire was completed (`SUCCESS` or `FAILURE`).|
| activities           |  {list}     |  List of metadata objects for each activity comprising the questionnaire, including `activity_id`, `timestamp`, and `status_code`.|
| id_fields            |  {list}     |  List of identity field names (not the values) supplied to the initial `generate` call.|
| is_valid             |  {boolean}  |  Whether the supplied identity is valid.|.|
| is_verifiable        |  {boolean}  |  Whether the supplied is verifiable.|
| n_questions          |  {int}      |  Number of questions asked.|


The CSV report includes a header line followed by a line for each questionnaire covered.
The CSV report is still encapsulated by a JSON response payload, but the `data` field contains the CSV string rather than a list of objects, as with the JSON report.
The following fields are returned for each CSV row:

| Field                |  Type       |  Description |
|---------------------|--------------|-----------|
| start_dt             |  {datetime} |  Timestamp questionnaire was initiated.|
| end_dt               |  {datetime} |  Timestamp questionnaire was completed; empty if questionnaire was not completed.|
| questionnaire_id     |  {string}   |  Questionnaire's ID.|
| verification_result  |  {string}   |  Verification result, if questionnaire was completed (`SUCCESS` or `FAILURE`).|
| generate_activity_id |  {string}   |  `activity_id` for the initial `generate` call.|
| generate_status      |  {int}      |  Response status code for the initial `generate` call.|
| id_fields            |  {string}   |  Comma-delimited list of identity field names (not the values) supplied to the initial generate call.|
| is_valid             |  {boolean}  |  Whether the supplied identity is valid.|
| is_verifiable        |  {boolean}  |  Whether the supplied is verifiable.|
| n_questions          |  {int}      |  Number of questions asked.|



#### Failure

> Failure

```
{
	"status": "FAILURE",
	"next_attempt": "2016-10-14T21:06:43.292695",
	"customer_notified": false
}
```

In this case the customer has answered enough questions inaccurately that we're confident that the user is
interacting with an imposter, and not the customer. To protect the customer's identity we refuse to generate
questions for that identity for 12 hours. To reflect this we include the `next_attempt` parameter; the datetime after
which the identity in question will again be serviced by the API. Finally, we include a boolean value,
`customer_notified` reflecting whether or not the customer has been notified of this KBA attempt.

#### Success

> Success

```
{
	"status": "SUCCESS",
	"customer_notified": false
}
```

In this case the customer has answered enough questions correctly that we're confident that they are who they say
they are.

#### PENDING

> Pending

```
{
	"status": "PENDING",
	"question": {"answers": [{"answer": "49557", "id": 1},
                             {"answer": "49511", "id": 2},
                             {"answer": "49728", "id": 3},
                             {"answer": "49230", "id": 4},
                             {"answer": "None Of The Above", "id": 5}],
                "id": 2,
                "text": "Which one of the following zip codes is associated with you?"}
}
```

In this case the scoring of the question did not grant us enough information to pass or fail the customer. Instead,
we return the next question associated with that questionnaire.
