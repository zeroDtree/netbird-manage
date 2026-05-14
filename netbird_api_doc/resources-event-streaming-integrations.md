# Event Streaming Integrations

POST/api/event-streaming

## [Create Event Streaming Integration](https://docs.netbird.io/ipa/resources/event-streaming-integrations#create-event-streaming-integration)

Creates a new event streaming integration for the authenticated account. The request body should conform to `CreateIntegrationRequest`. Note: Based on the provided Go code, the `enabled` field from the request is part of the `CreateIntegrationRequest` struct, but the backend `manager.CreateIntegration` function signature shown does not directly use this `enabled` field. The actual behavior for `enabled` during creation should be confirmed (e.g., it might have a server-side default or be handled by other logic).

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/event-streaming-integrations#request-body-parameters)

* Name
`platform`
Type
string
Required
required
Enum

Description

The event streaming platform to integrate with (e.g., "datadog", "s3", "firehose"). This field is used for creation. For updates (PUT), this field, if sent, is ignored by the backend.

* Name
`config`
Type
object
Required
required
Enum

Description

Platform-specific configuration as key-value pairs. For creation, all necessary credentials and settings must be provided. For updates, provide the fields to change or the entire new configuration.

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Specifies whether the integration is enabled. During creation (POST), this value is sent by the client, but the provided backend manager function `CreateIntegration` does not appear to use it directly, so its effect on creation should be verified. During updates (PUT), this field is used to enable or disable the integration.

### Request

POST

/api/event-streaming
```
curl -X POST https://api.netbird.io/api/event-streaming \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"platform": "s3",
"config": {
"bucket_name": "my-event-logs",
"region": "us-east-1",
"access_key_id": "AKIA...",
"secret_access_key": "YOUR_SECRET_KEY"
},
"enabled": true
}'

```

### Response
```
{
"id": 123,
"account_id": "acc_abcdef123456",
"enabled": true,
"platform": "datadog",
"created_at": "2023-05-15T10:30:00Z",
"updated_at": "2023-05-16T11:45:00Z",
"config": {
"api_key": "****",
"site": "datadoghq.com",
"region": "us-east-1"
}
}

```

* * *

GET/api/event-streaming

## [List Event Streaming Integrations](https://docs.netbird.io/ipa/resources/event-streaming-integrations#list-event-streaming-integrations)

Retrieves all event streaming integrations for the authenticated account.

### Request

GET

/api/event-streaming
```
curl -X GET https://api.netbird.io/api/event-streaming \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": 123,
"account_id": "acc_abcdef123456",
"enabled": true,
"platform": "datadog",
"created_at": "2023-05-15T10:30:00Z",
"updated_at": "2023-05-16T11:45:00Z",
"config": {
"api_key": "****",
"site": "datadoghq.com",
"region": "us-east-1"
}
}
]

```

* * *

GET/api/event-streaming/{id}

## [Get Event Streaming Integration](https://docs.netbird.io/ipa/resources/event-streaming-integrations#get-event-streaming-integration)

Retrieves a specific event streaming integration by its ID.

### Request

GET

/api/event-streaming/{id}
```
curl -X GET https://api.netbird.io/api/event-streaming/{id} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": 123,
"account_id": "acc_abcdef123456",
"enabled": true,
"platform": "datadog",
"created_at": "2023-05-15T10:30:00Z",
"updated_at": "2023-05-16T11:45:00Z",
"config": {
"api_key": "****",
"site": "datadoghq.com",
"region": "us-east-1"
}
}

```

* * *

PUT/api/event-streaming/{id}

## [Update Event Streaming Integration](https://docs.netbird.io/ipa/resources/event-streaming-integrations#update-event-streaming-integration)

Updates an existing event streaming integration. The request body structure is `CreateIntegrationRequest`. However, for updates: \- The `platform` field, if provided in the body, is ignored by the backend manager function, as the platform of an existing integration is typically immutable. \- The `enabled` and `config` fields from the request body are used to update the integration.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/event-streaming-integrations#request-body-parameters-2)

* Name
`platform`
Type
string
Required
required
Enum

Description

The event streaming platform to integrate with (e.g., "datadog", "s3", "firehose"). This field is used for creation. For updates (PUT), this field, if sent, is ignored by the backend.

* Name
`config`
Type
object
Required
required
Enum

Description

Platform-specific configuration as key-value pairs. For creation, all necessary credentials and settings must be provided. For updates, provide the fields to change or the entire new configuration.

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Specifies whether the integration is enabled. During creation (POST), this value is sent by the client, but the provided backend manager function `CreateIntegration` does not appear to use it directly, so its effect on creation should be verified. During updates (PUT), this field is used to enable or disable the integration.

### Request

PUT

/api/event-streaming/{id}
```
curl -X PUT https://api.netbird.io/api/event-streaming/{id} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"platform": "s3",
"config": {
"bucket_name": "my-event-logs",
"region": "us-east-1",
"access_key_id": "AKIA...",
"secret_access_key": "YOUR_SECRET_KEY"
},
"enabled": true
}'

```

### Response
```
{
"id": 123,
"account_id": "acc_abcdef123456",
"enabled": true,
"platform": "datadog",
"created_at": "2023-05-15T10:30:00Z",
"updated_at": "2023-05-16T11:45:00Z",
"config": {
"api_key": "****",
"site": "datadoghq.com",
"region": "us-east-1"
}
}

```

* * *

DELETE/api/event-streaming/{id}

## [Delete Event Streaming Integration](https://docs.netbird.io/ipa/resources/event-streaming-integrations#delete-event-streaming-integration)

Deletes an event streaming integration by its ID.

### Request

DELETE

/api/event-streaming/{id}
```
curl -X DELETE https://api.netbird.io/api/event-streaming/{id} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{}

```

* * *