# Identity Providers

GET/api/identity-providers

## [List all Identity Providers](https://docs.netbird.io/ipa/resources/identity-providers#list-all-identity-providers)

Returns a list of all identity providers configured for the account

### Request

GET

/api/identity-providers
```
curl -X GET https://api.netbird.io/api/identity-providers \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7l0",
"type": "oidc",
"name": "My OIDC Provider",
"issuer": "https://accounts.google.com",
"client_id": "123456789.apps.googleusercontent.com"
}
]

```

* * *

POST/api/identity-providers

## [Create an Identity Provider](https://docs.netbird.io/ipa/resources/identity-providers#create-an-identity-provider)

Creates a new identity provider configuration

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/identity-providers#request-body-parameters)

* Name
`type`
Type
string
Required
required
Enum

Description

Type of identity provider

* Name
`name`
Type
string
Required
required
Enum

Description

Human-readable name for the identity provider

* Name
`issuer`
Type
string
Required
required
Enum

Description

OIDC issuer URL

* Name
`client_id`
Type
string
Required
required
Enum

Description

OAuth2 client ID

* Name
`client_secret`
Type
string
Required
required
Enum

Description

OAuth2 client secret

### Request

POST

/api/identity-providers
```
curl -X POST https://api.netbird.io/api/identity-providers \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"type": "oidc",
"name": "My OIDC Provider",
"issuer": "https://accounts.google.com",
"client_id": "123456789.apps.googleusercontent.com",
"client_secret": "secret123"
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7l0",
"type": "oidc",
"name": "My OIDC Provider",
"issuer": "https://accounts.google.com",
"client_id": "123456789.apps.googleusercontent.com"
}

```

* * *

GET/api/identity-providers/{idpId}

## [Retrieve an Identity Provider](https://docs.netbird.io/ipa/resources/identity-providers#retrieve-an-identity-provider)

Get information about a specific identity provider

### [Path Parameters](https://docs.netbird.io/ipa/resources/identity-providers#path-parameters)

* Name
`idpId`
Type
string
Required
required
Enum

Description

The unique identifier of an identity provider

### Request

GET

/api/identity-providers/{idpId}
```
curl -X GET https://api.netbird.io/api/identity-providers/{idpId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7l0",
"type": "oidc",
"name": "My OIDC Provider",
"issuer": "https://accounts.google.com",
"client_id": "123456789.apps.googleusercontent.com"
}

```

* * *

PUT/api/identity-providers/{idpId}

## [Update an Identity Provider](https://docs.netbird.io/ipa/resources/identity-providers#update-an-identity-provider)

Update an existing identity provider configuration

### [Path Parameters](https://docs.netbird.io/ipa/resources/identity-providers#path-parameters-2)

* Name
`idpId`
Type
string
Required
required
Enum

Description

The unique identifier of an identity provider

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/identity-providers#request-body-parameters-2)

* Name
`type`
Type
string
Required
required
Enum

Description

Type of identity provider

* Name
`name`
Type
string
Required
required
Enum

Description

Human-readable name for the identity provider

* Name
`issuer`
Type
string
Required
required
Enum

Description

OIDC issuer URL

* Name
`client_id`
Type
string
Required
required
Enum

Description

OAuth2 client ID

* Name
`client_secret`
Type
string
Required
required
Enum

Description

OAuth2 client secret

### Request

PUT

/api/identity-providers/{idpId}
```
curl -X PUT https://api.netbird.io/api/identity-providers/{idpId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"type": "oidc",
"name": "My OIDC Provider",
"issuer": "https://accounts.google.com",
"client_id": "123456789.apps.googleusercontent.com",
"client_secret": "secret123"
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7l0",
"type": "oidc",
"name": "My OIDC Provider",
"issuer": "https://accounts.google.com",
"client_id": "123456789.apps.googleusercontent.com"
}

```

* * *

DELETE/api/identity-providers/{idpId}

## [Delete an Identity Provider](https://docs.netbird.io/ipa/resources/identity-providers#delete-an-identity-provider)

Delete an identity provider configuration

### [Path Parameters](https://docs.netbird.io/ipa/resources/identity-providers#path-parameters-3)

* Name
`idpId`
Type
string
Required
required
Enum

Description

The unique identifier of an identity provider

### Request

DELETE

/api/identity-providers/{idpId}
```
curl -X DELETE https://api.netbird.io/api/identity-providers/{idpId} \
-H 'Authorization: Token <TOKEN>'

```

* * *