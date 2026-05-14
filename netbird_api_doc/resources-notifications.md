# Notifications

GET/api/integrations/notifications/types

## [List Notification Event Types](https://docs.netbird.io/ipa/resources/notifications#list-notification-event-types)

Returns a map of all supported activity event type codes to their human-readable descriptions. Use these codes when configuring `event_types` on notification channels.

### Request

GET

/api/integrations/notifications/types
```
curl -X GET https://api.netbird.io/api/integrations/notifications/types \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"user.join": "User joined"
}

```

* * *

GET/api/integrations/notifications/channels

## [List Notification Channels](https://docs.netbird.io/ipa/resources/notifications#list-notification-channels)

Retrieves all notification channels configured for the authenticated account.

### Request

GET

/api/integrations/notifications/channels
```
curl -X GET https://api.netbird.io/api/integrations/notifications/channels \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"type": "email",
"target": {
"description": "Channel-specific target configuration. The shape depends on the `type` field:\n- `email`: an `EmailTarget` object\n- `webhook`: a `WebhookTarget` object\n",
"oneOf": [
{
"emails": [
"admin@example.com",
"ops@example.com"
]
},
{
"url": "https://hooks.example.com/netbird",
"headers": {
"Authorization": "Bearer token",
"X-Webhook-Secret": "secret"
}
}
]
},
"event_types": [
"user.join",
"peer.user.add",
"peer.login.expire"
],
"enabled": true
}
]

```

* * *

POST/api/integrations/notifications/channels

## [Create Notification Channel](https://docs.netbird.io/ipa/resources/notifications#create-notification-channel)

Creates a new notification channel for the authenticated account. Supported channel types are `email` and `webhook`.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/notifications#request-body-parameters)

* Name
`type`
Type
string
Required
required
Enum

Description

The type of notification channel.

* Name
`target`
Type

Required
optional
Enum

Description

Channel-specific target configuration. The shape depends on the `type` field: \- `email`: requires an `EmailTarget` object \- `webhook`: requires a `WebhookTarget` object

* Name
`event_types`
Type
string[]
Required
required
Enum

Description

List of activity event type codes this channel subscribes to.

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether this notification channel is active.

### Request

POST

/api/integrations/notifications/channels
```
curl -X POST https://api.netbird.io/api/integrations/notifications/channels \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"type": "email",
"target": {
"description": "Channel-specific target configuration. The shape depends on the `type` field:\n- `email`: requires an `EmailTarget` object\n- `webhook`: requires a `WebhookTarget` object\n",
"oneOf": [
{
"emails": [
"admin@example.com",
"ops@example.com"
]
},
{
"url": "https://hooks.example.com/netbird",
"headers": {
"Authorization": "Bearer token",
"X-Webhook-Secret": "secret"
}
}
]
},
"event_types": [
"user.join",
"peer.user.add",
"peer.login.expire"
],
"enabled": true
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"type": "email",
"target": {
"description": "Channel-specific target configuration. The shape depends on the `type` field:\n- `email`: an `EmailTarget` object\n- `webhook`: a `WebhookTarget` object\n",
"oneOf": [
{
"emails": [
"admin@example.com",
"ops@example.com"
]
},
{
"url": "https://hooks.example.com/netbird",
"headers": {
"Authorization": "Bearer token",
"X-Webhook-Secret": "secret"
}
}
]
},
"event_types": [
"user.join",
"peer.user.add",
"peer.login.expire"
],
"enabled": true
}

```

* * *

GET/api/integrations/notifications/channels/{channelId}

## [Get Notification Channel](https://docs.netbird.io/ipa/resources/notifications#get-notification-channel)

Retrieves a specific notification channel by its ID.

### Request

GET

/api/integrations/notifications/channels/{channelId}
```
curl -X GET https://api.netbird.io/api/integrations/notifications/channels/{channelId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"type": "email",
"target": {
"description": "Channel-specific target configuration. The shape depends on the `type` field:\n- `email`: an `EmailTarget` object\n- `webhook`: a `WebhookTarget` object\n",
"oneOf": [
{
"emails": [
"admin@example.com",
"ops@example.com"
]
},
{
"url": "https://hooks.example.com/netbird",
"headers": {
"Authorization": "Bearer token",
"X-Webhook-Secret": "secret"
}
}
]
},
"event_types": [
"user.join",
"peer.user.add",
"peer.login.expire"
],
"enabled": true
}

```

* * *

PUT/api/integrations/notifications/channels/{channelId}

## [Update Notification Channel](https://docs.netbird.io/ipa/resources/notifications#update-notification-channel)

Updates an existing notification channel.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/notifications#request-body-parameters-2)

* Name
`type`
Type
string
Required
required
Enum

Description

The type of notification channel.

* Name
`target`
Type

Required
optional
Enum

Description

Channel-specific target configuration. The shape depends on the `type` field: \- `email`: requires an `EmailTarget` object \- `webhook`: requires a `WebhookTarget` object

* Name
`event_types`
Type
string[]
Required
required
Enum

Description

List of activity event type codes this channel subscribes to.

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether this notification channel is active.

### Request

PUT

/api/integrations/notifications/channels/{channelId}
```
curl -X PUT https://api.netbird.io/api/integrations/notifications/channels/{channelId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"type": "email",
"target": {
"description": "Channel-specific target configuration. The shape depends on the `type` field:\n- `email`: requires an `EmailTarget` object\n- `webhook`: requires a `WebhookTarget` object\n",
"oneOf": [
{
"emails": [
"admin@example.com",
"ops@example.com"
]
},
{
"url": "https://hooks.example.com/netbird",
"headers": {
"Authorization": "Bearer token",
"X-Webhook-Secret": "secret"
}
}
]
},
"event_types": [
"user.join",
"peer.user.add",
"peer.login.expire"
],
"enabled": true
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"type": "email",
"target": {
"description": "Channel-specific target configuration. The shape depends on the `type` field:\n- `email`: an `EmailTarget` object\n- `webhook`: a `WebhookTarget` object\n",
"oneOf": [
{
"emails": [
"admin@example.com",
"ops@example.com"
]
},
{
"url": "https://hooks.example.com/netbird",
"headers": {
"Authorization": "Bearer token",
"X-Webhook-Secret": "secret"
}
}
]
},
"event_types": [
"user.join",
"peer.user.add",
"peer.login.expire"
],
"enabled": true
}

```

* * *

DELETE/api/integrations/notifications/channels/{channelId}

## [Delete Notification Channel](https://docs.netbird.io/ipa/resources/notifications#delete-notification-channel)

Deletes a notification channel by its ID.

### Request

DELETE

/api/integrations/notifications/channels/{channelId}
```
curl -X DELETE https://api.netbird.io/api/integrations/notifications/channels/{channelId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{}

```

* * *