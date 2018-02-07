## Claims Drafts




### Endpoint Description

The drafts endpoint allows a user to create and upload claims that are not ready for submission or are intended to be submitted at a later date. Once the drafts are uploaded, Claims Management App users can view the drafts in their app and submit them as 837 claims once they are complete. Since a draft that is uploaded to our system does not pass through our 837 validation, the draft can be submitted while it is still in an incomplete state. The Claims Drafts API is only available to Claims Management App users. For more information about the Claims Management App, please visit our product page: https://pokitdok.com/business/claims-management/ or contact your local biz-dev representative: https://pokitdok.com/contact/

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

The `/claims/validate/` endpoint accepts the same parameters as the Claims endpoint [here](#claims).

The `/claims/drafts` endpoint accepts the folowing parameter:


<!--- beginning of table -->

| Parameter | Description | 
|:---------|:-----------|
| draft | The claim draft. |

<!--- end of table -->

### Response

The `/claims/drafts` response contains the following fields:


<!--- beginning of table -->

| Parameter | Description | 
|:---------|:-----------|
| id | The ID of the draft. |
| draft | The claim draft. |
| validation_result | The result of the validation if requested. |

<!--- end of table -->
