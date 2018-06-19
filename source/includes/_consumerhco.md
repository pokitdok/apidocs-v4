## HCO
> Example POST request:

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"
    -XPOST -d '{
        "birth_date": "1981-04-27",
        "address": {"address_lines": ["123 Main Street",
                                      "Apt A"],
                    "city": "Charleston",
                    "state": "SC",
                    "zipcode": "29412"},
        "patient_responsibility": 5900.00,
        "gender": "male",
        "race": "other",
        "has_diabetes": false,
        "has_hypertension": true,
        "has_high_cholesterol": false,
        "smoker": false,
        "bmi": 19.2,
        "activity_level": 3,
        "fico": 670,
        "debt_to_income_ratio": 0.21,
        "has_hsa": true,
        "async": false,
    }' https://platform.pokitdok.com/api/v4/hco/consumer/
```

```python
params = {
    'birth_date': '1981-04-27',
    'address': {'address_lines': ['123 Main Street',
                                  'Apt A'],
                'city': 'Charleston',
                'state': 'SC',
                'zipcode': '29412'},
    'patient_responsibility': 5900.00,
    'gender': 'male',
    'race': 'other',
    'has_diabetes': False,
    'has_hypertension': True,
    'has_high_cholesterol': False,
    'smoker': False,
    'bmi': 19.2,
    'activity_level': 3,
    'fico': 670,
    'debt_to_income_ratio': 0.21,
    'has_hsa': True,
    'async': False,
}
response = pd.post('/hco/consumer/', data=params)
```

```csharp
string endpoint = "/hco/consumer/";
string method = "POST";
List<string> address_lines = new List<string>;
address_lines.Add("123 MAIN ST");
address_lines.Add("Apt A");
Dictionary<string, object> address = new Dictionary<string, object> {
    {"address_lines": address_lines},
    {"city": "San Mateo"},
    {"state": "CA"},
    {"zipcode": "99401"}
    };
Dictionary<string, object> data = new Dictionary<string, object> {
    "birth_date": "1981-04-27",
    "address": address},
    "patient_responsibility": 5900.00,
    "gender": "male",
    "race": "other",
    "has_diabetes": false,
    "has_hypertension": true,
    "has_high_cholesterol": false,
    "smoker": false,
    "bmi": 19.2,
    "activity_level": 3,
    "fico": 670,
    "debt_to_income_ratio": 0.21,
    "has_hsa": true,
    "async": false,
}
client.request(endpoint, method, data);
```

```ruby
client.request('/hco/consumer/', method='post', params={
    birth_date: '1981-04-27',
    address: {'address_lines': ['123 Main Street',
                                  'Apt A'],
                'city': 'Charleston',
                'state': 'SC',
                'zipcode': '29412'},
    patient_responsibility: 5900.00,
    gender: 'male',
    race: 'other',
    has_diabetes: false,
    has_hypertension: true,
    has_high_cholesterol: false,
    smoker: false,
    bmi: 19.2,
    activity_level: 3,
    fico: 670,
    debt_to_income_ratio: 0.21,
    has_hsa: true,
    async: false,
}
```

```swift
let data = [
    "birth_date": "1981-04-27",
    "address": {"address_lines": ["123 Main Street",
                                  "Apt A"],
                "city": "Charleston",
                "state": "SC",
                "zipcode": "29412"},
    "patient_responsibility": 5900.00,
    "gender": "male",
    "race": "other",
    "has_diabetes": false,
    "has_hypertension": true,
    "has_high_cholesterol": false,
    "smoker": false,
    "bmi": 19.2,
    "activity_level": 3,
    "fico": 670,
    "debt_to_income_ratio": 0.21,
    "has_hsa": true,
    "async": false,
] as [String:any]
try client.request(path: "/hco/consumer/", method: "POST", params: data)
```

The Consumer HCO API allows user to calculate financial risk of health care transactions. The model measures the likelihood a patient will pay their share of the procedure cost. The result is a numerical score between 0.0 and 100.0 where higher score means the consumer has a higher likelihood of paying.

### Endpoint Description

Available Endpoints:

<!--- beginning of table -->

| Endpoint | HTTP Method | Description |
| :--- | :--- | :--- |
| /hco/consumer | POST | Measure the likelihood of an individual paying their share of the procedure cost. |
| /hco/consumer/batch | POST | A batch endpoint for /hco/consumer to send a batch of requests. |

<!--- end of table -->

### Parameters

The POST `/hco/consumer` endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter | Type | Description | Presence |
| :--- | :--- | :--- | :--- |
| address | {object } | Dictionary of consumer adddress information. | Required |
| address.address_lines | {list} | List of strings representing the street address (e.g. ["123 Main ST.", "Suite 4"]). | Optional |
| address.city | {string} | The consumer's city. | Optional |
| address.state | {string} | The state component of an address (e.g. 'CA'). | Optional |
| address.zipcode | {string } | The zip/postal code (e.g. "94401"). | Required |
| patient_responsibility | {decimal} | The amount the patient is expected to pay. | Required |
| age | {int} | Consumer's age in years. | Optional |
| gender | {string} | Options are 'male' or 'female'. | Optional |
| race | {string} | Options are 'asian', 'black', 'hispanic', 'other', 'white'. | Optional |
| has_diabetes | {boolean} | Whether the consumer has diabetes or not. | Optional |
| has_hypertension | {boolean} | Whether the consumer has hypertension or not. | Optional |
| has_high_cholestorol | {boolean} | Whether the consumer has high cholesterol or not. | Optional |
| smoker | {boolean} | Whether the consumer is a smoker or not. | Optional |
| activity_level | {int} | Average days per week the consumer is active for at least 60 minutes. | Optional |
| bmi | {decimal | The consumer's BMI. | Optional |
| fico | {int} | The consumer's FICO score. | Optional |
| debt_to_income_ratio | {decimal} | A ratio calculated using the consumer's total monthly debt payments on the total debt obligations, excluding mortgage and the patient responsibility, divided by the consumer's monthly income. | Optional |
| has_hsa | {boolean} | Whether or not the consumer has a health saving account. | Optional |

<!--- end of table -->

The POST `/hco/consumer/batch` endpoint accepts the following parameters:

<!--- beginning of table -->
| Parameter | Type | Description | Presence |
| :--- | :--- | :--- | :---|
| data | {list} | A list of requests to `/hco/consumer`. | Required |
| callback_url  | {string} | The URL to be invoked to notify the client application the activity has completed. HTTPS must be used for callback URLs. For added security, a callback URL can be defined in the application. | Required |

<!--- end of table -->

### Response

The `/hco/consumer` response contains the following fields:

<!--- beginning of table -->
| Field | Type | Description |
| :--- | :--- | :--- |
| hco_score | {decimal} | The consumer's HCO score between 0.0 and 100.0 |
| credible_interval_95_percent | {list} | List of decimals representing the upper and lower bounds of the 95% [credible interval](https://en.wikipedia.org/wiki/Credible_interval) for the HCO score. |

<!--- end of table -->

The `/hco/consumer/batch` response contains the following field:

<!--- beginning of table -->
| Field | Type | Description |
| :--- | :--- | :--- |
| id | {string} | ID of this Activity. |
| name | {string} | Activity name. |
| state | {string} | Current state of this activity. |
| transition_path | {list} | The list of state transitions to be used for this Activity. |
| history | {object} | History for this activity. |
| history.record_dt | {datetime} | The datetime associated with the history. In ISO8601 format (YYYY-MM-DDThh:mm:ss.ssssss). |
| history.name | {string} | State name associated with the history. |
| history.title | {string} | State title associated with the history. |

<!--- end of table -->

You may use the [Activity API](#activities) to check on the status of the batch activity.
