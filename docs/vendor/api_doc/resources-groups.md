# Groups

GET/api/groups

## [List all Groups](https://docs.netbird.io/ipa/resources/groups#list-all-groups)

Returns a list of all groups

### [Query Parameters](https://docs.netbird.io/ipa/resources/groups#query-parameters)

* Name
`name`
Type
string
Required
optional
Enum

Description

Filter groups by name (exact match)

### Request

GET

/api/groups
```
curl -X GET https://api.netbird.io/api/groups \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api",
"peers": [
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1"
}
],
"resources": [
{
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
]
}
]

```

* * *

POST/api/groups

## [Create a Group](https://docs.netbird.io/ipa/resources/groups#create-a-group)

Creates a group

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/groups#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

Description

Group name identifier

* Name
`peers`
Type
string[]
Required
optional
Enum

Description

List of peers ids

* Name
`resources`
Type
object[]
Required
optional
Enum

Description
More Information

* Name
`id`
Type
string
Required
required
Enum

Description

ID of the resource

* Name
`type`
Type
string
Required
required
Enum

Description

Network resource type based of the address

### Request

POST

/api/groups
```
curl -X POST https://api.netbird.io/api/groups \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "devs",
"peers": [
"ch8i4ug6lnn4g9hqv7m1"
],
"resources": [
{
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
]
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api",
"peers": [
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1"
}
],
"resources": [
{
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
]
}

```

* * *

GET/api/groups/{groupId}

## [Retrieve a Group](https://docs.netbird.io/ipa/resources/groups#retrieve-a-group)

Get information about a group

### [Path Parameters](https://docs.netbird.io/ipa/resources/groups#path-parameters)

* Name
`groupId`
Type
string
Required
required
Enum

Description

The unique identifier of a group

### Request

GET

/api/groups/{groupId}
```
curl -X GET https://api.netbird.io/api/groups/{groupId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api",
"peers": [
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1"
}
],
"resources": [
{
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
]
}

```

* * *

PUT/api/groups/{groupId}

## [Update a Group](https://docs.netbird.io/ipa/resources/groups#update-a-group)

Update/Replace a group

### [Path Parameters](https://docs.netbird.io/ipa/resources/groups#path-parameters-2)

* Name
`groupId`
Type
string
Required
required
Enum

Description

The unique identifier of a group

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/groups#request-body-parameters-2)

* Name
`name`
Type
string
Required
required
Enum

Description

Group name identifier

* Name
`peers`
Type
string[]
Required
optional
Enum

Description

List of peers ids

* Name
`resources`
Type
object[]
Required
optional
Enum

Description
More Information

* Name
`id`
Type
string
Required
required
Enum

Description

ID of the resource

* Name
`type`
Type
string
Required
required
Enum

Description

Network resource type based of the address

### Request

PUT

/api/groups/{groupId}
```
curl -X PUT https://api.netbird.io/api/groups/{groupId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "devs",
"peers": [
"ch8i4ug6lnn4g9hqv7m1"
],
"resources": [
{
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
]
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api",
"peers": [
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1"
}
],
"resources": [
{
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
]
}

```

* * *

DELETE/api/groups/{groupId}

## [Delete a Group](https://docs.netbird.io/ipa/resources/groups#delete-a-group)

Delete a group

### [Path Parameters](https://docs.netbird.io/ipa/resources/groups#path-parameters-3)

* Name
`groupId`
Type
string
Required
required
Enum

Description

The unique identifier of a group

### Request

DELETE

/api/groups/{groupId}
```
curl -X DELETE https://api.netbird.io/api/groups/{groupId} \
-H 'Authorization: Token <TOKEN>'

```

* * *