# Ingress Ports

GET/api/peers/{peerId}/ingress/ports

## [List all Port Allocations cloud-only](https://docs.netbird.io/ipa/resources/ingress-ports#list-all-port-allocations)

Returns a list of all ingress port allocations for a peer

### [Path Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#path-parameters)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

### [Query Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#query-parameters)

* Name
`name`
Type
string
Required
optional
Enum

Description

Filters ingress port allocations by name

### Request

GET

/api/peers/{peerId}/ingress/ports
```
curl -X GET https://api.netbird.io/api/peers/{peerId}/ingress/ports \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "Ingress Peer Allocation 1",
"ingress_peer_id": "x7p3kqf2rdd8j5zxw4n9",
"region": "germany",
"enabled": true,
"ingress_ip": "192.34.0.123",
"port_range_mappings": [
{
"translated_start": 80,
"translated_end": 320,
"ingress_start": 1080,
"ingress_end": 1320,
"protocol": "tcp"
}
]
}
]

```

* * *

POST/api/peers/{peerId}/ingress/ports

## [Create a Port Allocation cloud-only](https://docs.netbird.io/ipa/resources/ingress-ports#create-a-port-allocation)

Creates a new ingress port allocation for a peer

### [Path Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#path-parameters-2)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

Description

Name of the ingress port allocation

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Indicates if an ingress port allocation is enabled

* Name
`port_ranges`
Type
object[]
Required
optional
Enum

Description
List of port ranges that are forwarded by the ingress peer

* Name
`start`
Type
integer
Required
required
Enum

Description

The starting port of the range of forwarded ports

* Name
`end`
Type
integer
Required
required
Enum

Description

The ending port of the range of forwarded ports

* Name
`protocol`
Type
string
Required
required
Enum

Description

The protocol accepted by the port range

* Name
`direct_port`
Type
object
Required
optional
Enum

Description
More Information

* Name
`count`
Type
integer
Required
required
Enum

Description

The number of ports to be forwarded

* Name
`protocol`
Type
string
Required
required
Enum

Description

The protocol accepted by the port

### Request

POST

/api/peers/{peerId}/ingress/ports
```
curl -X POST https://api.netbird.io/api/peers/{peerId}/ingress/ports \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Ingress Port Allocation 1",
"enabled": true,
"port_ranges": [
{
"start": 80,
"end": 320,
"protocol": "tcp"
}
],
"direct_port": {
"count": 5,
"protocol": "udp"
}
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "Ingress Peer Allocation 1",
"ingress_peer_id": "x7p3kqf2rdd8j5zxw4n9",
"region": "germany",
"enabled": true,
"ingress_ip": "192.34.0.123",
"port_range_mappings": [
{
"translated_start": 80,
"translated_end": 320,
"ingress_start": 1080,
"ingress_end": 1320,
"protocol": "tcp"
}
]
}

```

* * *

GET/api/peers/{peerId}/ingress/ports/{allocationId}

## [Retrieve a Port Allocation cloud-only](https://docs.netbird.io/ipa/resources/ingress-ports#retrieve-a-port-allocation)

Get information about an ingress port allocation

### [Path Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#path-parameters-3)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

* Name
`allocationId`
Type
string
Required
required
Enum

Description

The unique identifier of an ingress port allocation

### Request

GET

/api/peers/{peerId}/ingress/ports/{allocationId}
```
curl -X GET https://api.netbird.io/api/peers/{peerId}/ingress/ports/{allocationId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "Ingress Peer Allocation 1",
"ingress_peer_id": "x7p3kqf2rdd8j5zxw4n9",
"region": "germany",
"enabled": true,
"ingress_ip": "192.34.0.123",
"port_range_mappings": [
{
"translated_start": 80,
"translated_end": 320,
"ingress_start": 1080,
"ingress_end": 1320,
"protocol": "tcp"
}
]
}

```

* * *

PUT/api/peers/{peerId}/ingress/ports/{allocationId}

## [Update a Port Allocation cloud-only](https://docs.netbird.io/ipa/resources/ingress-ports#update-a-port-allocation)

Update information about an ingress port allocation

### [Path Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#path-parameters-4)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

* Name
`allocationId`
Type
string
Required
required
Enum

Description

The unique identifier of an ingress port allocation

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#request-body-parameters-2)

* Name
`name`
Type
string
Required
required
Enum

Description

Name of the ingress port allocation

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Indicates if an ingress port allocation is enabled

* Name
`port_ranges`
Type
object[]
Required
optional
Enum

Description
List of port ranges that are forwarded by the ingress peer

* Name
`start`
Type
integer
Required
required
Enum

Description

The starting port of the range of forwarded ports

* Name
`end`
Type
integer
Required
required
Enum

Description

The ending port of the range of forwarded ports

* Name
`protocol`
Type
string
Required
required
Enum

Description

The protocol accepted by the port range

* Name
`direct_port`
Type
object
Required
optional
Enum

Description
More Information

* Name
`count`
Type
integer
Required
required
Enum

Description

The number of ports to be forwarded

* Name
`protocol`
Type
string
Required
required
Enum

Description

The protocol accepted by the port

### Request

PUT

/api/peers/{peerId}/ingress/ports/{allocationId}
```
curl -X PUT https://api.netbird.io/api/peers/{peerId}/ingress/ports/{allocationId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Ingress Port Allocation 1",
"enabled": true,
"port_ranges": [
{
"start": 80,
"end": 320,
"protocol": "tcp"
}
],
"direct_port": {
"count": 5,
"protocol": "udp"
}
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "Ingress Peer Allocation 1",
"ingress_peer_id": "x7p3kqf2rdd8j5zxw4n9",
"region": "germany",
"enabled": true,
"ingress_ip": "192.34.0.123",
"port_range_mappings": [
{
"translated_start": 80,
"translated_end": 320,
"ingress_start": 1080,
"ingress_end": 1320,
"protocol": "tcp"
}
]
}

```

* * *

DELETE/api/peers/{peerId}/ingress/ports/{allocationId}

## [Delete a Port Allocation cloud-only](https://docs.netbird.io/ipa/resources/ingress-ports#delete-a-port-allocation)

Delete an ingress port allocation

### [Path Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#path-parameters-5)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

* Name
`allocationId`
Type
string
Required
required
Enum

Description

The unique identifier of an ingress port allocation

### Request

DELETE

/api/peers/{peerId}/ingress/ports/{allocationId}
```
curl -X DELETE https://api.netbird.io/api/peers/{peerId}/ingress/ports/{allocationId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

GET/api/ingress/peers

## [List all Ingress Peers cloud-only](https://docs.netbird.io/ipa/resources/ingress-ports#list-all-ingress-peers)

Returns a list of all ingress peers

### Request

GET

/api/ingress/peers
```
curl -X GET https://api.netbird.io/api/ingress/peers \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"peer_id": "x7p3kqf2rdd8j5zxw4n9",
"ingress_ip": "192.34.0.123",
"available_ports": {
"tcp": 45765,
"udp": 50000
},
"enabled": true,
"connected": true,
"fallback": true,
"region": "germany"
}
]

```

* * *

POST/api/ingress/peers

## [Create a Ingress Peer cloud-only](https://docs.netbird.io/ipa/resources/ingress-ports#create-a-ingress-peer)

Creates a new ingress peer

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#request-body-parameters-3)

* Name
`peer_id`
Type
string
Required
required
Enum

Description

ID of the peer that is used as an ingress peer

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Defines if an ingress peer is enabled

* Name
`fallback`
Type
boolean
Required
required
Enum

Description

Defines if an ingress peer can be used as a fallback if no ingress peer can be found in the region of the forwarded peer

### Request

POST

/api/ingress/peers
```
curl -X POST https://api.netbird.io/api/ingress/peers \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"peer_id": "ch8i4ug6lnn4g9hqv7m0",
"enabled": true,
"fallback": true
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"peer_id": "x7p3kqf2rdd8j5zxw4n9",
"ingress_ip": "192.34.0.123",
"available_ports": {
"tcp": 45765,
"udp": 50000
},
"enabled": true,
"connected": true,
"fallback": true,
"region": "germany"
}

```

* * *

GET/api/ingress/peers/{ingressPeerId}

## [Retrieve a Ingress Peer cloud-only](https://docs.netbird.io/ipa/resources/ingress-ports#retrieve-a-ingress-peer)

Get information about an ingress peer

### [Path Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#path-parameters-6)

* Name
`ingressPeerId`
Type
string
Required
required
Enum

Description

The unique identifier of an ingress peer

### Request

GET

/api/ingress/peers/{ingressPeerId}
```
curl -X GET https://api.netbird.io/api/ingress/peers/{ingressPeerId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"peer_id": "x7p3kqf2rdd8j5zxw4n9",
"ingress_ip": "192.34.0.123",
"available_ports": {
"tcp": 45765,
"udp": 50000
},
"enabled": true,
"connected": true,
"fallback": true,
"region": "germany"
}

```

* * *

PUT/api/ingress/peers/{ingressPeerId}

## [Update a Ingress Peer cloud-only](https://docs.netbird.io/ipa/resources/ingress-ports#update-a-ingress-peer)

Update information about an ingress peer

### [Path Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#path-parameters-7)

* Name
`ingressPeerId`
Type
string
Required
required
Enum

Description

The unique identifier of an ingress peer

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#request-body-parameters-4)

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Defines if an ingress peer is enabled

* Name
`fallback`
Type
boolean
Required
required
Enum

Description

Defines if an ingress peer can be used as a fallback if no ingress peer can be found in the region of the forwarded peer

### Request

PUT

/api/ingress/peers/{ingressPeerId}
```
curl -X PUT https://api.netbird.io/api/ingress/peers/{ingressPeerId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"enabled": true,
"fallback": true
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"peer_id": "x7p3kqf2rdd8j5zxw4n9",
"ingress_ip": "192.34.0.123",
"available_ports": {
"tcp": 45765,
"udp": 50000
},
"enabled": true,
"connected": true,
"fallback": true,
"region": "germany"
}

```

* * *

DELETE/api/ingress/peers/{ingressPeerId}

## [Delete a Ingress Peer cloud-only](https://docs.netbird.io/ipa/resources/ingress-ports#delete-a-ingress-peer)

Delete an ingress peer

### [Path Parameters](https://docs.netbird.io/ipa/resources/ingress-ports#path-parameters-8)

* Name
`ingressPeerId`
Type
string
Required
required
Enum

Description

The unique identifier of an ingress peer

### Request

DELETE

/api/ingress/peers/{ingressPeerId}
```
curl -X DELETE https://api.netbird.io/api/ingress/peers/{ingressPeerId} \
-H 'Authorization: Token <TOKEN>'

```

* * *