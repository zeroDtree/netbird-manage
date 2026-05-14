# Routes

GET/api/routes

## [List all Routes](https://docs.netbird.io/ipa/resources/routes#list-all-routes)

Returns a list of all routes

### Request

GET

/api/routes
```
curl -X GET https://api.netbird.io/api/routes \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "chacdk86lnnboviihd7g",
"network_type": "IPv4",
"description": "My first route",
"network_id": "Route 1",
"enabled": true,
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"network": "10.64.0.0/24",
"domains": [
"example.com"
],
"metric": 9999,
"masquerade": true,
"groups": [
"chacdk86lnnboviihd70"
],
"keep_route": true,
"access_control_groups": [
"chacbco6lnnbn6cg5s91"
],
"skip_auto_apply": false
}
]

```

* * *

POST/api/routes

## [Create a Route](https://docs.netbird.io/ipa/resources/routes#create-a-route)

Creates a Route

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/routes#request-body-parameters)

* Name
`description`
Type
string
Required
required
Enum

Description

Route description

* Name
`network_id`
Type
string
Required
required
Enum

**Possible Values:**`>=1 characters` and `<=40 characters`

Description

Route network identifier, to group HA routes

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Route status

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
`network`
Type
string
Required
optional
Enum

Description

Network range in CIDR format, Conflicts with domains

* Name
`domains`
Type
string[]
Required
optional
Enum

Description

Domain list to be dynamically resolved. Max of 32 domains can be added per route configuration. Conflicts with network

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
`groups`
Type
string[]
Required
required
Enum

Description

Group IDs containing routing peers

* Name
`keep_route`
Type
boolean
Required
required
Enum

Description

Indicate if the route should be kept after a domain doesn't resolve that IP anymore

* Name
`access_control_groups`
Type
string[]
Required
optional
Enum

Description

Access control group identifier associated with route.

* Name
`skip_auto_apply`
Type
boolean
Required
optional
Enum

Description

Indicate if this exit node route (0.0.0.0/0) should skip auto-application for client routing

### Request

POST

/api/routes
```
curl -X POST https://api.netbird.io/api/routes \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"description": "My first route",
"network_id": "Route 1",
"enabled": true,
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"network": "10.64.0.0/24",
"domains": [
"example.com"
],
"metric": 9999,
"masquerade": true,
"groups": [
"chacdk86lnnboviihd70"
],
"keep_route": true,
"access_control_groups": [
"chacbco6lnnbn6cg5s91"
],
"skip_auto_apply": false
}'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"network_type": "IPv4",
"description": "My first route",
"network_id": "Route 1",
"enabled": true,
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"network": "10.64.0.0/24",
"domains": [
"example.com"
],
"metric": 9999,
"masquerade": true,
"groups": [
"chacdk86lnnboviihd70"
],
"keep_route": true,
"access_control_groups": [
"chacbco6lnnbn6cg5s91"
],
"skip_auto_apply": false
}

```

* * *

GET/api/routes/{routeId}

## [Retrieve a Route](https://docs.netbird.io/ipa/resources/routes#retrieve-a-route)

Get information about a Routes

### [Path Parameters](https://docs.netbird.io/ipa/resources/routes#path-parameters)

* Name
`routeId`
Type
string
Required
required
Enum

Description

The unique identifier of a route

### Request

GET

/api/routes/{routeId}
```
curl -X GET https://api.netbird.io/api/routes/{routeId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"network_type": "IPv4",
"description": "My first route",
"network_id": "Route 1",
"enabled": true,
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"network": "10.64.0.0/24",
"domains": [
"example.com"
],
"metric": 9999,
"masquerade": true,
"groups": [
"chacdk86lnnboviihd70"
],
"keep_route": true,
"access_control_groups": [
"chacbco6lnnbn6cg5s91"
],
"skip_auto_apply": false
}

```

* * *

PUT/api/routes/{routeId}

## [Update a Route](https://docs.netbird.io/ipa/resources/routes#update-a-route)

Update/Replace a Route

### [Path Parameters](https://docs.netbird.io/ipa/resources/routes#path-parameters-2)

* Name
`routeId`
Type
string
Required
required
Enum

Description

The unique identifier of a route

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/routes#request-body-parameters-2)

* Name
`description`
Type
string
Required
required
Enum

Description

Route description

* Name
`network_id`
Type
string
Required
required
Enum

**Possible Values:**`>=1 characters` and `<=40 characters`

Description

Route network identifier, to group HA routes

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Route status

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
`network`
Type
string
Required
optional
Enum

Description

Network range in CIDR format, Conflicts with domains

* Name
`domains`
Type
string[]
Required
optional
Enum

Description

Domain list to be dynamically resolved. Max of 32 domains can be added per route configuration. Conflicts with network

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
`groups`
Type
string[]
Required
required
Enum

Description

Group IDs containing routing peers

* Name
`keep_route`
Type
boolean
Required
required
Enum

Description

Indicate if the route should be kept after a domain doesn't resolve that IP anymore

* Name
`access_control_groups`
Type
string[]
Required
optional
Enum

Description

Access control group identifier associated with route.

* Name
`skip_auto_apply`
Type
boolean
Required
optional
Enum

Description

Indicate if this exit node route (0.0.0.0/0) should skip auto-application for client routing

### Request

PUT

/api/routes/{routeId}
```
curl -X PUT https://api.netbird.io/api/routes/{routeId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"description": "My first route",
"network_id": "Route 1",
"enabled": true,
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"network": "10.64.0.0/24",
"domains": [
"example.com"
],
"metric": 9999,
"masquerade": true,
"groups": [
"chacdk86lnnboviihd70"
],
"keep_route": true,
"access_control_groups": [
"chacbco6lnnbn6cg5s91"
],
"skip_auto_apply": false
}'

```

### Response
```
{
"id": "chacdk86lnnboviihd7g",
"network_type": "IPv4",
"description": "My first route",
"network_id": "Route 1",
"enabled": true,
"peer": "chacbco6lnnbn6cg5s91",
"peer_groups": [
"chacbco6lnnbn6cg5s91"
],
"network": "10.64.0.0/24",
"domains": [
"example.com"
],
"metric": 9999,
"masquerade": true,
"groups": [
"chacdk86lnnboviihd70"
],
"keep_route": true,
"access_control_groups": [
"chacbco6lnnbn6cg5s91"
],
"skip_auto_apply": false
}

```

* * *

DELETE/api/routes/{routeId}

## [Delete a Route](https://docs.netbird.io/ipa/resources/routes#delete-a-route)

Delete a route

### [Path Parameters](https://docs.netbird.io/ipa/resources/routes#path-parameters-3)

* Name
`routeId`
Type
string
Required
required
Enum

Description

The unique identifier of a route

### Request

DELETE

/api/routes/{routeId}
```
curl -X DELETE https://api.netbird.io/api/routes/{routeId} \
-H 'Authorization: Token <TOKEN>'

```

* * *