# IDP Okta SCIM Integrations

POST/api/integrations/okta-scim-idp

## [Create Okta SCIM IDP Integration](https://docs.netbird.io/ipa/resources/idp-okta-scim-integrations#create-okta-scim-idp-integration)

Creates a new Okta SCIM IDP integration

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/idp-okta-scim-integrations#request-body-parameters)

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
`connection_name`
Type
string
Required
required
Enum

Description

The Okta enterprise connection name on Auth0

### Request

POST

/api/integrations/okta-scim-idp
```
curl -X POST https://api.netbird.io/api/integrations/okta-scim-idp \
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
"connection_name": "my-okta-connection"
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
"auth_token": "nbs_abc***********************************",
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

GET/api/integrations/okta-scim-idp

## [Get All Okta SCIM IDP Integrations](https://docs.netbird.io/ipa/resources/idp-okta-scim-integrations#get-all-okta-scim-idp-integrations)

Retrieves all Okta SCIM IDP integrations for the authenticated account

### Request

GET

/api/integrations/okta-scim-idp
```
curl -X GET https://api.netbird.io/api/integrations/okta-scim-idp \
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
"auth_token": "nbs_abc***********************************",
"last_synced_at": "2023-05-15T10:30:00Z"
}
]

```

* * *

GET/api/integrations/okta-scim-idp/{id}

## [Get Okta SCIM IDP Integration](https://docs.netbird.io/ipa/resources/idp-okta-scim-integrations#get-okta-scim-idp-integration)

Retrieves an Okta SCIM IDP integration by ID.

### Request

GET

/api/integrations/okta-scim-idp/{id}
```
curl -X GET https://api.netbird.io/api/integrations/okta-scim-idp/{id} \
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
"auth_token": "nbs_abc***********************************",
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

PUT/api/integrations/okta-scim-idp/{id}

## [Update Okta SCIM IDP Integration](https://docs.netbird.io/ipa/resources/idp-okta-scim-integrations#update-okta-scim-idp-integration)

Updates an existing Okta SCIM IDP integration.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/idp-okta-scim-integrations#request-body-parameters-2)

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

### Request

PUT

/api/integrations/okta-scim-idp/{id}
```
curl -X PUT https://api.netbird.io/api/integrations/okta-scim-idp/{id} \
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
"auth_token": "nbs_abc***********************************",
"last_synced_at": "2023-05-15T10:30:00Z"
}

```

* * *

DELETE/api/integrations/okta-scim-idp/{id}

## [Delete Okta SCIM IDP Integration](https://docs.netbird.io/ipa/resources/idp-okta-scim-integrations#delete-okta-scim-idp-integration)

Deletes an Okta SCIM IDP integration by ID.

### Request

DELETE

/api/integrations/okta-scim-idp/{id}
```
curl -X DELETE https://api.netbird.io/api/integrations/okta-scim-idp/{id} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{}

```

* * *

POST/api/integrations/okta-scim-idp/{id}/token

## [Regenerate Okta SCIM Token](https://docs.netbird.io/ipa/resources/idp-okta-scim-integrations#regenerate-okta-scim-token)

Regenerates the SCIM API token for an Okta SCIM IDP integration.

### Request

POST

/api/integrations/okta-scim-idp/{id}/token
```
curl -X POST https://api.netbird.io/api/integrations/okta-scim-idp/{id}/token \
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

GET/api/integrations/okta-scim-idp/{id}/logs

## [Get Okta SCIM Integration Sync Logs](https://docs.netbird.io/ipa/resources/idp-okta-scim-integrations#get-okta-scim-integration-sync-logs)

Retrieves synchronization logs for an Okta SCIM IDP integration.

### Request

GET

/api/integrations/okta-scim-idp/{id}/logs
```
curl -X GET https://api.netbird.io/api/integrations/okta-scim-idp/{id}/logs \
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