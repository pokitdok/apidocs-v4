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
                "code": "789.00",
                "date": "2014-10-01"
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
        "birth_date": "1970-01-01",
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
                "code": "789.00",
                "date": "2014-10-01"
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
        "birth_date": "1970-01-01",
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
    "event": {
        "category": "health_services_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "789.00",
                "date": "2014-10-01"
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
        "birth_date": "1970-01-01",
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
                    {"code", "789.00"},
                    {"date", "2014-10-01"}
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
            {"birth_date", "1970-01-01"},
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
buf.append("                \"code\": \"789.00\",");
buf.append("                \"date\": \"2014-10-01\"");
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
buf.append("        \"birth_date\": \"1970-01-01\",");
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

> Example authorizations response when the trading partner has authorized the request:

```json
{
    "event": {
        "category": "health_services_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "789.00",
                "date": "2014-10-01"
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
        "birth_date": "1970-01-01",
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
    "patient": {
        "birth_date": "1970-02-02",
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
        "last_name": "Aye-ay",
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

The /authorizations/ endpoint accepts the following parameters:

| Parameter                         | Description                                                                                                                                                                                  |
|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| event                             | The patient event, service or procedure that is being submitted for review.                                                                                                                                        |
| event.category                    | The category of the event being submitted for review. A full list of possible values can be found [below](#category).                                                                                                                                        |
| event.certification_type          | The type of certification being requested. For new authorization requests, a certification value of "initial" should be used.                                                                |
| event.delivery                    | Specifies the delivery pattern of the health care services.                                                                                                                                  |
| event.delivery.quantity           | The quantity of services being requested.                                                                                                                                                    |
| event.delivery.quantity_qualifier | The qualifier used to indicate the quantity type. (e.g. visits, month, hours, units, days)                                                                                                   |
| event.diagnoses                   | An array of diagnosis information related to the event.                                                                                                                                      |
| event.diagnoses.code              | The diagnosis code. (e.g. 789.00)                                                                                                                                                            |
| event.diagnoses.date              | The date of the diagnosis.                                                                                                                                                                   |
| event.place_of_service            | The location where health care services are rendered.                                                                                                                                        |
| event.provider                    | Information about the provider being requested for this event.                                                                                                                               |
| event.provider.first_name         | The event provider’s first name when the provider is an individual.                                                                                                                          |
| event.provider.last_name          | The event provider’s last name when the provider is an individual.                                                                                                                           |
| event.provider.npi                | The NPI for the event provider.                                                                                                                                                              |
| event.provider.organization_name  | The event provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                   |
| event.type                        | The type of service being requested. For example, a value of "diagnostic_medical" would be used when an abdominal ultrasound for a patient.                                                  |
| event.start_date                  | Optional: The start date of the given event. For a single date, provide only event.start_date. For a date range, provide event.start_date and event.end_date. Given in ISO8601 (YYYY-MM-DD). |
| event.end_date                    | Optional: The end date of the given event. Only provide the end_date if the start_date is also given. Given in ISO8601 (YYYY-MM-DD).                                                         |
| patient.birth_date                | The patient’s birth date as specified on their policy.                                                                                                                                       |
| patient.id                        | The patient’s member identifier.                                                                                                                                                             |
| patient.first_name                | The patient’s first name as specified on their policy.                                                                                                                                       |
| patient.last_name                 | The patient’s last name as specified on their policy.                                                                                                                                        |
| patient.last_menstrual_date       | Optional: The last menstrual date of the patient.                                                                                                                                         |
| patient.ssn                       | Optional: The social security number of the patient.                                                                                                                                          |
| patient.group_number              | Optional: The group number of the patient.                                                                                                                                                   |
| patient.estimated_date_of_birth   | Optional: The estimated date of birth of the patient.                                                                                                                                        |
| patient.illness_date              | Optional: The date the patient became ill.                                                                                                                                                   |
| provider.first_name               | The requesting provider’s first name when the provider is an individual.                                                                                                                     |
| provider.last_name                | The requesting provider’s last name when the provider is an individual.                                                                                                                      |
| provider.npi                      | The NPI for the requesting provider.                                                                                                                                                         |
| provider.organization_name        | The requesting provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                              |
| subscriber.birth_date             | Optional: The subscriber’s birth date as specified on their policy. Specify when the patient is not the subscriber.                                                                          |
| subscriber.first_name             | Optional: The subscriber’s first name as specified on their policy. Specify when the patient is not the subscriber.                                                                          |
| subscriber.id                     | Optional: The subscriber’s member identifier. Specify when the patient is not the subscriber.                                                                                                |
| subscriber.last_name              | Optional: The subscriber’s last name as specified on their policy. Specify when the patient is not the subscriber.                                                                           |
| trading_partner_id                | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.                                                                              |

If the authorization request is sent using a real-time interface, an authorization response may be returned depending on trading partner ability. Trading partner responses may vary or additional information may be requested via phone, email or fax. 

The /authorizations/ response contains the following fields:

| Parameter                         | Description                                                                                                                                                                                        |
|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| event                             | The patient event that is being submitted for approval.                                                                                                                                            |
| event.category                    | The category of the event being submitted for review. A full list of possible values can be found [below](#category).                                                                              |
| event.certification_type          | The type of certification being requested.  A full list of possible values can be found [below](#certification_type).                                                                              |
| event.delivery                    | Specifies the delivery pattern of the health care services.                                                                                                                                        |
| event.delivery.quantity           | The quantity of services being requested.                                                                                                                                                          |
| event.delivery.quantity_qualifier | The qualifier used to indicate the quantity type. (e.g. visits, month, hours, units, days)                                                                                                         |
| event.diagnoses                   | An array of diagnosis information related to the event.                                                                                                                                            |
| event.diagnoses.code              | The diagnosis code. (e.g. 789.00)                                                                                                                                                                  |
| event.diagnoses.date              | The date of the diagnosis.                                                                                                                                                                         |
| event.place_of_service            | The location where health care services are rendered.                                                                                                                                              |
| event.provider                    | Information about the provider being requested for this event.                                                                                                                                     |
| event.provider.first_name         | The event provider’s first name when the provider is an individual.                                                                                                                                |
| event.provider.last_name          | The event provider’s last name when the provider is an individual.                                                                                                                                 |
| event.provider.npi                | The NPI for the event provider.                                                                                                                                                                    |
| event.provider.organization_name  | The event provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                         |
| event.review                      | Information about the outcome of a health care services review.                                                                                                                                    |
| event.review.certification_action | Indicates the outcome of the review. For example, "certified_in_total" will be returned when the event is certified/authorized.  A full list of possible values can be found [below](#certaction). |
| event.review.certification_number | The review certification/reference number.                                                                                                                                                         |
| event.review.decision_reason      | If the event is not authorized, the reason for that decision.  A full list of possible values can be found [below](#decision).                                                                     |
| event.type                        | The type of service being requested.                                                                                                                                                               |
| patient.birth_date                | The patient’s birth date as specified on their policy.                                                                                                                                             |
| patient.id                        | The patient’s member identifier.                                                                                                                                                                   |
| patient.first_name                | The patient’s first name as specified on their policy.                                                                                                                                             |
| patient.last_name                 | The patient’s last name as specified on their policy.                                                                                                                                              |
| provider.first_name               | The requesting provider’s first name when the provider is an individual.                                                                                                                           |
| provider.last_name                | The requesting provider’s last name when the provider is an individual.                                                                                                                            |
| provider.npi                      | The NPI for the requesting provider.                                                                                                                                                               |
| provider.organization_name        | The requesting provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                    |
| subscriber.birth_date             | Optional: The subscriber’s birth date as specified on their policy. Specify when the patient is not the subscriber.                                                                                |
| subscriber.first_name             | Optional: The subscriber’s first name as specified on their policy. Specify when the patient is not the subscriber.                                                                                |
| subscriber.id                     | Optional: The subscriber’s member identifier. Specify when the patient is not the subscriber.                                                                                                      |
| subscriber.last_name              | Optional: The subscriber’s last name as specified on their policy. Specify when the patient is not the subscriber.                                                                                 |
| trading_partner_id                | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.                                                                                    |


<a name="certaction"></a>
Possible values that can be returned in the event.review.certification_action parameter on the authorization response:

| certification_action Values |                    |
|:----------------------------|:-------------------|
| cancelled                   | modified           |
| certified_in_total          | no_action_required |
| certified_partial           | not_certified      |
| contact_payer               | pended             |


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
