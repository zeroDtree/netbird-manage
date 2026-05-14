# EDR Peers

POST/api/peers/{peer-id}/edr/bypass

## [Bypass compliance for a non-compliant peer](https://docs.netbird.io/ipa/resources/edr-peers#bypass-compliance-for-a-non-compliant-peer)

Allows an admin to bypass EDR compliance checks for a specific peer. The peer will remain bypassed until the admin revokes it OR the device becomes naturally compliant in the EDR system.

### Request

POST

/api/peers/{peer-id}/edr/bypass
```
curl -X POST https://api.netbird.io/api/peers/{peer-id}/edr/bypass \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"peer_id": "chacbco6lnnbn6cg5s91"
}

```

* * *

DELETE/api/peers/{peer-id}/edr/bypass

## [Revoke compliance bypass for a peer](https://docs.netbird.io/ipa/resources/edr-peers#revoke-compliance-bypass-for-a-peer)

Removes the compliance bypass, subjecting the peer to normal EDR validation.

### Request

DELETE

/api/peers/{peer-id}/edr/bypass
```
curl -X DELETE https://api.netbird.io/api/peers/{peer-id}/edr/bypass \
-H 'Authorization: Token <TOKEN>'

```

* * *

GET/api/peers/edr/bypassed

## [List all bypassed peers](https://docs.netbird.io/ipa/resources/edr-peers#list-all-bypassed-peers)

Returns all peers that have compliance bypassed by an admin.

### Request

GET

/api/peers/edr/bypassed
```
curl -X GET https://api.netbird.io/api/peers/edr/bypassed \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"peer_id": "chacbco6lnnbn6cg5s91"
}
]

```

* * *