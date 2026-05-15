# EDR Falcon Integrations

POST/api/integrations/edr/falcon

## [Create EDR Falcon Integration](https://docs.netbird.io/ipa/resources/edr-falcon-integrations#create-edr-falcon-integration)

Creates a new EDR Falcon integration

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/edr-falcon-integrations#request-body-parameters)

* Name
`client_id`
Type
string
Required
required
Enum

Description

CrowdStrike API client ID

* Name
`secret`
Type
string
Required
required
Enum

Description

CrowdStrike API client secret

* Name
`cloud_id`
Type
string
Required
required
Enum

Description

CrowdStrike cloud identifier (e.g., "us-1", "us-2", "eu-1")

* Name
`groups`
Type
string[]
Required
required
Enum

Description

The Groups this integration applies to

* Name
`zta_score_threshold`
Type
integer
Required
required
Enum
0

**Possible Values:**`<=100`

0
Description

The minimum Zero Trust Assessment score required for agent approval (0-100)

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

/api/integrations/edr/falcon
```
curl -X POST https://api.netbird.io/api/integrations/edr/falcon \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"client_id": {
"type": "string",
"description": "CrowdStrike API client ID"
},
"secret": {
"type": "string",
"description": "CrowdStrike API client secret"
},
"cloud_id": {
"type": "string",
"description": "CrowdStrike cloud identifier (e.g., \"us-1\", \"us-2\", \"eu-1\")"
},
"groups": [
{
"type": "string"
}
],
"zta_score_threshold": 75,
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
"account_id": "ch8i4ug6lnn4g9hqv7l0",
"last_synced_at": "2023-05-15T10:30:00Z",
"created_by": {
"type": "string",
"description": "The user id that created the integration"
},
"created_at": "2023-05-15T10:30:00Z",
"updated_at": "2023-05-16T11:45:00Z",
"cloud_id": {
"type": "string",
"description": "CrowdStrike cloud identifier"
},
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
"zta_score_threshold": {
"type": "integer",
"description": "The minimum Zero Trust Assessment score required for agent approval (0-100)"
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled"
}
}

```

* * *

GET/api/integrations/edr/falcon

## [Get EDR Falcon Integration](https://docs.netbird.io/ipa/resources/edr-falcon-integrations#get-edr-falcon-integration)

Retrieves a specific EDR Falcon integration by its ID.

### Request

GET

/api/integrations/edr/falcon
```
curl -X GET https://api.netbird.io/api/integrations/edr/falcon \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": 123,
"account_id": "ch8i4ug6lnn4g9hqv7l0",
"last_synced_at": "2023-05-15T10:30:00Z",
"created_by": {
"type": "string",
"description": "The user id that created the integration"
},
"created_at": "2023-05-15T10:30:00Z",
"updated_at": "2023-05-16T11:45:00Z",
"cloud_id": {
"type": "string",
"description": "CrowdStrike cloud identifier"
},
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
"zta_score_threshold": {
"type": "integer",
"description": "The minimum Zero Trust Assessment score required for agent approval (0-100)"
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled"
}
}

```

* * *

PUT/api/integrations/edr/falcon

## [Update EDR Falcon Integration](https://docs.netbird.io/ipa/resources/edr-falcon-integrations#update-edr-falcon-integration)

Updates an existing EDR Falcon Integration.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/edr-falcon-integrations#request-body-parameters-2)

* Name
`client_id`
Type
string
Required
required
Enum

Description

CrowdStrike API client ID

* Name
`secret`
Type
string
Required
required
Enum

Description

CrowdStrike API client secret

* Name
`cloud_id`
Type
string
Required
required
Enum

Description

CrowdStrike cloud identifier (e.g., "us-1", "us-2", "eu-1")

* Name
`groups`
Type
string[]
Required
required
Enum

Description

The Groups this integration applies to

* Name
`zta_score_threshold`
Type
integer
Required
required
Enum
0

**Possible Values:**`<=100`

0
Description

The minimum Zero Trust Assessment score required for agent approval (0-100)

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

/api/integrations/edr/falcon
```
curl -X PUT https://api.netbird.io/api/integrations/edr/falcon \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"client_id": {
"type": "string",
"description": "CrowdStrike API client ID"
},
"secret": {
"type": "string",
"description": "CrowdStrike API client secret"
},
"cloud_id": {
"type": "string",
"description": "CrowdStrike cloud identifier (e.g., \"us-1\", \"us-2\", \"eu-1\")"
},
"groups": [
{
"type": "string"
}
],
"zta_score_threshold": 75,
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
"account_id": "ch8i4ug6lnn4g9hqv7l0",
"last_synced_at": "2023-05-15T10:30:00Z",
"created_by": {
"type": "string",
"description": "The user id that created the integration"
},
"created_at": "2023-05-15T10:30:00Z",
"updated_at": "2023-05-16T11:45:00Z",
"cloud_id": {
"type": "string",
"description": "CrowdStrike cloud identifier"
},
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
"zta_score_threshold": {
"type": "integer",
"description": "The minimum Zero Trust Assessment score required for agent approval (0-100)"
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled"
}
}

```

* * *

DELETE/api/integrations/edr/falcon

## [Delete EDR Falcon Integration](https://docs.netbird.io/ipa/resources/edr-falcon-integrations#delete-edr-falcon-integration)

Deletes an existing EDR Falcon Integration by its ID.

### Request

DELETE

/api/integrations/edr/falcon
```
curl -X DELETE https://api.netbird.io/api/integrations/edr/falcon \
-H 'Authorization: Token <TOKEN>'

```

* * *