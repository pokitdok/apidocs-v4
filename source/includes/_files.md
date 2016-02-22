## Files
> Example sending a batch file of eligibility requests to the MOCKPAYER trading partner

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -XPOST -F file=@eligibility_requests.270 -F trading_partner_id=MOCKPAYER  https://platform.pokitdok.com/api/v4/files/
```

```python
pd.files('MOCKPAYER', 'eligibility_requests.270')
```

```csharp
client.files(
			"MOCKPAYER",
			"../../tests/files/general-physician-office-visit.270"
		);
```

*Available modes of operation: batch/async*

All endpoints that result in the transmission of X12 transaction sets to our trading partners accept parameters via a JSON representation. This keeps applications developers from having to interact directly with raw X12 files.  The Files endpoint, however, accepts raw ASC X12 EDI files for transmission to our trading partners.

The content-type header of a POST request informs the endpoint what is being sent.  Normal, JSON API requests use a content type of "application/edi-x12", "text/plain", or "application/octet-stream" to indicate that a file is being sent.

The Files endpoint is included for legacy purposes, and it is highly recommended to consider
using one of the other endpoints that accepts JSON request payloads.

| Endpoint | HTTP Method | Description                                                         |
|:---------|:------------|:--------------------------------------------------------------------|
| /files/  | POST        | Submit an X12 file to the specified trading partner for processing. |
