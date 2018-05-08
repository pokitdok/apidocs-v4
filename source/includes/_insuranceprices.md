## Insurance Prices

> example fetching insurance price information

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/prices/insurance?cpt_code=99203&zip_code=94401
```

```python
client.insurance_prices(zip_code='94401', cpt_code='99203')
```

```csharp
client.insurancePrices(
			new Dictionary<string, string> {
				{ "zip_code", "94401" },
				{ "cpt_code", "99203" }
			});
```

```ruby
client.insurance_prices({zip_code: '94401', cpt_code: '99203'})
```

```java
HashMap<String, String>() query = new HashMap<String, String>();
query.put("zip_code", "94401");
query.put("cpt_code", "99203");

client.insurancePrices(query);
```

```swift
try client.insurancePrices(cptCode: "99203", zipCode: "94401")
```

>Example Response:

```json
{
  "amounts": [
    {
      "average_price": 123.3645,
      "high_price": 161.73,
      "low_price": 108.08,
      "median_price": 133.73,
      "payer_type": "insurance",
      "payment_type": "allowed",
      "standard_deviation": 15.85575484603303
    },
    {
      "average_price": 208.80499999999998,
      "high_price": 280.73,
      "low_price": 182.45,
      "median_price": 208.21,
      "payer_type": "insurance",
      "payment_type": "submitted",
      "standard_deviation": 34.80339356657624
    },
    {
      "average_price": 74.22024823703075,
      "high_price": 83.913333333,
      "low_price": 17.922,
      "median_price": 75.92828482041077,
      "payer_type": "medicare",
      "payment_type": "standardized",
      "standard_deviation": 7.521841261411875
    },
    {
      "average_price": 87.68441466859153,
      "high_price": 97.162777778,
      "low_price": 14.5365,
      "median_price": 90.50126353946429,
      "payer_type": "medicare",
      "payment_type": "paid",
      "standard_deviation": 9.672560546364663
    },
    {
      "average_price": 238.48777715084063,
      "high_price": 525,
      "low_price": 125,
      "median_price": 234,
      "payer_type": "medicare",
      "payment_type": "submitted",
      "standard_deviation": 59.51082623548598
    },
    {
      "average_price": 126.08792947814867,
      "high_price": 128.68,
      "low_price": 73.27,
      "median_price": 128.68,
      "payer_type": "medicare",
      "payment_type": "allowed",
      "standard_deviation": 8.986004924696134
    }
  ],
  "geo_zip_area": "944",
  "cpt_code": "99203"
}
```

*Available modes of operation: real-time*

The Insurance Prices endpoint allows access to our collection of insurance
pricing data. The data comes from private payer data as well as data from
Medicare.

While the endpoint requires a five-digit zip code, only the first three digits
are significant. This is because the index is only granular to the first three
digits of the zip code, commonly called a "geozip" or a "ZIP Code Prefix". These
three digits refer to the geographical regions surrounding major cities or
metropolitan areas. There are approximately 900 "geozips" in the United States.

### Endpoint Description

Available Insurance Prices Endpoints:

<!--- beginning of table -->

| Endpoint          | HTTP Method | Description                                                                                 |
|:------------------|:------------|:--------------------------------------------------------------------------------------------|
| /prices/insurance | GET         | Return a list of prices for a given procedure (by CPT Code) in a given region (by ZIP Code) |

<!--- end of table -->

### Parameters

The `/prices/insurance` endpoint accepts the following parameters:

<!--- beginning of table -->

| Parameter  | Type     | Description                                | Presence |
|:-----------|:---------|:-------------------------------------------|:---------|
| cpt_code   | {string} | The CPT code of the procedure in question  | Required |
| zip_code   | {string} | Zip code in which to search for procedures | Required |

<!--- end of table -->

### Response

The `/prices/insurance` response contains the following fields:

<!--- beginning of table -->

| Field                 	  | Type      | Description                                                     | Presence |
|:----------------------------|:----------|:----------------------------------------------------------------|:---------|
| cpt_code      	    	  | {string}  | The CPT code of the procedure                                   | Required |
| geo_zip_area  			  | {string}  | The three character zip code tabulation area code               | Required |
| amounts.high_price    	  | {decimal} | The maximum price for the procedure                             | Required |
| amounts.standard_deviation  | {decimal} | Standard deviation of the insurance price amounts.              | Required |
| amounts.average_price 	  | {decimal} | The weighted average price based on the number of procedures    | Required |
| amounts.low_price     	  | {decimal} | The lowest price for the procedure                              | Required |
| amounts.median_price  	  | {decimal} | The median price for the procedure                              | Required |
| amounts.payer_type    	  | {string}  | The insurance payer type: insurance or medicare                 | Required |
| amounts.payment_type  	  | {string}  | Possible values are "allowed", "submitted", "paid", or "standardized". The allowed amount when payer_type:insurance is the dollar amount typically considered payment-in-full by a payer and an associated network of healthcare providers. For Medicare (when payer_type:medicare) the allowed amount is the average of the Medicare allowed amount for the service; this figure is the sum of the amount Medicare pays, the deductible and coinsurance amounts, and any amounts that a third party is responsible for paying. The submitted amount is the dollar amount the provider submitted to the payer in the insurance claim. The paid amount is the dollar amount that was reimbursed to the provider.  The standardized amount removes geographic differences in payment rates for individual services. | Required |

<!--- end of table -->
