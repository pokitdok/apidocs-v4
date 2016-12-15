## Authorizations
>Here's an example authorization request for an abdominal ultrasound. In this example, the patient is also the subscriber on the insurance policy:

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "event": {
        "category": "health_services_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "R10.9",
                "date": "2016-01-25"
            }
        ],
        "place_of_service": "office",
        "provider": {
            "organization_name": "KELLY ULTRASOUND CENTER, LLC",
            "npi": "1760779011",
            "phone": "8642341234"
        },
        "services": [
            {
                "cpt_code": "76700",
                "measurement": "unit",
                "quantity": 1
            }
        ],
        "type": "diagnostic_medical"
    },
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "JEROME",
        "npi": "1467560003",
        "last_name": "AYA-AY"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/authorizations/
```

```python
client.authorizations({
    "event": {
        "category": "health_services_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "R10.9",
                "date": "2016-01-25"
            }
        ],
        "place_of_service": "office",
        "provider": {
            "organization_name": "KELLY ULTRASOUND CENTER, LLC",
            "npi": "1760779011",
            "phone": "8642341234"
        },
        "services": [
            {
                "cpt_code": "76700",
                "measurement": "unit",
                "quantity": 1
            }
        ],
        "type": "diagnostic_medical"
    },
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "JEROME",
        "npi": "1467560003",
        "last_name": "AYA-AY"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

```ruby
client.authorizations({
    event: {
        category: "health_services_review",
        certification_type: "initial",
        delivery: {
            quantity: 1,
            quantity_qualifier: "visits"
        },
        diagnoses: [
            {
                code: "R10.9",
                date: "2016-01-25"
            }
        ],
        place_of_service: "office",
        provider: {
            organization_name: "KELLY ULTRASOUND CENTER, LLC",
            npi: "1760779011",
            phone: "8642341234"
        },
        services: [
            {
                cpt_code: "76700",
                measurement: "unit",
                quantity: 1
            }
        ],
        type: "diagnostic_medical"
    },
    patient: {
        birth_date: "1970-01-25",
        first_name: "JANE",
        last_name: "DOE",
        id: "1234567890"
    },
    provider: {
        first_name: "JEROME",
        npi: "1467560003",
        last_name: "AYA-AY"
    },
    trading_partner_id: "MOCKPAYER"
})
```

```csharp
client.authorizations(
    new Dictionary<string, object> {
        {"event", new Dictionary<string, object> {
            {"category", "health_services_review"},
            {"certification_type", "initial"},
            {"delivery", new Dictionary<string, object> {
                {"quantity", 1.0},
                {"quantity_qualifier", "visits"}
            }},
            {"diagnoses", new Object[] {new Dictionary<string, string> {
                    {"code", "R10.9"},
                    {"date", "2016-01-25"}
            }}},
            {"place_of_service", "office"},
            {"provider", new Dictionary<string, string> {
                {"organization_name", "KELLY ULTRASOUND CENTER, LLC"},
                {"npi", "1760779011"},
                {"phone", "8642341234"}
            }},
            {"review", new Dictionary<string, string> {
                {"certification_action", "certified_in_total"},
                {"certification_number", "AUTH0002"}
            }},
            {"services", new Object[] {new Dictionary<string, object> {
                {"cpt_code", "76700"},
                {"measurement", "unit"},
                {"quantity", 1.0}
            }}},
            {"type", "diagnostic_medical"}
        }},
        {"patient", new Dictionary<string, string> {
            {"birth_date", "1970-01-25"},
            {"first_name", "JANE"},
            {"last_name", "DOE"},
            {"id", "1234567890"}
        }},
        {"provider", new Dictionary<string, string> {
            {"first_name", "JEROME"},
            {"npi", "1467560003"},
            {"last_name", "AYA-AY"}
        }},
        {"trading_partner_id", "MOCKPAYER"}
    });
```

```java
StringBuffer buf = new StringBuffer();
buf.append("{");
buf.append("    \"event\": {");
buf.append("        \"category\": \"health_services_review\",");
buf.append("        \"certification_type\": \"initial\",");
buf.append("        \"delivery\": {");
buf.append("            \"quantity\": 1,");
buf.append("            \"quantity_qualifier\": \"visits\"");
buf.append("        },");
buf.append("        \"diagnoses\": [");
buf.append("            {");
buf.append("                \"code\": \"R10.9\",");
buf.append("                \"date\": \"2016-01-25\"");
buf.append("            }");
buf.append("        ],");
buf.append("        \"place_of_service\": \"office\",");
buf.append("        \"provider\": {");
buf.append("            \"organization_name\": \"KELLY ULTRASOUND CENTER, LLC\",");
buf.append("            \"npi\": \"1760779011\",");
buf.append("            \"phone\": \"8642341234\"");
buf.append("        },");
buf.append("        \"services\": [");
buf.append("            {");
buf.append("                \"cpt_code\": \"76700\",");
buf.append("                \"measurement\": \"unit\",");
buf.append("                \"quantity\": 1");
buf.append("            }");
buf.append("        ],");
buf.append("        \"type\": \"diagnostic_medical\"");
buf.append("    },");
buf.append("    \"patient\": {");
buf.append("        \"birth_date\": \"1970-01-25\",");
buf.append("        \"first_name\": \"JANE\",");
buf.append("        \"last_name\": \"DOE\",");
buf.append("        \"id\": \"1234567890\"");
buf.append("    },");
buf.append("    \"provider\": {");
buf.append("        \"first_name\": \"JEROME\",");
buf.append("        \"npi\": \"1467560003\",");
buf.append("        \"last_name\": \"AYA-AY\"");
buf.append("    },");
buf.append("    \"trading_partner_id\": \"MOCKPAYER\"");
buf.append("}");

JSONObject query = (JSONObject) JSONValue.parse(buf.toString());
client.authorizations(query);
```

```swift
let data = [
    "event": [
        "category": "health_services_review",
        "certification_type": "initial",
        "delivery": [
            "quantity": 1,
            "quantity_qualifier": "visits"
        ],
        "diagnoses": [
            [
                "code": "R10.9",
                "date": "2016-01-25"
            ]
        ],
        "place_of_service": "office",
        "provider": [
            "organization_name": "KELLY ULTRASOUND CENTER, LLC",
            "npi": "1760779011",
            "phone": "8642341234"
        ],
        "services": [
            [
                "cpt_code": "76700",
                "measurement": "unit",
                "quantity": 1
            ]
        ],
        "type": "diagnostic_medical"
    ],
    "patient": [
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    ],
    "provider": [
        "first_name": "JEROME",
        "npi": "1467560003",
        "last_name": "AYA-AY"
    ],
    "trading_partner_id": "MOCKPAYER"
] as [String:Any]
try client.authorizations(params: data)
```
> Example authorizations response when the trading partner has rejected the submission:

```
{
    "client_id": "ASDFBOI87234CSDEAR",
    "correlation_id": "575037af0640fd518fe64c36",
    "event": {
        "category": "health_services_review",
        "certification_type": "initial",
        "delivery": {
            "quantity_qualifier": "visits",
            "quantity": 1
        },
        "place_of_service": "office",
        "provider": {
            "last_name": "AYA-AY",
            "first_name": "JEROME",
            "npi": "1467560003",
            "rejections": [
                {
                    "follow_up_action": "correct_and_resubmit",
                    "reason": "input_errors",
                    "valid_request": false
                }
            ]
        },
        "review": {
            "certification_action": "not_certified",
            "decision_reason": "services_not_considered_due_to_other_errors",
            "second_surgical_opinion_required": false
        },
        "services": [
            {
                "cpt_code": "97022",
                "rejections": [
                    {
                        "follow_up_action": "correct_and_resubmit",
                        "reason": "required_application_data_missing",
                        "valid_request": false
                    }
                ]
            }
        ]
    },
    "follow_up_action": "correct_and_resubmit",
    "originating_company_id": "987123654",
    "patient": {
        "birth_date": "1970-01-01",
        "gender": "unknown",
        "last_name": "DOE",
        "first_name": "JANE",
        "id": "W000000000"
    },
    "payer": {
        "organization_name": "MOCKPAYER",
        "id": "123456789"
    },
    "provider": {
        "organization_name": "POKITDOK TESTING",
        "npi": "1234567890",
        "rejections": [
            {
                "follow_up_action": "correct_and_resubmit",
                "reason": "invalid_provider_phone_number",
                "valid_request": false
            }
        ]
    },
    "reject_reason": "invalid_provider_phone_number",
    "trading_partner_id": "MOCKPAYER",
    "valid_request": false,
    "async": false
}
```
> Example authorizations response when the trading partner has authorized the request:

```json
{
    "client_id": "<client_id>",
    "event": {
        "category": "health_services_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "R10.9",
                "date": "2016-01-25"
            }
        ],
        "place_of_service": "office",
        "provider": {
            "organization_name": "KELLY ULTRASOUND CENTER, LLC",
            "npi": "1760779011",
            "phone": "8642341234"
        },
        "review": {
            "certification_action": "certified_in_total",
            "certification_number": "AUTH0002"
        },
        "services": [
            {
                "cpt_code": "76700",
                "measurement": "unit",
                "quantity": 1
            }
        ],
        "type": "diagnostic_medical"
    },
    "patient": {
        "birth_date": "1970-01-25",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "JEROME",
        "npi": "1467560003",
        "last_name": "AYA-AY"
    },
    "trading_partner_id": "MOCKPAYER"
}
```
> Example authorizations response when the trading partner has received the request and it is pending:

```
{
    "client_id": "<client_id>",
    "patient": {
        "birth_date": "1970-02-25",
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "W000000000"
    },
    "trading_partner_id": "abc_healthcare",
    "payer": {
        "organization_name": "ABC HealthCare",
        "id": ""
    },
    "originating_company_id": "1453504565",
    "correlation_id": "",
    "client_id": "",
    "provider": {
        "first_name": "JEROME",
        "last_name": "AYA-AY",
        "npi": "1760779011"
    },
    "async": false,
    "event": {
        "category": "health_services_review",
        "place_of_service": "office",
        "review": {
            "decision_reason": "requires_medical_review",
            "second_surgical_opinion_required": false,
            "certification_action": "pended"
        },
        "delivery": {
            "quantity_qualifier": "visits",
            "quantity": 1
        },
        "certification_type": "initial",
        "type": "diagnostic_lab"
    },
    "valid_request": true
}
```

*Available modes of operation: batch/async or real-time*

The Authorizations endpoint allows an application to submit a request for an authorization for a health care service. Providers can request permission (authorization) from the reviewing entity (e.g. Utilization Management Organization) to deliver health care services to a patient.

The Authorization request can also be used to request permission to admit a patient and/or gain authorization to deliver specific health care services to a patient that requires review.  Services requiring authorization are defined by the trading partner. Authorization request and responses may vary based on Trading Partner. 

Learn more about our Authorization API workflow.

Interested in requesting approval for a referral to a specialist? See PokitDok’s [Referrals](#referrals) endpoint.

Available Authorizations endpoints:

| Endpoint         | HTTP Method | Description                                                                                             |
|:-----------------|:------------|:--------------------------------------------------------------------------------------------------------|
| /authorizations/ | POST        | Submit a request for the review of healthcare services in order to obtain an authorization for that service. |

The /authorizations/ endpoint uses the same object for both its parameters and response. Most of the fields below can be passed in via the request object. Some of the fields will be assigned internally and can be seen in the response object.

| Field                             | Description                                                                                                                                                                                  |
|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| client_id                         | The unique identifier associated with the client making the eligibility request.                                                                                                                                        |
| event                             | The patient event, service or procedure that is being submitted for review.                                                                                         |
| event.category                    | The category of the event being submitted for review. A full list of possible values can be found [below](#category).                                                                                                                                        |
| event.certification_type          | The type of certification being requested. For new authorization requests, a certification value of "initial" should be used.                                                                |
| event.delivery                    | Specifies the delivery pattern of the health care services.                                                                                                                                  |
| event.delivery.units              | The units of services being requested.                                                                                                                                                    |
| event.delivery.sample_selection_modulus | Specify the sampling frequency in terms of a modulus of the Unit of Measure, e.g., every fifth bag, every 1.5 minutes.                                                                                                                                                  |
| event.delivery.delivery_frequency_code | Code which specifies frequency by which services can be performed.                                                                                                                                                 |
| event.delivery.delivery_pattern_time_code | Code which specifies the time delivery pattern of the services.                                                                                                                                                  |
| event.delivery.quantity           | The quantity of services being requested.                                                                                                                                                    |
| event.delivery.quantity_qualifier | The qualifier used to indicate the quantity type. (e.g. visits, month, hours, units, days)                                                                                                   |
| event.diagnoses                   | An array of diagnosis information related to the event.                                                                                                                                      |
| event.diagnoses.code              | The diagnosis code. (e.g. R10.9)                                                                                                                                                            |
| event.diagnoses.date              | The date of the diagnosis. In ISO8601 format (YYYY-MM-DD).                                                                                                                                                                  |
| event.place_of_service            | The location where health care services are rendered.                                                                                                                                        |
| event.provider                    | Information about the provider being requested for this event. The object used for provider can be seen [below](#service_review_provider_object).                                                                                                                               |
| event.provider.rejections         | Reject reasons related to errors in the event.provider section of the authorization submission.                                                                                                                               |
| event.services                    | List of services linked to the event.                                                                                                                               |
| event.rejections                  | Reject reasons related to errors in the event section of the authorization submission.                                                                                |
| event.services.rejections         | Reject reasons related to errors in the services section of the authorization submission.                                                                                                                                                                                         |
| event.services.amount             | The amount paid for a service.                                                                                                                              |
| event.services.cpt_code           | The CPT code indicating the type of service that was performed.                                                                                                                               |
| event.services.date               | The date of the service. In ISO8601 format (YYYY-MM-DD).                                                                                                                            |
| event.services.measurement        | Type of event services measurement. Possibilities: international_unit, minutes, and unit.                                                                                                                             |
| event.services.quantity           | The quantity of services being requested.                                                                                                                              |
| event.admission_date              | The date the patient was admitted. In ISO8601 format (YYYY-MM-DD).                                                                                                                            |
| event.discharge_date              | The date the patient was discharged. In ISO8601 format (YYYY-MM-DD).                                                                                                                            |
| event.review                      | Information about the outcome of a health care services review.                                                                                                                                    |
| event.review.certification_action | Indicates the outcome of the review. For example, "certified_in_total" will be returned when the event is certified/authorized.  A full list of possible values can be found [below](#certaction). |
| event.review.certification_number | The review certification/reference number.                                                                                                                                                         |
| event.review.decision_reason      | If the event is not authorized, the reason for that decision.  A full list of possible values can be found [below](#decision).                                                                     |
| event.review.event_start_date     | Effective date of authorization. In ISO8601 format (YYYY-MM-DD).                                                               |
| event.review.event_end_date       | End date for authorization. In ISO8601 format (YYYY-MM-DD).                                                                    |
| event.review.second_surgical_opinion_required      | Boolean of whether or not a second surgical opinion is required.                                                                     |
| event.type                        | The type of service being requested. For example, a value of "diagnostic_medical" would be used when an abdominal ultrasound for a patient. A full list of these values can be found under the eligibility section [below](#service-type).                                                  |
| event.start_date                  | Optional: The start date of the given event. For a single date, provide only event.start_date. For a date range, provide event.start_date and event.end_date. In ISO8601 format (YYYY-MM-DD). |
| event.end_date                    | Optional: The end date of the given event. Only provide the end_date if the start_date is also given. In ISO8601 format (YYYY-MM-DD).                                                         |
| follow_up_action                  | When an authorization request is rejected, a follow up action will be provided to inform your application how to proceed. See the possibilities [below](#follow_up_action).                                           |
| originating_company_id            | The id of the company where the request originated.                                                                                                                                     |
| payer                             | The information source providing authorization information; i.e., the insurance company.                                                                                                                                       |
| payer.organization_name           | The payer's organization name.                                                                                                                                       |
| payer.id                          | The payer's unique identifier.                                                                                                                                       |
| payer.rejections                  | Reject reasons related to errors in the payer section of the authorization submission.                                                                               |
| provider                          | The requesting provider. The object used for provider can be seen [below](#service_review_provider_object).                                                                                                                    |
| provider.rejections               | Reject reasons related to errors in the provider section of the authorization submission.                                                                                                                                                                                             |
| reject_reason                     | When a trading partner is unable to provide authorization information for an authorization request, they will provide a reject reason. A full list of possibilities can be seen under the eligibility section [below](#reject-reason).  When multiple reject reasons are returned on a single submission, the rejections will be returned under each section it was received (ex: payer.rejections, event.services.rejections) and the reject reason returned first in the X12 will present in the top level reject_reason field.                                                                                                                  |
| rejections                         | Reject reasons related to errors in the authorization submission.                                                                                                                                                                                             |
| patient                        | The patient for which the authorization request is being submitted. The object used for the patient can be seen [below](#service_review_member_object). If both patient and subscriber are submitted, patient information will be sent in the dependent loop.           |
| patient.rejections             | Reject reasons related to errors in the patient section of the authorization submission.                                                                   |
| subscriber                        | The subscriber for which the authorization request is being submitted. The object used for the subscriber can be seen [below](#service_review_member_object). If subscriber is not provided, patient information is sent in the subscriber loop.                                  |
| subscriber.rejections             | Reject reasons related to errors in the subscriber section of the authorization submission.                                                                   |
| trading_partner_id                | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.                                                                              |
| valid_request                     | A boolean of whether or not the request was valid.                                                                              |

If the authorization request is sent using a real-time interface, an authorization response may be returned depending on trading partner ability. Trading partner responses may vary or additional information may be requested via phone, email or fax.                                         

<a name="service_review_member_object"></a>
###Patient object:

| Field                             | Description                                                                           |
|:----------------------------------|:--------------------------------------------------------------------------------------|
| birth_date                        | The member’s birth date as specified on their policy. In ISO8601 format (YYYY-MM-DD). |
| gender                            | The member's gender (Male, Female, Unknown)                                           |
| last_name                         | The member’s last name as specified on their policy.                                  |
| first_name                        | The member’s first name as specified on their policy.                                 |
| middle_name                       | The member’s middle name as specified on their policy.                                |
| suffix                            | The suffix for the member                                                             |
| id                                | The member identifier.                                                                |
| last_menstrual_date               | The last menstrual date of the member. In ISO8601 format (YYYY-MM-DD).                |
| group_number                      | The group number of the patient.                                                      |
| ssn                               | The ssn of the member.                                                                |
| estimated_birth_date              | The estimated date of birth of the patient. In ISO8601 format (YYYY-MM-DD).           |
| illness_date                      | The date the member became ill. In ISO8601 format (YYYY-MM-DD).                       |
| accident_date                     | The date of the member's accident. In ISO8601 format (YYYY-MM-DD).                                                                                                                                    |

<a name="service_review_provider_object"></a>
###Provider object:

| Field                             | Description                                                           |
|:----------------------------------|:----------------------------------------------------------------------|
| first_name                        | The provider’s first name when the provider is an individual.                                                                                                                          |
| middle_name                       | The provider’s middle name when the provider is an individual.                                                                                                                                                   |
| last_name                         | The provider’s last name when the provider is an individual.                                                                                                                           |
| suffix                            | The suffix for the provider.                                                                         |
| tax_id                            | The federal tax id for the provider billing for services. For individual providers, this may be the tax id of the medical practice or organization where a provider works.                                                                        |
| phone                             | The phone number for the provider.                                                                         |
| fax                               | The fax number for the provider. |
| email                             | The e-mail for the provider. |
| url                               | The website URL for the provider. |
| taxonomy_code                     | The taxonomy code for the provider.                                                                         |
| npi                               | The NPI for the provider.                                                                                                                                                              |
| organization_name                 | The provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                   |

<a name="certaction"></a>
Possible values that can be returned in the event.review.certification_action parameter on the authorization response:

| certification_action Values |                    |
|:----------------------------|:-------------------|
| cancelled                   | modified           |
| certified_in_total          | no_action_required |
| certified_partial           | not_certified      |
| contact_payer               | pended             |

<a name="follow_up_action"></a>
Possible values that can be returned in the follow_up_action field on the authorization response:

| follow_up_action Values               |                                   |
|:--------------------------------------|:----------------------------------|
| do_not_resubmit_sent_to_third_party   | do_not_resubmit_will_respond_again|
| correct_and_resubmit                  | resubmit_original                 |
| wait_10_days_and_resubmit             | wait_30_days_and_resubmit         |
| resubmission_allowed                  | resubmission_not_allowed          |

<a name="decision"></a>
List of possible values that can be returned in the event.review.decision_reason parameter on the authorization response:

| decision_reason Values                                    |                                                      |
|:----------------------------------------------------------|:-----------------------------------------------------|
| additional_patient_information_required                   | patient_in_premium_payment_grace_period_second_month |
| administrative_cancellation                               | patient_in_premium_payment_grace_period_third_month  |
| ambulance_certification_transport_address_mismatch        | patient_restricted_to_specific_provider              |
| authorization_restrictions                                | pre_existing_condition                               |
| authorized_quantity_exceeded                              | price_authorization_expired                          |
| certification_not_required_service                        | price_authorization_no_longer_required               |
| certification_responsibility_external_review_organization | pricing                                              |
| computed_mileage_transport_information_mismatch           | primary_care_service                                 |
| contractual_geographic_restriction                        | product_delivery_pattern                             |
| contractual_guidelines_not_followed                       | product_not_on_the_price_authorization               |
| cosmetic                                                  | provider_not_primary_care_physician                  |
| disposition_pending_review                                | request_forwarded_to_external_review_organization    |
| duplicate_request                                         | requested_information_not_received                   |
| exceeds_plan_maximums                                     | requires_medical_review                              |
| experimental_service                                      | requires_pcp_authorization                           |
| inappropriate_facility_type                               | service_authorized_for_another_provider              |
| level_of_care_not_appropriate                             | service_inconsistent_with_diagnosis                  |
| mileage_cant_be_computed_based_on_data_submitted          | service_inconsistent_with_patient_age                |
| missing_provider_role                                     | service_inconsistent_with_patient_gender             |
| no_credit_allowed                                         | service_inconsistent_with_provider_type              |
| no_prior_approval                                         | services_not_considered_due_to_other_errors          |
| non_covered_service                                       | special_cost_incorrect                               |
| not_medically_necessary                                   | testing_not_included                                 |
| notification_received                                     | time_limits_not_met                                  |
| once_in_a_lifetime_restriction_applies                    | transport_request_denied                             |
| out_of_network                                            | unit_resale_higher_than_authorized                   |
| patient_in_premium_payment_grace_period_first_month       |                                                      |

<a name="certification_type"></a>
Possible values that can be returned in the event.certification_type parameter on the authorization response:

| certification_type |                 |
|:-------------------|:----------------|
| appeal_immediate   | initial         |
| appeal_standard    | reconsideration |
| cancel             | renewal         |
| extension          | revised         |

<a name="category"></a>
Possible values that can be returned in the event.category parameter on the authorization response:

| category               |                       |
|:-----------------------|:----------------------|
| admission_review       | individual            |
| health_services_review | specialty_care_review |
