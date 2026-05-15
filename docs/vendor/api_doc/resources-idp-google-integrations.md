# IDP Google Integrations

POST/api/integrations/google-idp

## [Create Google IDP Integration](https://docs.netbird.io/ipa/resources/idp-google-integrations#create-google-idp-integration)

Creates a new Google Workspace IDP integration

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/idp-google-integrations#request-body-parameters)

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
`service_account_key`
Type
string
Required
required
Enum

Description

Base64-encoded Google service account key

* Name
`customer_id`
Type
string
Required
required
Enum

Description

Customer ID from Google Workspace Account Settings

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

### Request

POST

/api/integrations/google-idp
```
curl -X POST https://api.netbird.io/api/integrations/google-idp \
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
"service_account_key": "eyJ0eXBlIjoic2VydmljZV9hY2NvdW50Ii...",
"customer_id": "C01234567",
"sync_interval": 300
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
"customer_id": "C01234567",
"sync_interval": 300,
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

GET/api/integrations/google-idp

## [Get All Google IDP Integrations](https://docs.netbird.io/ipa/resources/idp-google-integrations#get-all-google-idp-integrations)

Retrieves all Google Workspace IDP integrations for the authenticated account

### Request

GET

/api/integrations/google-idp
```
curl -X GET https://api.netbird.io/api/integrations/google-idp \
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
"customer_id": "C01234567",
"sync_interval": 300,
"last_synced_at": "2023-05-15T10:30:00Z"
}
]

```

* * *

GET/api/integrations/google-idp/{id}

## [Get Google IDP Integration](https://docs.netbird.io/ipa/resources/idp-google-integrations#get-google-idp-integration)

Retrieves a Google IDP integration by ID.

### Request

GET

/api/integrations/google-idp/{id}
```
curl -X GET https://api.netbird.io/api/integrations/google-idp/{id} \
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
"customer_id": "C01234567",
"sync_interval": 300,
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

PUT/api/integrations/google-idp/{id}

## [Update Google IDP Integration](https://docs.netbird.io/ipa/resources/idp-google-integrations#update-google-idp-integration)

Updates an existing Google Workspace IDP integration.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/idp-google-integrations#request-body-parameters-2)

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
`service_account_key`
Type
string
Required
optional
Enum

Description

Base64-encoded Google service account key

* Name
`customer_id`
Type
string
Required
optional
Enum

Description

Customer ID from Google Workspace Account Settings

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

/api/integrations/google-idp/{id}
```
curl -X PUT https://api.netbird.io/api/integrations/google-idp/{id} \
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
"service_account_key": {
"type": "string",
"description": "Base64-encoded Google service account key"
},
"customer_id": {
"type": "string",
"description": "Customer ID from Google Workspace Account Settings"
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
"customer_id": "C01234567",
"sync_interval": 300,
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

DELETE/api/integrations/google-idp/{id}

## [Delete Google IDP Integration](https://docs.netbird.io/ipa/resources/idp-google-integrations#delete-google-idp-integration)

Deletes a Google IDP integration by ID.

### Request

DELETE

/api/integrations/google-idp/{id}
```
curl -X DELETE https://api.netbird.io/api/integrations/google-idp/{id} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{}

```

* * *

POST/api/integrations/google-idp/{id}/sync

## [Sync Google IDP Integration](https://docs.netbird.io/ipa/resources/idp-google-integrations#sync-google-idp-integration)

Triggers a manual synchronization for a Google IDP integration.

### Request

POST

/api/integrations/google-idp/{id}/sync
```
curl -X POST https://api.netbird.io/api/integrations/google-idp/{id}/sync \
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

GET/api/integrations/google-idp/{id}/logs

## [Get Google Integration Sync Logs](https://docs.netbird.io/ipa/resources/idp-google-integrations#get-google-integration-sync-logs)

Retrieves synchronization logs for a Google IDP integration.

### Request

GET

/api/integrations/google-idp/{id}/logs
```
curl -X GET https://api.netbird.io/api/integrations/google-idp/{id}/logs \
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