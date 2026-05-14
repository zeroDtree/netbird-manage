# EDR Huntress Integrations

POST/api/integrations/edr/huntress

## [Create EDR Huntress Integration](https://docs.netbird.io/ipa/resources/edr-huntress-integrations#create-edr-huntress-integration)

Creates a new EDR Huntress integration

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/edr-huntress-integrations#request-body-parameters)

* Name
`api_key`
Type
string
Required
required
Enum

Description

Huntress API key

* Name
`api_secret`
Type
string
Required
required
Enum

Description

Huntress API secret

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

The devices last sync requirement interval in hours. Minimum value is 24 hours

* Name
`enabled`
Type
boolean
Required
optional
Enum

Description

Indicates whether the integration is enabled

* Name
`match_attributes`
Type
object
Required
required
Enum

Description
Attribute conditions to match when approving agents

* Name
`defender_policy_status`
Type
string
Required
optional
Enum

Description

Policy status of Defender AV for Managed Antivirus.

* Name
`defender_status`
Type
string
Required
optional
Enum

Description

Status of Defender AV Managed Antivirus.

* Name
`defender_substatus`
Type
string
Required
optional
Enum

Description

Sub-status of Defender AV Managed Antivirus.

* Name
`firewall_status`
Type
string
Required
optional
Enum

Description

Status of agent firewall. Can be one of Disabled, Enabled, Pending Isolation, Isolated, Pending Release.

### Request

POST

/api/integrations/edr/huntress
```
curl -X POST https://api.netbird.io/api/integrations/edr/huntress \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"api_key": {
"type": "string",
"description": "Huntress API key"
},
"api_secret": {
"type": "string",
"description": "Huntress API secret"
},
"groups": [
{
"type": "string"
}
],
"last_synced_interval": {
"type": "integer",
"description": "The devices last sync requirement interval in hours. Minimum value is 24 hours",
"minimum": 24
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled",
"default": true
},
"match_attributes": {
"defender_policy_status": "Compliant",
"defender_status": "Healthy",
"defender_substatus": "Up to date",
"firewall_status": "Enabled"
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
"description": "Indicates whether the integration is enabled",
"default": true
},
"match_attributes": {
"defender_policy_status": "Compliant",
"defender_status": "Healthy",
"defender_substatus": "Up to date",
"firewall_status": "Enabled"
}
}

```

* * *

GET/api/integrations/edr/huntress

## [Get EDR Huntress Integration](https://docs.netbird.io/ipa/resources/edr-huntress-integrations#get-edr-huntress-integration)

Retrieves a specific EDR Huntress integration by its ID.

### Request

GET

/api/integrations/edr/huntress
```
curl -X GET https://api.netbird.io/api/integrations/edr/huntress \
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
"description": "Indicates whether the integration is enabled",
"default": true
},
"match_attributes": {
"defender_policy_status": "Compliant",
"defender_status": "Healthy",
"defender_substatus": "Up to date",
"firewall_status": "Enabled"
}
}

```

* * *

PUT/api/integrations/edr/huntress

## [Update EDR Huntress Integration](https://docs.netbird.io/ipa/resources/edr-huntress-integrations#update-edr-huntress-integration)

Updates an existing EDR Huntress Integration.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/edr-huntress-integrations#request-body-parameters-2)

* Name
`api_key`
Type
string
Required
required
Enum

Description

Huntress API key

* Name
`api_secret`
Type
string
Required
required
Enum

Description

Huntress API secret

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

The devices last sync requirement interval in hours. Minimum value is 24 hours

* Name
`enabled`
Type
boolean
Required
optional
Enum

Description

Indicates whether the integration is enabled

* Name
`match_attributes`
Type
object
Required
required
Enum

Description
Attribute conditions to match when approving agents

* Name
`defender_policy_status`
Type
string
Required
optional
Enum

Description

Policy status of Defender AV for Managed Antivirus.

* Name
`defender_status`
Type
string
Required
optional
Enum

Description

Status of Defender AV Managed Antivirus.

* Name
`defender_substatus`
Type
string
Required
optional
Enum

Description

Sub-status of Defender AV Managed Antivirus.

* Name
`firewall_status`
Type
string
Required
optional
Enum

Description

Status of agent firewall. Can be one of Disabled, Enabled, Pending Isolation, Isolated, Pending Release.

### Request

PUT

/api/integrations/edr/huntress
```
curl -X PUT https://api.netbird.io/api/integrations/edr/huntress \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"api_key": {
"type": "string",
"description": "Huntress API key"
},
"api_secret": {
"type": "string",
"description": "Huntress API secret"
},
"groups": [
{
"type": "string"
}
],
"last_synced_interval": {
"type": "integer",
"description": "The devices last sync requirement interval in hours. Minimum value is 24 hours",
"minimum": 24
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled",
"default": true
},
"match_attributes": {
"defender_policy_status": "Compliant",
"defender_status": "Healthy",
"defender_substatus": "Up to date",
"firewall_status": "Enabled"
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
"description": "Indicates whether the integration is enabled",
"default": true
},
"match_attributes": {
"defender_policy_status": "Compliant",
"defender_status": "Healthy",
"defender_substatus": "Up to date",
"firewall_status": "Enabled"
}
}

```

* * *

DELETE/api/integrations/edr/huntress

## [Delete EDR Huntress Integration](https://docs.netbird.io/ipa/resources/edr-huntress-integrations#delete-edr-huntress-integration)

Deletes an EDR Huntress Integration by its ID.

### Request

DELETE

/api/integrations/edr/huntress
```
curl -X DELETE https://api.netbird.io/api/integrations/edr/huntress \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{}

```

* * *