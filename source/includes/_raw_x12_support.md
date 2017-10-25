# Raw X12 Support

The PokitDok Platform allows for raw X12 transactions to be routed through the X12-based APIs.
The default mode of operation for the X12 APIs is to exchange X12-based data in a convenient and simple
JSON request and response format.  This default mode of operation often works well for new companies just
starting out or for companies that wish to no longer operate on X12 healthcare transactions directly.
Some companies may have a significant investment in X12 transaction handling and need to continue using it
with their systems.  In order to help these companies take advantage of other PokitDok Platform capabilities
and services, raw X12 transactions may be routed through the X12 based APIs by adjusting the Content-Type
and Accept header values on their API requests.  When raw X12 processing is requested, the APIs will only
consider the first transaction found in the X12 transaction set.   This ensures a 1-to-1 alignment with
the platform activity tracking that's available for JSON based requests.  If it's desirable to exchange
large batches of transactions via raw X12 files, you may transmit those via sftp and the transactions
from those batch files will be streamed into the platform as activities and associated with your platform application.
[Contact us](/contact) if you wish to exchange transactions via batch files.

## Supported Content-Type and Accept header values

The X12 APIs currently support three different mime type values that may be provided in the Content-Type and Accept
header values to control the input and output data format.

An additional Accept header value to control the output data format is `application/vnd.pokitdok.v4+x12-segments-json`.

### application/json

This is the default Content-Type and Accept value.  Use `application/json` when you wish to use the X12 APIs
using the convenient JSON request and response format.   Request and response examples are included throughout
the API documentation.

### application/vnd.pokitdok.v4+edi-x12-json

Use this value when you'd like to exchange Raw X12 data with the platform and desire to receive `meta` information back
in responses similar to what's returned with the `application/json` response format.

Example Request:
```
{
  "x12": "ISA*...IEA*1*000000001~"
}
```

Example Response:
```
{
  "data": {
    "x12": "ISA*...IEA*1*000000001~"
  },
  "meta": {
    "activity_id": "abcabcabcabcabcabcabcabc",
    "application_mode": "production",
    "credits_billed": 1,
    "credits_remaining": 1000,
    "processing_time": 165,
    "rate_limit_amount": 2,
    "rate_limit_cap": 5000,
    "rate_limit_reset": 1477423058
  }
}
```

### application/vnd.pokitdok.v4+x12-segments-json

This value can be used when you would like to receive the full x12 data back but not in the raw X12 format.

Here's an example full X12 response that you might see from the eligibility API when `application/vnd.pokitdok.v4+x12-segments-json` is requested via the `Accept` header:
```
{
    "x12_segments": [
        {
            "data": {
                "hierarchical_structure_code": "0010", 
                "reference_identification": "69c8aaca-584f-4513-8c13-e22026dd4a39", 
                "transaction_set_creation_date": "20140424", 
                "transaction_set_creation_time": "16521192", 
                "transaction_set_purpose_code": "08", 
                "transaction_type_code": "DG"
            }, 
            "segment_id": "BHT"
        }, 
        {
            "data": {
                "hierarchical_child_code": "1", 
                "hierarchical_id_number": "1", 
                "hierarchical_level_code": "20"
            }, 
            "segment_id": "HL"
        }, 
        {
            "data": {
                "entity_identifier_code": "PR", 
                "entity_type_qualifier": "2", 
                "identification_code_qualifier": "PI", 
                "last_or_organization_name": "PAYERA", 
                "primary_identifier": "60054"
            }, 
            "segment_id": "NM1"
        }, 
        {
            "data": {
                "hierarchical_child_code": "1", 
                "hierarchical_id_number": "2", 
                "hierarchical_level_code": "21", 
                "hierarchical_parent_id": "1"
            }, 
            "segment_id": "HL"
        }, 
        {
            "data": {
                "entity_identifier_code": "41", 
                "entity_type_qualifier": "1", 
                "first_name": "STEPHEN", 
                "identification_code_qualifier": "46", 
                "last_or_organization_name": "KNOX", 
                "primary_identifier": "1255439345"
            }, 
            "segment_id": "NM1"
        }, 
        {
            "data": {
                "hierarchical_child_code": "1", 
                "hierarchical_id_number": "3", 
                "hierarchical_level_code": "19", 
                "hierarchical_parent_id": "2"
            }, 
            "segment_id": "HL"
        }, 
        {
            "data": {
                "entity_identifier_code": "1P", 
                "entity_type_qualifier": "1", 
                "first_name": "STEPHEN", 
                "identification_code_qualifier": "XX", 
                "last_or_organization_name": "KNOX", 
                "primary_identifier": "1255439345"
            }, 
            "segment_id": "NM1"
        }, 
        {
            "data": {
                "hierarchical_child_code": "0", 
                "hierarchical_id_number": "4", 
                "hierarchical_level_code": "22", 
                "hierarchical_parent_id": "3"
            }, 
            "segment_id": "HL"
        }, 
        {
            "data": {
                "entity_identifier_code": "IL", 
                "entity_type_qualifier": "1", 
                "first_name": "JANE", 
                "identification_code_qualifier": "MI", 
                "last_or_organization_name": "DOE", 
                "primary_identifier": "ABC1234567"
            }, 
            "segment_id": "NM1"
        }, 
        {
            "data": {
                "trace_number": "E1TWCYYMF", 
                "trace_type_code": "2"
            }, 
            "segment_id": "TRN"
        }, 
        {
            "data": {
                "claim_payment_amount": "0", 
                "health_care_claim_status": "E0:21", 
                "health_care_claim_status_2": "E0:0", 
                "health_care_claim_status_3": "E0:1", 
                "status_information_effective_date": "20160308", 
                "total_claim_charge_amount": "0"
            }, 
            "segment_id": "STC"
        }, 
        {
            "data": {
                "adjudication_finalized_date": "20140321", 
                "claim_payment_amount": "125", 
                "health_care_claim_status": "F1:107", 
                "remittance_date": "20140409", 
                "remittance_trace_number": "08608-035632423", 
                "status_information_effective_date": "20140424", 
                "total_claim_charge_amount": "150"
            }, 
            "segment_id": "STC"
        }, 
        {
            "data": {
                "reference_identification": "E1TWCYYMF00", 
                "reference_identification_qualifier": "1K"
            }, 
            "segment_id": "REF"
        }, 
        {
            "data": {
                "date_time_period": "20140305-20140305", 
                "date_time_period_format_qualifier": "RD8", 
                "date_time_qualifier": "472"
            }, 
            "segment_id": "DTP"
        }, 
        {
            "data": {
                "composite_medical_procedure_identifier": "HC:99214", 
                "line_item_charge_amount": "150", 
                "line_item_provider_payment_amount": "125", 
                "original_units_of_service_count": "1"
            }, 
            "segment_id": "SVC"
        }, 
        {
            "data": {
                "health_care_claim_status": "F1:107", 
                "status_information_effective_date": "20140424"
            }, 
            "segment_id": "STC"
        }, 
        {
            "data": {
                "date_time_period": "20140305-20140305", 
                "date_time_period_format_qualifier": "RD8", 
                "date_time_qualifier": "472"
            }, 
            "segment_id": "DTP"
        }
    ]
}
```

### application/edi-x12

Use this value when you wish to send and receive raw X12 with no extra wrapping or information.
This mime type is most useful for systems that don't have good JSON support and wish to send and receive
X12 transactions directly.

Example Request data `POST`ed to an X12-based API:
```
ISA*...IEA*1*000000001~
```

Example Response:
```
ISA*...IEA*1*000000001~
```

## Mixing mime types

The platform also supports using different mime type values for requests and responses.
Some systems may prefer to send requests in JSON and receive raw X12 data back (or vice versa).
Feel free to specify the mime types that work best for your system in the Content-Type and Accept headers.

## Examples


Here's an example using cURL that submits a raw X12 270 transaction for real time processing
and receives a raw X12 271 transaction back using the `application/vnd.pokitdok.v4+edi-x12-json`:


```shell
curl -v -XPOST -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/vnd.pokitdok.v4+edi-x12-json" -H "Accept: application/vnd.pokitdok.v4+edi-x12-json"  https://platform.pokitdok.com/api/v4/eligibility/ -d '{"x12": "ISA*03*0123456789*01*1234567890*30*000000005      *30*12345          *131031*1147*^*00501*000000907*1*T*:~GS*HS*000000005*12345*20131031*1147*1*X*005010X279A1~ST*270*0001*005010X279A1~BHT*0022*13*10001234*20131031*1147~HL*1**20*1~NM1*PR*2*MOCKPAYER*****PI*MOCKPAYER~HL*2*1*21*1~NM1*1P*2*POKITDOK, INC.*****XX*1912301953~HL*3*2*22*0~TRN*1*930000000000*9800000004~NM1*IL*1*DOE*JOHN****MI*00000000001~DMG*D8*19700101~DTP*291*D8*20131031~EQ*30~SE*13*0001~GE*1*1~IEA*1*000000907~"}'
{
  "meta": {
    "processing_time": 133,
    "application_mode": "production",
    "credits_billed": 1,
    "credits_remaining": 1000,
    "rate_limit_cap": 5000,
    "rate_limit_reset": 1477423057,
    "rate_limit_amount": 4,
    "activity_id": "abcabcabcabcabcabcabcabc"
  },
  "data": {
    "x12": "ISA*00*          *00*          *00*X12            *00*X12            *161025*1856*^*00501*000000001*0*P*:~GS*HB*X12*X12*20161025*1856*1*X~ST*271*0001~BHT*0022*13*be0e7966-9ae4-11e6-9312-0242ac110003*20161025*1856~HL*1**20*1~NM1*PR*2*MOCK PAYER INC*****PI*MOCKPAYER~HL*2*1*21*1~NM1*1P*2*PokitDok, Inc.*****XX*1912301953~HL*3*2*22*0~TRN*1*1*1453915417~NM1*IL*1*DOE*JOHN****MI*00000000001~REF*6P*088818801000013*MOCK INDIVIDUAL ADVANTAGE PLAN~N3*123 MAIN ST~N4*SPARTANBURG*SC*29307~DMG*D8*19700101*M~EB*1*ESP*30^98*PR*Open Choice~DTP*346*D8*20130215~DTP*356*D8*20120201~EB*B*ESP*98****20*****Y~MSG*PRIMARY OFFICE~EB*B*ESP*98****30*****W~MSG*GYN OFFICE VS~MSG*GYN VISIT~MSG*SPEC OFFICE~MSG*SPEC VISIT~MSG*PRIME CARE VST~EB*A*ESP*98*********Y~MSG*GYN OFFICE VS~MSG*GYN VISIT~MSG*SPEC OFFICE~MSG*SPEC VISIT~MSG*PRIMARY OFFICE~MSG*PRIME CARE VST~EB*A*ESP*98*****0.5****N~MSG*GYN OFFICE VS,COINS APPLIES TO OUT OF POCKET~MSG*GYN VISIT,COINS APPLIES TO OUT OF POCKET~MSG*SPEC OFFICE,COINS APPLIES TO OUT OF POCKET~MSG*SPEC VISIT,COINS APPLIES TO OUT OF POCKET~MSG*PRIME CARE VST,COINS APPLIES TO OUT OF POCKET~EB*C*FAM*30***23*6000*****Y~DTP*307*D8*20130101~MSG*INT MED AND RX,GYN OFFICE VS,DED INCLUDED IN OOP,GYN VISIT,SPEC OFFICE,SPEC VISIT,PRIMARY OFFICE,PRIME CARE VST~EB*C*FAM*30***29*5956.09*****Y~MSG*INT MED AND RX~EB*C*IND*30***23*3000*****Y~DTP*307*D8*20130101~MSG*INT MED AND RX,GYN OFFICE VS,DED INCLUDED IN OOP,GYN VISIT,SPEC OFFICE,SPEC VISIT,PRIMARY OFFICE,PRIME CARE VST~EB*C*IND*30***29*2983.57*****Y~MSG*INT MED AND RX~EB*C*FAM*30***23*12000*****N~DTP*307*D8*20130101~MSG*INT MED AND RX,GYN OFFICE VS,DED INCLUDED IN OOP,GYN VISIT,SPEC OFFICE,SPEC VISIT,PRIME CARE VST~EB*C*FAM*30***29*11956.09*****N~MSG*INT MED AND RX~EB*C*IND*30***23*6000*****N~DTP*307*D8*20130101~MSG*INT MED AND RX,GYN OFFICE VS,DED INCLUDED IN OOP,GYN VISIT,SPEC OFFICE,SPEC VISIT,PRIME CARE VST~EB*C*IND*30***29*5983.57*****N~MSG*INT MED AND RX~EB*G*IND*30****3000*****Y~EB*G*IND*30***29*2983.57*****Y~EB*G*FAM*30****6000*****Y~EB*G*FAM*30***29*5956.09*****Y~EB*G*IND*30****12500*****N~EB*G*IND*30***29*12483.57*****N~EB*G*FAM*30****25000*****N~EB*G*FAM*30***29*24956.09*****N~SE*66*0001~GE*1*1~IEA*1*000000001~"
  }
}
```

Here's another curl example sending and receiving raw X12 as `application/edi-x12` strings.

```shell
curl -v -XPOST -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/edi-x12" -H "Accept: application/edi-x12"  https://platform.pokitdok.com/api/v4/eligibility/ -d 'ISA*03*0123456789*01*1234567890*30*000000005      *30*12345          *131031*1147*^*00501*000000907*1*T*:~GS*HS*000000005*12345*20131031*1147*1*X*005010X279A1~ST*270*0001*005010X279A1~BHT*0022*13*10001234*20131031*1147~HL*1**20*1~NM1*PR*2*MOCKPAYER*****PI*MOCKPAYER~HL*2*1*21*1~NM1*1P*2*POKITDOK, INC.*****XX*1912301953~HL*3*2*22*0~TRN*1*930000000000*9800000004~NM1*IL*1*DOE*JOHN****MI*00000000001~DMG*D8*19700101~DTP*291*D8*20131031~EQ*30~SE*13*0001~GE*1*1~IEA*1*000000907~'
ISA*00*          *00*          *00*X12            *00*X12            *161025*1908*^*00501*000000001*0*P*:~GS*HB*X12*X12*20161025*1908*1*X~ST*271*0001~BHT*0022*13*be0e7966-9ae4-11e6-9312-0242ac110003*20161025*1908~HL*1**20*1~NM1*PR*2*MOCK PAYER INC*****PI*MOCKPAYER~HL*2*1*21*1~NM1*1P*2*PokitDok, Inc.*****XX*1912301953~HL*3*2*22*0~TRN*1*1*1453915417~NM1*IL*1*DOE*JOHN****MI*00000000001~REF*6P*088818801000013*MOCK INDIVIDUAL ADVANTAGE PLAN~N3*123 MAIN ST~N4*SPARTANBURG*SC*29307~DMG*D8*19700101*M~EB*1*ESP*30^98*PR*Open Choice~DTP*346*D8*20130215~DTP*356*D8*20120201~EB*B*ESP*98****20*****Y~MSG*PRIMARY OFFICE~EB*B*ESP*98****30*****W~MSG*GYN OFFICE VS~MSG*GYN VISIT~MSG*SPEC OFFICE~MSG*SPEC VISIT~MSG*PRIME CARE VST~EB*A*ESP*98*********Y~MSG*GYN OFFICE VS~MSG*GYN VISIT~MSG*SPEC OFFICE~MSG*SPEC VISIT~MSG*PRIMARY OFFICE~MSG*PRIME CARE VST~EB*A*ESP*98*****0.5****N~MSG*GYN OFFICE VS,COINS APPLIES TO OUT OF POCKET~MSG*GYN VISIT,COINS APPLIES TO OUT OF POCKET~MSG*SPEC OFFICE,COINS APPLIES TO OUT OF POCKET~MSG*SPEC VISIT,COINS APPLIES TO OUT OF POCKET~MSG*PRIME CARE VST,COINS APPLIES TO OUT OF POCKET~EB*C*FAM*30***23*6000*****Y~DTP*307*D8*20130101~MSG*INT MED AND RX,GYN OFFICE VS,DED INCLUDED IN OOP,GYN VISIT,SPEC OFFICE,SPEC VISIT,PRIMARY OFFICE,PRIME CARE VST~EB*C*FAM*30***29*5956.09*****Y~MSG*INT MED AND RX~EB*C*IND*30***23*3000*****Y~DTP*307*D8*20130101~MSG*INT MED AND RX,GYN OFFICE VS,DED INCLUDED IN OOP,GYN VISIT,SPEC OFFICE,SPEC VISIT,PRIMARY OFFICE,PRIME CARE VST~EB*C*IND*30***29*2983.57*****Y~MSG*INT MED AND RX~EB*C*FAM*30***23*12000*****N~DTP*307*D8*20130101~MSG*INT MED AND RX,GYN OFFICE VS,DED INCLUDED IN OOP,GYN VISIT,SPEC OFFICE,SPEC VISIT,PRIME CARE VST~EB*C*FAM*30***29*11956.09*****N~MSG*INT MED AND RX~EB*C*IND*30***23*6000*****N~DTP*307*D8*20130101~MSG*INT MED AND RX,GYN OFFICE VS,DED INCLUDED IN OOP,GYN VISIT,SPEC OFFICE,SPEC VISIT,PRIME CARE VST~EB*C*IND*30***29*5983.57*****N~MSG*INT MED AND RX~EB*G*IND*30****3000*****Y~EB*G*IND*30***29*2983.57*****Y~EB*G*FAM*30****6000*****Y~EB*G*FAM*30***29*5956.09*****Y~EB*G*IND*30****12500*****N~EB*G*IND*30***29*12483.57*****N~EB*G*FAM*30****25000*****N~EB*G*FAM*30***29*24956.09*****N~SE*66*0001~GE*1*1~IEA*1*000000001~
```


## Trading Partners

When submitting raw X12 transactions to the platform, you'll need to specify the PokitDok trading partner
id value in the NM109 segment element where you'd include a payer id with other clearinghouse services.
This ensures your raw X12 transactions are routed properly for processing.
Please review our <a href="https://platform.pokitdok.com/tradingpartners">trading partners list</a> for 
valid trading partner id values.
If NM109 is not populated with an available PokitDok trading partner id value, an error like the below will be returned:

```
{
    "data": {
        "errors": {
            "query": "Unable to find configuration for trading_partner_id: 123456789, transaction_set_name: eligibility"
        }
    }
}    
```

## Activities

The activities API may also be used to retrieve a Raw X12 view of past X12 API activity
on the platform.  This works for activities created as a result of Raw X12 API requests as well
as our standard JSON based X12 API requests.
To access the `x12_request` and `x12_response` values along with the standard activity 
information, you can use an `Accept` header value of `application/vnd.pokitdok.v4+activity-x12-json`
when making `GET /activities/<id>` requests.

```shell
curl -H "Authorization: Bearer $ACCESS_TOKEN" -H "Accept: application/vnd.pokitdok.v4+activity-x12-json" https://platform.pokitdok.com/api/v4/activities/<insert activity id here>
```
