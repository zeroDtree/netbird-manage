# Events

GET/api/events/audit

## [List all Audit Events](https://docs.netbird.io/ipa/resources/events#list-all-audit-events)

Returns a list of all audit events

### Request

GET

/api/events/audit
```
curl -X GET https://api.netbird.io/api/events/audit \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": 10,
"timestamp": "2023-05-05T10:04:37.473542Z",
"activity": "Route created",
"activity_code": "route.add",
"initiator_id": "google-oauth2|123456789012345678901",
"initiator_name": "John Doe",
"initiator_email": "demo@netbird.io",
"target_id": "chad9d86lnnc59g18ou0",
"meta": {
"name": "my route",
"network_range": "10.64.0.0/24",
"peer_id": "chacbco6lnnbn6cg5s91"
}
}
]

```

* * *

GET/api/events/network-traffic

## [List all Traffic Events cloud-only experimental](https://docs.netbird.io/ipa/resources/events#list-all-traffic-events)

Returns a list of all network traffic events

### [Query Parameters](https://docs.netbird.io/ipa/resources/events#query-parameters)

* Name
`page`
Type
integer
Required
optional
Enum

Description

Page number

* Name
`page_size`
Type
integer
Required
optional
Enum

Description

Number of items per page

* Name
`user_id`
Type
string
Required
optional
Enum

Description

Filter by user ID

* Name
`reporter_id`
Type
string
Required
optional
Enum

Description

Filter by reporter ID

* Name
`protocol`
Type
integer
Required
optional
Enum

Description

Filter by protocol

* Name
`type`
Type
string
Required
optional
Enum

Description

Filter by event type

* Name
`connection_type`
Type
string
Required
optional
Enum

Description

Filter by connection type

* Name
`direction`
Type
string
Required
optional
Enum

Description

Filter by direction

* Name
`search`
Type
string
Required
optional
Enum

Description

Case-insensitive partial match on user email, source/destination names, and source/destination addresses

* Name
`start_date`
Type
string
Required
optional
Enum

Description

Start date for filtering events (ISO 8601 format, e.g., 2024-01-01T00:00:00Z).

* Name
`end_date`
Type
string
Required
optional
Enum

Description

End date for filtering events (ISO 8601 format, e.g., 2024-01-31T23:59:59Z).

### Request

GET

/api/events/network-traffic
```
curl -X GET https://api.netbird.io/api/events/network-traffic \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"data": [
{
"flow_id": "61092452-b17c-4b14-b7cf-a2158c549826",
"reporter_id": "ch8i4ug6lnn4g9hqv7m0",
"source": {
"id": "ch8i4ug6lnn4g9hqv7m0",
"type": "PEER",
"name": "My Peer",
"geo_location": {
"city_name": "Berlin",
"country_code": "DE"
},
"os": "Linux",
"address": "100.64.0.10:51820",
"dns_label": "*.mydomain.com"
},
"destination": {
"id": "ch8i4ug6lnn4g9hqv7m0",
"type": "PEER",
"name": "My Peer",
"geo_location": {
"city_name": "Berlin",
"country_code": "DE"
},
"os": "Linux",
"address": "100.64.0.10:51820",
"dns_label": "*.mydomain.com"
},
"user": {
"id": "google-oauth2|123456789012345678901",
"email": "alice@netbird.io",
"name": "Alice Smith"
},
"policy": {
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "All to All"
},
"icmp": {
"type": 8,
"code": 0
},
"protocol": 6,
"direction": "INGRESS",
"rx_bytes": 1234,
"rx_packets": 5,
"tx_bytes": 1234,
"tx_packets": 5,
"events": [
{
"type": "TYPE_START",
"timestamp": {}
}
]
}
],
"page": {
"type": "integer",
"description": "Current page number"
},
"page_size": {
"type": "integer",
"description": "Number of items per page"
},
"total_records": {
"type": "integer",
"description": "Total number of event records available"
},
"total_pages": {
"type": "integer",
"description": "Total number of pages available"
}
}

```

* * *

GET/api/events/proxy

## [List all Reverse Proxy Access Logs](https://docs.netbird.io/ipa/resources/events#list-all-reverse-proxy-access-logs)

Returns a paginated list of all reverse proxy access log entries

### [Query Parameters](https://docs.netbird.io/ipa/resources/events#query-parameters-2)

* Name
`page`
Type
integer
Required
optional
Enum

Description

Page number for pagination (1-indexed)

* Name
`page_size`
Type
integer
Required
optional
Enum

Description

Number of items per page (max 100)

* Name
`sort_by`
Type
string
Required
optional
Enum

Description

Field to sort by (url sorts by host then path)

* Name
`sort_order`
Type
string
Required
optional
Enum

Description

Sort order (ascending or descending)

* Name
`search`
Type
string
Required
optional
Enum

Description

General search across request ID, host, path, source IP, user email, and user name

* Name
`source_ip`
Type
string
Required
optional
Enum

Description

Filter by source IP address

* Name
`host`
Type
string
Required
optional
Enum

Description

Filter by host header

* Name
`path`
Type
string
Required
optional
Enum

Description

Filter by request path (supports partial matching)

* Name
`user_id`
Type
string
Required
optional
Enum

Description

Filter by authenticated user ID

* Name
`user_email`
Type
string
Required
optional
Enum

Description

Filter by user email (partial matching)

* Name
`user_name`
Type
string
Required
optional
Enum

Description

Filter by user name (partial matching)

* Name
`method`
Type
string
Required
optional
Enum

Description

Filter by HTTP method

* Name
`status`
Type
string
Required
optional
Enum

Description

Filter by status (success = 2xx/3xx, failed = 1xx/4xx/5xx)

* Name
`status_code`
Type
integer
Required
optional
Enum

Description

Filter by HTTP status code

* Name
`start_date`
Type
string
Required
optional
Enum

Description

Filter by timestamp >= start_date (RFC3339 format)

* Name
`end_date`
Type
string
Required
optional
Enum

Description

Filter by timestamp <= end_date (RFC3339 format)

### Request

GET

/api/events/proxy
```
curl -X GET https://api.netbird.io/api/events/proxy \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"data": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"service_id": "ch8i4ug6lnn4g9hqv7m0",
"timestamp": "2024-01-31T15:30:00Z",
"method": "GET",
"host": "example.com",
"path": "/api/users",
"duration_ms": 150,
"status_code": 200,
"source_ip": "192.168.1.100",
"reason": "Authentication failed",
"user_id": "user-123",
"auth_method_used": "oidc",
"country_code": "US",
"city_name": "San Francisco",
"subdivision_code": "CA",
"bytes_upload": 1024,
"bytes_download": 8192,
"protocol": "http",
"metadata": {
"type": "object",
"additionalProperties": {
"type": "string"
},
"description": "Extra context about the request (e.g. crowdsec_verdict)"
}
}
],
"page": 1,
"page_size": 50,
"total_records": 523,
"total_pages": 11
}

```

* * *