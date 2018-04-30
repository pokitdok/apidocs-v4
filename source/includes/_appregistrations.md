## App Registrations
> Example POST request:

```shell
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json"
    -XPOST -d '{
        "trading_partner_id": "MOCKPAYER",
        "trading_partner_set_name": "eligibility,
        "tax_id": ["123456789"],
        "npi": "1234567893"
    }' https://platform.pokitdok.com/api/v4/appregistrations
```


```python
params = {
    'trading_partner_id': 'MOCKPAYER',
    'transaction_set_name': 'eligibility',
    'tax_id': ['123456789'],
    'npi': '1234567893'
}

response = pd.post('/appregistrations/', data=params)
```

```csharp
string endpoint = "/appregistrations/";
string method - "POST";
List<string> tax_id = new List<string>
tax_id.Add("123456789")
Dictionary<string, object> data = new Dictionary<string, object> {
    {"trading_partner_id", "MOCKPAYER"},
    {"transaction_set_name", "eligibility" },
    {"tax_id", tax_id},
    {"npi", "1234567893" }
    };
client.request(endpoint, method, data);
```

```ruby
client.request('/appregistrations/', method='post', params={
    trading_partner_id: "MOCKPAYER",
    transaction_set_name: "eligibility",
    tax_id: ["123456789"],
    npi: "1234567893"
})
```

```swift
let data = [
    "trading_partner_id": "MOCKPAYER",
    "transaction_set_name": "eligibility",
    "tax_id": ["123456789"],
    "npi": "1234567893"
] as [String:any]
try client.request(path: "/appregistrations", method: "POST", params: data)
```

> Example response:

```json
{
    "data": {
        "_uuid": "2f201868-47f4-11e8-a91a-0242ac12000a",
        "app_name": "<app_name>",
        "client_id": "<client_id>",
        "npi": "1234567893",
        "tax_id": ["123456789"],
        "trading_partner_id": "MOCKPAYER",
        "transaction_set_name": "eligibility"
    },
    "meta": {
        "...": "..."
    }
}
```

The App Regisrations endpoint allows users to to manage their app registrations. These endpoints can be used to create, edit, and delete app registrations.

### Endpoint Description

Available Endpoints:

<!--- beginning of table -->
| Endpoint | HTTP Method | Description |
|:---|:---|:---|
| /appregistrations | GET | List current app registrations. |
| /appregistrations/{uuid} | GET | Retrieve the app registration with the given UUID. |
| /appregistrations | POST | Create an app registration. |
| /appregistrations/csv | POST | Create app registrations based on the CSV file. |
| /appregistrations/{uuid} | PUT | Edit the app registration with the given UUID. |
| /appregistrations/{uuid} | DELETE | Delete the app registration with the given UUID. |
| /appregistrations/{uuid}/undelete | POST |Undelete the app registration with the given UUID |

<!--- end of table -->

### Parameters

The POST `/appregistrations/` and PUT `/appregistrations/` endpoints accept the following parameters:

<!--- beginning of table -->

| Parameter | Type | Description | Presence |
|:---|:---|:---|:--- |
|trading_partner_id| {string} | Unique ID for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.| Required |
| transaction_set_name | {string} | Transaction this app registration is to be used for (e.g. 'eligibility' or 'claims'). | Required |
| tax_id | {list} | List of  federal tax ids for the provider. For individual providers, this may be the tax id of the medical practice or organization where a provider works. | Required |
| npi | {string} | The provider's NPI. | Required |

<!--- end of table -->

### Response

The `/appregistrations/` response contains the following fields:

<!--- beginning of table -->
| Field | Type | Description |
|:---|:---|:---|
| _uuid | {string} | The unique ID for this app registration.|
| app_name | {string} | The name of the app associated to the app registration. |
| client_id | {string} | The client ID of the app associated to the app registration. |
|trading_partner_id| {string} | Unique ID for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.|
| transaction_set_name | {string} | Transaction this app registration is to be used for (e.g. 'eligibility' or 'claims'). |
| tax_id | {list} | List of  federal tax ids for the provider. For individual providers, this may be the tax id of the medical practice or organization where a provider works. |
| npi | {string} | The provider's NPI. |
