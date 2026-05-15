# IDP Azure Integrations

POST/api/integrations/azure-idp

## [Create Azure IDP Integration](https://docs.netbird.io/ipa/resources/idp-azure-integrations#create-azure-idp-integration)

Creates a new Azure AD IDP integration

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/idp-azure-integrations#request-body-parameters)

* Name
`group_prefixes`
Type
string[]
Required
optional
Enum

Description

List of start_with string patterns for groups to sync

* Name
`user_group_prefixes`
Type
string[]
Required
optional
Enum

Description

List of start_with string patterns for groups which users to sync

* Name
`connector_id`
Type
string
Required
optional
Enum

Description

DEX connector ID for embedded IDP setups

* Name
`client_secret`
Type
string
Required
required
Enum

Description

Base64-encoded Azure AD client secret

* Name
`client_id`
Type
string
Required
required
Enum

Description

Azure AD application (client) ID

* Name
`tenant_id`
Type
string
Required
required
Enum

Description

Azure AD tenant ID

* Name
`sync_interval`
Type
integer
Required
optional
Enum

**Possible Values:**`>=300`

Description

Sync interval in seconds (minimum 300). Defaults to 300 if not specified.

* Name
`host`
Type
string
Required
required
Enum

Description

Azure host domain for the Graph API

### Request

POST

/api/integrations/azure-idp
```
curl -X POST https://api.netbird.io/api/integrations/azure-idp \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"group_prefixes": [
"Engineering",
"Sales"
],
"user_group_prefixes": [
"Users"
],
"connector_id": {
"type": "string",
"description": "DEX connector ID for embedded IDP setups"
},
"client_secret": "c2VjcmV0...",
"client_id": "12345678-1234-1234-1234-123456789012",
"tenant_id": "87654321-4321-4321-4321-210987654321",
"sync_interval": 300,
"host": "microsoft.com"
}'

```

### Response
```
{
"enabled": true,
"group_prefixes": [
"Engineering",
"Sales"
],
"user_group_prefixes": [
"Users"
],
"connector_id": {
"type": "string",
"description": "DEX connector ID for embedded IDP setups"
},
"id": 1,
"client_id": "12345678-1234-1234-1234-123456789012",
"tenant_id": "87654321-4321-4321-4321-210987654321",
"sync_interval": 300,
"host": "microsoft.com",
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

GET/api/integrations/azure-idp

## [Get All Azure IDP Integrations](https://docs.netbird.io/ipa/resources/idp-azure-integrations#get-all-azure-idp-integrations)

Retrieves all Azure AD IDP integrations for the authenticated account

### Request

GET

/api/integrations/azure-idp
```
curl -X GET https://api.netbird.io/api/integrations/azure-idp \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"enabled": true,
"group_prefixes": [
"Engineering",
"Sales"
],
"user_group_prefixes": [
"Users"
],
"connector_id": {
"type": "string",
"description": "DEX connector ID for embedded IDP setups"
},
"id": 1,
"client_id": "12345678-1234-1234-1234-123456789012",
"tenant_id": "87654321-4321-4321-4321-210987654321",
"sync_interval": 300,
"host": "microsoft.com",
"last_synced_at": "2023-05-15T10:30:00Z"
}
]

```

* * *

GET/api/integrations/azure-idp/{id}

## [Get Azure IDP Integration](https://docs.netbird.io/ipa/resources/idp-azure-integrations#get-azure-idp-integration)

Retrieves an Azure IDP integration by ID.

### Request

GET

/api/integrations/azure-idp/{id}
```
curl -X GET https://api.netbird.io/api/integrations/azure-idp/{id} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"enabled": true,
"group_prefixes": [
"Engineering",
"Sales"
],
"user_group_prefixes": [
"Users"
],
"connector_id": {
"type": "string",
"description": "DEX connector ID for embedded IDP setups"
},
"id": 1,
"client_id": "12345678-1234-1234-1234-123456789012",
"tenant_id": "87654321-4321-4321-4321-210987654321",
"sync_interval": 300,
"host": "microsoft.com",
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

PUT/api/integrations/azure-idp/{id}

## [Update Azure IDP Integration](https://docs.netbird.io/ipa/resources/idp-azure-integrations#update-azure-idp-integration)

Updates an existing Azure AD IDP integration.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/idp-azure-integrations#request-body-parameters-2)

* Name
`enabled`
Type
boolean
Required
optional
Enum

Description

Whether the integration is enabled

* Name
`group_prefixes`
Type
string[]
Required
optional
Enum

Description

List of start_with string patterns for groups to sync

* Name
`user_group_prefixes`
Type
string[]
Required
optional
Enum

Description

List of start_with string patterns for groups which users to sync

* Name
`connector_id`
Type
string
Required
optional
Enum

Description

DEX connector ID for embedded IDP setups

* Name
`client_secret`
Type
string
Required
optional
Enum

Description

Base64-encoded Azure AD client secret

* Name
`client_id`
Type
string
Required
optional
Enum

Description

Azure AD application (client) ID

* Name
`tenant_id`
Type
string
Required
optional
Enum

Description

Azure AD tenant ID

* Name
`sync_interval`
Type
integer
Required
optional
Enum

**Possible Values:**`>=300`

Description

Sync interval in seconds (minimum 300)

### Request

PUT

/api/integrations/azure-idp/{id}
```
curl -X PUT https://api.netbird.io/api/integrations/azure-idp/{id} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"enabled": true,
"group_prefixes": [
"Engineering",
"Sales"
],
"user_group_prefixes": [
"Users"
],
"connector_id": {
"type": "string",
"description": "DEX connector ID for embedded IDP setups"
},
"client_secret": {
"type": "string",
"description": "Base64-encoded Azure AD client secret"
},
"client_id": {
"type": "string",
"description": "Azure AD application (client) ID"
},
"tenant_id": {
"type": "string",
"description": "Azure AD tenant ID"
},
"sync_interval": {
"type": "integer",
"description": "Sync interval in seconds (minimum 300)",
"minimum": 300
}
}'

```

### Response
```
{
"enabled": true,
"group_prefixes": [
"Engineering",
"Sales"
],
"user_group_prefixes": [
"Users"
],
"connector_id": {
"type": "string",
"description": "DEX connector ID for embedded IDP setups"
},
"id": 1,
"client_id": "12345678-1234-1234-1234-123456789012",
"tenant_id": "87654321-4321-4321-4321-210987654321",
"sync_interval": 300,
"host": "microsoft.com",
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

DELETE/api/integrations/azure-idp/{id}

## [Delete Azure IDP Integration](https://docs.netbird.io/ipa/resources/idp-azure-integrations#delete-azure-idp-integration)

Deletes an Azure IDP integration by ID.

### Request

DELETE

/api/integrations/azure-idp/{id}
```
curl -X DELETE https://api.netbird.io/api/integrations/azure-idp/{id} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{}

```

* * *

POST/api/integrations/azure-idp/{id}/sync

## [Sync Azure IDP Integration](https://docs.netbird.io/ipa/resources/idp-azure-integrations#sync-azure-idp-integration)

Triggers a manual synchronization for an Azure IDP integration.

### Request

POST

/api/integrations/azure-idp/{id}/sync
```
curl -X POST https://api.netbird.io/api/integrations/azure-idp/{id}/sync \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"result": "ok"
}

```

* * *

GET/api/integrations/azure-idp/{id}/logs

## [Get Azure Integration Sync Logs](https://docs.netbird.io/ipa/resources/idp-azure-integrations#get-azure-integration-sync-logs)

Retrieves synchronization logs for an Azure IDP integration.

### Request

GET

/api/integrations/azure-idp/{id}/logs
```
curl -X GET https://api.netbird.io/api/integrations/azure-idp/{id}/logs \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": 123,
"level": "info",
"timestamp": "2023-05-15T10:30:00Z",
"message": "Successfully synchronized users and groups"
}
]

```

* * *