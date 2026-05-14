# Tokens

GET/api/users/{userId}/tokens

## [List all Tokens](https://docs.netbird.io/ipa/resources/tokens#list-all-tokens)

Returns a list of all tokens for a user

### [Path Parameters](https://docs.netbird.io/ipa/resources/tokens#path-parameters)

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

GET

/api/users/{userId}/tokens
```
curl -X GET https://api.netbird.io/api/users/{userId}/tokens \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i54g6lnn4g9hqv7n0",
"name": "My first token",
"expiration_date": "2023-05-05T14:38:28.977616Z",
"created_by": "google-oauth2|277474792786460067937",
"created_at": "2023-05-02T14:48:20.465209Z",
"last_used": "2023-05-04T12:45:25.9723616Z"
}
]

```

* * *

POST/api/users/{userId}/tokens

## [Create a Token](https://docs.netbird.io/ipa/resources/tokens#create-a-token)

Create a new token for a user

### [Path Parameters](https://docs.netbird.io/ipa/resources/tokens#path-parameters-2)

* Name
`userId`
Type
string
Required
required
Enum

Description

The unique identifier of a user

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/tokens#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

Description

Name of the token

* Name
`expires_in`
Type
integer
Required
required
Enum

**Possible Values:**`>=1` and `<=365`

Description

Expiration in days

### Request

POST

/api/users/{userId}/tokens
```
curl -X POST https://api.netbird.io/api/users/{userId}/tokens \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "My first token",
"expires_in": 30
}'

```

### Response
```
{
"plain_token": {},
"personal_access_token": {
"id": "ch8i54g6lnn4g9hqv7n0",
"name": "My first token",
"expiration_date": "2023-05-05T14:38:28.977616Z",
"created_by": "google-oauth2|277474792786460067937",
"created_at": "2023-05-02T14:48:20.465209Z",
"last_used": "2023-05-04T12:45:25.9723616Z"
}
}

```

* * *

GET/api/users/{userId}/tokens/{tokenId}

## [Retrieve a Token](https://docs.netbird.io/ipa/resources/tokens#retrieve-a-token)

Returns a specific token for a user

### [Path Parameters](https://docs.netbird.io/ipa/resources/tokens#path-parameters-3)

* Name
`userId`
Type
string
Required
required
Enum

Description

The unique identifier of a user

* Name
`tokenId`
Type
string
Required
required
Enum

Description

The unique identifier of a token

### Request

GET

/api/users/{userId}/tokens/{tokenId}
```
curl -X GET https://api.netbird.io/api/users/{userId}/tokens/{tokenId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i54g6lnn4g9hqv7n0",
"name": "My first token",
"expiration_date": "2023-05-05T14:38:28.977616Z",
"created_by": "google-oauth2|277474792786460067937",
"created_at": "2023-05-02T14:48:20.465209Z",
"last_used": "2023-05-04T12:45:25.9723616Z"
}

```

* * *

DELETE/api/users/{userId}/tokens/{tokenId}

## [Delete a Token](https://docs.netbird.io/ipa/resources/tokens#delete-a-token)

Delete a token for a user

### [Path Parameters](https://docs.netbird.io/ipa/resources/tokens#path-parameters-4)

* Name
`userId`
Type
string
Required
required
Enum

Description

The unique identifier of a user

* Name
`tokenId`
Type
string
Required
required
Enum

Description

The unique identifier of a token

### Request

DELETE

/api/users/{userId}/tokens/{tokenId}
```
curl -X DELETE https://api.netbird.io/api/users/{userId}/tokens/{tokenId} \
-H 'Authorization: Token <TOKEN>'

```

* * *