# Setup Keys

GET/api/setup-keys

## [List all Setup Keys](https://docs.netbird.io/ipa/resources/setup-keys#list-all-setup-keys)

Returns a list of all Setup Keys

### Request

GET

/api/setup-keys
```
curl -X GET https://api.netbird.io/api/setup-keys \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": 2531583362,
"name": "Default key",
"expires": "2023-06-01T14:47:22.291057Z",
"type": "reusable",
"valid": true,
"revoked": false,
"used_times": 2,
"last_used": "2023-05-05T09:00:35.477782Z",
"state": "valid",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"updated_at": "2023-05-05T09:00:35.477782Z",
"usage_limit": 0,
"ephemeral": true,
"allow_extra_dns_labels": true,
"key": "A6160****"
}
]

```

* * *

POST/api/setup-keys

## [Create a Setup Key](https://docs.netbird.io/ipa/resources/setup-keys#create-a-setup-key)

Creates a setup key

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/setup-keys#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

Description

Setup Key name

* Name
`type`
Type
string
Required
required
Enum

Description

Setup key type, one-off for single time usage and reusable

* Name
`expires_in`
Type
integer
Required
required
Enum

**Possible Values:**`>=86400` and `<=31536000`

Description

Expiration time in seconds

* Name
`auto_groups`
Type
string[]
Required
required
Enum

Description

List of group IDs to auto-assign to peers registered with this key

* Name
`usage_limit`
Type
integer
Required
required
Enum

Description

A number of times this key can be used. The value of 0 indicates the unlimited usage.

* Name
`ephemeral`
Type
boolean
Required
optional
Enum

Description

Indicate that the peer will be ephemeral or not

* Name
`allow_extra_dns_labels`
Type
boolean
Required
optional
Enum

Description

Allow extra DNS labels to be added to the peer

### Request

POST

/api/setup-keys
```
curl -X POST https://api.netbird.io/api/setup-keys \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Default key",
"type": "reusable",
"expires_in": 86400,
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"usage_limit": 0,
"ephemeral": true,
"allow_extra_dns_labels": true
}'

```

### Response
```
{
"id": 2531583362,
"name": "Default key",
"expires": "2023-06-01T14:47:22.291057Z",
"type": "reusable",
"valid": true,
"revoked": false,
"used_times": 2,
"last_used": "2023-05-05T09:00:35.477782Z",
"state": "valid",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"updated_at": "2023-05-05T09:00:35.477782Z",
"usage_limit": 0,
"ephemeral": true,
"allow_extra_dns_labels": true,
"key": "A616097E-FCF0-48FA-9354-CA4A61142761"
}

```

* * *

GET/api/setup-keys/{keyId}

## [Retrieve a Setup Key](https://docs.netbird.io/ipa/resources/setup-keys#retrieve-a-setup-key)

Get information about a setup key

### [Path Parameters](https://docs.netbird.io/ipa/resources/setup-keys#path-parameters)

* Name
`keyId`
Type
string
Required
required
Enum

Description

The unique identifier of a setup key

### Request

GET

/api/setup-keys/{keyId}
```
curl -X GET https://api.netbird.io/api/setup-keys/{keyId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": 2531583362,
"name": "Default key",
"expires": "2023-06-01T14:47:22.291057Z",
"type": "reusable",
"valid": true,
"revoked": false,
"used_times": 2,
"last_used": "2023-05-05T09:00:35.477782Z",
"state": "valid",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"updated_at": "2023-05-05T09:00:35.477782Z",
"usage_limit": 0,
"ephemeral": true,
"allow_extra_dns_labels": true,
"key": "A6160****"
}

```

* * *

PUT/api/setup-keys/{keyId}

## [Update a Setup Key](https://docs.netbird.io/ipa/resources/setup-keys#update-a-setup-key)

Update information about a setup key

### [Path Parameters](https://docs.netbird.io/ipa/resources/setup-keys#path-parameters-2)

* Name
`keyId`
Type
string
Required
required
Enum

Description

The unique identifier of a setup key

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/setup-keys#request-body-parameters-2)

* Name
`revoked`
Type
boolean
Required
required
Enum

Description

Setup key revocation status

* Name
`auto_groups`
Type
string[]
Required
required
Enum

Description

List of group IDs to auto-assign to peers registered with this key

### Request

PUT

/api/setup-keys/{keyId}
```
curl -X PUT https://api.netbird.io/api/setup-keys/{keyId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"revoked": false,
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
]
}'

```

### Response
```
{
"id": 2531583362,
"name": "Default key",
"expires": "2023-06-01T14:47:22.291057Z",
"type": "reusable",
"valid": true,
"revoked": false,
"used_times": 2,
"last_used": "2023-05-05T09:00:35.477782Z",
"state": "valid",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"updated_at": "2023-05-05T09:00:35.477782Z",
"usage_limit": 0,
"ephemeral": true,
"allow_extra_dns_labels": true,
"key": "A6160****"
}

```

* * *

DELETE/api/setup-keys/{keyId}

## [Delete a Setup Key](https://docs.netbird.io/ipa/resources/setup-keys#delete-a-setup-key)

Delete a Setup Key

### [Path Parameters](https://docs.netbird.io/ipa/resources/setup-keys#path-parameters-3)

* Name
`keyId`
Type
string
Required
required
Enum

Description

The unique identifier of a setup key

### Request

DELETE

/api/setup-keys/{keyId}
```
curl -X DELETE https://api.netbird.io/api/setup-keys/{keyId} \
-H 'Authorization: Token <TOKEN>'

```

* * *