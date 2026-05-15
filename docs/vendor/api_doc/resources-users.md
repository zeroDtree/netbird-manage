# Users

GET/api/users

## [List all Users](https://docs.netbird.io/ipa/resources/users#list-all-users)

Returns a list of all users

### [Query Parameters](https://docs.netbird.io/ipa/resources/users#query-parameters)

* Name
`service_user`
Type
boolean
Required
optional
Enum

Description

Filters users and returns either regular users or service users

### Request

GET

/api/users
```
curl -X GET https://api.netbird.io/api/users \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "google-oauth2|277474792786460067937",
"email": "demo@netbird.io",
"password": "super_secure_password",
"name": "Tom Schulz",
"role": "admin",
"status": "active",
"last_login": "2023-05-05T09:00:35.477782Z",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"is_current": true,
"is_service_user": false,
"is_blocked": false,
"pending_approval": false,
"issued": "api",
"idp_id": "okta-abc123",
"permissions": {
"is_restricted": {
"type": "boolean",
"description": "Indicates whether this User's Peers view is restricted"
},
"modules": {
"networks": {
"read": true,
"create": false,
"update": false,
"delete": false
},
"peers": {
"read": false,
"create": false,
"update": false,
"delete": false
}
}
}
}
]

```

* * *

POST/api/users

## [Create a User](https://docs.netbird.io/ipa/resources/users#create-a-user)

Creates a new service user or sends an invite to a regular user

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/users#request-body-parameters)

* Name
`email`
Type
string
Required
optional
Enum

Description

User's Email to send invite to

* Name
`name`
Type
string
Required
optional
Enum

Description

User's full name

* Name
`role`
Type
string
Required
required
Enum

Description

User's NetBird account role

* Name
`auto_groups`
Type
string[]
Required
required
Enum

Description

Group IDs to auto-assign to peers registered by this user

* Name
`is_service_user`
Type
boolean
Required
required
Enum

Description

Is true if this user is a service user

### Request

POST

/api/users
```
curl -X POST https://api.netbird.io/api/users \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"email": "demo@netbird.io",
"name": "Tom Schulz",
"role": "admin",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"is_service_user": false
}'

```

### Response
```
{
"id": "google-oauth2|277474792786460067937",
"email": "demo@netbird.io",
"password": "super_secure_password",
"name": "Tom Schulz",
"role": "admin",
"status": "active",
"last_login": "2023-05-05T09:00:35.477782Z",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"is_current": true,
"is_service_user": false,
"is_blocked": false,
"pending_approval": false,
"issued": "api",
"idp_id": "okta-abc123",
"permissions": {
"is_restricted": {
"type": "boolean",
"description": "Indicates whether this User's Peers view is restricted"
},
"modules": {
"networks": {
"read": true,
"create": false,
"update": false,
"delete": false
},
"peers": {
"read": false,
"create": false,
"update": false,
"delete": false
}
}
}
}

```

* * *

PUT/api/users/{userId}

## [Update a User](https://docs.netbird.io/ipa/resources/users#update-a-user)

Update information about a User

### [Path Parameters](https://docs.netbird.io/ipa/resources/users#path-parameters)

* Name
`userId`
Type
string
Required
required
Enum

Description

The unique identifier of a user

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/users#request-body-parameters-2)

* Name
`role`
Type
string
Required
required
Enum

Description

User's NetBird account role

* Name
`auto_groups`
Type
string[]
Required
required
Enum

Description

Group IDs to auto-assign to peers registered by this user

* Name
`is_blocked`
Type
boolean
Required
required
Enum

Description

If set to true then user is blocked and can't use the system

### Request

PUT

/api/users/{userId}
```
curl -X PUT https://api.netbird.io/api/users/{userId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"role": "admin",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"is_blocked": false
}'

```

### Response
```
{
"id": "google-oauth2|277474792786460067937",
"email": "demo@netbird.io",
"password": "super_secure_password",
"name": "Tom Schulz",
"role": "admin",
"status": "active",
"last_login": "2023-05-05T09:00:35.477782Z",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"is_current": true,
"is_service_user": false,
"is_blocked": false,
"pending_approval": false,
"issued": "api",
"idp_id": "okta-abc123",
"permissions": {
"is_restricted": {
"type": "boolean",
"description": "Indicates whether this User's Peers view is restricted"
},
"modules": {
"networks": {
"read": true,
"create": false,
"update": false,
"delete": false
},
"peers": {
"read": false,
"create": false,
"update": false,
"delete": false
}
}
}
}

```

* * *

DELETE/api/users/{userId}

## [Delete a User](https://docs.netbird.io/ipa/resources/users#delete-a-user)

This method removes a user from accessing the system. For this leaves the IDP user intact unless the `--user-delete-from-idp` is passed to management startup.

### [Path Parameters](https://docs.netbird.io/ipa/resources/users#path-parameters-2)

* Name
`userId`
Type
string
Required
required
Enum

Description

The unique identifier of a user

### Request

DELETE

/api/users/{userId}
```
curl -X DELETE https://api.netbird.io/api/users/{userId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

POST/api/users/{userId}/invite

## [Resend user invitation](https://docs.netbird.io/ipa/resources/users#resend-user-invitation)

Resend user invitation

### [Path Parameters](https://docs.netbird.io/ipa/resources/users#path-parameters-3)

* Name
`userId`
Type
string
Required
required
Enum

Description

The unique identifier of a user

### Request

POST

/api/users/{userId}/invite
```
curl -X POST https://api.netbird.io/api/users/{userId}/invite \
-H 'Authorization: Token <TOKEN>'

```

* * *

POST/api/users/{userId}/approve

## [Approve user](https://docs.netbird.io/ipa/resources/users#approve-user)

Approve a user that is pending approval

### [Path Parameters](https://docs.netbird.io/ipa/resources/users#path-parameters-4)

* Name
`userId`
Type
string
Required
required
Enum

Description

The unique identifier of a user

### Request

POST

/api/users/{userId}/approve
```
curl -X POST https://api.netbird.io/api/users/{userId}/approve \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "google-oauth2|277474792786460067937",
"email": "demo@netbird.io",
"password": "super_secure_password",
"name": "Tom Schulz",
"role": "admin",
"status": "active",
"last_login": "2023-05-05T09:00:35.477782Z",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"is_current": true,
"is_service_user": false,
"is_blocked": false,
"pending_approval": false,
"issued": "api",
"idp_id": "okta-abc123",
"permissions": {
"is_restricted": {
"type": "boolean",
"description": "Indicates whether this User's Peers view is restricted"
},
"modules": {
"networks": {
"read": true,
"create": false,
"update": false,
"delete": false
},
"peers": {
"read": false,
"create": false,
"update": false,
"delete": false
}
}
}
}

```

* * *

DELETE/api/users/{userId}/reject

## [Reject user](https://docs.netbird.io/ipa/resources/users#reject-user)

Reject a user that is pending approval by removing them from the account

### [Path Parameters](https://docs.netbird.io/ipa/resources/users#path-parameters-5)

* Name
`userId`
Type
string
Required
required
Enum

Description

The unique identifier of a user

### Request

DELETE

/api/users/{userId}/reject
```
curl -X DELETE https://api.netbird.io/api/users/{userId}/reject \
-H 'Authorization: Token <TOKEN>'

```

* * *

PUT/api/users/{userId}/password

## [Change user password](https://docs.netbird.io/ipa/resources/users#change-user-password)

Change the password for a user. Only available when embedded IdP is enabled. Users can only change their own password.

### [Path Parameters](https://docs.netbird.io/ipa/resources/users#path-parameters-6)

* Name
`userId`
Type
string
Required
required
Enum

Description

The unique identifier of a user

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/users#request-body-parameters-3)

* Name
`old_password`
Type
string
Required
required
Enum

Description

The current password

* Name
`new_password`
Type
string
Required
required
Enum

Description

The new password to set

### Request

PUT

/api/users/{userId}/password
```
curl -X PUT https://api.netbird.io/api/users/{userId}/password \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"old_password": "currentPassword123",
"new_password": "newSecurePassword456"
}'

```

* * *

GET/api/users/current

## [Retrieve current user](https://docs.netbird.io/ipa/resources/users#retrieve-current-user)

Get information about the current user

### Request

GET

/api/users/current
```
curl -X GET https://api.netbird.io/api/users/current \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "google-oauth2|277474792786460067937",
"email": "demo@netbird.io",
"password": "super_secure_password",
"name": "Tom Schulz",
"role": "admin",
"status": "active",
"last_login": "2023-05-05T09:00:35.477782Z",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"is_current": true,
"is_service_user": false,
"is_blocked": false,
"pending_approval": false,
"issued": "api",
"idp_id": "okta-abc123",
"permissions": {
"is_restricted": {
"type": "boolean",
"description": "Indicates whether this User's Peers view is restricted"
},
"modules": {
"networks": {
"read": true,
"create": false,
"update": false,
"delete": false
},
"peers": {
"read": false,
"create": false,
"update": false,
"delete": false
}
}
}
}

```

* * *

GET/api/users/invites

## [List user invites](https://docs.netbird.io/ipa/resources/users#list-user-invites)

Lists all pending invites for the account. Only available when embedded IdP is enabled.

### Request

GET

/api/users/invites
```
curl -X GET https://api.netbird.io/api/users/invites \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "d5p7eedra0h0lt6f59hg",
"email": "user@example.com",
"name": "John Doe",
"role": "user",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"expires_at": "2024-01-25T10:00:00Z",
"created_at": "2024-01-22T10:00:00Z",
"expired": false,
"invite_token": "nbi_Xk5Lz9mP2vQwRtYu1aN3bC4dE5fGh0ABC123"
}
]

```

* * *

POST/api/users/invites

## [Create a user invite](https://docs.netbird.io/ipa/resources/users#create-a-user-invite)

Creates an invite link for a new user. Only available when embedded IdP is enabled. The user is not created until they accept the invite.

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/users#request-body-parameters-4)

* Name
`email`
Type
string
Required
required
Enum

Description

User's email address

* Name
`name`
Type
string
Required
required
Enum

Description

User's full name

* Name
`role`
Type
string
Required
required
Enum

Description

User's NetBird account role

* Name
`auto_groups`
Type
string[]
Required
required
Enum

Description

Group IDs to auto-assign to peers registered by this user

* Name
`expires_in`
Type
integer
Required
optional
Enum

Description

Invite expiration time in seconds (default 72 hours)

### Request

POST

/api/users/invites
```
curl -X POST https://api.netbird.io/api/users/invites \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"email": "user@example.com",
"name": "John Doe",
"role": "user",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"expires_in": 259200
}'

```

### Response
```
{
"id": "d5p7eedra0h0lt6f59hg",
"email": "user@example.com",
"name": "John Doe",
"role": "user",
"auto_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"expires_at": "2024-01-25T10:00:00Z",
"created_at": "2024-01-22T10:00:00Z",
"expired": false,
"invite_token": "nbi_Xk5Lz9mP2vQwRtYu1aN3bC4dE5fGh0ABC123"
}

```

* * *

DELETE/api/users/invites/{inviteId}

## [Delete a user invite](https://docs.netbird.io/ipa/resources/users#delete-a-user-invite)

Deletes a pending invite. Only available when embedded IdP is enabled.

### [Path Parameters](https://docs.netbird.io/ipa/resources/users#path-parameters-7)

* Name
`inviteId`
Type
string
Required
required
Enum

Description

The ID of the invite to delete

### Request

DELETE

/api/users/invites/{inviteId}
```
curl -X DELETE https://api.netbird.io/api/users/invites/{inviteId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

POST/api/users/invites/{inviteId}/regenerate

## [Regenerate a user invite](https://docs.netbird.io/ipa/resources/users#regenerate-a-user-invite)

Regenerates an invite link for an existing invite. Invalidates the previous token and creates a new one.

### [Path Parameters](https://docs.netbird.io/ipa/resources/users#path-parameters-8)

* Name
`inviteId`
Type
string
Required
required
Enum

Description

The ID of the invite to regenerate

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/users#request-body-parameters-5)

* Name
`expires_in`
Type
integer
Required
optional
Enum

Description

Invite expiration time in seconds (default 72 hours)

### Request

POST

/api/users/invites/{inviteId}/regenerate
```
curl -X POST https://api.netbird.io/api/users/invites/{inviteId}/regenerate \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"expires_in": 259200
}'

```

### Response
```
{
"invite_token": "nbi_Xk5Lz9mP2vQwRtYu1aN3bC4dE5fGh0ABC123",
"invite_expires_at": "2024-01-28T10:00:00Z"
}

```

* * *

GET/api/users/invites/{token}

## [Get invite information](https://docs.netbird.io/ipa/resources/users#get-invite-information)

Retrieves public information about an invite. This endpoint is unauthenticated and protected by the token itself.

### [Path Parameters](https://docs.netbird.io/ipa/resources/users#path-parameters-9)

* Name
`token`
Type
string
Required
required
Enum

Description

The invite token

### Request

GET

/api/users/invites/{token}
```
curl -X GET https://api.netbird.io/api/users/invites/{token} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"email": "user@example.com",
"name": "John Doe",
"expires_at": "2024-01-25T10:00:00Z",
"valid": true,
"invited_by": "Admin User"
}

```

* * *

POST/api/users/invites/{token}/accept

## [Accept an invite](https://docs.netbird.io/ipa/resources/users#accept-an-invite)

Accepts an invite and creates the user with the provided password. This endpoint is unauthenticated and protected by the token itself.

### [Path Parameters](https://docs.netbird.io/ipa/resources/users#path-parameters-10)

* Name
`token`
Type
string
Required
required
Enum

Description

The invite token

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/users#request-body-parameters-6)

* Name
`password`
Type
string
Required
required
Enum

**Possible Values:**`>=8 characters`

Description

The password the user wants to set. Must be at least 8 characters long and contain at least one uppercase letter, one digit, and one special character (any character that is not a letter or digit, including spaces).

### Request

POST

/api/users/invites/{token}/accept
```
curl -X POST https://api.netbird.io/api/users/invites/{token}/accept \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"password": "SecurePass123!"
}'

```

### Response
```
{
"success": true
}

```

* * *