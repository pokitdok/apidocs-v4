# Security And Authorization

```shell
# define your client id and secret
CLIENT_ID=<YOUR_CLIENT_ID>
CLIENT_SECRET=<YOUR_CLIENT_SECRET>

# remove control characters if necessary (may occur with base64 on some OS platforms)
CREDENTIALS=$(echo "$CLIENT_ID":"$CLIENT_SECRET" | base64 | tr -d "[:cntrl:]")

# request an access token
curl -i -X POST -H "Authorization: Basic $CREDENTIALS" -d "grant_type=client_credentials" https://platform.pokitdok.com/oauth2/token; echo ""

# the response from https://platform.pokitdok.com/oauth2/token
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
    "access_token": "s8KYRJGTO0rWMy0zz1CCSCwsSesDyDlbNdZoRqVR",
    "token_type": "bearer",
    "expires_in": 3600
}

# save and use the access token in subsequent requests
ACCESS_TOKEN='s8KYRJGTO0rWMy0zz1CCSCwsSesDyDlbNdZoRqVR'
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/activities/5317f51527a27620f2ec7533
```

```python
# not using the PokitDok client library
from base64 import urlsafe_b64encode
import requests

client_id = 'your_client_id'
client_secret = 'your_client_secret'
access_token = requests.post('https://platform.pokitdok.com/oauth2/token',
                             headers={'Authorization': 'Basic ' + urlsafe_b64encode(client_id + ':' + client_secret)},
                             data={'grant_type': 'client_credentials'}).json()['access_token']

activity = requests.get('https://platform.pokitdok.com/api/v4/activities/5317f51527a27620f2ec7533',
                        headers={'Authorization': 'Bearer ' + access_token}).json()
```

```python
# using https://github.com/pokitdok/pokitdok-python
import pokitdok

client = pokitdok.api.connect('your_client_id', 'your_client_secret')
activity = client.activities('5317f51527a27620f2ec7533')
```

```ruby
# using https://github.com/pokitdok/pokitdok-ruby
require 'pokitdok'
client = PokitDok::PokitDok.new("your_client_id", "your_client_secret")
```

```csharp
// using https://github.com/pokitdok/pokitdok-csharp
using pokitdokcsharp;

PlatformClient client = new PlatformClient("your_client_id", "your_client_secret");
```

```java
// using https://github.com/pokitdok/pokitdok-java
import com.pokitdok.PokitDok;

PokitDok client = new PokitDok("your_client_id", "your_client_secret");
client.connect();
```

```swift
// using https://github.com/pokitdok/pokitdok-swift
import pokitdok

// Using an access token
let client = try Pokitdok(token: "your-access-token")

// Using client id and client secret
let client = try Pokitdok(clientId: "your_client_id", clientSecret: "your_client_secret")

/*
It is highly recommended that you do not release an iOS app with your Client ID and Client Secret
values baked into the app, as they may be vulnerable to exposure there. A suitable alternative
would be to utilize an external identity service that authenticates your users and requests
an access token that can then be returned to your app to utilize.
*/
```

**Security via TLS**

All calls to PokitDok's APIs are encrypted over HTTPS. Our APIs support connections using
TLS version 1.2 or higher. All modern languages and frameworks support TLS 1.2 (although
[specific older ones](https://fullmetalhealth.com/ssl-upgrade-notice/) do not).


**Authorization via OAuth2**

Access to our APIs is controlled via [OAuth2](https://tools.ietf.org/html/rfc6749) using the
[client credentials](https://tools.ietf.org/html/rfc6749#section-1.3.4) grant. This is a secure
authorization workflow that allows you to obtain a short-lived (1 hour) `access token` that must
be transmitted with your API request.

In the cURL tab to the right you can see an example of obtaining an `access token` via the
command line, then making a call to the Activities API with that token. Likewise, the Python tab
contains an example of authorization from scratch using the popular `requests` library. While
these examples illustrate the typical process of obtaining an `access token` and then properly
utilizing that token in an `Authorization` header for subsequent API requests, be aware that it is
extremely inefficient to request a new token if you already obtained one that is still valid (note
the number of seconds specified in the `expires_in` parameter in the cURL example's response). For
this reason we recommend using a PokitDok [client library](#client-libraries), giving you the
ability to instantiate and use a long-lived PokitDok client connection that provides automatic
handling of token retrieval, expiration, and rotation.

The 2nd example in the Python tab illustrates how much easier it can be to use our client
libraries -- you just pass in your Client ID and Client Secret and the library does the rest.

The Swift tab contains an example of authentication by entering a Client ID and Client Secret,
as well as an example of authentication using only an access token. This is because it is highly
recommended that you do not release an iOS app with your Client ID and Client Secret values
baked into the app, as they may be vulnerable to exposure there. A suitable alternative would be
to utilize an external identity service that authenticates your users and requests an access token
that can then be returned to your app to utilize.
