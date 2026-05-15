# EDR FleetDM Integrations

POST/api/integrations/edr/fleetdm

## [Create EDR FleetDM Integration](https://docs.netbird.io/ipa/resources/edr-fleetdm-integrations#create-edr-fleet-dm-integration)

Creates a new EDR FleetDM integration

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/edr-fleetdm-integrations#request-body-parameters)

* Name
`api_url`
Type
string
Required
required
Enum

Description

FleetDM server URL

* Name
`api_token`
Type
string
Required
required
Enum

Description

FleetDM API token

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
Attribute conditions to match when approving FleetDM hosts. Most attributes work with FleetDM's free/open-source version. Premium-only attributes are marked accordingly

* Name
`disk_encryption_enabled`
Type
boolean
Required
optional
Enum

Description

Whether disk encryption (FileVault/BitLocker) must be enabled on the host

* Name
`failing_policies_count_max`
Type
integer
Required
optional
Enum
00
Description

Maximum number of allowed failing policies. Use 0 to require all policies to pass

* Name
`vulnerable_software_count_max`
Type
integer
Required
optional
Enum
00
Description

Maximum number of allowed vulnerable software on the host

* Name
`status_online`
Type
boolean
Required
optional
Enum

Description

Whether the host must be online (recently seen by Fleet)

* Name
`required_policies`
Type
integer[]
Required
optional
Enum

Description

List of FleetDM policy IDs that must be passing on the host. If any of these policies is failing, the host is non-compliant

### Request

POST

/api/integrations/edr/fleetdm
```
curl -X POST https://api.netbird.io/api/integrations/edr/fleetdm \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"api_url": {
"type": "string",
"description": "FleetDM server URL"
},
"api_token": {
"type": "string",
"description": "FleetDM API token"
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
"disk_encryption_enabled": {
"type": "boolean",
"description": "Whether disk encryption (FileVault/BitLocker) must be enabled on the host"
},
"failing_policies_count_max": 0,
"vulnerable_software_count_max": 0,
"status_online": {
"type": "boolean",
"description": "Whether the host must be online (recently seen by Fleet)"
},
"required_policies": [
1,
5,
12
]
}
}'

```

### Response
```
{
"id": 123,
"account_id": "ch8i4ug6lnn4g9hqv7l0",
"api_url": {
"type": "string",
"description": "FleetDM server URL"
},
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
"disk_encryption_enabled": {
"type": "boolean",
"description": "Whether disk encryption (FileVault/BitLocker) must be enabled on the host"
},
"failing_policies_count_max": 0,
"vulnerable_software_count_max": 0,
"status_online": {
"type": "boolean",
"description": "Whether the host must be online (recently seen by Fleet)"
},
"required_policies": [
1,
5,
12
]
}
}

```

* * *

GET/api/integrations/edr/fleetdm

## [Get EDR FleetDM Integration](https://docs.netbird.io/ipa/resources/edr-fleetdm-integrations#get-edr-fleet-dm-integration)

Retrieves a specific EDR FleetDM integration by its ID.

### Request

GET

/api/integrations/edr/fleetdm
```
curl -X GET https://api.netbird.io/api/integrations/edr/fleetdm \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": 123,
"account_id": "ch8i4ug6lnn4g9hqv7l0",
"api_url": {
"type": "string",
"description": "FleetDM server URL"
},
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
"disk_encryption_enabled": {
"type": "boolean",
"description": "Whether disk encryption (FileVault/BitLocker) must be enabled on the host"
},
"failing_policies_count_max": 0,
"vulnerable_software_count_max": 0,
"status_online": {
"type": "boolean",
"description": "Whether the host must be online (recently seen by Fleet)"
},
"required_policies": [
1,
5,
12
]
}
}

```

* * *

PUT/api/integrations/edr/fleetdm

## [Update EDR FleetDM Integration](https://docs.netbird.io/ipa/resources/edr-fleetdm-integrations#update-edr-fleet-dm-integration)

Updates an existing EDR FleetDM Integration.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/edr-fleetdm-integrations#request-body-parameters-2)

* Name
`api_url`
Type
string
Required
required
Enum

Description

FleetDM server URL

* Name
`api_token`
Type
string
Required
required
Enum

Description

FleetDM API token

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
Attribute conditions to match when approving FleetDM hosts. Most attributes work with FleetDM's free/open-source version. Premium-only attributes are marked accordingly

* Name
`disk_encryption_enabled`
Type
boolean
Required
optional
Enum

Description

Whether disk encryption (FileVault/BitLocker) must be enabled on the host

* Name
`failing_policies_count_max`
Type
integer
Required
optional
Enum
00
Description

Maximum number of allowed failing policies. Use 0 to require all policies to pass

* Name
`vulnerable_software_count_max`
Type
integer
Required
optional
Enum
00
Description

Maximum number of allowed vulnerable software on the host

* Name
`status_online`
Type
boolean
Required
optional
Enum

Description

Whether the host must be online (recently seen by Fleet)

* Name
`required_policies`
Type
integer[]
Required
optional
Enum

Description

List of FleetDM policy IDs that must be passing on the host. If any of these policies is failing, the host is non-compliant

### Request

PUT

/api/integrations/edr/fleetdm
```
curl -X PUT https://api.netbird.io/api/integrations/edr/fleetdm \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"api_url": {
"type": "string",
"description": "FleetDM server URL"
},
"api_token": {
"type": "string",
"description": "FleetDM API token"
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
"disk_encryption_enabled": {
"type": "boolean",
"description": "Whether disk encryption (FileVault/BitLocker) must be enabled on the host"
},
"failing_policies_count_max": 0,
"vulnerable_software_count_max": 0,
"status_online": {
"type": "boolean",
"description": "Whether the host must be online (recently seen by Fleet)"
},
"required_policies": [
1,
5,
12
]
}
}'

```

### Response
```
{
"id": 123,
"account_id": "ch8i4ug6lnn4g9hqv7l0",
"api_url": {
"type": "string",
"description": "FleetDM server URL"
},
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
"disk_encryption_enabled": {
"type": "boolean",
"description": "Whether disk encryption (FileVault/BitLocker) must be enabled on the host"
},
"failing_policies_count_max": 0,
"vulnerable_software_count_max": 0,
"status_online": {
"type": "boolean",
"description": "Whether the host must be online (recently seen by Fleet)"
},
"required_policies": [
1,
5,
12
]
}
}

```

* * *

DELETE/api/integrations/edr/fleetdm

## [Delete EDR FleetDM Integration](https://docs.netbird.io/ipa/resources/edr-fleetdm-integrations#delete-edr-fleet-dm-integration)

Deletes an EDR FleetDM Integration by its ID.

### Request

DELETE

/api/integrations/edr/fleetdm
```
curl -X DELETE https://api.netbird.io/api/integrations/edr/fleetdm \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{}

```

* * *