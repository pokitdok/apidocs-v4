## Cash Prices
> Example fetching cash price information:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/prices/cash?cpt_code=87799&zip_code=32218
```

```python
pd.cash_prices(zip_code='32218', cpt_code='87799')
```

```csharp
client.pricesCash(
			new Dictionary<string, string> {
				{ "zip_code", "30012" },
				{ "cpt_code", "88142" }
			});
```

*Available modes of operation: real-time*

The Cash Prices endpoint allow access to our internal collection of pricing
data. The data comes from actual providers selling actual services. For a
location where a cash price has not been collected, a price is estimated using a
multivariate model.

While the endpoint requires a five-digit zip code, only the first three digits
are significant. This is because the index is only granular to the first three
digits of the zip code, commonly called a "geozip" or a "ZIP Code Prefix". These
three digits refer to the geographical regions surrounding major cities or
metropolitan areas. There are approximately 900 "geozips" in the United States.

| Endpoint     | HTTP Method | Description                                                                                 |
|:-------------|:------------|:--------------------------------------------------------------------------------------------|
| /prices/cash | GET         | Return a list of prices for a given procedure (by CPT Code) in a given region (by ZIP Code) |

The /prices/cash endpoint accepts the following parameters:

| Field    | Type     | Description                                |
|:---------|:---------|:-------------------------------------------|
| cpt_code | {string} | The CPT code of the procedure in question  |
| zip_code | {string} | Zip code in which to search for procedures |

The /prices/cash response contains the following fields:

| Field                      | Type      | Description                                                               |
|:---------------------------|:----------|:--------------------------------------------------------------------------|
| amounts.average_price      | {decimal} | The average cash price for the procedure                                  |
| amounts.cpt_code           | {string}  | The CPT code of the procedure                                             |
| amounts.geo_zip_area       | {string}  | The three character zip code tabulation area code                         |
| amounts.high_price         | {decimal} | The maximum price for the procedure                                       |
| amounts.low_price          | {decimal} | The lowest price for the procedure                                        |
| amounts.median_price       | {decimal} | The median price for the procedure                                        |
| amounts.standard_deviation | {decimal} | The standard deviation, or variation measure, of prices for the procedure |
