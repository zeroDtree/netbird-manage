# Policies

GET/api/policies

## [List all Policies](https://docs.netbird.io/ipa/resources/policies#list-all-policies)

Returns a list of all policies

### Request

GET

/api/policies
```
curl -X GET https://api.netbird.io/api/policies \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"name": "ch8i4ug6lnn4g9hqv7mg",
"description": "This is a default policy that allows connections between all the resources",
"enabled": true,
"id": "ch8i4ug6lnn4g9hqv7mg",
"source_posture_checks": [
"chacdk86lnnboviihd70"
],
"rules": [
{
"name": "Default",
"description": "This is a default rule that allows connections between all the resources",
"enabled": true,
"action": "accept",
"bidirectional": true,
"protocol": "tcp",
"ports": [
"80"
],
"port_ranges": [
{
"start": 80,
"end": 320
}
],
"authorized_groups": {
"description": "Map of user group ids to a list of local users",
"type": "object",
"additionalProperties": [
"group1"
]
},
"id": "ch8i4ug6lnn4g9hqv7mg",
"sources": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"sourceResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
},
"destinations": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"destinationResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
}
]
}
]

```

* * *

POST/api/policies

## [Create a Policy](https://docs.netbird.io/ipa/resources/policies#create-a-policy)

Creates a policy

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/policies#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

Description

Policy name identifier

* Name
`description`
Type
string
Required
optional
Enum

Description

Policy friendly description

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Policy status

* Name
`source_posture_checks`
Type
string[]
Required
optional
Enum

Description

Posture checks ID's applied to policy source groups

* Name
`rules`
Type
object[]
Required
required
Enum

Description
Policy rule object for policy UI editor

* Name
`name`
Type
string
Required
required
Enum

Description

Policy rule name identifier

* Name
`description`
Type
string
Required
optional
Enum

Description

Policy rule friendly description

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Policy rule status

* Name
`action`
Type
string
Required
required
Enum

Description

Policy rule accept or drops packets

* Name
`bidirectional`
Type
boolean
Required
required
Enum

Description

Define if the rule is applicable in both directions, sources, and destinations.

* Name
`protocol`
Type
string
Required
required
Enum

Description

Policy rule type of the traffic

* Name
`ports`
Type
string[]
Required
optional
Enum

Description

Policy rule affected ports

* Name
`port_ranges`
Type
object[]
Required
optional
Enum

Description
Policy rule affected ports ranges list

* Name
`start`
Type
integer
Required
required
Enum

Description

The starting port of the range

* Name
`end`
Type
integer
Required
required
Enum

Description

The ending port of the range

* Name
`authorized_groups`
Type
object
Required
optional
Enum

Description

Map of user group ids to a list of local users

* Name
`id`
Type
string
Required
optional
Enum

Description

Policy rule ID

* Name
`sources`
Type
string[]
Required
optional
Enum

Description

Policy rule source group IDs

* Name
`sourceResource`
Type
object
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

* Name
`destinations`
Type
string[]
Required
optional
Enum

Description

Policy rule destination group IDs

* Name
`destinationResource`
Type
object
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

/api/policies
```
curl -X POST https://api.netbird.io/api/policies \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "ch8i4ug6lnn4g9hqv7mg",
"description": "This is a default policy that allows connections between all the resources",
"enabled": true,
"source_posture_checks": [
"chacdk86lnnboviihd70"
],
"rules": [
{
"name": "Default",
"description": "This is a default rule that allows connections between all the resources",
"enabled": true,
"action": "accept",
"bidirectional": true,
"protocol": "tcp",
"ports": [
"80"
],
"port_ranges": [
{
"start": 80,
"end": 320
}
],
"authorized_groups": {
"description": "Map of user group ids to a list of local users",
"type": "object",
"additionalProperties": [
"group1"
]
},
"id": "ch8i4ug6lnn4g9hqv7mg",
"sources": [
"ch8i4ug6lnn4g9hqv797"
],
"sourceResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
},
"destinations": [
"ch8i4ug6lnn4g9h7v7m0"
],
"destinationResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
}
]
}'

```

### Response
```
{
"name": "ch8i4ug6lnn4g9hqv7mg",
"description": "This is a default policy that allows connections between all the resources",
"enabled": true,
"id": "ch8i4ug6lnn4g9hqv7mg",
"source_posture_checks": [
"chacdk86lnnboviihd70"
],
"rules": [
{
"name": "Default",
"description": "This is a default rule that allows connections between all the resources",
"enabled": true,
"action": "accept",
"bidirectional": true,
"protocol": "tcp",
"ports": [
"80"
],
"port_ranges": [
{
"start": 80,
"end": 320
}
],
"authorized_groups": {
"description": "Map of user group ids to a list of local users",
"type": "object",
"additionalProperties": [
"group1"
]
},
"id": "ch8i4ug6lnn4g9hqv7mg",
"sources": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"sourceResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
},
"destinations": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"destinationResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
}
]
}

```

* * *

GET/api/policies/{policyId}

## [Retrieve a Policy](https://docs.netbird.io/ipa/resources/policies#retrieve-a-policy)

Get information about a Policies

### [Path Parameters](https://docs.netbird.io/ipa/resources/policies#path-parameters)

* Name
`policyId`
Type
string
Required
required
Enum

Description

The unique identifier of a policy

### Request

GET

/api/policies/{policyId}
```
curl -X GET https://api.netbird.io/api/policies/{policyId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"name": "ch8i4ug6lnn4g9hqv7mg",
"description": "This is a default policy that allows connections between all the resources",
"enabled": true,
"id": "ch8i4ug6lnn4g9hqv7mg",
"source_posture_checks": [
"chacdk86lnnboviihd70"
],
"rules": [
{
"name": "Default",
"description": "This is a default rule that allows connections between all the resources",
"enabled": true,
"action": "accept",
"bidirectional": true,
"protocol": "tcp",
"ports": [
"80"
],
"port_ranges": [
{
"start": 80,
"end": 320
}
],
"authorized_groups": {
"description": "Map of user group ids to a list of local users",
"type": "object",
"additionalProperties": [
"group1"
]
},
"id": "ch8i4ug6lnn4g9hqv7mg",
"sources": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"sourceResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
},
"destinations": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"destinationResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
}
]
}

```

* * *

PUT/api/policies/{policyId}

## [Update a Policy](https://docs.netbird.io/ipa/resources/policies#update-a-policy)

Update/Replace a Policy

### [Path Parameters](https://docs.netbird.io/ipa/resources/policies#path-parameters-2)

* Name
`policyId`
Type
string
Required
required
Enum

Description

The unique identifier of a policy

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/policies#request-body-parameters-2)

* Name
`name`
Type
string
Required
required
Enum

Description

Policy name identifier

* Name
`description`
Type
string
Required
optional
Enum

Description

Policy friendly description

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Policy status

* Name
`source_posture_checks`
Type
string[]
Required
optional
Enum

Description

Posture checks ID's applied to policy source groups

* Name
`rules`
Type
object[]
Required
required
Enum

Description
Policy rule object for policy UI editor

* Name
`name`
Type
string
Required
required
Enum

Description

Policy rule name identifier

* Name
`description`
Type
string
Required
optional
Enum

Description

Policy rule friendly description

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Policy rule status

* Name
`action`
Type
string
Required
required
Enum

Description

Policy rule accept or drops packets

* Name
`bidirectional`
Type
boolean
Required
required
Enum

Description

Define if the rule is applicable in both directions, sources, and destinations.

* Name
`protocol`
Type
string
Required
required
Enum

Description

Policy rule type of the traffic

* Name
`ports`
Type
string[]
Required
optional
Enum

Description

Policy rule affected ports

* Name
`port_ranges`
Type
object[]
Required
optional
Enum

Description
Policy rule affected ports ranges list

* Name
`start`
Type
integer
Required
required
Enum

Description

The starting port of the range

* Name
`end`
Type
integer
Required
required
Enum

Description

The ending port of the range

* Name
`authorized_groups`
Type
object
Required
optional
Enum

Description

Map of user group ids to a list of local users

* Name
`id`
Type
string
Required
optional
Enum

Description

Policy rule ID

* Name
`sources`
Type
string[]
Required
optional
Enum

Description

Policy rule source group IDs

* Name
`sourceResource`
Type
object
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

* Name
`destinations`
Type
string[]
Required
optional
Enum

Description

Policy rule destination group IDs

* Name
`destinationResource`
Type
object
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

/api/policies/{policyId}
```
curl -X PUT https://api.netbird.io/api/policies/{policyId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "ch8i4ug6lnn4g9hqv7mg",
"description": "This is a default policy that allows connections between all the resources",
"enabled": true,
"source_posture_checks": [
"chacdk86lnnboviihd70"
],
"rules": [
{
"name": "Default",
"description": "This is a default rule that allows connections between all the resources",
"enabled": true,
"action": "accept",
"bidirectional": true,
"protocol": "tcp",
"ports": [
"80"
],
"port_ranges": [
{
"start": 80,
"end": 320
}
],
"authorized_groups": {
"description": "Map of user group ids to a list of local users",
"type": "object",
"additionalProperties": [
"group1"
]
},
"id": "ch8i4ug6lnn4g9hqv7mg",
"sources": [
"ch8i4ug6lnn4g9hqv797"
],
"sourceResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
},
"destinations": [
"ch8i4ug6lnn4g9h7v7m0"
],
"destinationResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
}
]
}'

```

### Response
```
{
"name": "ch8i4ug6lnn4g9hqv7mg",
"description": "This is a default policy that allows connections between all the resources",
"enabled": true,
"id": "ch8i4ug6lnn4g9hqv7mg",
"source_posture_checks": [
"chacdk86lnnboviihd70"
],
"rules": [
{
"name": "Default",
"description": "This is a default rule that allows connections between all the resources",
"enabled": true,
"action": "accept",
"bidirectional": true,
"protocol": "tcp",
"ports": [
"80"
],
"port_ranges": [
{
"start": 80,
"end": 320
}
],
"authorized_groups": {
"description": "Map of user group ids to a list of local users",
"type": "object",
"additionalProperties": [
"group1"
]
},
"id": "ch8i4ug6lnn4g9hqv7mg",
"sources": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"sourceResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
},
"destinations": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"destinationResource": {
"id": "chacdk86lnnboviihd7g",
"type": "host"
}
}
]
}

```

* * *

DELETE/api/policies/{policyId}

## [Delete a Policy](https://docs.netbird.io/ipa/resources/policies#delete-a-policy)

Delete a policy

### [Path Parameters](https://docs.netbird.io/ipa/resources/policies#path-parameters-3)

* Name
`policyId`
Type
string
Required
required
Enum

Description

The unique identifier of a policy

### Request

DELETE

/api/policies/{policyId}
```
curl -X DELETE https://api.netbird.io/api/policies/{policyId} \
-H 'Authorization: Token <TOKEN>'

```

* * *