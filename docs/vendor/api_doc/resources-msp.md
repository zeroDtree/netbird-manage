# MSP

GET/api/integrations/msp/tenants

## [Get MSP tenants](https://docs.netbird.io/ipa/resources/msp#get-msp-tenants)

### Request

GET

/api/integrations/msp/tenants
```
curl -X GET https://api.netbird.io/api/integrations/msp/tenants \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "My new tenant",
"domain": "tenant.com",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"role": "admin"
}
],
"activated_at": "2021-08-01T12:00:00Z",
"dns_challenge": "YXNkYSBkYXNhc2Rhc2RhIGFzZGFzZDJhc2QyNDUxNQ",
"created_at": "2021-08-01T12:00:00Z",
"updated_at": "2021-08-01T12:00:00Z",
"invited_at": "2021-08-01T12:00:00Z",
"status": "active"
}
]

```

* * *

POST/api/integrations/msp/tenants

## [Create MSP tenant](https://docs.netbird.io/ipa/resources/msp#create-msp-tenant)

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/msp#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

Description

The name for the MSP tenant

* Name
`domain`
Type
string
Required
required
Enum

Description

The name for the MSP tenant

* Name
`groups`
Type
object[]
Required
required
Enum

Description
MSP users Groups that can access the Tenant and Roles to assume

* Name
`id`
Type
string
Required
required
Enum

Description

The Group ID

* Name
`role`
Type
string
Required
required
Enum

Description

The Role name

### Request

POST

/api/integrations/msp/tenants
```
curl -X POST https://api.netbird.io/api/integrations/msp/tenants \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "My new tenant",
"domain": "tenant.com",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"role": "admin"
}
]
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "My new tenant",
"domain": "tenant.com",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"role": "admin"
}
],
"activated_at": "2021-08-01T12:00:00Z",
"dns_challenge": "YXNkYSBkYXNhc2Rhc2RhIGFzZGFzZDJhc2QyNDUxNQ",
"created_at": "2021-08-01T12:00:00Z",
"updated_at": "2021-08-01T12:00:00Z",
"invited_at": "2021-08-01T12:00:00Z",
"status": "active"
}

```

* * *

PUT/api/integrations/msp/tenants/{id}

## [Update MSP tenant](https://docs.netbird.io/ipa/resources/msp#update-msp-tenant)

### [Path Parameters](https://docs.netbird.io/ipa/resources/msp#path-parameters)

* Name
`id`
Type
string
Required
required
Enum

Description

The unique identifier of a tenant account

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/msp#request-body-parameters-2)

* Name
`name`
Type
string
Required
required
Enum

Description

The name for the MSP tenant

* Name
`groups`
Type
object[]
Required
required
Enum

Description
MSP users Groups that can access the Tenant and Roles to assume

* Name
`id`
Type
string
Required
required
Enum

Description

The Group ID

* Name
`role`
Type
string
Required
required
Enum

Description

The Role name

### Request

PUT

/api/integrations/msp/tenants/{id}
```
curl -X PUT https://api.netbird.io/api/integrations/msp/tenants/{id} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "My new tenant",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"role": "admin"
}
]
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "My new tenant",
"domain": "tenant.com",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"role": "admin"
}
],
"activated_at": "2021-08-01T12:00:00Z",
"dns_challenge": "YXNkYSBkYXNhc2Rhc2RhIGFzZGFzZDJhc2QyNDUxNQ",
"created_at": "2021-08-01T12:00:00Z",
"updated_at": "2021-08-01T12:00:00Z",
"invited_at": "2021-08-01T12:00:00Z",
"status": "active"
}

```

* * *

POST/api/integrations/msp/tenants/{id}/unlink

## [Unlink a tenant](https://docs.netbird.io/ipa/resources/msp#unlink-a-tenant)

### [Path Parameters](https://docs.netbird.io/ipa/resources/msp#path-parameters-2)

* Name
`id`
Type
string
Required
required
Enum

Description

The unique identifier of a tenant account

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/msp#request-body-parameters-3)

* Name
`owner`
Type
string
Required
required
Enum

Description

The new owners user ID.

### Request

POST

/api/integrations/msp/tenants/{id}/unlink
```
curl -X POST https://api.netbird.io/api/integrations/msp/tenants/{id}/unlink \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"owner": "google-oauth2|123456789012345678901"
}'

```

* * *

POST/api/integrations/msp/tenants/{id}/dns

## [Verify a tenant domain DNS challenge](https://docs.netbird.io/ipa/resources/msp#verify-a-tenant-domain-dns-challenge)

### [Path Parameters](https://docs.netbird.io/ipa/resources/msp#path-parameters-3)

* Name
`id`
Type
string
Required
required
Enum

Description

The unique identifier of a tenant account

### Request

POST

/api/integrations/msp/tenants/{id}/dns
```
curl -X POST https://api.netbird.io/api/integrations/msp/tenants/{id}/dns \
-H 'Authorization: Token <TOKEN>'

```

* * *

POST/api/integrations/msp/tenants/{id}/subscription

## [Create subscription for Tenant](https://docs.netbird.io/ipa/resources/msp#create-subscription-for-tenant)

### [Path Parameters](https://docs.netbird.io/ipa/resources/msp#path-parameters-4)

* Name
`id`
Type
string
Required
required
Enum

Description

The unique identifier of a tenant account

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/msp#request-body-parameters-4)

* Name
`priceID`
Type
string
Required
required
Enum

Description

The Price ID to change the subscription to.

### Request

POST

/api/integrations/msp/tenants/{id}/subscription
```
curl -X POST https://api.netbird.io/api/integrations/msp/tenants/{id}/subscription \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"priceID": "price_1HhxOpBzq4JbCqRmJxkpzL2V"
}'

```

* * *

POST/api/integrations/msp/tenants/{id}/invite

## [Invite existing account as a Tenant to the MSP account](https://docs.netbird.io/ipa/resources/msp#invite-existing-account-as-a-tenant-to-the-msp-account)

### [Path Parameters](https://docs.netbird.io/ipa/resources/msp#path-parameters-5)

* Name
`id`
Type
string
Required
required
Enum

Description

The unique identifier of an existing tenant account

### Request

POST

/api/integrations/msp/tenants/{id}/invite
```
curl -X POST https://api.netbird.io/api/integrations/msp/tenants/{id}/invite \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "My new tenant",
"domain": "tenant.com",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"role": "admin"
}
],
"activated_at": "2021-08-01T12:00:00Z",
"dns_challenge": "YXNkYSBkYXNhc2Rhc2RhIGFzZGFzZDJhc2QyNDUxNQ",
"created_at": "2021-08-01T12:00:00Z",
"updated_at": "2021-08-01T12:00:00Z",
"invited_at": "2021-08-01T12:00:00Z",
"status": "active"
}

```

* * *

PUT/api/integrations/msp/tenants/{id}/invite

## [Response by the invited Tenant account owner](https://docs.netbird.io/ipa/resources/msp#response-by-the-invited-tenant-account-owner)

### [Path Parameters](https://docs.netbird.io/ipa/resources/msp#path-parameters-6)

* Name
`id`
Type
string
Required
required
Enum

Description

The unique identifier of an existing tenant account

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/msp#request-body-parameters-5)

* Name
`value`
Type
string
Required
required
Enum

Description

Accept or decline the invitation.

### Request

PUT

/api/integrations/msp/tenants/{id}/invite
```
curl -X PUT https://api.netbird.io/api/integrations/msp/tenants/{id}/invite \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"value": {
"type": "string",
"description": "Accept or decline the invitation.",
"enum": [
"accept",
"decline"
]
}
}'

```

* * *