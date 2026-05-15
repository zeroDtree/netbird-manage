# EDR Intune Integrations

POST/api/integrations/edr/intune

## [Create EDR Intune Integration](https://docs.netbird.io/ipa/resources/edr-intune-integrations#create-edr-intune-integration)

Creates a new EDR Intune integration for the authenticated account.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/edr-intune-integrations#request-body-parameters)

* Name
`client_id`
Type
string
Required
required
Enum

Description

The Azure application client id

* Name
`tenant_id`
Type
string
Required
required
Enum

Description

The Azure tenant id

* Name
`secret`
Type
string
Required
required
Enum

Description

The Azure application client secret

* Name
`groups`
Type
string[]
Required
required
Enum

Description

The Groups this integrations applies to

* Name
`last_synced_interval`
Type
integer
Required
required
Enum

**Possible Values:**`>=24`

Description

The devices last sync requirement interval in hours. Minimum value is 24 hours.

* Name
`enabled`
Type
boolean
Required
optional
Enum

Description

Indicates whether the integration is enabled

### Request

POST

/api/integrations/edr/intune
```
curl -X POST https://api.netbird.io/api/integrations/edr/intune \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"client_id": {
"type": "string",
"description": "The Azure application client id"
},
"tenant_id": {
"type": "string",
"description": "The Azure tenant id"
},
"secret": {
"type": "string",
"description": "The Azure application client secret"
},
"groups": [
{
"type": "string"
}
],
"last_synced_interval": {
"type": "integer",
"description": "The devices last sync requirement interval in hours. Minimum value is 24 hours.",
"minimum": 24
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled",
"default": true
}
}'

```

### Response
```
{
"id": 123,
"account_id": "acc_abcdef123456",
"last_synced_at": "2023-05-15T10:30:00Z",
"created_by": {
"type": "string",
"description": "The user id that created the integration"
},
"created_at": "2023-05-15T10:30:00Z",
"updated_at": "2023-05-16T11:45:00Z",
"client_id": "acc_abcdef123456",
"tenant_id": "acc_abcdef123456",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api",
"peers": [
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1"
}
],
"resources": [
{
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
]
}
],
"last_synced_interval": {
"type": "integer",
"description": "The devices last sync requirement interval in hours."
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled"
}
}

```

* * *

GET/api/integrations/edr/intune

## [Get EDR Intune Integration](https://docs.netbird.io/ipa/resources/edr-intune-integrations#get-edr-intune-integration)

Retrieves a specific EDR Intune integration by its ID.

### Request

GET

/api/integrations/edr/intune
```
curl -X GET https://api.netbird.io/api/integrations/edr/intune \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": 123,
"account_id": "acc_abcdef123456",
"last_synced_at": "2023-05-15T10:30:00Z",
"created_by": {
"type": "string",
"description": "The user id that created the integration"
},
"created_at": "2023-05-15T10:30:00Z",
"updated_at": "2023-05-16T11:45:00Z",
"client_id": "acc_abcdef123456",
"tenant_id": "acc_abcdef123456",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api",
"peers": [
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1"
}
],
"resources": [
{
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
]
}
],
"last_synced_interval": {
"type": "integer",
"description": "The devices last sync requirement interval in hours."
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled"
}
}

```

* * *

PUT/api/integrations/edr/intune

## [Update EDR Intune Integration](https://docs.netbird.io/ipa/resources/edr-intune-integrations#update-edr-intune-integration)

Updates an existing EDR Intune Integration. The request body structure is `EDRIntuneRequest`.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/edr-intune-integrations#request-body-parameters-2)

* Name
`client_id`
Type
string
Required
required
Enum

Description

The Azure application client id

* Name
`tenant_id`
Type
string
Required
required
Enum

Description

The Azure tenant id

* Name
`secret`
Type
string
Required
required
Enum

Description

The Azure application client secret

* Name
`groups`
Type
string[]
Required
required
Enum

Description

The Groups this integrations applies to

* Name
`last_synced_interval`
Type
integer
Required
required
Enum

**Possible Values:**`>=24`

Description

The devices last sync requirement interval in hours. Minimum value is 24 hours.

* Name
`enabled`
Type
boolean
Required
optional
Enum

Description

Indicates whether the integration is enabled

### Request

PUT

/api/integrations/edr/intune
```
curl -X PUT https://api.netbird.io/api/integrations/edr/intune \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"client_id": {
"type": "string",
"description": "The Azure application client id"
},
"tenant_id": {
"type": "string",
"description": "The Azure tenant id"
},
"secret": {
"type": "string",
"description": "The Azure application client secret"
},
"groups": [
{
"type": "string"
}
],
"last_synced_interval": {
"type": "integer",
"description": "The devices last sync requirement interval in hours. Minimum value is 24 hours.",
"minimum": 24
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled",
"default": true
}
}'

```

### Response
```
{
"id": 123,
"account_id": "acc_abcdef123456",
"last_synced_at": "2023-05-15T10:30:00Z",
"created_by": {
"type": "string",
"description": "The user id that created the integration"
},
"created_at": "2023-05-15T10:30:00Z",
"updated_at": "2023-05-16T11:45:00Z",
"client_id": "acc_abcdef123456",
"tenant_id": "acc_abcdef123456",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api",
"peers": [
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1"
}
],
"resources": [
{
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
]
}
],
"last_synced_interval": {
"type": "integer",
"description": "The devices last sync requirement interval in hours."
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled"
}
}

```

* * *

DELETE/api/integrations/edr/intune

## [Delete EDR Intune Integration](https://docs.netbird.io/ipa/resources/edr-intune-integrations#delete-edr-intune-integration)

Deletes an EDR Intune Integration by its ID.

### Request

DELETE

/api/integrations/edr/intune
```
curl -X DELETE https://api.netbird.io/api/integrations/edr/intune \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{}

```

* * *