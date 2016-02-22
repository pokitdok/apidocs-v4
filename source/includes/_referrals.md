## Referrals
> Here's an example referral request to an Otolaryngologist (ENT) by a primary
care physician. In this example, the patient is also the subscriber on the
insurance policy.

```shell
curl -i -H "Authorization: Bearer $ACCESS_TOKEN" -H "Content-Type: application/json" -XPOST -d '{
    "event": {
        "category": "specialty_care_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "384.20",
                "date": "2014-09-30"
            }
        ],
        "place_of_service": "office",
        "provider": {
            "first_name": "JOHN",
            "npi": "1154387751",
            "last_name": "FOSTER",
            "phone": "8645822900"
        },
        "type": "consultation"
    },
    "patient": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "CHRISTINA",
        "last_name": "BERTOLAMI",
        "npi": "1619131232"
    },
    "trading_partner_id": "MOCKPAYER"
}' https://platform.pokitdok.com/api/v4/referrals/
```
```python
pd.referrals({
    "event": {
        "category": "specialty_care_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "384.20",
                "date": "2014-09-30"
            }
        ],
        "place_of_service": "office",
        "provider": {
            "first_name": "JOHN",
            "npi": "1154387751",
            "last_name": "FOSTER",
            "phone": "8645822900"
        },
        "type": "consultation"
    },
    "patient": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "CHRISTINA",
        "last_name": "BERTOLAMI",
        "npi": "1619131232"
    },
    "trading_partner_id": "MOCKPAYER"
})
```

```csharp
 client.referrals(
			new Dictionary<string, object> {
				{"event", new Dictionary<string, object> {
						{"category", "specialty_care_review"},
						{"certification_type", "initial"},
						{"delivery", new Dictionary<string, object> {
							{"quantity", 1},
							{"quantity_qualifier", "visits"}
							}},
						{"diagnoses", new Dictionary<string, string>[] {
							new Dictionary<string, string> {
								{"code", "384.20"},
								{"date", "2014-09-30"}
							}}},
						{"place_of_service", "office"},
						{"provider", new Dictionary<string, string> {
							{"first_name", "JOHN"},
							{"npi", "1154387751"},
							{"last_name", "FOSTER"},
							{"phone", "8645822900"}
							}},
						{"type", "consultation"},
					}},
				{"patient", new Dictionary<string, string> {
						{"birth_date", "1970-01-01"},
						{"first_name", "JANE"},
						{"last_name", "DOE"},
						{"id", "1234567890"}
					}},
				{"provider", new Dictionary<string, string> {
						{"first_name", "CHRISTINA"},
						{"last_name", "BERTOLAMI"},
						{"npi", "1619131232"}
					}},
				{"trading_partner_id", "MOCKPAYER"}
			});
```

> Example referrals response when the trading partner has authorized the request:

```
{
    "event": {
        "category": "specialty_care_review",
        "certification_type": "initial",
        "delivery": {
            "quantity": 1,
            "quantity_qualifier": "visits"
        },
        "diagnoses": [
            {
                "code": "384.20",
                "date": "2014-09-30"
            }
        ],
        "place_of_service": "office",
        "provider": {
            "first_name": "JOHN",
            "npi": "1154387751",
            "last_name": "FOSTER",
            "phone": "8645822900"
        },
        "review": {
            "certification_action": "certified_in_total",
            "certification_number": "AUTH0001"
        },
        "type": "consultation"
    },
    "patient": {
        "birth_date": "1970-01-01",
        "first_name": "JANE",
        "last_name": "DOE",
        "id": "1234567890"
    },
    "provider": {
        "first_name": "CHRISTINA",
        "last_name": "BERTOLAMI",
        "npi": "1619131232"
    },
    "trading_partner_id": "MOCKPAYER"
}
```

*Available modes of operation: batch/async or real-time*

The Referrals endpoint allows an application to request approval for a referral
to another health care provider.

Primary Care Physicians can enable their patients to receive the consult and services
of a specialist or specialist entity. This request will be sent to the reviewing
entity (e.g. Utilization Management Organization) for approval.

Available Referrals endpoints:

| Endpoint    | HTTP Method | Description                                                                |
|:------------|:------------|:---------------------------------------------------------------------------|
| /referrals/ | POST        | Submit a specialty care referral request to a trading partner for approval |

The /referrals/ endpoint accepts the following parameters:

| Parameter                         | Description                                                                                                                                                                                  |
|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| event                             | The patient event that is being submitted for approval.                                                                                                                                      |
| event.category                    | The category of the event being submitted for review. For referrals to specialists, a category value of "specialty_care_review" should always be used.                                       |
| event.certification_type          | The type of certification being requested. For new referrals, a certification value of "initial" should always be used.                                                                      |
| event.delivery                    | Specifies the delivery pattern of the health care services.                                                                                                                                  |
| event.delivery.quantity           | The quantity of services being requested.                                                                                                                                                    |
| event.delivery.quantity_qualifier | The qualifier used to indicate the quantity type. (e.g. visits, month, hours, units, days)                                                                                                   |
| event.diagnoses                   | An array of diagnosis information related to the event.                                                                                                                                      |
| event.diagnoses.code              | The diagnosis code. (e.g. 384.20)                                                                                                                                                            |
| event.diagnoses.date              | The date of the diagnosis.                                                                                                                                                                   |
| event.place_of_service            | The location where health care services are rendered.                                                                                                                                        |
| event.provider                    | Information about the provider being requested for this event.                                                                                                                               |
| event.provider.first_name         | The event provider’s first name when the provider is an individual.                                                                                                                          |
| event.provider.last_name          | The event provider’s last name when the provider is an individual.                                                                                                                           |
| event.provider.npi                | The NPI for the event provider.                                                                                                                                                              |
| event.provider.organization_name  | The event provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                   |
| event.type                        | The type of service being requested. For example, a value of consultation would be used when referring to a specialist for an initial consultation.                                          |
| event.start_date                  | Optional: The start date of the given event. For a single date, provide only event.start_date. For a date range, provide event.start_date and event.end_date. Given in ISO8601 (YYYY-MM-DD). |
| event.end_date                    | Optional: The end date of the given event. Only provide the end_date if the start_date is also given. Given in ISO8601 (YYYY-MM-DD).                                                         |
| patient.birth_date                | The patient’s birth date as specified on their policy.                                                                                                                                       |
| patient.id                        | The patient’s member identifier.                                                                                                                                                             |
| patient.first_name                | The patient’s first name as specified on their policy.                                                                                                                                       |
| patient.last_name                 | The patient’s last name as specified on their policy.                                                                                                                                        |
| provider.first_name               | The referring provider’s first name when the provider is an individual.                                                                                                                      |
| provider.last_name                | The referring provider’s last name when the provider is an individual.                                                                                                                       |
| provider.npi                      | The NPI for the referring provider.                                                                                                                                                          |
| provider.organization_name        | The referring provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                               |
| patient.illness_date              | Optional: The date the patient became ill.                                                                                                                                                   |
| subscriber.birth_date             | Optional: The subscriber’s birth date as specified on their policy. Specify when the patient is not the subscriber.                                                                          |
| subscriber.first_name             | Optional: The subscriber’s first name as specified on their policy. Specify when the patient is not the subscriber.                                                                          |
| subscriber.id                     | Optional: The subscriber’s member identifier. Specify when the patient is not the subscriber.                                                                                                |
| subscriber.last_name              | Optional: The subscriber’s last name as specified on their policy. Specify when the patient is not the subscriber.                                                                           |
| trading_partner_id                | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.                                                                              |

If the referral request is sent using a real-time interface, a referral response will be returned.

The /referrals/ response contains the following fields:

| Parameter                         | Description                                                                                                                                                                                                              |
|:----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| event                             | The patient event that is being submitted for approval.                                                                                                                                                                  |
| event.category                    | The category of the event being submitted for review. For referrals to specialists, a category value of "specialty_care_review" should always be used. A full list of possible values can be found [below](#r_category). |
| event.certification_type          | The type of certification being requested. For new referrals, a certification value of "initial" should always be used. A full list of possible values can be found [below](#certification_r_type).                      |
| event.delivery                    | Specifies the delivery pattern of the health care services.                                                                                                                                                              |
| event.delivery.quantity           | The quantity of services being requested.                                                                                                                                                                                |
| event.delivery.quantity_qualifier | The qualifier used to indicate the quantity type. (e.g. visits, month, hours, units, days)                                                                                                                               |
| event.diagnoses                   | An array of diagnosis information related to the event.                                                                                                                                                                  |
| event.diagnoses.code              | The diagnosis code. (e.g. 384.20)                                                                                                                                                                                        |
| event.diagnoses.date              | The date of the diagnosis.                                                                                                                                                                                               |
| event.place_of_service            | The location where health care services are rendered.                                                                                                                                                                    |
| event.provider                    | Information about the provider being requested for this event.                                                                                                                                                           |
| event.provider.first_name         | The event provider’s first name when the provider is an individual.                                                                                                                                                      |
| event.provider.last_name          | The event provider’s last name when the provider is an individual.                                                                                                                                                       |
| event.provider.npi                | The NPI for the event provider.                                                                                                                                                                                          |
| event.provider.organization_name  | The event provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                                               |
| event.review                      | Information about the outcome of a health care services review.                                                                                                                                                          |
| event.review.certification_action | Indicates the outcome of the review. For example, "certified_in_total" will be returned when the event is certified/authorized.  A full list of possible values can be found [below](#certaction).                       |
| event.review.certification_number | The review certification/reference number.                                                                                                                                                                               |
| event.review.decision_reason      | If the event is not authorized, the reason for that decision.  A full list of possible values can be found [below](#decision).                                                                                           |
| event.type                        | The type of service being requested. For example, a value of "consultation" would be used when referring to a specialist for an initial consultation.                                                                    |
| patient.birth_date                | The patient’s birth date as specified on their policy.                                                                                                                                                                   |
| patient.id                        | The patient’s member identifier.                                                                                                                                                                                         |
| patient.first_name                | The patient’s first name as specified on their policy.                                                                                                                                                                   |
| patient.last_name                 | The patient’s last name as specified on their policy.                                                                                                                                                                    |
| provider.first_name               | The referring provider’s first name when the provider is an individual.                                                                                                                                                  |
| provider.last_name                | The referring provider’s last name when the provider is an individual.                                                                                                                                                   |
| provider.npi                      | The NPI for the referring provider.                                                                                                                                                                                      |
| provider.organization_name        | The referring provider’s name when the provider is an organization. first_name and last_name should be omitted when sending organization_name.                                                                           |
| subscriber.birth_date             | Optional: The subscriber’s birth date as specified on their policy. Specify when the patient is not the subscriber.                                                                                                      |
| subscriber.first_name             | Optional: The subscriber’s first name as specified on their policy. Specify when the patient is not the subscriber.                                                                                                      |
| subscriber.id                     | Optional: The subscriber’s member identifier. Specify when the patient is not the subscriber.                                                                                                                            |
| subscriber.last_name              | Optional: The subscriber’s last name as specified on their policy. Specify when the patient is not the subscriber.                                                                                                       |
| trading_partner_id                | Unique id for the intended trading partner, as specified by the [Trading Partners](#trading-partners) endpoint.                                                                                                          |


Interested in requesting authorization for a particular service for a patient? See PokitDok’s
[Authorizations](#authorizations) endpoint.

<a name="certaction"></a>
Full list of possible values that can be returned in the event.review.certification_action parameter
on the referral response:

| certification_action Values |                    |
|:----------------------------|:-------------------|
| cancelled                   | modified           |
| certified_in_total          | no_action_required |
| certified_partial           | not_certified      |
| contact_payer               | pended             |


<a name="decision"></a>
Full list of possible values that can be returned in the event.review.decision_reason parameter on the authorization response:

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

<a name="certification_r_type"></a>
Full list of possible values that can be returned in the event.certification_type parameter on the referral response:

| certification_type |                 |
|:-------------------|:----------------|
| appeal_immediate   | initial         |
| appeal_standard    | reconsideration |
| cancel             | renewal         |
| extension          | revised         |


<a name="r_category"></a>
Full list of possible values that can be returned in the event.category parameter on the referral response:

| category               |                       |
|:-----------------------|:----------------------|
| admission_review       | individual            |
| health_services_review | specialty_care_review |
