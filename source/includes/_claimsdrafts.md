## Claims Drafts




### Endpoint Description

<!--- beginning of table -->

| Endpoint | HTTP Method | Description                                      |
|:---------|:------------|:-------------------------------------------------|
| /claims/drafts/ | POST | Submit a new claim object for storage. |
| /claims/drafts/ | GET | Fetch an index listing of current claim drafts that have been stored.|
| /claims/drafts/id | GET | Fetch an existing Claim Draft object that was previously stored.|
| /claims/drafts/id | PUT | Update an existing claim draft object. |
| /claims/drafts/id | DELETE | Remove a claim draft from the system. |
| /claims/validate/ | POST | Validate a claims request based on the X12 837 specifications. |
| /claims/drafts/id/validate | GET | Fetch a claim draft's validation status. |
<!--- end of table -->

### Parameters

The `/claims/drafts/` and `/claims/validate/` endpoint accepts the same parameters as the Claims endpoint [here](#claims).

### Response

The `/claims/drafts` response contains the following fields:


<!--- beginning of table -->

| Parameter | Description | 
|:---------|:-----------|
| id | The ID of the draft. |
| draft | The claim draft. |
| validation_result | The result of the validation if requested. |

<!--- end of table -->
