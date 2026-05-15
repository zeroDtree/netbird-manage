# Instance

GET/api/instance

## [Get Instance Status](https://docs.netbird.io/ipa/resources/instance#get-instance-status)

Returns the instance status including whether initial setup is required. This endpoint does not require authentication.

### Request

GET

/api/instance
```
curl -X GET https://api.netbird.io/api/instance \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"setup_required": true
}

```

* * *

GET/api/instance/version

## [Get Version Info](https://docs.netbird.io/ipa/resources/instance#get-version-info)

Returns version information for NetBird components including the current management server version and latest available versions from GitHub.

### Request

GET

/api/instance/version
```
curl -X GET https://api.netbird.io/api/instance/version \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"management_current_version": "0.35.0",
"dashboard_available_version": "2.10.0",
"management_available_version": "0.35.0",
"management_update_available": true
}

```

* * *

POST/api/setup

## [Setup Instance](https://docs.netbird.io/ipa/resources/instance#setup-instance)

Creates the initial admin user for the instance. This endpoint does not require authentication but only works when setup is required (no accounts exist and embedded IDP is enabled).

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/instance#request-body-parameters)

* Name
`email`
Type
string
Required
required
Enum

Description

Email address for the admin user

* Name
`password`
Type
string
Required
required
Enum

**Possible Values:**`>=8 characters`

Description

Password for the admin user (minimum 8 characters)

* Name
`name`
Type
string
Required
required
Enum

Description

Display name for the admin user (defaults to email if not provided)

### Request

POST

/api/setup
```
curl -X POST https://api.netbird.io/api/setup \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"email": "admin@example.com",
"password": "securepassword123",
"name": "Admin User"
}'

```

### Response
```
{
"user_id": "abc123def456",
"email": "admin@example.com"
}

```

* * *