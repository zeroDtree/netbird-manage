# EDR SentinelOne Integrations

POST/api/integrations/edr/sentinelone

## [Create EDR SentinelOne Integration](https://docs.netbird.io/ipa/resources/edr-sentinelone-integrations#create-edr-sentinel-one-integration)

Creates a new EDR SentinelOne integration

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/edr-sentinelone-integrations#request-body-parameters)

* Name
`api_token`
Type
string
Required
required
Enum

Description

SentinelOne API token

* Name
`api_url`
Type
string
Required
required
Enum

Description

The Base URL of SentinelOne API

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
`active_threats`
Type
integer
Required
optional
Enum

Description

The maximum allowed number of active threats on the agent

* Name
`encrypted_applications`
Type
boolean
Required
optional
Enum

Description

Whether disk encryption is enabled on the agent

* Name
`firewall_enabled`
Type
boolean
Required
optional
Enum

Description

Whether the agent firewall is enabled

* Name
`infected`
Type
boolean
Required
optional
Enum

Description

Whether the agent is currently flagged as infected

* Name
`is_active`
Type
boolean
Required
optional
Enum

Description

Whether the agent has been recently active and reporting

* Name
`is_up_to_date`
Type
boolean
Required
optional
Enum

Description

Whether the agent is running the latest available version

* Name
`network_status`
Type
string
Required
optional
Enum

Description

The current network connectivity status of the device

* Name
`operational_state`
Type
string
Required
optional
Enum

Description

The current operational state of the agent

### Request

POST

/api/integrations/edr/sentinelone
```
curl -X POST https://api.netbird.io/api/integrations/edr/sentinelone \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"api_token": {
"type": "string",
"description": "SentinelOne API token"
},
"api_url": {
"type": "string",
"description": "The Base URL of SentinelOne API"
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
},
"match_attributes": {
"active_threats": 0,
"encrypted_applications": {
"description": "Whether disk encryption is enabled on the agent",
"type": "boolean"
},
"firewall_enabled": {
"description": "Whether the agent firewall is enabled",
"type": "boolean"
},
"infected": {
"description": "Whether the agent is currently flagged as infected",
"type": "boolean"
},
"is_active": {
"description": "Whether the agent has been recently active and reporting",
"type": "boolean"
},
"is_up_to_date": {
"description": "Whether the agent is running the latest available version",
"type": "boolean"
},
"network_status": {
"description": "The current network connectivity status of the device",
"type": "string",
"enum": [
"connected",
"disconnected",
"quarantined"
]
},
"operational_state": {
"description": "The current operational state of the agent",
"type": "string"
}
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
"api_url": {
"type": "string",
"description": "The Base URL of SentinelOne API"
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
"last_synced_interval": {
"type": "integer",
"description": "The devices last sync requirement interval in hours."
},
"match_attributes": {
"active_threats": 0,
"encrypted_applications": {
"description": "Whether disk encryption is enabled on the agent",
"type": "boolean"
},
"firewall_enabled": {
"description": "Whether the agent firewall is enabled",
"type": "boolean"
},
"infected": {
"description": "Whether the agent is currently flagged as infected",
"type": "boolean"
},
"is_active": {
"description": "Whether the agent has been recently active and reporting",
"type": "boolean"
},
"is_up_to_date": {
"description": "Whether the agent is running the latest available version",
"type": "boolean"
},
"network_status": {
"description": "The current network connectivity status of the device",
"type": "string",
"enum": [
"connected",
"disconnected",
"quarantined"
]
},
"operational_state": {
"description": "The current operational state of the agent",
"type": "string"
}
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled"
}
}

```

* * *

GET/api/integrations/edr/sentinelone

## [Get EDR SentinelOne Integration](https://docs.netbird.io/ipa/resources/edr-sentinelone-integrations#get-edr-sentinel-one-integration)

Retrieves a specific EDR SentinelOne integration by its ID.

### Request

GET

/api/integrations/edr/sentinelone
```
curl -X GET https://api.netbird.io/api/integrations/edr/sentinelone \
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
"api_url": {
"type": "string",
"description": "The Base URL of SentinelOne API"
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
"last_synced_interval": {
"type": "integer",
"description": "The devices last sync requirement interval in hours."
},
"match_attributes": {
"active_threats": 0,
"encrypted_applications": {
"description": "Whether disk encryption is enabled on the agent",
"type": "boolean"
},
"firewall_enabled": {
"description": "Whether the agent firewall is enabled",
"type": "boolean"
},
"infected": {
"description": "Whether the agent is currently flagged as infected",
"type": "boolean"
},
"is_active": {
"description": "Whether the agent has been recently active and reporting",
"type": "boolean"
},
"is_up_to_date": {
"description": "Whether the agent is running the latest available version",
"type": "boolean"
},
"network_status": {
"description": "The current network connectivity status of the device",
"type": "string",
"enum": [
"connected",
"disconnected",
"quarantined"
]
},
"operational_state": {
"description": "The current operational state of the agent",
"type": "string"
}
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled"
}
}

```

* * *

PUT/api/integrations/edr/sentinelone

## [Update EDR SentinelOne Integration](https://docs.netbird.io/ipa/resources/edr-sentinelone-integrations#update-edr-sentinel-one-integration)

Updates an existing EDR SentinelOne Integration.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/edr-sentinelone-integrations#request-body-parameters-2)

* Name
`api_token`
Type
string
Required
required
Enum

Description

SentinelOne API token

* Name
`api_url`
Type
string
Required
required
Enum

Description

The Base URL of SentinelOne API

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
`active_threats`
Type
integer
Required
optional
Enum

Description

The maximum allowed number of active threats on the agent

* Name
`encrypted_applications`
Type
boolean
Required
optional
Enum

Description

Whether disk encryption is enabled on the agent

* Name
`firewall_enabled`
Type
boolean
Required
optional
Enum

Description

Whether the agent firewall is enabled

* Name
`infected`
Type
boolean
Required
optional
Enum

Description

Whether the agent is currently flagged as infected

* Name
`is_active`
Type
boolean
Required
optional
Enum

Description

Whether the agent has been recently active and reporting

* Name
`is_up_to_date`
Type
boolean
Required
optional
Enum

Description

Whether the agent is running the latest available version

* Name
`network_status`
Type
string
Required
optional
Enum

Description

The current network connectivity status of the device

* Name
`operational_state`
Type
string
Required
optional
Enum

Description

The current operational state of the agent

### Request

PUT

/api/integrations/edr/sentinelone
```
curl -X PUT https://api.netbird.io/api/integrations/edr/sentinelone \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"api_token": {
"type": "string",
"description": "SentinelOne API token"
},
"api_url": {
"type": "string",
"description": "The Base URL of SentinelOne API"
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
},
"match_attributes": {
"active_threats": 0,
"encrypted_applications": {
"description": "Whether disk encryption is enabled on the agent",
"type": "boolean"
},
"firewall_enabled": {
"description": "Whether the agent firewall is enabled",
"type": "boolean"
},
"infected": {
"description": "Whether the agent is currently flagged as infected",
"type": "boolean"
},
"is_active": {
"description": "Whether the agent has been recently active and reporting",
"type": "boolean"
},
"is_up_to_date": {
"description": "Whether the agent is running the latest available version",
"type": "boolean"
},
"network_status": {
"description": "The current network connectivity status of the device",
"type": "string",
"enum": [
"connected",
"disconnected",
"quarantined"
]
},
"operational_state": {
"description": "The current operational state of the agent",
"type": "string"
}
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
"api_url": {
"type": "string",
"description": "The Base URL of SentinelOne API"
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
"last_synced_interval": {
"type": "integer",
"description": "The devices last sync requirement interval in hours."
},
"match_attributes": {
"active_threats": 0,
"encrypted_applications": {
"description": "Whether disk encryption is enabled on the agent",
"type": "boolean"
},
"firewall_enabled": {
"description": "Whether the agent firewall is enabled",
"type": "boolean"
},
"infected": {
"description": "Whether the agent is currently flagged as infected",
"type": "boolean"
},
"is_active": {
"description": "Whether the agent has been recently active and reporting",
"type": "boolean"
},
"is_up_to_date": {
"description": "Whether the agent is running the latest available version",
"type": "boolean"
},
"network_status": {
"description": "The current network connectivity status of the device",
"type": "string",
"enum": [
"connected",
"disconnected",
"quarantined"
]
},
"operational_state": {
"description": "The current operational state of the agent",
"type": "string"
}
},
"enabled": {
"type": "boolean",
"description": "Indicates whether the integration is enabled"
}
}

```

* * *

DELETE/api/integrations/edr/sentinelone

## [Delete EDR SentinelOne Integration](https://docs.netbird.io/ipa/resources/edr-sentinelone-integrations#delete-edr-sentinel-one-integration)

Deletes an EDR SentinelOne Integration by its ID.

### Request

DELETE

/api/integrations/edr/sentinelone
```
curl -X DELETE https://api.netbird.io/api/integrations/edr/sentinelone \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{}

```

* * *