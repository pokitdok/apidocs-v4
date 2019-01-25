# Drop-in UI
The PokitDok Drop-in UI enables anyone to add functionality like eligibility checks, out-of-pocket cost estimation, or pharmacy drug price comparisons to their own website with a fully styled and functional UI.

* One simple drop-in with full customization
* All major insurance carriers
* Detailed eligibility info including deductible status and co-pays
* Out-of-pocket cost estimation based on location and eligibility information
* Compare pharmacy drug prices, restrictions, and other comparison points


## 1. Get Drop-in Token

<aside class="warning">
please <a href="https://pokitdok.com/contact/">contact us</a> in order to enable the Drop-in UI on your PokitDok Platform account
</aside>

First you will need to <a href='https://platform.pokitdok.com/signup' target='\_blank'\>sign up for a PokitDok Platform account</a>
and generate a `Drop-In Token` from the Platform dashboard <a href='https://platform.pokitdok.com/dashboard#/dropins' target='\_blank'\>Drop-In UI</a> page. You will need
to provide the hostname of the website where you'll be using the drop-in UI, as well as select the type of drop-in UI widget you'll be using. For hostname,
provide the base URL of the site that you intend on embedding the widget (i.e.- `https://pokitdok.com` not `https://pokitdok.com/page/with/widget`).


## 2. Include JS File

```html
<body>
    ...
    <script src="https://platform.pokitdok.com/sdk/dropin.min.js"></script>
    ...
</body>
```

Include the `dropin.min.js` file inside the `<body>` of your website.


## 3. Add HTML Container

```html
<body>
    ...
    <div id="dropin-ui"></div>
    ...
</body>
```

Add an HTML container with a specific ID that will house your drop-in UI.


## 4. Initialize Drop-in

```javascript
pokitdok.dropin("INSERT YOUR DROP-IN TOKEN HERE", {
   container: "dropin-ui",
   type: "eligibility"
});
```

Using javascript, call the `pokitdok.dropin` function, using your PokitDok Platform `Drop-In Token` and <a href='/#options'>options</a>.

The drop-in UI form will auto-populate in the HTML container that you specified.

## Types
There are three types of drop-in UIs to choose from:

### Eligibility

> Eligibility example with minimum required options:

```javascript
pokitdok.dropin("INSERT YOUR DROP-IN TOKEN HERE", {
    container: "dropin-ui",
    type: "eligibility"
});
```

Displays a form that requires First & Last Name, Birth Date, Insurance Provider, and Member ID.
Returns eligibility information in an easy to read format with detailed info including deductible status and co-pays.

### Calculator

<aside class="warning">
<strong>procedures</strong> are required
</aside>

> Calculator example with minimum required options:

```javascript
pokitdok.dropin("INSERT YOUR DROP-IN TOKEN HERE", {
    container: "dropin-ui",
    type: "calculator",
    procedures: [
        {
            "name": "Test Procedure",
            "cpt_code": "xxxxx"
        }
    ]
});
```

Displays a form that requires all the same fields as the Eligibility type, with an added required procedure field and geolocation functionality
for closest possible price estimation. Returns an out of pocket cost estimation based on average insurance prices and location information for the procedure that was selected, as well as
eligibility. Displays in an easy to read format with detailed info including deductible status and co-pays.

#### Calculator Specific Options:

Name                    | Type                    | Default  | Description
------------------------|-------------------------|----------|--------------------------------------------------------------------------------------
procedures              | Array                   | Null     | Procedure(s) to populate the procedure dropdown with; `name` and `cpt_code` are required
procedures.name         | String                  | Null     | The name of the procedure that will show in the form dropdown
procedures.cpt_code     | String/Array (cpt code) | Null     | Either an array of associated CPT Codes or a string of a single CPT Code for the procedure
values.procedure        | String/Array (cpt code) | Null     | The procedure that will be auto-selected once the form loads
showPriceRange          | Boolean                 | False    | Show insurance price and out-of-pocket estimate results as a range of prices rather than an average
showCalculatorMessages  | Boolean                 | False    | Show a message below the out-of-pocket results explaining how calculation was made
eligibilityResultsFirst | Boolean                 | False    | On results page, show eligibility results first and out-of-pocket results below that

### Pharmacy Coverage

<aside class="warning">
<strong>pharmacy_npi</strong> is required. <strong>prescriber</strong> is required, unless you set <strong>enablePrescriberFields</strong> to <strong>true</strong>
</aside>

> Pharmacy coverage example with preset prescriber information:

```javascript
pokitdok.dropin("INSERT YOUR DROP-IN TOKEN HERE", {
    container: "dropin-ui",
    type: "pharmacy-coverage",
    values: {
        "pharmacy_npi": "xxxxxxxx",
        "prescriber": {
            "npi": "xxxxxxxx",
            "last_name": "xxxxxxxx"
        }
    }
});
```

> Pharmacy coverage example with prescriber information editable in the UI:

```javascript
pokitdok.dropin("INSERT YOUR DROP-IN TOKEN HERE", {
    container: "dropin-ui",
    type: "pharmacy-coverage",
    enablePrescriberFields: true,
    values: {
        "pharmacy_npi": "xxxxxxxx"
    }
});
```

> Pharmacy coverage example with type specific options:

```javascript
pokitdok.dropin("INSERT YOUR DROP-IN TOKEN HERE", {
    container: "dropin-ui",
    type: "pharmacy-coverage",
    labels: [
        {"name": "patient_header", "label": "Custom patient information header"},
        {"name": "search_header", "label": "Custom search bar header"}
    ],
    values: {
        "drugs": [
            "11111111111"
        ]
        "pharmacy_npi": "xxxxxxxx",
        "prescriber": {
            "npi": "xxxxxxxx",
            "last_name": "xxxxxxxx"
        },
        "insurance": {
            "cardholder_id": "123",
            "group_id": "456",
            "bin_number": "123",
            "pcn": "PCN"
        }
    }
});
```

Displays a form that requires First & Last Name, Gender, Birth Date, and Insurance (Member ID, RxBIN, RxGroup, and RxPCN) on the first step. Once that's submitted it allows the user to enter multiple
drug NDCs to search and compare prices, restrictions, and other comparison points in an easy to read table.

#### Pharmacy Coverage Specific Options:

Name                           | Type                    | Default                                 | Description
-------------------------------|-------------------------|-----------------------------------------|--------------------------------------------------------------------------------------
enablePrescriberFields         | Boolean                 | False                                   | Enable entering prescriber NPI and Last Name in the UI rather than `values.prescriber` object
labels.patient_header          | String                  | 'Enter patient information'             | Change the form header on patient information form, enter blank string to remove header
labels.search_header           | String                  | 'Enter drug NDCs to search and compare' | Change the form header on drug search form, enter blank string to remove header
values.pharmacy_npi            | String                  | Null                                    | Pharmacy NPI that is registered with PokitDok, used when making pharmacy-coverage API calls
values.prescriber              | Object                  | Null                                    | Prescriber information to use when making pharmacy-coverage API calls; `npi` and `last_name` are required
values.prescriber.npi          | String                  | Null                                    | Prescriber NPI
values.prescriber.last_name    | String                  | Null                                    | Prescriber last name
values.drugs                   | Array                   | Null                                    | An array of drug NDCs to pre-populate the drug NDC search bar with
values.insurance               | Object                  | Null                                    | Pre-populate the patient insurance information
values.insurance.cardholder_id | String                  | Null                                    | Pre-populate the patient insurance member id
values.insurance.group_id      | String                  | Null                                    | Pre-populate the patient insurance RxGroup
values.insurance.bin_number    | String                  | Null                                    | Pre-populate the patient insurance RxBIN
values.insurance.pcn           | String                  | Null                                    | Pre-populate the patient insurance RxPCN

## Options

> Example with options:

```javascript
pokitdok.dropin("INSERT YOUR DROP-IN TOKEN HERE", {
    container: "dropin-ui",
    type: "eligibility",
    styles: "http://www.example.com/styles.css",
    values: {
        "trading_partner_id": "MOCKPAYER"
    },
    labels: [
        {"name": "first_name", "label": "CUSTOM LABEL"},
    ],
    pieChartColors: {
        "fill": "#000000",
        "background": "#333333"
    },
    autoSubmit: true,
    resetButton: true,
    onFormSuccess: function() {
        // do stuff here
    },
    onFormLoad: function() {
        // do stuff here
    }
});
```

> Example of some fields pre-populated using `values` option:

```json

{
    "zip_code": "94401",
    "member": {
        "first_name": "Jane",
        "last_name": "Doe",
        "id": "123456789",
        "birth_date": "01-25-1970"
    },
    "trading_partner_id": "MOCKPAYER",
    "procedure": "xxxxx",
    "provider": {
        "first_name": "JEROME",
        "last_name": "AYA-AY",
        "npi": "1467560003"
    }
}
```

> Example of some input labels changed using `labels` option:

```json

[
    {"name": "zip_code", "label": "CUSTOM LABEL"},
    {"name": "procedure", "label": "CUSTOM LABEL"},
    {"name": "first_name", "label": "CUSTOM LABEL"},
    {"name": "last_name", "label": "CUSTOM LABEL"},
    {"name": "birth_date", "label": "CUSTOM LABEL"},
    {"name": "insurance", "label": "CUSTOM LABEL"},
    {"name": "member_id", "label": "CUSTOM LABEL"},
    {"name": "submit_button", "label": "CUSTOM LABEL"}
]
```

<aside class="warning">
<strong>container</strong> and <strong>type</strong> are required options for any drop-in UI to work
</aside>

Name                      | Type                | Default  | Description
--------------------------|---------------------|----------|--------------------------------------------------------------------------------------
container                 | String              | Null     | The id of the HTML container that the drop-in UI will be housed in
type                      | String              | Null     | Set the desired functionality of the drop-in; either `eligibility`, `calculator`, or `pharmacy-coverage`
styles                    | String (url)        | Null     | URL pointing to a css file to overwrite styles
pieChartColors            | Object              | Null     | Change the colors of the pie chart in the eligibility results
pieChartColors.fill       | String (hex color)  | Null     | Color of the filled-in section of the pie chart on the eligibility results
pieChartColors.background | String (hex color)  | Null     | Color of the background section of the pie chart on the eligibility results
values                    | Object              | Null     | An object of values that the form will pre-populate with
values.provider           | Object              | Null     | NPI to use for eligibility checks
labels                    | Array               | Null     | Change individual input labels by adding an object to this array where the `name` value is the input name and `label` is your custom label
autoSubmit                | Boolean             | False    | Form should submit automatically once all fields are filled
resetButton               | Boolean             | False    | A button should show that allows form to be reset once submitted
onFormSuccess             | Function            | Null     | Call when the form has been submitted successfully
onFormLoad                | Function            | Null     | Call when the form has been loaded successfully