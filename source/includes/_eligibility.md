## Eligibility
> Example eligibility request to determine general health benefit coverage using the `primary_search_option`:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/eligibility/
```

```python
client.eligibility({
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
 client.eligibility (
			new Dictionary<string, object> {
			 	{"member", new Dictionary<string, object> {
					{"id", "W000000000"},
					{"birth_date", "1970-01-25"},
					{"first_name", "Jane"},
					{"last_name", "Doe"}
					}},
				{"provider", new Dictionary<string, object> {
					{"npi", "1234567893"},
					{"last_name", "BLACKWELL"},
					{"first_name", "ELIZABETH"}
					}},
				{"service_types", new string[] { "health_benefit_plan_coverage" }},
				{"trading_partner_id", "MOCKPAYER"}
		});
```

```ruby
client.eligibility({
    member: {
        birth_date: "1970-01-25",
        first_name: "Jane",
        last_name: "Doe",
        id: "W000000000"
    },
    provider: {
        first_name: "ELIZABETH",
        last_name: "BLACKWELL",
        npi: "1234567893"
    },
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"member\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"id\": \"W000000000\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"ELIZABETH\",");
buf.append("        \"last_name\": \"BLACKWELL\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.eligibility(query);
```

```swift
let data = [
    "member": [
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    ],
    "provider": [
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    ],
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.eligibility(params: data)
```

> Example eligibility request to determine general health benefit coverage using the `no_first_name_search` search option:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "member": {
        "birth_date": "1970-01-25",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/eligibility/
```

```python
client.eligibility({
    "member": {
        "birth_date": "1970-01-25",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
 client.eligibility (
			new Dictionary<string, object> {
			 	{"member", new Dictionary<string, object> {
					{"id", "W000000000"},
					{"birth_date", "1970-01-25"},
					{"last_name", "Doe"}
					}},
				{"provider", new Dictionary<string, object> {
					{"npi", "1234567893"},
					{"last_name", "BLACKWELL"},
					{"first_name", "ELIZABETH"}
					}},
				{"service_types", new string[] { "health_benefit_plan_coverage" }},
				{"trading_partner_id", "MOCKPAYER"}
		});
```

```ruby
client.eligibility({
    member: {
        birth_date: "1970-01-25",
        last_name: "Doe",
        id: "W000000000"
    },
    provider: {
        first_name: "ELIZABETH",
        last_name: "BLACKWELL",
        npi: "1234567893"
    },
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"member\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"id\": \"W000000000\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"ELIZABETH\",");
buf.append("        \"last_name\": \"BLACKWELL\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.eligibility(query);
```

```swift
let data = [
    "member": [
        "birth_date": "1970-01-25",
        "last_name": "Doe",
        "id": "W000000000"
    ],
    "provider": [
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    ],
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.eligibility(params: data)
```

> Example eligibility request to determine general health benefit coverage using the `no_birth_date_search` search option:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "member": {
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/eligibility/
```

```python
client.eligibility({
    "member": {
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
 client.eligibility (
			new Dictionary<string, object> {
			 	{"member", new Dictionary<string, object> {
					{"id", "W000000000"},
					{"first_name", "Jane"},
					{"last_name", "Doe"}
					}},
				{"provider", new Dictionary<string, object> {
					{"npi", "1234567893"},
					{"last_name", "BLACKWELL"},
					{"first_name", "ELIZABETH"}
					}},
				{"service_types", new string[] { "health_benefit_plan_coverage" }},
				{"trading_partner_id", "MOCKPAYER"}
		});
```

```ruby
client.eligibility({
    member: {
        first_name: "Jane",
        last_name: "Doe",
        id: "W000000000"
    },
    provider: {
        first_name: "ELIZABETH",
        last_name: "BLACKWELL",
        npi: "1234567893"
    },
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"member\": {");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"id\": \"W000000000\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"ELIZABETH\",");
buf.append("        \"last_name\": \"BLACKWELL\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.eligibility(query);
```

```swift
let data = [
    "member": [
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    ],
    "provider": [
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    ],
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.eligibility(params: data)
```

> Example eligibility request to determine general health benefit coverage using the `no_name_search` search option:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "member": {
        "birth_date": "1970-01-25",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/eligibility/
```

```python
client.eligibility({
    "member": {
        "birth_date": "1970-01-25",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
 client.eligibility (
			new Dictionary<string, object> {
			 	{"member", new Dictionary<string, object> {
					{"id", "W000000000"},
					{"birth_date", "1970-01-25"}
					}},
				{"provider", new Dictionary<string, object> {
					{"npi", "1234567893"},
					{"last_name", "BLACKWELL"},
					{"first_name", "ELIZABETH"}
					}},
				{"service_types", new string[] { "health_benefit_plan_coverage" }},
				{"trading_partner_id", "MOCKPAYER"}
		});
```

```ruby
client.eligibility({
    member: {
        birth_date: "1970-01-25",
        id: "W000000000"
    },
    provider: {
        first_name: "ELIZABETH",
        last_name: "BLACKWELL",
        npi: "1234567893"
    },
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"member\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"id\": \"W000000000\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"ELIZABETH\",");
buf.append("        \"last_name\": \"BLACKWELL\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.eligibility(query);
```

```swift
let data = [
    "member": [
        "birth_date": "1970-01-25",
        "id": "W000000000"
    ],
    "provider": [
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    ],
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.eligibility(params: data)
```

> Example eligibility request to determine general health benefit coverage using the `no_id_search` search option:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/eligibility/
```

```python
client.eligibility({
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
 client.eligibility (
			new Dictionary<string, object> {
			 	{"member", new Dictionary<string, object> {
					{"birth_date", "1970-01-25"},
					{"first_name", "Jane"},
					{"last_name", "Doe"}
					}},
				{"provider", new Dictionary<string, object> {
					{"npi", "1234567893"},
					{"last_name", "BLACKWELL"},
					{"first_name", "ELIZABETH"}
					}},
				{"service_types", new string[] { "health_benefit_plan_coverage" }},
				{"trading_partner_id", "MOCKPAYER"}
		});
```

```ruby
client.eligibility({
    member: {
        birth_date: "1970-01-25",
        first_name: "Jane",
        last_name: "Doe"
    },
    provider: {
        first_name: "ELIZABETH",
        last_name: "BLACKWELL",
        npi: "1234567893"
    },
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"member\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"ELIZABETH\",");
buf.append("        \"last_name\": \"BLACKWELL\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.eligibility(query);
```

```swift
let data = [
    "member": [
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe"
    ],
    "provider": [
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    ],
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.eligibility(params: data)
```

> Example eligibility request to determine general health benefit coverage when a member has a specific group number value assigned:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000",
        "group_number": "123456"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/eligibility/
```

```python
client.eligibility({
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000",
        "group_number": "123456"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

```ruby
client.eligibility({
    member: {
        birth_date: "1970-01-25",
        first_name: "Jane",
        last_name: "Doe",
        id: "W000000000",
        group_number: "123456"
    },
    provider: {
        first_name: "ELIZABETH",
        last_name: "BLACKWELL",
        npi: "1234567893"
    },
    trading_partner_id: "MOCKPAYER"
})
```


```csharp
client.eligibility(
    new Dictionary<string, object> {
        {"member", new Dictionary<string, string> {
                {"birth_date", "1970-01-25"},
                {"first_name", "Jane"},
                {"last_name", "Doe"},
                {"id", "W000000000"},
                {"group_number", "123456"}
            }},
        {"provider", new Dictionary<string, string> {
                {"first_name", "ELIZABETH"},
                {"last_name", "BLACKWELL"},
                {"npi", "1234567893"}
            }},
        {"trading_partner_id", "MOCKPAYER"}
    }
);
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"member\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"id\": \"W000000000\",");
buf.append("        \"group_number\": \"123456\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"ELIZABETH\",");
buf.append("        \"last_name\": \"BLACKWELL\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.eligibility(query);
```

```swift
let data = [
    "member": [
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000",
        "group_number": "123456"
    ],
    "provider": [
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    ],
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.eligibility(params: data)
```

> Some trading partners support eligibility requests using specific service type codes. Here's an example using a service type code to request eligibility information:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "service_types": [ "emergency_services" ],
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/eligibility/
```

```python
client.eligibility({
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "service_types": [ "emergency_services" ],
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
client.eligibility(
    new Dictionary<string, object> {
        {"member", new Dictionary<string, string> {
                {"birth_date", "1970-01-25"},
                {"first_name", "Jane"},
                {"last_name", "Doe"},
                {"id", "W000000000"}
            }},
        {"provider", new Dictionary<string, string> {
                {"first_name", "ELIZABETH"},
                {"last_name", "BLACKWELL"},
                {"npi", "1234567893"}
            }},
        {"service_types", new string[] { "emergency_services" }},
        {"trading_partner_id", "MOCKPAYER"}
    }
);
```

```ruby
client.eligibility({
    member: {
        birth_date: "1970-01-25",
        first_name: "Jane",
        last_name: "Doe",
        id: "W000000000"
    },
    provider: {
        first_name: "ELIZABETH",
        last_name: "BLACKWELL",
        npi: "1234567893"
    },
    "service_types": [ "emergency_services" ],
    "trading_partner_id": "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"member\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"id\": \"W000000000\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"ELIZABETH\",");
buf.append("        \"last_name\": \"BLACKWELL\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"service_types\": [\"emergency_services\"],");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.eligibility(query);
```

```swift
let data = [
    "member": [
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    ],
    "provider": [
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    ],
    "service_types": [ "emergency_services" ],
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.eligibility(params: data)
```

> Some trading partners support eligibility requests using a CPT code. Here's an example using a CPT code to request eligibility information:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "cpt_code": "81291",
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/eligibility/
```

```python
client.eligibility({
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "cpt_code": "81291",
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
client.eligibility(
    new Dictionary<string, object> {
        {"member", new Dictionary<string, string> {
                {"birth_date", "1970-01-25"},
                {"first_name", "Jane"},
                {"last_name", "Doe"},
                {"id", "W000000000"}
            }},
        {"provider", new Dictionary<string, string> {
                {"first_name", "ELIZABETH"},
                {"last_name", "BLACKWELL"},
                {"npi", "1234567893"}
            }},
        {"cpt_code", "81291"},
        {"trading_partner_id", "MOCKPAYER"}
    }
);
```

```ruby
client.eligibility({
    member: {
        birth_date: "1970-01-25",
        first_name: "Jane",
        last_name: "Doe",
        id: "W000000000"
    },
    provider: {
        first_name: "ELIZABETH",
        last_name: "BLACKWELL",
        npi: "1234567893"
    },
    cpt_code: "81291",
    trading_partner_id: "MOCKPAYER"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"member\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"id\": \"W000000000\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"ELIZABETH\",");
buf.append("        \"last_name\": \"BLACKWELL\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"cpt_code\": \"81291\",");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.eligibility(query);
```

```swift
let data = [
    "member": [
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    ],
    "provider": [
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    ],
    "cpt_code": "81291",
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.eligibility(params: data)
```

> Example medicare_national eligibility request including HCPCS code:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "procedure_id": "G0120",
    "procedure_id_qualifier": "hcpcs",
    "trading_partner_id": "medicare_national"
}' https://platform.pokitdok.com/api/v4/eligibility/
```

```python
client.eligibility({
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "procedure_id": "G0120",
    "procedure_id_qualifier": "hcpcs",
    "trading_partner_id": "medicare_national"
})
```

```csharp
 client.eligibility (
			new Dictionary<string, object> {
			 	{"member", new Dictionary<string, object> {
					{"id", "W000000000"},
					{"birth_date", "1970-01-25"},
					{"first_name", "Jane"},
					{"last_name", "Doe"}
					}},
				{"provider", new Dictionary<string, object> {
					{"npi", "1234567893"},
					{"last_name", "BLACKWELL"},
					{"first_name", "ELIZABETH"}
					}},
				{"procedure_id", "G0120"},
				{"procedure_id_qualifier", "hcpcs"},
				{"trading_partner_id", "medicare_national"}
		});
```

```ruby
client.eligibility({
    member: {
        birth_date: "1970-01-25",
        first_name: "Jane",
        last_name: "Doe",
        id: "W000000000"
    },
    provider: {
        first_name: "ELIZABETH",
        last_name: "BLACKWELL",
        npi: "1234567893"
    },
    procedure_id: "G0120",
    procedure_id_qualifier: "hcpcs",
    trading_partner_id: "medicare_national"
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"member\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"id\": \"W000000000\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"ELIZABETH\",");
buf.append("        \"last_name\": \"BLACKWELL\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"procedure_id\": \"G0120\",");
buf.append("    \"procedure_id_qualifier\": \"hcpcs\",");
buf.append("    \"trading_partner_id\": \"medicare_national\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.eligibility(query);
```

```swift
let data = [
    "member": [
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    ],
    "provider": [
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    ],
    "procedure_id": "G0120",
    "procedure_id_qualifier": "hcpcs",
    "trading_partner_id": "medicare_national"
] as [String:Any]
try client.eligibility(params: data)
```

> Example eligibility request using custom application data for easy handling of asynchronous responses:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER",
    "application_data": {
        "patient_id": "ABC1234XYZ",
        "location_id": 123,
        "transaction_uuid": "93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf"
    }
}' https://platform.pokitdok.com/api/v4/eligibility/
```

```python
client.eligibility({
    "member": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "trading_partner_id": "MOCKPAYER",
    "application_data": {
        "patient_id": "ABC1234XYZ",
        "location_id": 123,
        "transaction_uuid": "93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf"
    }
})
```

```csharp
client.eligibility(
    new Dictionary<string, object> {
        {"member", new Dictionary<string, string> {
                {"birth_date", "1970-01-25"},
                {"first_name", "Jane"},
                {"last_name", "Doe"},
                {"id", "W000000000"}
            }},
        {"provider", new Dictionary<string, string> {
                {"first_name", "ELIZABETH"},
                {"last_name", "BLACKWELL"},
                {"npi", "1234567893"}
            }},
        {"trading_partner_id", "MOCKPAYER"},
        {"application_data", new Dictionary<string, object> {
                {"patient_id", "ABC1234XYZ"},
                {"location_id", 123},
                {"transaction_uuid", "93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf"}
            }}
);
```

```ruby
client.eligiblity({
    member: {
        birth_date: "1970-01-25",
        first_name: "Jane",
        last_name: "Doe",
        id: "W000000000"
    },
    provider: {
        first_name: "ELIZABETH",
        last_name: "BLACKWELL",
        npi: "1234567893"
    },
    trading_partner_id: "MOCKPAYER",
    application_data: {
        patient_id: "ABC1234XYZ",
        location_id: 123,
        transaction_uuid: "93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf"
    }
})
```

```java
StringBuffer buf = new StringBuffer();

buf.append("{");
buf.append("    \"member\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"Jane\",");
buf.append("        \"last_name\": \"Doe\",");
buf.append("        \"id\": \"W000000000\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"ELIZABETH\",");
buf.append("        \"last_name\": \"BLACKWELL\",");
buf.append("        \"npi\": \"1234567893\"");
buf.append("    },");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\",");
buf.append("    \"application_data\": {");
buf.append("        \"patient_id\": \"ABC1234XYZ\",");
buf.append("        \"location_id\": 123,");
buf.append("        \"transaction_uuid\": \"93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf\"");
buf.append("    }");
buf.append("");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
Map<String, Object> results = client.eligibility(query);
```

```swift
let data = [
    "member": [
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    ],
    "provider": [
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    ],
    "trading_partner_id": "MOCKPAYER",
    "application_data": [
        "patient_id": "ABC1234XYZ",
        "location_id": 123,
        "transaction_uuid": "93f38f1b-b2cd-4da1-8b55-c6e3ab380dbf"
    ]
] as [String:Any]
try client.eligibility(params: data)
```

> Example eligibility response when the trading partner is unable to respond at this time:

```json
{   
    "client_id": "<client_id>",
    "coverage": {
        "active": false
        },
    "follow_up_action": "resubmission_allowed",
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "reject_reason": "unable_to_respond_now",
    "subscriber": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "gender": "unknown",
        "id": "W000000000",
        "last_name": "Doe"
    },
    "trading_partner_id": "MOCKPAYER",
    "valid_request": true
}
```

> Example eligibility response when the trading partner is unable to find the member specified in the
eligibility request:

```json
{
    "client_id": "<client_id>",
    "coverage": {
        "service_date": "2014-06-25"
    },
    "follow_up_action": "correct_and_resubmit",
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "reject_reason": "subscriber_insured_not_found",
    "subscriber": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "id": "W000000000",
        "last_name": "Doe"
    },
    "trading_partner_id": "MOCKPAYER",
    "valid_request": false
}
```

> Example eligibility response when the trading partner is able to find a member based on the eligibility request, but the specified birth date does not match their records:

```json
{
    "client_id": "<client_id>",
    "coverage": {
        "service_date": "2014-06-25"
    },
    "follow_up_action": "correct_and_resubmit",
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "reject_reason": "patient_birth_date_mismatch",
    "subscriber": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "id": "W000000000",
        "last_name": "Doe"
    },
    "trading_partner_id": "MOCKPAYER",
    "valid_request": false
}
```

> Example eligibility response when the trading partner cannot process eligibility requests using
a CPT code:

```json
{
    "client_id": "<client_id>",
    "coverage": {
        "service_date": "2014-06-25"
    },
    "follow_up_action": "resubmission_not_allowed",
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "reject_reason": "unable_to_respond_now",
    "subscriber": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "id": "W000000000",
        "last_name": "Doe"
    },
    "trading_partner_id": "MOCKPAYER",
    "valid_request": false
}
```

> Example eligibility response when the trading partner returns multiple reject reason codes and cannot process the request:

```json
{
    "client_id": "<client id>",
    "coverage": {
        "active": false,
        "cannot_process": [
            {
                "messages": [
                    {
                        "message": "Payer cannot process the specified service types."
                    }
                ],
                "service_types": [
                    "health_benefit_plan_coverage"
                ],
                "service_type_codes": [
                    "30"
                ]
            }
        ]
    },
    "follow_up_action": "correct_and_resubmit",
    "reject_reason": "provider_not_on_file",
    "subscriber": {
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "id": "W000000000",
        "last_name": "Doe",
        "rejections": [
            {
                "valid_request": false,
                "reject_reason": "invalid_date_of_service",
                "follow_up_action": "correct_and_resubmit"
            },
            {
                "valid_request": false,
                "reject_reason": "patient_birth_date_mismatch",
                "follow_up_action": "correct_and_resubmit"
            },
            {
                "valid_request": false,
                "reject_reason": "death_precedes_date_of_service",
                "follow_up_action": "resubmission_not_allowed"
            }
        ]
    },
    "valid_request": false,
    "trading_partner_id": "MOCKPAYER",
    "pharmacy": {
        "is_eligible": false
    }
}
```



> Sample eligibility response for a successfully executed eligibility request:

```json
{   
    "client_id": "<client_id>",
    "summary": {
         "deductible": {
             "individual": {
                  "in_network": {
                      "applied": {
                          "currency": "USD",
                          "amount": "16.43"
                     },
                      "limit": {
                          "currency": "USD",
                          "amount": "3000"
                      },
                      "remaining": {
                          "currency": "USD",
                          "amount": "2983.57"
                      }
                    },
                  "out_of_network": {
                       "applied": {
                          "currency": "USD",
                          "amount": "16.43"
                      },
                      "limit": {
                          "currency": "USD",
                          "amount": "6000"
                      },
                      "remaining": {
                          "currency": "USD",
                          "amount": "5983.57"
                      }
                  }
              },
              "family": {
                 "in_network": {
                      "applied": {
                          "currency": "USD",
                          "amount": "43.91"
                      },
                      "limit": {
                          "currency": "USD",
                          "amount": "6000"
                      },
                      "remaining": {
                          "currency": "USD",
                          "amount": "5956.09"
                      }
                 },
                  "out_of_network": {
                      "applied": {
                          "currency": "USD",
                          "amount": "43.91"
                      },
                      "limit": {
                          "currency": "USD",
                          "amount": "12000"
                      },
                      "remaining": {
                          "currency": "USD",
                          "amount": "11956.09"
                      }
                  }
              }
          },
          "out_of_pocket": {
              "individual": {
                  "in_network": {
                      "applied": {
                          "currency": "USD",
                          "amount": "16.43"
                      },
                      "limit": {
                          "currency": "USD",
                          "amount": "3000"
                      },
                      "remaining": {
                          "currency": "USD",
                          "amount": "2983.57"
                      }
                  },
                  "out_of_network": {
                      "applied": {
                          "currency": "USD",
                          "amount": "16.43"
                      },
                      "limit": {
                          "currency": "USD",
                          "amount": "12500"
                      },
                      "remaining": {
                          "currency": "USD",
                          "amount": "12483.57"
                      }
                  }
              },
              "family": {
                  "in_network": {
                      "applied": {
                          "currency": "USD",
                          "amount": "43.91"
                      },
                     "limit": {
                          "currency": "USD",
                          "amount": "6000"
                      },
                      "remaining": {
                          "currency": "USD",
                          "amount": "5956.09"
                      }
                 },
                  "out_of_network": {
                      "applied": {
                          "currency": "USD",
                          "amount": "43.91"
                      },
                      "limit": {
                          "currency": "USD",
                          "amount": "25000"
                      },
                      "remaining": {
                          "currency": "USD",
                          "amount": "24956.09"
                      }
                  }
              }
          }
      },

    "coverage": {
        "coinsurance": [
            {
                "benefit_percent": 0.0,
                "authorization_required": "yes",
                "coverage_level": "employee_and_spouse",
                "in_plan_network": "yes",
                "messages": [],
                "service_type_codes": [
                    "98"
                ],
                "service_types": [
                    "professional_physician_visit_office"
                ]
            },
            {
                "benefit_percent": 0.5,
                "coverage_level": "employee_and_spouse",
                "in_plan_network": "no",
                "messages": [],
                "service_type_codes": [
                    "98"
                ],
                "service_types": [
                    "professional_physician_visit_office"
                ]
            }
        ],
        "copay": [
            {
                "authorization_required": "yes",
                "copayment": {
                    "amount": "0",
                    "currency": "USD"
                },
                "coverage_level": "employee_and_spouse",
                "in_plan_network": "yes",
                "messages": [
                    {
                        "message": "PRIMARY OFFICE"
                    }
                ],
                "service_type_codes": [
                    "98"
                ],
                "service_types": [
                    "professional_physician_visit_office"
                ]
            },
            {
                "copayment": {
                    "amount": "0",
                    "currency": "USD"
                },
                "coverage_level": "employee_and_spouse",
                "in_plan_network": "not_applicable",
                "messages": [
                    {
                        "message": "GYN OFFICE VS"
                    },
                    {
                        "message": "GYN VISIT"
                    },
                    {
                        "message": "SPEC OFFICE"
                    },
                    {
                        "message": "SPEC VISIT"
                    },
                    {
                        "message": "PRIME CARE VST"
                    },
                    {
                        "message": "Plan Requires PreCert"
                    },
                    {
                        "message": "Commercial"
                    },
                    {
                        "message": "Plan includes NAP"
                    },
                    {
                        "message": "Pre-Existing may apply"
                    }
                ],
                "service_type_codes": [
                    "98"
                ],
                "service_types": [
                    "professional_physician_visit_office"
                ]
            }
        ],
	"benefit_related_entities": [
           {
             "address": {
                 "address_lines": [
                     "123 TEST ROAD"
                 ],
                 "city": "LITTLE TOWN",
                 "state": "CA",
                 "zipcode": "12345"
             },
             "contacts": [
                 {
                     "phone": "8001234567"
                 }
             ],
             "entity_identifier_code": "primary_care_provider",
             "entity_type": "organization",
             "first_name": "JANET",
             "middle_name": "E",
             "organization_name": "DOE",
             "provider_code": "admitting"
           },
           {
             "contacts": [
                 {
                     "name": "PAYERC BENEFITS HOTLINE",
                     "phone": "8006762583"
                 }
             ],
             "entity_identifier_code": "plan_sponsor",
             "entity_type": "organization",
             "organization_name": "PAYERC"
           }
        ],
        "deductibles": [
            {
                "benefit_amount": {
                    "amount": "6000",
                    "currency": "USD"
                },
                "coverage_level": "family",
                "eligibility_date": "2013-01-25",
                "in_plan_network": "yes",
                "messages": [],
                "time_period": "calendar_year"
            },
            {
                "benefit_amount": {
                    "amount": "5956.09",
                    "currency": "USD"
                },
                "coverage_level": "family",
                "in_plan_network": "yes",
                "messages": [],
                "time_period": "remaining"
            },
            {
                "benefit_amount": {
                    "amount": "3000",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "eligibility_date": "2013-01-25",
                "in_plan_network": "yes",
                "messages": [],
                "time_period": "calendar_year"
            },
            {
                "benefit_amount": {
                    "amount": "2983.57",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "in_plan_network": "yes",
                "messages": [],
                "time_period": "remaining"
            },
            {
                "benefit_amount": {
                    "amount": "12000",
                    "currency": "USD"
                },
                "coverage_level": "family",
                "eligibility_date": "2013-01-25",
                "in_plan_network": "no",
                "messages": [],
                "time_period": "calendar_year"
            },
            {
                "benefit_amount": {
                    "amount": "11956.09",
                    "currency": "USD"
                },
                "coverage_level": "family",
                "in_plan_network": "no",
                "messages": [],
                "time_period": "remaining"
            },
            {
                "benefit_amount": {
                    "amount": "6000",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "eligibility_date": "2013-01-25",
                "in_plan_network": "no",
                "messages": [],
                "time_period": "calendar_year"
            },
            {
                "benefit_amount": {
                    "amount": "5983.57",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "in_plan_network": "no",
                "messages": [],
                "time_period": "remaining"
            }
        ],
        "eligibility_begin_date": "2012-02-25",
        "policy_effective_date": "2016-01-01",
        "group_description": "MOCK INDIVIDUAL ADVANTAGE PLAN",
        "group_number": "000000000000013",
        "level": "employee_and_spouse",
        "out_of_pocket": [
            {
                "benefit_amount": {
                    "amount": "3000",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "in_plan_network": "yes"
            },
            {
                "benefit_amount": {
                    "amount": "2983.57",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "in_plan_network": "yes",
                "time_period": "remaining"
            },
            {
                "benefit_amount": {
                    "amount": "6000",
                    "currency": "USD"
                },
                "coverage_level": "family",
                "in_plan_network": "yes"
            },
            {
                "benefit_amount": {
                    "amount": "5956.09",
                    "currency": "USD"
                },
                "coverage_level": "family",
                "in_plan_network": "yes",
                "time_period": "remaining"
            },
            {
                "benefit_amount": {
                    "amount": "12500",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "in_plan_network": "no"
            },
            {
                "benefit_amount": {
                    "amount": "12483.57",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "in_plan_network": "no",
                "time_period": "remaining"
            },
            {
                "benefit_amount": {
                    "amount": "25000",
                    "currency": "USD"
                },
                "coverage_level": "family",
                "in_plan_network": "no"
            },
            {
                "benefit_amount": {
                    "amount": "24956.09",
                    "currency": "USD"
                },
                "coverage_level": "family",
                "in_plan_network": "no",
                "messages": [],
                "time_period": "remaining"
            }
        ],
        "plan_begin_date": "2013-02-25",
        "plan_number": "0000000",
        "service_date": "2013-08-25",
        "service_type_codes": [
            "98"
        ],
        "service_types": [
            "professional_physician_visit_office"
        ]
    },
    "payer": {
        "id": "MOCKPAYER",
        "name": "MOCK PAYER INC"
    },
    "provider": {
        "first_name": "ELIZABETH",
        "last_name": "BLACKWELL",
        "npi": "1234567893"
    },
    "service_type_codes": [
        "98"
    ],
    "service_types": [
        "professional_physician_visit_office"
    ],
    "subscriber": {
        "address": {
            "address_lines": [
                "123 MAIN ST"
            ],
            "city": "SAN MATEO",
            "state": "CA",
            "zipcode": "94401"
        },
        "birth_date": "1970-01-25",
        "first_name": "Jane",
        "id": "W000000000",
        "last_name": "Doe"
    },
    "trading_partner_id": "MOCKPAYER",
    "valid_request": true
}
```

> Sample medicare_national eligibility response for a member with Medicare Part D coverage.
  Notice that medicare members with part D coverage will have pharmacy.is_eligible set to true and
  the pharmacy.plan_number will contain their medicare part D plan number:

```json
{
    "client_id": "<client_id>",
    "coverage": {
        "active": true,
        "coinsurance": [
            {
                "benefit_percent": 0.2,
                "service_type_codes": [
                    "98"
                ],
                "service_types": [
                    "health_benefit_plan_coverage"
                ]
            },
            {
                "benefit_percent": 0.0,
                "service_type_codes": [
                    "98"
                ],
                "service_types": [
                    "alcoholism",
                    "smoking_cessation",
                    "home_health_care"
                ]
            }
        ],
        "deductibles": [
            {
                "benefit_amount": {
                    "amount": "1288",
                    "currency": "USD"
                },
                "insurance_type": "medicare_part_a",
                "service_type_codes": [
                    "30"
                ],
                "service_types": [
                    "health_benefit_plan_coverage"
                ],
                "time_period": "episode"
            },
            {
                "benefit_amount": {
                    "amount": "1288",
                    "currency": "USD"
                },
                "insurance_type": "medicare_part_a",
                "service_type_codes": [
                    "30"
                ],
                "service_types": [
                    "health_benefit_plan_coverage"
                ],
                "time_period": "remaining"
            },
            {
                "benefit_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "insurance_type": "medicare_part_a",
                "service_type_codes": [
                    "45",
                    "42"
                ],
                "service_types": [
                    "hospice",
                    "home_health_care"
                ],
                "time_period": "episode"
            },
            {
                "benefit_amount": {
                    "amount": "166",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "in_plan_network": "unknown",
                "insurance_type": "medicare_part_b",
                "service_type_codes": [
                    "30"
                ],
                "service_types": [
                    "health_benefit_plan_coverage"
                ],
                "time_period": "calendar_year"
            },
            {
                "benefit_amount": {
                    "amount": "166",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "in_plan_network": "unknown",
                "insurance_type": "medicare_part_b",
                "service_type_codes": [
                    "30"
                ],
                "service_types": [
                    "health_benefit_plan_coverage"
                ],
                "time_period": "remaining"
            },
            {
                "benefit_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "coverage_level": "individual",
                "in_plan_network": "unknown",
                "insurance_type": "medicare_part_b",
                "service_type_codes": [
                    "AJ",
                    "67",
                    "42"
                ],
                "service_types": [
                    "alcoholism",
                    "smoking_cessation",
                    "home_health_care"
                ],
                "time_period": "calendar_year"
            }
        ],
        "insurance_type": "medicare_part_b",
        "non_covered": [
            {
                "benefit_amount": {
                    "amount": "0",
                    "currency": "USD"
                },
                "service_type_codes": [
                    "54",
                    "41"
                ],
                "service_types": [
                    "long_term_care",
                    "routine_preventive_dental"
                ]
            }
        ],
        "other_payers": [
            {
                "coordination_of_benefits": "primary_payer",
                "name": "UNITEDHEALTHCARE INSURANCE COMPANY",
                "service_type_codes": [
                    "88"
                ],
                "service_types": [
                    "pharmacy"
                ]
            }
        ],
        "plan_begin_date": "2016-01-25",
        "plan_end_date": "2016-12-25",
        "service_type_codes": [
            "30",
            "UC",
            "DM",
            "BV",
            "BU",
            "BT",
            "AL",
            "AK",
            "AJ",
            "AI",
            "A8",
            "A6",
            "A4",
            "98",
            "86",
            "83",
            "76",
            "73",
            "69",
            "67",
            "53",
            "52",
            "51",
            "50",
            "42",
            "40",
            "39",
            "38",
            "37",
            "36",
            "33",
            "3",
            "28",
            "27",
            "26",
            "25",
            "24",
            "23",
            "2"
        ],
        "service_types": [
            "health_benefit_plan_coverage",
            "urgent_care",
            "medical_equipment",
            "obstetrical_gynecological",
            "obstetrical",
            "gynecological",
            "vision_optometry",
            "drug_addiction",
            "alcoholism",
            "substance_abuse",
            "psychiatric_outpatient",
            "psychotherapy",
            "psychiatric",
            "professional_physician_visit_office",
            "emergency_services",
            "infertility",
            "dialysis",
            "diagnostic_medical",
            "maternity",
            "smoking_cessation",
            "hospital_ambulatory_surgical",
            "hospital_emergency_medical",
            "hospital_emergency_accident",
            "hospital_outpatient",
            "home_health_care",
            "oral_surgery",
            "prosthodontics",
            "orthodontics",
            "dental_accident",
            "dental_crowns",
            "chiropractic",
            "consultation",
            "adjunctive_dental_services",
            "maxillofacial_prosthetics",
            "endodontics",
            "restorative",
            "periodontics",
            "diagnostic_dental",
            "surgical"
        ]
    },
    "pharmacy": {
        "benefits_manager": {
            "name": "UNITEDHEALTHCARE INSURANCE COMPANY",
            "phone": "8778423210",
            "url": "www.AARPMedicareRx.com"
        },
        "is_eligible": true,
        "plan_number": "S5820 003"
    },
    "service_type_codes": [
        "30",
        "UC",
        "DM",
        "BV",
        "BU",
        "BT",
        "AL",
        "AK",
        "AJ",
        "AI",
        "A8",
        "A6",
        "A4",
        "98",
        "86",
        "83",
        "76",
        "73",
        "69",
        "67",
        "53",
        "52",
        "51",
        "50",
        "42",
        "40",
        "39",
        "38",
        "37",
        "36",
        "33",
        "3",
        "28",
        "27",
        "26",
        "25",
        "24",
        "23",
        "2"
    ],
    "service_types": [
        "health_benefit_plan_coverage",
        "urgent_care",
        "medical_equipment",
        "obstetrical_gynecological",
        "obstetrical",
        "gynecological",
        "vision_optometry",
        "drug_addiction",
        "alcoholism",
        "substance_abuse",
        "psychiatric_outpatient",
        "psychotherapy",
        "psychiatric",
        "professional_physician_visit_office",
        "emergency_services",
        "infertility",
        "dialysis",
        "diagnostic_medical",
        "maternity",
        "smoking_cessation",
        "hospital_ambulatory_surgical",
        "hospital_emergency_medical",
        "hospital_emergency_accident",
        "hospital_outpatient",
        "home_health_care",
        "oral_surgery",
        "prosthodontics",
        "orthodontics",
        "dental_accident",
        "dental_crowns",
        "chiropractic",
        "consultation",
        "adjunctive_dental_services",
        "maxillofacial_prosthetics",
        "endodontics",
        "restorative",
        "periodontics",
        "diagnostic_dental",
        "surgical"
    ],
    "subscriber": {
        "address": {
            "address_lines": [
                "123 MAIN ST",
                "APT 123"
            ],
            "city": "ENGLEWOOD",
            "state": "NJ",
            "zipcode": "07631"
        },
        "birth_date": "1940-01-25",
        "first_name": "JANE",
        "gender": "female",
        "id": "000000000A",
        "last_name": "DOE",
        "middle_name": "M"
    },
    "summary": {
        "deductible": {
            "individual": {
                "in_network": {
                    "applied": {
                        "amount": "0.00",
                        "currency": "USD"
                    },
                    "limit": {
                        "amount": "166",
                        "currency": "USD"
                    },
                    "remaining": {
                        "amount": "166",
                        "currency": "USD"
                    }
                },
                "out_of_network": {
                    "applied": {
                        "amount": "0.00",
                        "currency": "USD"
                    },
                    "limit": {
                        "amount": "166",
                        "currency": "USD"
                    },
                    "remaining": {
                        "amount": "166",
                        "currency": "USD"
                    }
                }
            }
        },
        "out_of_pocket": {
            "individual": {
                "in_network": {
                    "applied": {
                        "amount": "0.00",
                        "currency": "USD"
                    },
                    "limit": {
                        "amount": "0",
                        "currency": "USD"
                    },
                    "remaining": {
                        "amount": "0",
                        "currency": "USD"
                    }
                },
                "out_of_network": {
                    "applied": {
                        "amount": "0.00",
                        "currency": "USD"
                    },
                    "limit": {
                        "amount": "0",
                        "currency": "USD"
                    },
                    "remaining": {
                        "amount": "0",
                        "currency": "USD"
                    }
                }
            }
        }
    },
    "trading_partner_id": "medicare_national",
    "valid_request": true
}
```

*Available modes of operation: batch/async or real-time*

The Eligibility endpoint makes it easy to verify a member's insurance information in real-time. You can check
co-insurance, copay, deductible and out of pocket amounts for a member along with other benefit information.

Use the [Trading Partners](#trading-partners) endpoint to determine available trading_partner_id values for use with the
Eligibility API.

### Endpoint Description


<!--- beginning of table -->

| Endpoint      | HTTP Method | Description                                                  |
|:--------------|:------------|:-------------------------------------------------------------|
| /eligibility/ | POST        | Determine eligibility via an X12 270 Request For Eligibility |

<!--- end of table -->


All eligibility requests must include a valid Provider NPI. Some trading partners require that the submitting provider’s
NPI be registered or be a participating provider with that health plan to successfully check eligibility.

The Eligibility endpoint allows you to request eligibility for service types. The service_type parameter
allows you to specify particular service(s), however, if no service type is specified the
request will be made for general benefit coverage (health_benefit_plan_coverage). Some trading partners may not support specific service type inquiries. A full listing of possible service_types values is included [below](#service-type).

Some trading partners allow combinations of the below parameters to return a successful eligibility response.  PokitDok now only requires those specific parameters required by the trading partner being called. Details on available search options per trading partner can be found by using the [Trading Partners](#trading-partners) endpoint.  There are example eligibility requests for each of the search option combinations to the right as well.

### Parameters

The `/eligibility/` endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter                  | Description                                                                                                                                                                                                     |
|:---------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cpt_code                   | The CPT code that should be used to request specific eligibility information. Note: requests based on CPT code are not supported by all trading partners.                                                       |
| industry_code              | The industry code for the request                                                                                                                            |
| payer                      | The payer associated with a request. Uses the payer [object](#eligibility-payer).                                                                                                                               |
| member.birth_date          | The named insured’s birth date as specified on their policy. May be omitted if member.id is provided. In ISO8601 format (YYYY-MM-DD).                                                                           |
| member.gender              | The member's gender.                                                                                                                                                                                            |
| member.first_name          | The named insured’s first name as specified on their policy.                                                                                                                                                    |
| member.middle_name         | The named insured’s middle name as specified on their policy.                                                                                                                                                   |
| member.suffix              | The named insured’s suffix.                                                                                                                                                                                     |
| member.id                  | The named insured’s member identifier. May be omitted if member.birth_date is provided.                                                                                                                         |
| member.last_name           | The named insured’s last name as specified on their policy.                                                                                                                                                     |
| member.plan_start_date     | Used to convey date information related to the member's policy.  Use this field if you are looking to return eligibility results as of a certain date. In ISO8601 format (YYYY-MM-DD).                          |
| member.group_number        | Group number for the member.                                                                                                                                                                                    |
| provider.first_name        | The provider’s first name when the provider is an individual.                                                                                                                                                   |
| provider.middle_name       | The provider’s middle name when the provider is an individual.                                                                                                                                                  |
| provider.last_name         | The provider’s last name when the provider is an individual.                                                                                                                                                    |
| provider.suffix            | The provider’s name suffix.                                                                                                                                                                                     |
| provider.pin               | The personal identification number of the provider.                                                                                                                                                             |
| provider.npi               | The NPI for the provider.                                                                                                                                                                                       |
| provider.organization_name | The provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                                            |
| provider.tax_id            | The provider's tax ID. This is an optional field and may be required by certain trading partners with specific rules.|
| service_types              | The service type(s) the eligibility request is being made against. Defaults to health_benefit_plan_coverage. Service Type Codes supported by the PokitDok API can be retrieved by using GET /eligibility/constants.  A full listing of possible service_types values is included [below](#service-type).                |
| procedure_id               | The unique identifier of the procedure.                                                                                                                                                                         |
| procedure_id_qualifier     | The qualifier associated with the procedure id (e.g. cpt). A full list of possible values is included [below](#procedure-id-qualifier).                                                                         |
| transaction_code           | The purpose of the eligibility transaction. Defaults to request. Other possibility is cancellation.                                                                                                             |
| trading_partner_id         | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) Endpoint.                                                                                                 |

<!--- end of table -->


Eligibility and benefit responses vary depending on the trading partner and the plan in which a member is enrolled. Some trading partners may not provide deductible, out-of-pocket, copayment, coinsurance or other specific plan information. PokitDok will return all information received from the trading partner in the eligibility response.

PokitDok adds a Summary section in the eligibility response for convenience as a quick overview of a member's deductible and out-of-pocket information.  This should not be seen as a total replacement for the detailed deductible and out-of-pocket information in the coverage section of the eligibility response.  The Summary section contains deductible and out-of-pocket values for overall health benefit plan coverage as well as any additional service types for which deductible and out-of-pocket information is received.  When a value of $0 is returned in the Summary section, users should reference the Coverage section to determine if the trading partner returned a zero value or if the information was not provided in the response.

### Response

The `/eligibility/` response contains the following fields:


<!--- beginning of table -->

| Field                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:----------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| client_id                                           | The unique identifier associated with the client making the eligibility request.                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.active                                     | A boolean value that is true when the member has active coverage. It is false when membership information could not be returned or when inactive coverage is indicated by the trading partner.                                                                                                                                                                                                                                                                                      |
| benefit_related_entities                   | Identifies additional entities associated with eligibility and benefits.  Uses the benefit related entities [object](#benefit-related-entities).                                                                                                                                                                                                                                                                                                                                  |
| coverage.added_date                                 | Date coverage was added. |
| coverage.coverage_details                           | Additional information relating to the coverage.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.benefit_begin_date                           | The date benefits begin for the member.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.benefit_begin                          | The date benefits begin for the member.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.benefit_end_date                           | The date benefits end for the member.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.coverage_details.status                    | The status of the coverage.  Often used when member is in an Individual Exchange Grace Period.  Possible values include active_pending_investigation, inactive_pending_investigation and inactive_pending_eligibility_update.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| coverage.coverage_details.period_start_date            | The start date for the coverage period. Often used when member is in an Individual Exchange Grace Period.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| coverage.coverage_details.period_end_date            | The end date for the coverage period. Often used when member is in an Individual Exchange Grace Period.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| coverage.coverage_details.messages                    | List of messages relating to the coverage details.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| coverage.coverage_details.messages.message            | Messages relating to the coverage details.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| coverage.coverage_details.group_or_policy_number    | The group or policy number associated with the coverage.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| coverage.coverage_details.plan_description          | The product name or special program name for the insurance plan. This is often the brand or marketing name for the plan.                                                                                                                                                                                                                                                                                                                                                              |
| coverage.coverage_details.insurance_type            | The type of insurance coverage. Possible values include: hmo, ppo, pos, cobra, commercial, medicaid, medicare_part_a, medicare_part_b, other.                                                                                                                                                                                                                                                                                                                                          |
| coverage.coverage_details.service_types             | The service type(s) returned by the trading partner.  A full listing of possible service_types values is included [below](#service-type).                                                                                                                                                                                                                                                                                      |
| coverage.coverage_details.service_type_codes        | The numerical value for the service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.plan_benefit_description                   | Description for the plan benefits.                                                                                                                                                                                                                                                                                                                                                                                                                      				|
| coverage.plan_benefit_description.benefit_begin                  | The date plan benefits begin for the member.                                                                                                                                                                                                                                                                                                                                                                                                                     				|
| coverage.plan_benefit_description.messages.message  | Messages associated with the plan benefits.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| coverage.plan_benefit_description.coverage_level    | The coverage level that applies to the plan benefits. Possible values include: employee_only, employee_and_spouse, employee_and_children, family, individual                                                                                                                                                                                                                                                                                                               |
| coverage.plan_benefit_description.service_types     | The service type(s) returned by the trading partner. A full listing of possible service_types values is included [below](#service-type).                                                                                                                                                                                                                                                                                      |
| coverage.plan_benefit_description.service_type_codes| The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.group_or_policy_number                     | The group or policy number associated with the coverage.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| coverage.member_identification_number                     | Used for member identification if value returned for member id is a unique health identifier.                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.case_number                     | Case number for member specified in eligibility response.                                                                                                                                                                                                                                                                                                              |
| coverage.family_unit_number                     | Used when the member has a suffix to their member ID and the information source is a Pharmacy Benefit Manager (PBM).                                                                                                                                                                                                                                                                                                                                                              |
| coverage.class_of_contract_code                    | Used if enough information is provided in the eligibility request to determine the Class of Contract for claims processing.                                                                                                                                                                                                                                                                                                                                                              |
| coverage.contract_number                    | Used to identify the provider's contract number.                                                                                                                                                                                                                                                                                                                      |
| coverage.medical_record_identification_num        | Identification number for medical record for member specified in the eligibility response.                                                                                                                                                                                                                                                                      |
| coverage.patient_account_number                    | The account number for the patient.                                                                                                                                                                                                                                                                                                                      |
| coverage.health_insurance_claim_number               | Used when the Health Insurance Claim (HIC) Number and member id values are different.                                                                                                                                                                                                                                                              |
| coverage.identification_card_serial_number           | Used to uniquely identify the Identification Card when multiple cards have been or will be issued to a member.                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.identity_card_number		             | Used when the Identity Card Number and member id values are different.                                                                                                                                                                                                                                                                               |
| coverage.issue_number			           | The member's issue number.                                                                                                                                                                                                                                                                                                                                       |
| coverage.insurance_policy_number			| The member's insurance policy number.                                                                                                                                                                                                                                                                                                                       |
| coverage.plan_network_identification_number		| Used to identify a member's plan network.                                                                                                                                                                                                                                                                                                                    |
| coverage.plan_network_description			| Description for plan network for the member specified in the eligibility response.                                                                                                                                                                                                                                                                     |
| coverage.medicaid_recipient_identification_number	| Used when the Medicaid Recipient Identification Number and member id values are different.                                                                                                                                                                                                                                                  		   |
| coverage.prior_identifier_number			| Used when a corrected or new identification number is returned in the member id field.                                                                                                                                                                                                                                               			      |
| coverage.agency_claim_number				| Used only when the information source is a Property and Casualty payer.                                                                                                                                                                                                                                                  					   |
| coverage.social_security_number			| The member's social security number.                                                                                                                                                                                            |
| coverage.healthcare_facilities                      | Healthcare facility payer information (used when coordination of benefits is needed). Like TPA/IPA.                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.healthcare_facilities.address              | The address of the healthcare facility. Uses the address [object](#eligibility-address).                                                                                                                                                                                                                                                                                                                                                                                              |
| coverage.healthcare_facilities.name                 | The name of the healthcare facility.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| coverage.healthcare_facilities.phone                | The phone number of the healthcare facility.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| coverage.healthcare_facilities.email                | The email of the healthcare facility.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| coverage.healthcare_facilities.url                  | The the url associacted with the healthcare facility.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| coverage.healthcare_facilities.fax                  | The fax of the healthcare facility.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.healthcare_facilities.facility_type        | The type of healthcare facility.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.healthcare_facilities.service_types        | The service type(s) returned by the trading partner. A full listing of possible service_types values is included [below](#service-type).                                                                                                                                                                                                                       |
| coverage.healthcare_facilities.service_type_codes   | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                      		  |
| coverage.coinsurance                                | List of co-insurance information for the member.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.coinsurance.service_types                  | The service type(s) returned by the trading partner. A full listing of possible service_types values is included [below](#service-type).                                                                                                                                                                                                                      |
| coverage.coinsurance.service_type_codes             | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.coinsurance.description                              | Additional benefit level description associated with coinsurance.                                                                                                                                                                                                                                                                        |
| coverage.coinsurance.plan_description                              | The product name or special program name for the insurance plan. This is often the brand or marketing name for the plan.                                                                                                                                                                                                                                                                                                                                          |
| coverage.coinsurance.insurance_type                              | Type of insurance associated with coinsurance.                                                                                                                                                                                                                                                                                              |
| coverage.coinsurance.authorization_required         | Whether or not authorization is required. List of possible values can be seen [below](#authz-req).                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.coinsurance.procedure_id                   | The unique identifier of the procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.coinsurance.procedure_id_qualifier         | The qualifier associated with the procedure id (e.g. cpt). A full list of possible values is included [below](#procedure-id-qualifier).                                                                                                                                                                                                                                                                                                                                               |
| coverage.coinsurance.messages.message               | Messages associated with the coverages coinsurance.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.coinsurance.delivery                       | Object containing service delivery information. Uses the delivery [object](#eligibility-delivery).                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.coinsurance.benefit_percent                | A percentage that represents the patient's portion of the responsibility for a benefit. (e.g. 0.2 when the patient's portion of the responsibility is 20% )                                                                                                                                                                                                                                                                                                                           |
| coverage.coinsurance.coverage_level                 | The coverage level that applies to this co-insurance information. Possible values include: employee_only, employee_and_spouse, employee_and_children, family, individual                                                                                                                                                                                                                                                                                                              |
| coverage.coinsurance.in_plan_network                | Indicates whether or not the co-insurance information applies to in or out of network. providers. If the co-insurance information is not dependent upon network status, not_applicable may be returned to indicate the value is the same for in and out of network providers.                                                                                                                                                                                                         |
| coverage.coinsurance.plan_begin_date                | Coinsurance plan begin date for the member specified in the eligibility response. In ISO8601 format (YYYY-MM-DD). |
| coverage.coinsurance.plan_end_date                  | Coinsurance plan end date for the member specified in the eligibility response. In ISO8601 format (YYYY-MM-DD). |
| coverage.limitations		                 |    List of limitations for the coverage.                                                                                                                                                                                                                                                                                                                          |
| coverage.limitations.benefit_amount                 | Monetary amount for the benefit limitation. Uses the monetary amount [object](#eligibility-monetary-amount).                                                                                                                                                                                                                                                                                                                                                                          |
| coverage.limitations.delivery                       | Object containing service delivery information. Uses the delivery [object](#eligibility-delivery).                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.limitations.plan_description                       | The product name or special program name for the insurance plan. This is often the brand or marketing name for the plan.                                                                                                                                                                                                                                                                                                                                                     |
| coverage.limitations.description                       | Additional benefit level description associated with the coverage's limitations.                                                                                                                                                                                                                                                                                                                                                                                           |
| coverage.limitations.messages.message               | Messages associated with the coverage's limitations.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| coverage.limitations.service_type_codes             | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.limitations.procedure_id                   | The unique identifier of the procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.limitations.procedure_id_qualifier         | The qualifier associated with the procedure id (e.g. cpt). A full list of possible values is included [below](#procedure-id-qualifier).                                                                                                                                                                                                                                                                                                                                               |
| coverage.limitations.time_period_qualifier         | The time period for which limitiations apply. A full list of possible values is included [below](#eligibility_time_period_qualifier)                                                                                                                                                                                                                                                                                                           |
| coverage.limitations.coverage_level                 | The coverage level that applies to this limitation. This can be at family or individual levels.                                                                                                                                                                                                                                                                                                                                                                                       |
| coverage.limitations.in_plan_network                | Indicates whether or not the limitation applies to in or out of network providers. If the limitation is not dependent upon network status, not_applicable may be returned to indicate the value is the same for in and out of network providers.                                                                                                                                                                                                                                      |
| coverage.limitations.service_types                  | A list of service types returned by the trading partner. A full list of possible values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                                                             |
| coverage.limitations.latest_visit_or_consultation_date | Latest visit or consultation date for this limitation. |
| coverage.limitations.quantity                       | `[DEPRECATED]`|
| coverage.limitations.quantity_qualifier             | `[DEPRECATED]` |
| coverage.contacts                                   | List of contacts related to the member's coverage. This may include contact information for the payer as well as vendors or third party administrators.                                                                                                                                                                                                                                                                                                                               |
| coverage.contacts.name                              | The name of this contact.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| coverage.contacts.id                                | The primary identifier for this contact.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| coverage.contacts.email                             | The email address that may be used for this contact.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.contacts.phone                             | The phone number for this contact.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| coverage.contacts.url                               | The URL for this contact. This is typically a link to the contact's web site.                                                                                                                                                                                                                                                                                                                                                                                                             |
| coverage.contacts.contact_type                      | The type of entity related to this contact information. Possible values include: vendor, third_party_administrator, plan_sponsor, payer, primary_payer, secondary_payer, tertiary_payer, utilization_management_organization.                                                                                                                                                                                                                                                          |
| coverage.contacts.address                           | The contact's address information. Uses the address [object](#eligibility-address).                                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.contacts.service_types                     | A list of service types returned by the trading partner. A full list of possible values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                                                    |
| coverage.contacts.service_type_codes                | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.contacts.procedure_id                      | The unique identifier of the procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.contacts.procedure_id_qualifier            | The qualifier associated with the procedure id (e.g. cpt). A full list of possible values is included [below](#procedure-id-qualifier).                                                                                                                                                                                                                                                                                                                                               |
| coverage.contacts.messages.message                  | Messages associated with a contact.  Instructions for acquiring more information that cannot be provided electronically may be included here.                                                                                                                                                                                                                                                                                                                                         |
| coverage.copay                                      | List of co-payment information for the member.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| coverage.copay.copayment                            | Monetary amount for this copay item (e.g. 15 for a $15 co-pay). Uses the monetary amount [object](#eligibility-monetary-amount).                                                                                                                                                                                                                                                                                                                                                      |
| coverage.copay.coverage_level                       | The coverage level that applies to this co-pay information. Possible values include: employee_only, employee_and_spouse, employee_and_children, family, individual.                                                                                                                                                                                                                                                                                                                   |
| coverage.copay.in_plan_network                      | Indicates whether or not the copay information applies to in or out of network providers. If the copay information is not dependent upon network status, not_applicable may be returned to indicate the value is the same for in and out of network providers.                                                                                                                                                                                                                        |
| coverage.copay.insurance_type                      | Type of insurance associated with a copay.                                                                                                                                                                                          |
| coverage.copay.description                      | Additional benefit level description associated with a copay.                                                                                                                                                                          |
| coverage.copay.plan_description                      | The product name or special program name for the insurance plan. This is often the brand or marketing name for the plan.                                                                                                        |
| coverage.copay.service_types                        | A list of service types returned by the trading partner. A full list of possible values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                                                     |
| coverage.copay.service_type_codes                   | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.copay.authorization_required               | Whether or not authorization is required. List of possible values can be seen [below](#authz-req).                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.copay.messages.message                     | Messages associated with the coverage's copay.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| coverage.copay.procedure_id                         | The unique identifier of the procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.copay.procedure_id_qualifier               | The qualifier associated with the procedure id (e.g. cpt). A full list of possible values is included [below](#procedure-id-qualifier).                                                                                                                                                                                                                                                                                                                                               |
| coverage.copay.delivery                             | Object containing service delivery information. Uses the delivery [object](#eligibility-delivery).                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.deductibles                                | List of deductible information for the member.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| coverage.deductibles.messages.message               | Messages associated with the coverage's deductible.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.deductibles.eligibility_date               | The eligibility date of the deductible. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.deductibles.delivery                       | Object containing service delivery information. Uses the delivery [object](#eligibility-delivery).                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.deductibles.description                       | Additional benefit level description associated with a deductible.                                                                                                                                                                                                                                                                              |
| coverage.deductibles.plan_description                       | The product name or special program name for the insurance plan. This is often the brand or marketing name for the plan.                                                                                                                                                                                                                                    |
| coverage.deductibles.service_type_codes             | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.deductibles.procedure_id                   | The unique identifier of the procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.deductibles.procedure_id_qualifier         | The qualifier associated with the procedure id (e.g. cpt). A full list of possible values is included [below](#procedure-id-qualifier).                                                                                                                                                                                                                                                                                                                                               |
| coverage.deductibles.insurance_type                 | Type of insurance associated with a deductible.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| coverage.deductibles.benefit_amount                 | Monetary amount for this deductible item. For calendar year deductible information, this will be the deductible for the calendar year for the associated coverage level and in/out of plan network indicator. (e.g. $7000.00 for in network, family coverage)                                                                                                                                                                                                                         |
| coverage.deductibles.coverage_level                 | The coverage level that applies to this deductible information. When a family (or more than one person) is covered, you'll see deductible information for the family as well as the individual that was referenced in the eligibility response.                                                                                                                                                                                                                                        |
| coverage.deductibles.in_plan_network                | Indicates whether or not the deductible information applies to in or out of network providers. If the deductible information is not dependent upon network status, not_applicable may be returned to indicate the value is the same for in and out of network providers.                                                                                                                                                                                                              |
| coverage.deductibles.time_period                    | The period of time for which this deductible item applies. Possible values include: calendar_year, remaining, and service_year. remaining indicates the amount that remains in the calendar year for the member to reach their deductible. calendar_year indicates that the amount represents the total deductible amount for the current year. When no time period applies to deductible information, time_period will not be included for that deductible in the response. If a member has a health plan which does not operate on the calendar_year, they will have accumulators that follow the service_year instead.                          |
| coverage.deductibles.service_types                  | A list of service types returned by the trading partner. A full list of possible values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                                                 |
| coverage.disclaimer.messages.message                | Messages associated with the coverage's disclaimer.  If a trading partner provides benefit disclaimer information as part of their response, it will be included here.                                                                                                                                                                                                                                                                                                                |
| coverage.cannot_process                             | Returned if the payer cannot process specified service types.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| coverage.cannot_process.messages.message            | Messages associated with the reason why a payer was unable to process a service.                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.cannot_process.service_types               | The service type(s) returned by the trading partner. A full listing of possible service_types values is included [below](#service-type).                                                                                                                                                                                                                                                                                      |
| coverage.cannot_process.service_type_codes          | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.other_payers                               | A list of other payers that provide coverage for the member. This list of payers is primarily used to communicate information related to the coordination of benefits.                                                                                                                                                                                                                                                                                                                |
| coverage.other_payers.service_type_codes            | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.other_payers.procedure_id                  | The unique identifier of the procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.other_payers.procedure_id_qualifier        | The qualifier associated with the procedure id (e.g. cpt). A full list of possible values is included [below](#procedure-id-qualifier).                                                                                                                                                                                                                                                                                                                                               |
| coverage.other_payers.plan_description              | The product name or special program name for the insurance plan. This is often the brand or marketing name for the plan.                                                                                                                                                                                                                                                                                                                                                              |
| coverage.other_payers.plan_number                   | Plan ID/number for the member specified in the eligibility request.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.other_payers.coordination_of_benefits      | The role of this payer in the coordination of benefits. Possible values include: primary_payer, secondary_payer, tertiary_payer                                                                                                                                                                                                                                                                                                                                                       |
| coverage.other_payers.coordination_of_benefits_date | The date when this payer started participating in the coordination of benefits. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                                       |
| coverage.other_payers.coverage_level                | The coverage level for this plan. Possible values include: employee_only, employee_and_spouse, employee_and_children, family, individual                                                                                                                                                                                                                                                                                                                                              |
| coverage.other_payers.id                            | The unique id used for this payer.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.other_payers.name                          | The name of this payer. (e.g. MEDICARE).                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| coverage.other_payers.subscriber                    | The subscriber information associated with this payer. Uses the subscriber [object](#eligibility-subscriber).                                                                                                                                                                                                                                                                                                                                                                         |
| coverage.other_payers.service_types                 | A list of service types that apply to this payer information. A full list of possible values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                                                      |
| coverage.other_payers.benefit_begin_date            | The benefit begin date for this other payers coverage. |
| coverage.out_of_pocket                              | List of out of pocket (stop loss) information for the member.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| coverage.out_of_pocket.description                              | Additional benefit level description associated with out of pocket information.                                                                                                                                                                                                                                                                                                                                                                                       |
| coverage.out_of_pocket.plan_description                              | The product name or special program name for the insurance plan. This is often the brand or marketing name for the plan.                                                                                                                                                                                                                                                                                                                                          |
| coverage.out_of_pocket.insurance_type                              | Type of insurance associated with out of pocket information.                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.out_of_pocket.messages.message             | Messages associated with the coverage's out of pocket.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| coverage.out_of_pocket.delivery                     | Object containing service delivery information. Uses the delivery [object](#eligibility-delivery).                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.out_of_pocket.service_type_codes           | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.out_of_pocket.procedure_id                 | The unique identifier of the procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.out_of_pocket.procedure_id_qualifier       | The qualifier associated with the procedure id (e.g. cpt). A full list of possible values is included [below](#procedure-id-qualifier).                                                                                                                                                                                                                                                                                                                                               |
| coverage.out_of_pocket.benefit_amount               | Monetary amount for this out of pocket item. For calendar year out of pocket information, this will be the out of pocket amount for the calendar year for the associated coverage level and in/out of plan network indicator (e.g. $12600.00 for in network, family coverage). Uses the monetary amount [object](#eligibility-monetary-amount).                                                                                                                                       |
| coverage.out_of_pocket.coverage_level               | The coverage level that applies to this out of pocket information. When a family (or more than one person) is covered, you'll see out of pocket information for the family as well as the individual that was referenced in the eligibility request.                                                                                                                                                                                                                                  |
| coverage.out_of_pocket.in_plan_network              | Indicates whether or not the out of pocket information applies to in or out of network providers. If the out of pocket information is not dependent upon network status, not_applicable may be returned to indicate the value is the same for in and out of network providers.                                                                                                                                                                                                        |
| coverage.out_of_pocket.time_period                  | The period of time for which this out of pocket item applies. Possible values include: calendar_year and remaining. remaining indicates the amount that remains in the calendar year for the member to reach their out of pocket amount. calendar_year indicates that the amount represents the total out of pocket amount for the current year. When no time period applies to deductible information, time_period will not be included for that out of pocket item in the response. |
| coverage.out_of_pocket.service_types                | A list of service types returned by the trading partner. A full list of possible values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                                              |
| coverage.non_covered                                | List of eligibility benefits that are not covered.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.non_covered.messages.message               | Messages associated with the reason why an eligibility benefit is not covered.                                                                                                                                                                                                                                                                                                                                                                                                        |
| coverage.non_covered.in_plan_network                | Whether or not the non-covered benefit is within the plan network.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.non_covered.description                              | Additional benefit level description associated with non-covered benefits.                                                                                                                                                                                                                                                                                                                                                                                       |
| coverage.non_covered.plan_description                              | The product name or special program name for the insurance plan. This is often the brand or marketing name for the plan.                                                                                                                                                                                                                                                                                                                                          |
| coverage.non_covered.insurance_type                              | Type of insurance associated with non-covered benefits.                                                                                                                                                                                                                                                                                                                                                                                                      |
| coverage.non_covered.coverage_level                 | The coverage level that applies to this deductible information. When a family (or more than one person) is covered, you'll see deductible information for the family as well as the individual that was referenced in the eligibility request. A full list of possible values is included [below](#coverage-level).                                                                                                                                                                   |
| coverage.non_covered.benefit_amount                 | Monetary amount for this out of pocket item. For calendar year out of pocket information, this will be the out of pocket amount for the calendar year for the associated coverage level and in/out of plan network indicator (e.g. $12600.00 for in network, family coverage). Uses the monetary amount [object](#eligibility-monetary-amount).                                                                                                                                       |
| coverage.non_covered.delivery                       | Object containing service delivery information. Uses the delivery [object](#eligibility-delivery).                                                                                                                                                                                                                                                                                                                                                                                    |
| coverage.non_covered.time_period                    | Defines the time frame in which services are to be rendered or continued. A full list of possibilities can be seen [below](#eligibility_time_period_qualifier).                                                                                                                                                                                                                                                                                                                       |
| coverage.non_covered.service_types                  | The service type(s) returned by the trading partner. A full listing of possible service_types values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                                |
| coverage.non_covered.service_type_codes             | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.non_covered.procedure_id                   | The unique identifier of the procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.non_covered.procedure_id_qualifier         | The qualifier associated with the procedure id (e.g. cpt). A full list of possible values is included [below](#procedure-id-qualifier).                                                                                                                                                                                                                                                                                                                                               |
| coverage.non_covered.quantity                       | The quantity amount specified by quantity_qualifier. |
| coverage.non_covered.quantity_qualifier             | The qualifier used to indicate the quantity type. A full list of possible values is included [below](#quantity-qualifier). |   
| coverage.service_types                              | The service type(s) returned by the trading partner. A full listing of possible service_types values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                                |
| coverage.service_type_codes                         | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| coverage.procedure_id                               | The unique identifier of the procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.procedure_id_qualifier                     | The qualifier associated with the procedure id (e.g. cpt). A full list of possible values is included [below](#procedure-id-qualifier).                                                                                                                                                                                                                                                                                                                                               |
| coverage.plan_date                                  | The plan date associated with the coverage. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                                                                           |
| coverage.primary_care_provider                      | The primary care provider for the eligibility check.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| coverage.primary_care_provider.phone                | The phone number for the primary care provider.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| coverage.primary_care_provider.email                | The email for the primary care provider.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.primary_care_provider.url                  | The URL associated with the primary care provider.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| coverage.primary_care_provider.fax                  | The fax number for the primary care provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| coverage.primary_care_provider.address              | The primary care provider's address information. Uses the address [object](#eligibility-address).                                                                                                                                                                                                                                                                                                                                                                                     |
| coverage.primary_care_provider.first_name           | The primary care provider's first name.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| coverage.primary_care_provider.middle_name          | The primary care provider's middle name.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| coverage.primary_care_provider.last_name            | The primary care provider's last name.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| coverage.primary_care_provider.suffix               | The primary care provider's suffix.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.primary_care_provider.organization_name    | The primary care provider's name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                                                                                                                                                                                                                                                                                                     |
| coverage.primary_care_provider.messages.message     | Messages associated with the primary care provider.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| coverage.primary_care_provider.primary_care_provider_begin_date | The primary care provider begin date.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| coverage.primary_care_provider.primary_care_provider_end_date | The primary care provider end date. |
| coverage.plans                                      | A complete list of plans that are included in the member's coverage. |
| coverage.eligibility_begin_date                     | The date eligibility started for the member's plan. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.eligibility_end_date                       | The date eligibility ends for the member's plan. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.policy_effective_date                       | The date the member's policy becomes effective. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.policy_expiration_date                       | The date the member's policy expires. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                                                                   |
| coverage.group_description                          | Group description for the member specified in the eligibility request.                                                                                                                                                                                                                                                                                                                                                                                                                |
| coverage.group_number                               | Group number for the member specified in the eligibility request.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| coverage.insurance_type                             | The type of insurance coverage. Possible values include: hmo, ppo, pos, cobra, commercial, medicaid, medicare_part_a, medicare_part_b, other.                                                                                                                                                                                                                                                                                                                                          |
| coverage.level                                      | The coverage level the member has for their plan. Possible values include: employee_only, employee_and_spouse, employee_and_children, family, individual.                                                                                                                                                                                                                                                                                                                              |
| coverage.plan_begin_date                            | The date that plan coverage started for the member specified in the eligibility response. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                              |
| coverage.plan_end_date                              | The date that plan coverage ends for the member specified in the eligibility response. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                                 |
| coverage.plan_description                           | The product name or special program name for the insurance plan. This is often the brand or marketing name for the plan.                                                                                                                                                                                                                                                                                                                                                              |
| coverage.plan_number                                | The plan number for the member specified in the eligibility response.                                                                                                                                                                                                                                                                                                                                                                                                             |
| coverage.quantity                                   | The quantity amount specified by quantity_qualifier. |
| coverage.quantity_qualifier                         | The qualifier used to indicate the quantity type. A full list of possible values is included [below](#quantity-qualifier). |   
| coverage.service_date                               | The date the eligibility request was processed. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                                                                       |
| follow_up_action                                    | When an eligibility request is rejected, a follow up action will be provided to inform your application how to proceed. Possible values include: correct_and_resubmit, resubmit_original, resubmission_not_allowed.                                                                                                                                                                                                                                                                    |
| dependent                                           | The dependent associated with the eligibility response.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| dependent.address                                   | The dependent's address information. Uses the address [object](#eligibility-address).                                                                                                                                                                                                                                                                                                                                                                                                 |
| dependent.gender                                    | The dependent's gender.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| dependent.first_name                                | The dependent's first name.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| dependent.middle_name                               | The dependent's middle name.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| dependent.last_name                                 | The dependent's last name.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| dependent.id                                        | The dependent's unique identifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| dependent.relationship                              | The dependent's relationship.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| dependent.group_number                              | The group number associated with the dependent.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| dependent.rejections                                | Reject reasons related to errors in the dependent section of the eligibility submission.                                                                                                                                                                                                                                                                     |
| payer                                               | The payer returned by the trading partner for the eligibility response. Uses the payer [object](#eligibility-payer).                                                                                                                                                                                                                                                                                                                                                                |
| payer.rejections                                    | Reject reasons related to errors in the payer section of the eligibility submission.                                                                                                                                                                                                                                                                     |
| pharmacy.benefits_manager                           | The pharmacy benefits manager information.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| pharmacy.benefit_date                               | The benefit date associated with pharmacy benefits. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                                                                                                                                                                                                                        |
| pharmacy.benefits_manager.name                      | The name of the entity that is responsible for managing pharmacy benefits.                                                                                                                                                                                                                                                                                                                                                                                                            |
| pharmacy.benefits_manager.phone                     | Contact phone number for the pharmacy benefits manager.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| pharmacy.benefits_manager.url                       | The pharmacy benefits manager's web site.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| pharmacy.benefits_manager.coverage_description      | The coverage description associated with the pharmacy benefits manager.                                                                                                                                                                                                                                                                                                                                                                                                               |
| pharmacy.is_eligible                                | A boolean value used to indicate if the member specified in the eligibility request has active pharmacy benefits.                                                                                                                                                                                                                                                                                                                                                                     |
| pharmacy.plan_number                                | Plan ID/number for the member's pharmacy benefits.  A pharmacy plan number will be present when trading partners include it in their eligibility response.  For example, medicare members will have pharmacy.plan_number populated if they're enrolled in a Medicare Part D Prescription Drug Plan.                                                                                                                                                                                   |
| pharmacy.copay                                      | A list of copay data that will be included when available from the associated pharmacy.                                                                                                                                                                                                                                                                                                                                                                                               |
| pharmacy.copay.copayment                            | The copayment amount associated with a copay. Uses the monetary amount [object](#eligibility-monetary-amount).                                                                                                                                                                                                                                                                                                                                                                        |
| pharmacy.copay.tier                                 | The tier associated with a pharmacy copay.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| pharmacy.copay.type                                 | The service type(s) the copay is being made for. A full listing of possible service_types values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                                                  |
| pharmacy.copay.notes                                | Any notes associated with a pharmacy copay.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pharmacy.copay.supply                               | The supply associated with a pharmacy copay.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| provider.npi                                        | The NPI for the provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| provider.first_name                                 | The provider’s first name when the provider is an individual.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| provider.middle_name                                | The provider’s middle name when the provider is an individual.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| provider.last_name                                  | The provider’s last name when the provider is an individual.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| provider.suffix                                     | The provider’s suffix when the provider is an individual.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| provider.pin                                        | The provider’s personal identification number.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| provider.organization_name                          | The provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                                                                                                                                                                                  |
| provider.rejections                                 | Reject reasons related to errors in the provider section of the eligibility submission.                                                                                                                                                                                                                                                                     |
| reject_reason                                       | When a trading partner is unable to provide eligibility information for an eligibility request, they will provide a reject reason. A full list of reasons and their description is included [below](#reject-reason).                                                                                                                                                                                                                                                        |
| subscriber                                          | The subscriber associated with the eligibility request. Uses the subscriber [object](#eligibility-subscriber).                                                                                                                                                                                                                                                                                                                                                                        |
| subscriber.rejections                               | Reject reasons related to errors in the subscriber section of the eligibility submission.                                                                                                                                                                                                                                                                     |
| trading_partner_id                                  | Unique id for the trading partner used to process the request.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| service_types                                       | The service type(s) returned by the trading partner. A full listing of possible service_types values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                                |
| service_type_codes                                  | The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).                                                                                                                                                                                                                                                                                                                        |
| valid_request                                       | A boolean value used to indicate that a trading partner considered the eligibility request valid and returned a full eligibility response. If valid_request is false, it means the trading partner was unable to respond to the request. Check the parameters reject_reason and follow_up_action for more information on how to proceed when valid_request is false.                                                                                                                  |
| summary                                             | Summary section for convenience as a quick overview of a member's deductible and out-of-pocket information.                                                                                                                                                                                                                                                                                                                                                                           |
| summary.services                                    | Like its parent summary but embedded in a dictionary. Has the same deductible and out-of-pocket summaries that its parent contains.                                                                                                                                                                                                                                                                                                                                                   |
| summary.deductible                                  | List of deductible information for the member for overall health benefit plan coverage.                                                                                                                                                                                                                                                                                                                                                                                               |
| summary.deductible.family                           | Family deductible information.  The subproperties can be seen [below](#deductible-outofpocket).                                                                                                                                                                                                                                                                                                                                                                                       |
| summary.deductible.individual                       | Individual deductible information. The subproperties can be seen [below](#deductible-outofpocket).                                                                                                                                                                                                                                                                                                                                                                                    |
| summary.out_of_pocket                               | List of out-of-pocket (stop loss) information for the member for overall health benefit plan coverage.                                                                                                                                                                                                                                                                                                                                                                                |
| summary.out_of_pocket.family                        | Family out-of-pocket information.  The subproperties can be seen [below](#deductible-outofpocket).                                                                                                                                                                                                                                                                                                                                                                                       |
| summary.out_of_pocket.individual                    | Individual out-of-pocket information. The subproperties can be seen [below](#deductible-outofpocket).                                                                                                                                                                                                                                                                                                                                                                                    |

<!--- end of table -->

### Additional Object Tables

<a name="eligibility-payer"></a>
Payer Object

<!--- beginning of table -->


| Parameter                  | Description                                                                           |
|:---------------------------|:--------------------------------------------------------------------------------------|
| id                         | The unique identifier of the payer                                                    |
| tax_id                     | The unique tax identifier of the payer                                                |
| name                       | The name of the payer.                                                                |
| phone                      | The phone number of the payer.                                                        |
| email                      | The email of the payer.                                                               |
| url                        | The the url associacted with the payer                                                |
| fax                        | The fax of the payer.                                                                 |

<!--- end of table -->

<a name="eligibility-address"></a>
Address Object:

<!--- beginning of table -->

| Field                                 | Description                                                                                                       |
|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| address_lines                         | List of strings representing the street address. (e.g. ["123 MAIN ST.", "Suite 4"])                               |
| city                                  | The city component of a address. (e.g. "SAN MATEO")                                                               |
| state                                 | The state component of a address. (e.g. "CA")                                                                     |
| zipcode                               | The zip/postal code. (e.g. "94401")                                                                               |
| country                               | The country component of a address.                                                                               |

<!--- end of table -->

<a name="eligibility-subscriber"></a>
Subscriber Object

<!--- beginning of table -->

| Parameter                  | Description                                                                                                                                                                                                                                                                                      |
|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| address                    | The subscriber's address information. Uses the address [object](#eligibility-address).                                                                                                                                                                                                           |
| id                         | The subscriber's member identifier.                                                                                                                                                                                                                                                              |
| first_name                 | The subscriber’s first name as specified on their policy.                                                                                                                                                                                                                                        |
| middle_name                | The subscriber's middle name as specified on their policy.                                                                                                                                                                                                                                       |
| last_name                  | The subscriber’s last name as specified on their policy.                                                                                                                                                                                                                                         |
| birth_date                 | The subscriber’s birth date as specified on their policy. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                                                        |
| gender                     | The subscriber’s gender as specified on their policy. Possible values include: 'female', 'male', and 'unknown'. 'unknown' will be returned when gender is not specified in the trading partner's eligibility data or when the trading partner explicitly returns a value of 'unknown'.           |
| relationship               | The subscriber's relationship.                                                                                                                                                                                                                                                                   |
| group_number               | Group number for the subscriber.                                                                                                                                                                                                                                                                 |
| military_personnel_information | Information pertaining to the subscriber's military service.  This information may be returned for dependents as well.  Uses the military personnel information [object](#eligibility-military).
										|

<!--- end of table -->


<a name="eligibility-military"></a>
Military Personnel Information Object

<!--- beginning of table -->

| Parameter                  | Description                                                                                                                                                                                                                                                                                      |
|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| information_status         | The status of the subscriber's military information.  (ex: partial, current, prior)                                                                                                                                                                                   				                                |
| employment_status          | The status of the subscriber's military employment.  (ex: active_reserve, contractor, retired_military_usa)                                                                                                                                                                                    |
| government_service_affiliation     | The government service affiliation of the subscriber. (ex: air_force, army, navy)                                                                                                                                                                                                          |
| description                | Used to clarify the exact military unit.                                                                                                                                                                                                                                                           |
| rank                       | The subscriber's military rank.                                                                                                                                                                                                                                                                    |
| start_date                 | The start date defined for military service.                                                                                                                                                                                                                                                       |
| end_date                   | The end date defined for military service.                                                                                                                                                                                                                                                         |

<!--- end of table -->


<a name="eligibility-delivery"></a>
Delivery Object:

<!--- beginning of table -->

| Field                                 | Description                                                                                                                                                                               |
|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| units                                 | The units of services being requested.                                                                                                                                                    |
| sample_selection_modulus              | Specify the sampling frequency in terms of a modulus of the Unit of Measure, e.g., every fifth bag, every 1.5 minutes.                                                                    |
| time_period_qualifier                 | Defines the time frame in which services are to be rendered or continued. A full list of possibilities can be seen [below](#eligibility_time_period_qualifier).                           |
| period_count                          | Used to indicate the number of time_period_qualifiers.                                                                                                                                    |
| delivery_frequency_code               | Code which specifies frequency by which services can be performed.                                                                                                                        |
| delivery_pattern_time_code            | Code which specifies the time delivery pattern of the services.                                                                                                                           |
| quantity                              | The quantity of services being requested.                                                                                                                                                 |
| quantity_qualifier                    | The qualifier used to indicate the quantity type. A full list of possible values is included [below](#quantity-qualifier). |   

<!--- end of table -->

<a name="eligibility-monetary-amount"></a>
Monetary Amount Object:

<!--- beginning of table -->

| Field                                 | Description                                                                                                                                                                               |
|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| amount                                | The value amount for this item.                                                                                                                                                           |
| currency                              | The currency used in the amount.                                                                                                                                                          |

<!--- end of table -->

<a name="deductible-outofpocket"></a>
Object base that is used both by the deductible summary and out of pocket summary:

<!--- beginning of table -->

| Field                                 | Description                                                                                                                                                                               |
|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| limit                                 | Monetary limit value associated with a deductible. Uses the monetary amount [object](#eligibility-monetary-amount).                                                                       |
| applied                               | Monetary value applied to a deductible. Uses the monetary amount [object](#eligibility-monetary-amount).                                                                                  |
| remaining                             | Monetary value remaining related to a deductible. Uses the monetary amount [object](#eligibility-monetary-amount).                                                                        |

<!--- end of table -->


<a name="benefit-related-entities"></a>
Benefit Related Entities Object:

<!--- beginning of table -->

| Field                                 | Description                                                                                                                                                                               |
|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| entity_identifier_code                | Identifies entity as organization, physical location, property or individual.															  |
| entity_type                           | Defines the entity as either a person or non-person.							                                                                            	          |
| first_name                            | The first name of the entity if the entity is identified as an individual.			                                                            	                  		  |
| middle_name	                        | The middle name of the entity if the entity is identified as an individual.															  |
| last_name                             | The last name of the entity if the entity is identified as an individual.                                                                              		     			      |
| organization_name                     | The name of the organization if the entity is identified as non-person.
														  |
| suffix	                        | The suffix of the entity if the entity is identified as an individual.															  |
| id_qualifier                          | Indicates the code set being used for for the id (ex: centers_for_medicare_medicaid_npi, federal_taxpayer_identification, facility_identification).                     |
| id                                    | The identification code for the entity.
														  |
| relationship_code                     | The benefit related entity's relationship to the patient.																	  |
| address                               | The address for the entity.  Uses the address [object](#eligibility-address).                                                                          				              |
| contacts                              | The contact information for the entity.
                                                                     				                  |
| provider_code                         | Identifies the type of provider (ex: admitting, consulting, hospital).                                                                       						             |
| taxonomy_code                         | The taxonomy code for the entity.
                                                            						          |
| eligibility_or_benefit_information    | The eligibility or benefit information indicator returned by the trading partner.  Possible values include deductible, active_coverage, other_source_of_data, etc.
                                                            						          |
| coverage_level		        | The coverage level that applies to the eligibility or benefit information returned by the trading partner.  A full list of possible values is included [below](#coverage-level).
                                                            						          |
| service_types			  	| The service type(s) returned by the trading partner. A full listing of possible service_types values is included [below](#service-type).
                                                            						          |
| service_type_codes			| The service type codes returned by the trading partner. A full listing of possible service_type_codes values is included [below](#service-type).
                                                            						          |
| benefit_amount			| The monetary amount associated with the eligibility_or_benefit_information and service_types provided. Uses the monetary amount [object](#eligibility-monetary-amount).
                                                            						          |

<!--- end of table -->


<a name="procedure-id-qualifier"></a>
Full list of possible `procedure_id_qualifier` values that may be used in the eligiblity request or returned in an eligibility response:

<!--- beginning of table -->

| procedure_id_qualifier                |                 |
|:--------------------------------------|:----------------|
| ada_code                              | cpt             |
| hcpcs                                 | icd_9_cm        |
| hiec_product_service_code             | ndc_5_4_2_format|
| mutually_defined                      |                 |

<!--- end of table -->

<a name="coverage-level"></a>
Full list of possible `coverage_level` values that may be returned in an eligibility response:

<!--- beginning of table -->

| coverage_level                        |                           |
|:--------------------------------------|:--------------------------|
| children_only                         | dependents_only           |
| employee_and_children                 | employee_only             |
| employee_and_spouse                   | family                    |
| individual                            | spouse_and_children       |
| spouse_only                           |                           |

<!--- end of table -->

<a name="eligibility_time_period_qualifier"></a>
Possible values that can be used in the `delivery.time_period_qualifier` parameter:

<!--- beginning of table -->

| time_period_qualifier Values |                    |
|:-----------------------------|:-------------------|
| 24_hours                     | admission          |
| calendar_year                | contract           |
| day                          | episode            |
| exceed                       | hour               |
| lifetime                     | lifetime_remaining |
| month                        | not_exceeded       |
| outlier                      | remaining          |
| service_year                 | visit              |
| week                         | year_to_date       |
| years                        |                    |

<!--- end of table -->

<a name="quantity-qualifier"></a>
Possible values that can be used as `quantity_qualifier` parameter:

<!--- beginning of table -->

| quantity_qualifier Values |                            |
|:--------------------------|:---------------------------|
| minimum | quantity_used |
| covered_actual | covered_estimated |
| coinsurance_days | deductible_blood_units |
| days | hours |
| life_time_reserve_actual | life_time_reserve_estimated |
| maximum | month |
| services_or_procedures | quantity_approved |
| age_high_value | age_low_value |
| visits | years |

<!--- end of table -->

<a name="service-type"></a>
Full list of possible `service_type` values with the associated code (from X12 specification) that may be used in the eligiblity request or returned in an eligibility response:

<!--- beginning of table -->

| service_type                                          | Code (X12 Spec) |
|:------------------------------------------------------|:----------------|
| abortion                                              | 84              |
| acupuncture                                           | 64              |
| adjunctive_dental_services                            | 28              |
| aids                                                  | 85              |
| air_transportation                                    | 57              |
| alcoholism                                            | AJ              |
| allergy                                               | GY              |
| allergy_testing                                       | 79              |
| allied_behavioral_analysis_therapy                    | E0              |
| alternate_method_dialysis                             | 15              |
| ambulatory_service_facility                           | 13              |
| anesthesia                                            | 7               |
| anesthesiologist                                      | 97              |
| audiology_exam                                        | 71              |
| basic_restorative_dental                              | E12             |
| blood_charges                                         | 10              |
| brand_name_prescription_drug                          | 91              |
| brand_name_prescription_drug_formulary                | B2              |
| brand_name_prescription_drug_non_formulary            | B3              |
| burn_care                                             | B1              |
| cabulance                                             | 58              |
| cancer                                                | 87              |
| cardiac                                               | BL              |
| cardiac_rehabilitation                                | BG              |
| case_management                                       | CQ              |
| cat_scan                                              | ED              |
| chemotherapy                                          | 78              |
| chiropractic                                          | 33              |
| chiropractic_office_visits                            | 34              |
| chronic_renal_disease_equipment                       | 16              |
| cognitive_therapy                                     | BD              |
| comprehensive_medication_therapy_management_review    | E26             |
| consultation                                          | 3               |
| contact_lenses                                        | EF              |
| convenience_care                                      | E36             |
| coronary_care                                         | C1              |
| day_care_psychiatric                                  | BC              |
| dental_accident                                       | 37              |
| dental_care                                           | 35              |
| dental_coverage                                       | F3              |
| dental_crowns                                         | 36              |
| dental_implants                                       | E22             |
| dental_prophylaxis                                    | E18             |
| dermatology                                           | DG              |
| diabetic_education                                    | E39             |
| diabetic_supplies                                     | DS              |
| diagnostic_dental                                     | 23              |
| diagnostic_imaging                                    | E11             |
| diagnostic_lab                                        | 5               |
| diagnostic_medical                                    | 73              |
| diagnostic_x_ray                                      | 4               |
| dialysis                                              | 76              |
| dietary_nutritional_services                          | E28             |
| donor_procedures                                      | 63              |
| drug_addiction                                        | AK              |
| durable_medical_equipment_new                         | EC              |
| emergency_services                                    | 86              |
| endocrine                                             | BP              |
| endodontics                                           | 26              |
| experimental_drug_therapy                             | AR              |
| eye                                                   | BR              |
| eyewear_and_accessories                               | CP              |
| family_planning                                       | 82              |
| fixed_prosthodontics                                  | E14             |
| flouride_treatments                                   | E21             |
| flu_vaccination                                       | CO              |
| frames                                                | AM              |
| free_standing_prescription_drug                       | 89              |
| gastrointestinal                                      | BN              |
| general_benefits                                      | 60              |
| generic_prescription_drug                             | 92              |
| generic_prescription_drug_formulary                   | GF              |
| generic_prescription_drug_non_formulary               | GN              |
| gynecological                                         | BT              |
| health_benefit_plan_coverage                          | 30              |
| hearing_coverage                                      | F4              |
| home_health_care                                      | 42              |
| home_health_prescriptions                             | 43              |
| home_health_visits                                    | 44              |
| hospice                                               | 45              |
| hospital                                              | 47              |
| hospital_ambulatory_surgical                          | 53              |
| hospital_emergency_accident                           | 51              |
| hospital_emergency_medical                            | 52              |
| hospital_inpatient                                    | 48              |
| hospital_outpatient                                   | 50              |
| hospital_room_and_board                               | 49              |
| immunizations                                         | 80              |
| in_vitro_fertilization                                | 61              |
| independent_medical_evaluation                        | BA              |
| infertility                                           | 83              |
| inhalation_therapy                                    | 72              |
| intensive_cardiac_rehabilitation                      | E33             |
| intensive_cardiac_rehabilitation_technical_component  | E32             |
| intensive_care                                        | IC              |
| intraoral_images_complete_series                      | E16             |
| invasive_procedures                                   | BS              |
| lenses                                                | AO              |
| level_of_care_1                                       | E6              |
| level_of_care_2                                       | E7              |
| level_of_care_3                                       | E8              |
| level_of_care_4                                       | E9              |
| licensed_ambulance                                    | 59              |
| long_term_care                                        | 54              |
| long_term_care_pharmacy                               | E25             |
| lymphatic                                             | BM              |
| mail_order_prescription_drug                          | BX              |
| mail_order_prescription_drug_brand_name               | 90              |
| mail_order_prescription_drug_generic                  | BW              |
| major_medical                                         | 55              |
| major_restorative_dental                              | E13             |
| mammogram_high_risk_patient                           | CM              |
| mammogram_low_risk_patient                            | CN              |
| massage_therapy                                       | BE              |
| maternity                                             | 69              |
| maxillofacial_prosthetics                             | 27              |
| medical_care                                          | 1               |
| medical_coverage                                      | F1              |
| medical_equipment                                     | DM              |
| medical_equipment_purchase                            | 12              |
| medical_equipment_rental                              | 18              |
| medically_related_transportation                      | 56              |
| mental_health                                         | MH              |
| mental_health_coverage                                | F8              |
| mental_health_facility_inpatient                      | CG              |
| mental_health_facility_outpatient                     | CH              |
| mental_health_provider_inpatient                      | CE              |
| mental_health_provider_outpatient                     | CF              |
| mri_cat_scan                                          | 62              |
| neonatal_intensive_care                               | NI              |
| neurology                                             | BQ              |
| newborn_care                                          | 65              |
| non_medical_equipment_non_dme                         | E1              |
| nonmedically_necessary_physical                       | AQ              |
| nursery                                               | BI              |
| obstetrical                                           | BU              |
| obstetrical_gynecological                             | BV              |
| occupational_therapy                                  | AD              |
| oncology                                              | ON              |
| ophthalmology                                         | EE              |
| oral_evaluation                                       | E17             |
| oral_surgery                                          | 40              |
| orthodontics                                          | 38              |
| orthodontia_coverage                                  | F7              |
| orthopedic                                            | BK              |
| other_medical                                         | 9               |
| otological_exam                                       | 77              |
| panoramic_images                                      | E19             |
| partial_hospitalization_psychiatric                   | BB              |
| pathology                                             | 66              |
| pediatric                                             | BH              |
| periodontics                                          | 24              |
| pharmacist_services                                   | E38             |
| pharmacy                                              | 88              |
| physical_medicine                                     | AE              |
| physical_therapy                                      | PT              |
| physician_visit_office_sick                           | BY              |
| physician_visit_office_well                           | BZ              |
| plan_waiting_period                                   | 32              |
| pneumonia_vaccine                                     | 19              |
| podiatry                                              | 93              |
| podiatry_nursing_home_visits                          | 95              |
| podiatry_office_visits                                | 94              |
| positron_emission_tomography_pet_scan                 | PE              |
| pre_admission_testing                                 | 17              |
| prescription_drug_coverage                            | F5              |
| preventive_services                                   | EA              |
| private_duty_nursing                                  | 74              |
| private_duty_nursing_home                             | CB              |
| private_duty_nursing_inpatient                        | CA              |
| professional_cardiac_rehabilitation_services_component| E30             |
| professional_intensive_cardiac_rehabilitation_services_component  | E31             |
| professional_physician                                | 96              |
| professional_physician_visit_home                     | A3              |
| professional_physician_visit_inpatient                | 99              |
| professional_physician_visit_nursing_home             | A1              |
| professional_physician_visit_office                   | 98              |
| professional_physician_visit_outpatient               | A0              |
| professional_physician_visit_skilled_nursing_facility | A2              |
| prosthetic_device                                     | 75              |
| prosthodontics                                        | 39              |
| psychiatric                                           | A4              |
| psychiatric_emergency                                 | E2              |
| psychiatric_inpatient                                 | A7              |
| psychiatric_outpatient                                | A8              |
| psychiatric_room_and_board                            | A5              |
| psychotherapy                                         | A6              |
| pulmonary                                             | PU              |
| pulmonary_rehabilitation                              | BF              |
| pulmonary_rehabilitation_professional_component       | E35             |
| pulmonary_rehabilitation_technical_component          | E34             |
| radiation_therapy                                     | 6               |
| radiographs                                           | E10             |
| rehabilitation                                        | A9              |
| rehabilitation_inpatient                              | AB              |
| rehabilitation_outpatient                             | AC              |
| rehabilitation_room_and_board                         | AA              |
| removable_prosthodontics                              | E15             |
| renal                                                 | RN              |
| renal_supplies_in_the_home                            | 14              |
| residential_psychiatric_treatment                     | RT              |
| respite_care                                          | 46              |
| restorative                                           | 25              |
| retail_pharmacy_prescription_drug                     | E24             |
| routine_exam                                          | AN              |
| routine_eye_exam                                      | AP              |
| routine_physical                                      | 81              |
| routine_preventive_dental                             | 41              |
| screening_laboratory                                  | CL              |
| screening_x_ray                                       | CK              |
| sealants                                              | E20             |
| second_surgical_opinion                               | 20              |
| serious_mental_health                                 | SMH             |
| skilled_nursing_care                                  | AG              |
| skilled_nursing_care_room_and_board                   | AH              |
| skilled_nursing_facility_head_level_of_care           | E4              |
| skilled_nursing_facility_ventilator_level_of_care     | E5              |
| skin                                                  | BJ              |
| smoking_cessation                                     | 67              |
| social_work                                           | 22              |
| social_work_coverage                                  | F2              |
| specialty_pharmacy                                    | EB              |
| speech_therapy                                        | AF              |
| step_down_unit                                        | E3              |
| substance_abuse                                       | AI              |
| substance_abuse_facility_inpatient                    | CI              |
| substance_abuse_facility_outpatient                   | CJ              |
| surgical                                              | 2               |
| surgical_assistance                                   | 8               |
| surgical_benefits_facility                            | CD              |
| surgical_benefits_professional_physician              | CC              |
| targeted_medication_therapy_management_review         | E27             |
| technical_cardiac_rehabilitation_services_component   | E29             |
| telemedicine                                          | E37             |
| temporomandibular_joint_dysfunction                   | E23             |
| third_surgical_opinion                                | 21              |
| transitional_care                                     | TC              |
| transitional_nursery_care                             | TN              |
| transplants                                           | 70              |
| urgent_care                                           | UC              |
| used_medical_equipment                                | 11              |
| vision_coverage                                       | F6              |
| vision_optometry                                      | AL              |
| well_baby_care                                        | 68              |

<!--- end of table -->


<a name="authz-req"></a>
Full list of possible `authorization_required` values returned (or not) in an eligibility response:

<!--- beginning of table -->

| value   | Meaning                                                                                            |
|:--------|:---------------------------------------------------------------------------------------------------|
| yes     | indicates that an authorization or certification is required per plan provisions                   |
| no      | indicates that an authorization or certification is not required per plan provisions               |
| unknown | indicates that it is unknown whether the plan provisions require an authorization or certification |

<!--- end of table -->

**NOTE:** authorization_required is situational, so it could also be empty


<a name="reject-reason"></a>
Most common `reject_reasons` on the eligibility response with description:

<!--- beginning of table -->

| reject_reason                   | Description                                                                                                                                            |
|:--------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| invalid_provider_id             | submitting provider (NPI) is not valid, please submit with a valid NPI                                                                                 |
| provider_not_on_file            | submitting provider (NPI) is not valid, please submit with a valid NPI                                                                                 |
| provider_ineligible_for_inquiries | submitting provider (NPI) is not valid, please submit with a valid NPI
							          |
| invalid_subscriber_id           | subscriber id not found                                                                                                                                |
| invalid_subscriber_insured_id   | subscriber id not found                                                                                                                                |
| invalid_subscriber_insured_name | subscriber name not found                                                                                                                              |
| subscriber_insured_not_found    | subscriber not found                                                                                                                                   |
| patient_birth_date_mismatch     | birth date does not match subscriber found                                                                                                             |
| unable_to_respond_now           | trading partner is experiencing downtime and not able to complete request.  if this is a known outage the response meta section and PokitDok [status page](https://pokitdok.com/status/) will have more details.|

<!--- end of table -->
