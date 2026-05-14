# Peers

GET/api/peers

## [List all Peers](https://docs.netbird.io/ipa/resources/peers#list-all-peers)

Returns a list of all peers

### [Query Parameters](https://docs.netbird.io/ipa/resources/peers#query-parameters)

* Name
`name`
Type
string
Required
optional
Enum

Description

Filter peers by name

* Name
`ip`
Type
string
Required
optional
Enum

Description

Filter peers by IP address

### Request

GET

/api/peers
```
curl -X GET https://api.netbird.io/api/peers \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1",
"created_at": "2023-05-05T09:00:35.477782Z",
"ip": "10.64.0.1",
"connection_ip": "35.64.0.1",
"connected": true,
"last_seen": "2023-05-05T10:05:26.420578Z",
"os": "Darwin 13.2.1",
"kernel_version": "23.2.0",
"geoname_id": 2643743,
"version": "0.14.0",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"ssh_enabled": true,
"user_id": "google-oauth2|277474792786460067937",
"hostname": "stage-host-1",
"ui_version": "0.14.0",
"dns_label": "stage-host-1.netbird.cloud",
"login_expiration_enabled": false,
"login_expired": false,
"last_login": "2023-05-05T09:00:35.477782Z",
"inactivity_expiration_enabled": false,
"approval_required": true,
"disapproval_reason": {
"description": "(Cloud only) Reason why the peer requires approval",
"type": "string"
},
"country_code": "DE",
"city_name": "Berlin",
"serial_number": "C02XJ0J0JGH7",
"extra_dns_labels": [
"stage-host-1"
],
"ephemeral": false,
"local_flags": {
"rosenpass_enabled": true,
"rosenpass_permissive": false,
"server_ssh_allowed": true,
"disable_client_routes": false,
"disable_server_routes": false,
"disable_dns": false,
"disable_firewall": false,
"block_lan_access": false,
"block_inbound": false,
"lazy_connection_enabled": false
},
"accessible_peers_count": 5
}
]

```

* * *

GET/api/peers/{peerId}

## [Retrieve a Peer](https://docs.netbird.io/ipa/resources/peers#retrieve-a-peer)

Get information about a peer

### [Path Parameters](https://docs.netbird.io/ipa/resources/peers#path-parameters)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

### Request

GET

/api/peers/{peerId}
```
curl -X GET https://api.netbird.io/api/peers/{peerId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1",
"created_at": "2023-05-05T09:00:35.477782Z",
"ip": "10.64.0.1",
"connection_ip": "35.64.0.1",
"connected": true,
"last_seen": "2023-05-05T10:05:26.420578Z",
"os": "Darwin 13.2.1",
"kernel_version": "23.2.0",
"geoname_id": 2643743,
"version": "0.14.0",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"ssh_enabled": true,
"user_id": "google-oauth2|277474792786460067937",
"hostname": "stage-host-1",
"ui_version": "0.14.0",
"dns_label": "stage-host-1.netbird.cloud",
"login_expiration_enabled": false,
"login_expired": false,
"last_login": "2023-05-05T09:00:35.477782Z",
"inactivity_expiration_enabled": false,
"approval_required": true,
"disapproval_reason": {
"description": "(Cloud only) Reason why the peer requires approval",
"type": "string"
},
"country_code": "DE",
"city_name": "Berlin",
"serial_number": "C02XJ0J0JGH7",
"extra_dns_labels": [
"stage-host-1"
],
"ephemeral": false,
"local_flags": {
"rosenpass_enabled": true,
"rosenpass_permissive": false,
"server_ssh_allowed": true,
"disable_client_routes": false,
"disable_server_routes": false,
"disable_dns": false,
"disable_firewall": false,
"block_lan_access": false,
"block_inbound": false,
"lazy_connection_enabled": false
}
}

```

* * *

PUT/api/peers/{peerId}

## [Update a Peer](https://docs.netbird.io/ipa/resources/peers#update-a-peer)

Update information about a peer

### [Path Parameters](https://docs.netbird.io/ipa/resources/peers#path-parameters-2)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/peers#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

Description

* Name
`ssh_enabled`
Type
boolean
Required
required
Enum

Description

* Name
`login_expiration_enabled`
Type
boolean
Required
required
Enum

Description

* Name
`inactivity_expiration_enabled`
Type
boolean
Required
required
Enum

Description

* Name
`approval_required`
Type
boolean
Required
optional
Enum

Description

(Cloud only) Indicates whether peer needs approval

* Name
`ip`
Type
string
Required
optional
Enum

Description

Peer's IP address

### Request

PUT

/api/peers/{peerId}
```
curl -X PUT https://api.netbird.io/api/peers/{peerId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "stage-host-1",
"ssh_enabled": true,
"login_expiration_enabled": false,
"inactivity_expiration_enabled": false,
"approval_required": true,
"ip": "100.64.0.15"
}'

```

### Response
```
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1",
"created_at": "2023-05-05T09:00:35.477782Z",
"ip": "10.64.0.1",
"connection_ip": "35.64.0.1",
"connected": true,
"last_seen": "2023-05-05T10:05:26.420578Z",
"os": "Darwin 13.2.1",
"kernel_version": "23.2.0",
"geoname_id": 2643743,
"version": "0.14.0",
"groups": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "devs",
"peers_count": 2,
"resources_count": 5,
"issued": "api"
}
],
"ssh_enabled": true,
"user_id": "google-oauth2|277474792786460067937",
"hostname": "stage-host-1",
"ui_version": "0.14.0",
"dns_label": "stage-host-1.netbird.cloud",
"login_expiration_enabled": false,
"login_expired": false,
"last_login": "2023-05-05T09:00:35.477782Z",
"inactivity_expiration_enabled": false,
"approval_required": true,
"disapproval_reason": {
"description": "(Cloud only) Reason why the peer requires approval",
"type": "string"
},
"country_code": "DE",
"city_name": "Berlin",
"serial_number": "C02XJ0J0JGH7",
"extra_dns_labels": [
"stage-host-1"
],
"ephemeral": false,
"local_flags": {
"rosenpass_enabled": true,
"rosenpass_permissive": false,
"server_ssh_allowed": true,
"disable_client_routes": false,
"disable_server_routes": false,
"disable_dns": false,
"disable_firewall": false,
"block_lan_access": false,
"block_inbound": false,
"lazy_connection_enabled": false
}
}

```

* * *

DELETE/api/peers/{peerId}

## [Delete a Peer](https://docs.netbird.io/ipa/resources/peers#delete-a-peer)

Delete a peer

### [Path Parameters](https://docs.netbird.io/ipa/resources/peers#path-parameters-3)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

### Request

DELETE

/api/peers/{peerId}
```
curl -X DELETE https://api.netbird.io/api/peers/{peerId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

GET/api/peers/{peerId}/accessible-peers

## [List accessible Peers](https://docs.netbird.io/ipa/resources/peers#list-accessible-peers)

Returns a list of peers that the specified peer can connect to within the network.

### [Path Parameters](https://docs.netbird.io/ipa/resources/peers#path-parameters-4)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

### Request

GET

/api/peers/{peerId}/accessible-peers
```
curl -X GET https://api.netbird.io/api/peers/{peerId}/accessible-peers \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "chacbco6lnnbn6cg5s90",
"name": "stage-host-1",
"ip": "10.64.0.1",
"dns_label": "stage-host-1.netbird.cloud",
"user_id": "google-oauth2|277474792786460067937",
"os": "linux",
"country_code": "DE",
"city_name": "Berlin",
"geoname_id": 2643743,
"connected": true,
"last_seen": "2023-05-05T10:05:26.420578Z"
}
]

```

* * *

POST/api/peers/{peerId}/temporary-access

## [Create a Temporary Access Peer](https://docs.netbird.io/ipa/resources/peers#create-a-temporary-access-peer)

Creates a temporary access peer that can be used to access this peer and this peer only. The temporary access peer and its access policies will be automatically deleted after it disconnects.

### [Path Parameters](https://docs.netbird.io/ipa/resources/peers#path-parameters-5)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/peers#request-body-parameters-2)

* Name
`name`
Type
string
Required
required
Enum

Description

Peer's hostname

* Name
`wg_pub_key`
Type
string
Required
required
Enum

Description

Peer's WireGuard public key

* Name
`rules`
Type
string[]
Required
required
Enum

Description

List of temporary access rules

### Request

POST

/api/peers/{peerId}/temporary-access
```
curl -X POST https://api.netbird.io/api/peers/{peerId}/temporary-access \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "temp-host-1",
"wg_pub_key": "n0r3pL4c3h0ld3rK3y==",
"rules": [
"tcp/80"
]
}'

```

### Response
```
{
"name": "temp-host-1",
"id": "chacbco6lnnbn6cg5s90",
"rules": [
"tcp/80"
]
}

```

* * *