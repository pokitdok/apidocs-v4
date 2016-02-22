## Medical Procedure Code
> example fetching medical procedure information by code

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/mpc/99213
```

```python
pd.mpc(code='99213')
```

```csharp
client.medicalProcedureCode("99211");
```


> curl example searching medical procedure information by consumer friendly name

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" https://platform.pokitdok.com/api/v4/mpc/?name=office
```

```python
pd.mpc(name='office')
```

```csharp
client.medicalProcedureCode(
            new Dictionary<string, string> {
                {"name", "Established patient office or other outpatient visit, typically 15 minutes"}
            });
```

*Available modes of operation: real-time only*

The Medical Procedure Code endpoints provide access to clinical and consumer
friendly information related to medical procedures. It's useful for identifying
the procedure code (or codes) that match search queries. It can also be used
for determining the official descriptions for a specific procedure code.

Available Medical Procedure Code Endpoints:

| Endpoint    | HTTP Method | Description                                                                 |
|:------------|:------------|:----------------------------------------------------------------------------|
| /mpc/       | GET         | Get a list of medical procedure information meeting certain search criteria |
| /mpc/{code} | GET         | Retrieve the data for a specific procedure code                             |
The /mpc/ endpoint accepts the following parameters:

| Field       | Type     | Description                                                                      |
|:------------|:---------|:---------------------------------------------------------------------------------|
| name        | {string} | Search medical procedure information by consumer friendly name                   |
| description | {string} | A partial or full description to be used to locate medical procedure information |

The /mpc/ response contains the following fields

| Field       | Type     | Description                                        |
|:------------|:---------|:---------------------------------------------------|
| code        | {string} | The procedure code                                 |
| name        | {string} | A consumer friendly name for the medical procedure |
| description | {string} | The medical procedure's clinical description       |
