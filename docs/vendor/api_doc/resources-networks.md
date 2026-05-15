# Networks

GET/api/networks

## [List all Networks](https://docs.netbird.io/ipa/resources/networks#list-all-networks)

Returns a list of all networks

### Request

GET

/api/networks
```
curl -X GET https://api.netbird.io/api/networks \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "chacdk86lnnboviihd7g",
"routers": [
"ch8i4ug6lnn4g9hqv7m0"
],
"routing_peers_count": 2,
"resources": [
"ch8i4ug6lnn4g9hqv7m1"
],
"policies": [
"ch8i4ug6lnn4g9hqv7m2"
],
"name": "Remote Network 1",
"description": "A remote network that needs to be accessed"
}
]

```

* * *

POST/api/networks

## [Create a Network](https://docs.netbird.io/ipa/resources/networks#create-a-network)

Creates a Network

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/networks#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

Description

Network name

* Name
`description`
Type
string
Required
optional
Enum

Description

Network description

### Request

POST

/api/networks
```
curl -X POST https://api.netbird.io/api/networks \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Remote Network 1",
"description": "A remote network that needs to be accessed"
}'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"routers": [
"ch8i4ug6lnn4g9hqv7m0"
],
"routing_peers_count": 2,
"resources": [
"ch8i4ug6lnn4g9hqv7m1"
],
"policies": [
"ch8i4ug6lnn4g9hqv7m2"
],
"name": "Remote Network 1",
"description": "A remote network that needs to be accessed"
}

```

* * *

GET/api/networks/{networkId}

## [Retrieve a Network](https://docs.netbird.io/ipa/resources/networks#retrieve-a-network)

Get information about a Network

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

### Request

GET

/api/networks/{networkId}
```
curl -X GET https://api.netbird.io/api/networks/{networkId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"routers": [
"ch8i4ug6lnn4g9hqv7m0"
],
"routing_peers_count": 2,
"resources": [
"ch8i4ug6lnn4g9hqv7m1"
],
"policies": [
"ch8i4ug6lnn4g9hqv7m2"
],
"name": "Remote Network 1",
"description": "A remote network that needs to be accessed"
}

```

* * *

PUT/api/networks/{networkId}

## [Update a Network](https://docs.netbird.io/ipa/resources/networks#update-a-network)

Update/Replace a Network

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-2)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/networks#request-body-parameters-2)

* Name
`name`
Type
string
Required
required
Enum

Description

Network name

* Name
`description`
Type
string
Required
optional
Enum

Description

Network description

### Request

PUT

/api/networks/{networkId}
```
curl -X PUT https://api.netbird.io/api/networks/{networkId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Remote Network 1",
"description": "A remote network that needs to be accessed"
}'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"routers": [
"ch8i4ug6lnn4g9hqv7m0"
],
"routing_peers_count": 2,
"resources": [
"ch8i4ug6lnn4g9hqv7m1"
],
"policies": [
"ch8i4ug6lnn4g9hqv7m2"
],
"name": "Remote Network 1",
"description": "A remote network that needs to be accessed"
}

```

* * *

DELETE/api/networks/{networkId}

## [Delete a Network](https://docs.netbird.io/ipa/resources/networks#delete-a-network)

Delete a network

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-3)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

### Request

DELETE

/api/networks/{networkId}
```
curl -X DELETE https://api.netbird.io/api/networks/{networkId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

GET/api/networks/{networkId}/resources

## [List all Network Resources](https://docs.netbird.io/ipa/resources/networks#list-all-network-resources)

Returns a list of all resources in a network

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-4)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

### Request

GET

/api/networks/{networkId}/resources
```
curl -X GET https://api.netbird.io/api/networks/{networkId}/resources \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "chacdk86lnnboviihd7g",
"type": "host",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"name": "Remote Resource 1",
"description": "A remote resource inside network 1",
"address": "1.1.1.1",
"enabled": true
}
]

```

* * *

POST/api/networks/{networkId}/resources

## [Create a Network Resource](https://docs.netbird.io/ipa/resources/networks#create-a-network-resource)

Creates a Network Resource

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-5)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/networks#request-body-parameters-3)

* Name
`name`
Type
string
Required
required
Enum

Description

Network resource name

* Name
`description`
Type
string
Required
optional
Enum

Description

Network resource description

* Name
`address`
Type
string
Required
required
Enum

Description

Network resource address (either a direct host like 1.1.1.1 or 1.1.1.1/32, or a subnet like 192.168.178.0/24, or domains like example.com and *.example.com)

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Network resource status

* Name
`groups`
Type
string[]
Required
required
Enum

Description

Group IDs containing the resource

### Request

POST

/api/networks/{networkId}/resources
```
curl -X POST https://api.netbird.io/api/networks/{networkId}/resources \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Remote Resource 1",
"description": "A remote resource inside network 1",
"address": "1.1.1.1",
"enabled": true,
"groups": [
"chacdk86lnnboviihd70"
]
}'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"type": "host",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"name": "Remote Resource 1",
"description": "A remote resource inside network 1",
"address": "1.1.1.1",
"enabled": true
}

```

* * *

GET/api/networks/{networkId}/resources/{resourceId}

## [Retrieve a Network Resource](https://docs.netbird.io/ipa/resources/networks#retrieve-a-network-resource)

Get information about a Network Resource

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-6)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

* Name
`resourceId`
Type
string
Required
required
Enum

Description

The unique identifier of a network resource

### Request

GET

/api/networks/{networkId}/resources/{resourceId}
```
curl -X GET https://api.netbird.io/api/networks/{networkId}/resources/{resourceId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"type": "host",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"name": "Remote Resource 1",
"description": "A remote resource inside network 1",
"address": "1.1.1.1",
"enabled": true
}

```

* * *

PUT/api/networks/{networkId}/resources/{resourceId}

## [Update a Network Resource](https://docs.netbird.io/ipa/resources/networks#update-a-network-resource)

Update a Network Resource

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-7)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

* Name
`resourceId`
Type
string
Required
required
Enum

Description

The unique identifier of a resource

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/networks#request-body-parameters-4)

* Name
`name`
Type
string
Required
required
Enum

Description

Network resource name

* Name
`description`
Type
string
Required
optional
Enum

Description

Network resource description

* Name
`address`
Type
string
Required
required
Enum

Description

Network resource address (either a direct host like 1.1.1.1 or 1.1.1.1/32, or a subnet like 192.168.178.0/24, or domains like example.com and *.example.com)

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Network resource status

* Name
`groups`
Type
string[]
Required
required
Enum

Description

Group IDs containing the resource

### Request

PUT

/api/networks/{networkId}/resources/{resourceId}
```
curl -X PUT https://api.netbird.io/api/networks/{networkId}/resources/{resourceId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Remote Resource 1",
"description": "A remote resource inside network 1",
"address": "1.1.1.1",
"enabled": true,
"groups": [
"chacdk86lnnboviihd70"
]
}'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"type": "host",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"name": "Remote Resource 1",
"description": "A remote resource inside network 1",
"address": "1.1.1.1",
"enabled": true
}

```

* * *

DELETE/api/networks/{networkId}/resources/{resourceId}

## [Delete a Network Resource](https://docs.netbird.io/ipa/resources/networks#delete-a-network-resource)

Delete a network resource

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-8)

* Name
`networkId`
Type
string
Required
required
Enum

Description

* Name
`resourceId`
Type
string
Required
required
Enum

Description

### Request

DELETE

/api/networks/{networkId}/resources/{resourceId}
```
curl -X DELETE https://api.netbird.io/api/networks/{networkId}/resources/{resourceId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

GET/api/networks/{networkId}/routers

## [List all Network Routers](https://docs.netbird.io/ipa/resources/networks#list-all-network-routers)

Returns a list of all routers in a network

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-9)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

### Request

GET

/api/networks/{networkId}/routers
```
curl -X GET https://api.netbird.io/api/networks/{networkId}/routers \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "chacdk86lnnboviihd7g",
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"metric": 9999,
"masquerade": true,
"enabled": true
}
]

```

* * *

POST/api/networks/{networkId}/routers

## [Create a Network Router](https://docs.netbird.io/ipa/resources/networks#create-a-network-router)

Creates a Network Router

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-10)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/networks#request-body-parameters-5)

* Name
`peer`
Type
string
Required
optional
Enum

Description

Peer Identifier associated with route. This property can not be set together with `peer_groups`

* Name
`peer_groups`
Type
string[]
Required
optional
Enum

Description

Peers Group Identifier associated with route. This property can not be set together with `peer`

* Name
`metric`
Type
integer
Required
required
Enum

**Possible Values:**`>=1` and `<=9999`

Description

Route metric number. Lowest number has higher priority

* Name
`masquerade`
Type
boolean
Required
required
Enum

Description

Indicate if peer should masquerade traffic to this route's prefix

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Network router status

### Request

POST

/api/networks/{networkId}/routers
```
curl -X POST https://api.netbird.io/api/networks/{networkId}/routers \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"metric": 9999,
"masquerade": true,
"enabled": true
}'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"metric": 9999,
"masquerade": true,
"enabled": true
}

```

* * *

GET/api/networks/{networkId}/routers/{routerId}

## [Retrieve a Network Router](https://docs.netbird.io/ipa/resources/networks#retrieve-a-network-router)

Get information about a Network Router

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-11)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

* Name
`routerId`
Type
string
Required
required
Enum

Description

The unique identifier of a router

### Request

GET

/api/networks/{networkId}/routers/{routerId}
```
curl -X GET https://api.netbird.io/api/networks/{networkId}/routers/{routerId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"metric": 9999,
"masquerade": true,
"enabled": true
}

```

* * *

PUT/api/networks/{networkId}/routers/{routerId}

## [Update a Network Router](https://docs.netbird.io/ipa/resources/networks#update-a-network-router)

Update a Network Router

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-12)

* Name
`networkId`
Type
string
Required
required
Enum

Description

The unique identifier of a network

* Name
`routerId`
Type
string
Required
required
Enum

Description

The unique identifier of a router

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/networks#request-body-parameters-6)

* Name
`peer`
Type
string
Required
optional
Enum

Description

Peer Identifier associated with route. This property can not be set together with `peer_groups`

* Name
`peer_groups`
Type
string[]
Required
optional
Enum

Description

Peers Group Identifier associated with route. This property can not be set together with `peer`

* Name
`metric`
Type
integer
Required
required
Enum

**Possible Values:**`>=1` and `<=9999`

Description

Route metric number. Lowest number has higher priority

* Name
`masquerade`
Type
boolean
Required
required
Enum

Description

Indicate if peer should masquerade traffic to this route's prefix

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Network router status

### Request

PUT

/api/networks/{networkId}/routers/{routerId}
```
curl -X PUT https://api.netbird.io/api/networks/{networkId}/routers/{routerId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"metric": 9999,
"masquerade": true,
"enabled": true
}'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"metric": 9999,
"masquerade": true,
"enabled": true
}

```

* * *

DELETE/api/networks/{networkId}/routers/{routerId}

## [Delete a Network Router](https://docs.netbird.io/ipa/resources/networks#delete-a-network-router)

Delete a network router

### [Path Parameters](https://docs.netbird.io/ipa/resources/networks#path-parameters-13)

* Name
`networkId`
Type
string
Required
required
Enum

Description

* Name
`routerId`
Type
string
Required
required
Enum

Description

### Request

DELETE

/api/networks/{networkId}/routers/{routerId}
```
curl -X DELETE https://api.netbird.io/api/networks/{networkId}/routers/{routerId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

GET/api/networks/routers

## [List all Network Routers](https://docs.netbird.io/ipa/resources/networks#list-all-network-routers-2)

Returns a list of all routers in a network

### Request

GET

/api/networks/routers
```
curl -X GET https://api.netbird.io/api/networks/routers \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "chacdk86lnnboviihd7g",
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"metric": 9999,
"masquerade": true,
"enabled": true
}
]

```

* * *