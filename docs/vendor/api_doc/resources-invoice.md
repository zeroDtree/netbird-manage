# Invoice

GET/api/integrations/billing/invoices

## [Get account's paid invoices](https://docs.netbird.io/ipa/resources/invoice#get-accounts-paid-invoices)

### Request

GET

/api/integrations/billing/invoices
```
curl -X GET https://api.netbird.io/api/integrations/billing/invoices \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "in_1MtHbELkdIwHu7ixl4OzzPMv",
"type": {
"type": "string",
"description": "The invoice type",
"enum": [
"account",
"tenants"
]
},
"period_start": "2021-08-01T12:00:00Z",
"period_end": "2021-08-31T12:00:00Z"
}
]

```

* * *

GET/api/integrations/billing/invoices/{id}/pdf

## [Get account invoice URL to Stripe.](https://docs.netbird.io/ipa/resources/invoice#get-account-invoice-url-to-stripe)

### [Path Parameters](https://docs.netbird.io/ipa/resources/invoice#path-parameters)

* Name
`id`
Type
string
Required
required
Enum

Description

The unique identifier of the invoice

### Request

GET

/api/integrations/billing/invoices/{id}/pdf
```
curl -X GET https://api.netbird.io/api/integrations/billing/invoices/{id}/pdf \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"url": "https://invoice.stripe.com/i/acct_1M2DaBKina4I2KUb/test_YWNjdF8xTTJEdVBLaW5hM0kyS1ViLF1SeFpQdEJZd3lUOGNEajNqeWdrdXY2RFM4aHcyCnpsLDEzMjg3GTgyNQ02000JoIHc1X?s=db"
}

```

* * *

GET/api/integrations/billing/invoices/{id}/csv

## [Get account invoice CSV.](https://docs.netbird.io/ipa/resources/invoice#get-account-invoice-csv)

### [Path Parameters](https://docs.netbird.io/ipa/resources/invoice#path-parameters-2)

* Name
`id`
Type
string
Required
required
Enum

Description

The unique identifier of the invoice

### Request

GET

/api/integrations/billing/invoices/{id}/csv
```
curl -X GET https://api.netbird.io/api/integrations/billing/invoices/{id}/csv \
-H 'Authorization: Token <TOKEN>'

```

* * *