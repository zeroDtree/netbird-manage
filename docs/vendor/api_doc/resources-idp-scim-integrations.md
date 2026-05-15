# IDP SCIM Integrations

POST/api/integrations/scim-idp

## [Create SCIM IDP Integration](https://docs.netbird.io/ipa/resources/idp-scim-integrations#create-scim-idp-integration)

Creates a new SCIM integration

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/idp-scim-integrations#request-body-parameters)

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
`prefix`
Type
string
Required
required
Enum

Description

The connection prefix used for the SCIM provider

* Name
`provider`
Type
string
Required
required
Enum

Description

Name of the SCIM identity provider

### Request

POST

/api/integrations/scim-idp
```
curl -X POST https://api.netbird.io/api/integrations/scim-idp \
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
"prefix": {
"type": "string",
"description": "The connection prefix used for the SCIM provider"
},
"provider": {
"type": "string",
"description": "Name of the SCIM identity provider"
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
"id": 123,
"prefix": {
"type": "string",
"description": "The connection prefix used for the SCIM provider"
},
"provider": {
"type": "string",
"description": "Name of the SCIM identity provider"
},
"auth_token": "nbs_abc***********************************",
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

GET/api/integrations/scim-idp

## [Get All SCIM IDP Integrations](https://docs.netbird.io/ipa/resources/idp-scim-integrations#get-all-scim-idp-integrations)

Retrieves all SCIM IDP integrations for the authenticated account

### Request

GET

/api/integrations/scim-idp
```
curl -X GET https://api.netbird.io/api/integrations/scim-idp \
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
"id": 123,
"prefix": {
"type": "string",
"description": "The connection prefix used for the SCIM provider"
},
"provider": {
"type": "string",
"description": "Name of the SCIM identity provider"
},
"auth_token": "nbs_abc***********************************",
"last_synced_at": "2023-05-15T10:30:00Z"
}
]

```

* * *

GET/api/integrations/scim-idp/{id}

## [Get SCIM IDP Integration](https://docs.netbird.io/ipa/resources/idp-scim-integrations#get-scim-idp-integration)

Retrieves an SCIM IDP integration by ID.

### Request

GET

/api/integrations/scim-idp/{id}
```
curl -X GET https://api.netbird.io/api/integrations/scim-idp/{id} \
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
"id": 123,
"prefix": {
"type": "string",
"description": "The connection prefix used for the SCIM provider"
},
"provider": {
"type": "string",
"description": "Name of the SCIM identity provider"
},
"auth_token": "nbs_abc***********************************",
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

PUT/api/integrations/scim-idp/{id}

## [Update SCIM IDP Integration](https://docs.netbird.io/ipa/resources/idp-scim-integrations#update-scim-idp-integration)

Updates an existing SCIM IDP Integration.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/idp-scim-integrations#request-body-parameters-2)

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
`prefix`
Type
string
Required
optional
Enum

Description

The connection prefix used for the SCIM provider

### Request

PUT

/api/integrations/scim-idp/{id}
```
curl -X PUT https://api.netbird.io/api/integrations/scim-idp/{id} \
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
"prefix": {
"type": "string",
"description": "The connection prefix used for the SCIM provider"
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
"id": 123,
"prefix": {
"type": "string",
"description": "The connection prefix used for the SCIM provider"
},
"provider": {
"type": "string",
"description": "Name of the SCIM identity provider"
},
"auth_token": "nbs_abc***********************************",
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

DELETE/api/integrations/scim-idp/{id}

## [Delete SCIM IDP Integration](https://docs.netbird.io/ipa/resources/idp-scim-integrations#delete-scim-idp-integration)

Deletes an SCIM IDP integration by ID.

### Request

DELETE

/api/integrations/scim-idp/{id}
```
curl -X DELETE https://api.netbird.io/api/integrations/scim-idp/{id} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{}

```

* * *

POST/api/integrations/scim-idp/{id}/token

## [Regenerate SCIM Token](https://docs.netbird.io/ipa/resources/idp-scim-integrations#regenerate-scim-token)

Regenerates the SCIM API token for an SCIM IDP integration.

### Request

POST

/api/integrations/scim-idp/{id}/token
```
curl -X POST https://api.netbird.io/api/integrations/scim-idp/{id}/token \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"auth_token": "nbs_F3f0d..."
}

```

* * *

GET/api/integrations/scim-idp/{id}/logs

## [Get SCIM Integration Sync Logs](https://docs.netbird.io/ipa/resources/idp-scim-integrations#get-scim-integration-sync-logs)

Retrieves synchronization logs for a SCIM IDP integration.

### Request

GET

/api/integrations/scim-idp/{id}/logs
```
curl -X GET https://api.netbird.io/api/integrations/scim-idp/{id}/logs \
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