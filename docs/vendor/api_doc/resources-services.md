# Services

GET/api/reverse-proxies/clusters

## [List available proxy clusters](https://docs.netbird.io/ipa/resources/services#list-available-proxy-clusters)

Returns a list of available proxy clusters with their connection status

### Request

GET

/api/reverse-proxies/clusters
```
curl -X GET https://api.netbird.io/api/reverse-proxies/clusters \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"address": "eu.proxy.netbird.io",
"connected_proxies": 3
}
]

```

* * *

GET/api/reverse-proxies/services

## [List all Services](https://docs.netbird.io/ipa/resources/services#list-all-services)

Returns a list of all reverse proxy services

### Request

GET

/api/reverse-proxies/services
```
curl -X GET https://api.netbird.io/api/reverse-proxies/services \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "cs8i4ug6lnn4g9hqv7mg",
"name": "myapp.example.netbird.app",
"domain": "myapp.example.netbird.app",
"mode": "http",
"listen_port": 8443,
"port_auto_assigned": false,
"proxy_cluster": "eu.proxy.netbird.io",
"targets": [
{
"target_id": "cs8i4ug6lnn4g9hqv7mg",
"target_type": "subnet",
"path": "/",
"protocol": "http",
"host": "10.10.0.1",
"port": 8080,
"enabled": true,
"options": {
"skip_tls_verify": false,
"request_timeout": "30s",
"path_rewrite": "preserve",
"custom_headers": {
"X-Custom-Header": "value"
},
"proxy_protocol": false,
"session_idle_timeout": "2m"
}
}
],
"enabled": true,
"terminated": false,
"pass_host_header": false,
"rewrite_redirects": false,
"auth": {
"password_auth": {
"enabled": true,
"password": "s3cret"
},
"pin_auth": {
"enabled": false,
"pin": "1234"
},
"bearer_auth": {
"enabled": true,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7mg"
]
},
"link_auth": {
"enabled": false
},
"header_auths": [
{
"enabled": true,
"header": "X-API-Key",
"value": "my-secret-api-key"
}
]
},
"access_restrictions": {
"allowed_cidrs": [
"192.168.1.0/24"
],
"blocked_cidrs": [
"10.0.0.0/8"
],
"allowed_countries": [
"US"
],
"blocked_countries": [
"DE"
],
"crowdsec_mode": {
"type": "string",
"enum": [
"off",
"enforce",
"observe"
],
"default": "off",
"description": "CrowdSec IP reputation mode. Only available when the proxy cluster supports CrowdSec."
}
},
"meta": {
"created_at": "2024-02-03T10:30:00Z",
"certificate_issued_at": "2024-02-03T10:35:00Z",
"status": "active"
}
}
]

```

* * *

POST/api/reverse-proxies/services

## [Create a Service](https://docs.netbird.io/ipa/resources/services#create-a-service)

Creates a new reverse proxy service

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/services#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

Description

Service name

* Name
`domain`
Type
string
Required
required
Enum

Description

Domain for the service

* Name
`mode`
Type
string
Required
optional
Enum

Description

Service mode. "http" for L7 reverse proxy, "tcp"/"udp"/"tls" for L4 passthrough.

* Name
`listen_port`
Type
integer
Required
optional
Enum
0

**Possible Values:**`<=65535`

0
Description

Port the proxy listens on (L4/TLS only). Set to 0 for auto-assignment.

* Name
`targets`
Type
object[]
Required
optional
Enum

Description
List of target backends for this service

* Name
`target_id`
Type
string
Required
required
Enum

Description

Target ID

* Name
`target_type`
Type
string
Required
required
Enum

Description

Target type

* Name
`path`
Type
string
Required
optional
Enum

Description

URL path prefix for this target (HTTP only)

* Name
`protocol`
Type
string
Required
required
Enum

Description

Protocol to use when connecting to the backend

* Name
`host`
Type
string
Required
optional
Enum

Description

Backend ip or domain for this target

* Name
`port`
Type
integer
Required
required
Enum

**Possible Values:**`>=1` and `<=65535`

Description

Backend port for this target

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether this target is enabled

* Name
`options`
Type
object
Required
optional
Enum

Description
More Information

* Name
`skip_tls_verify`
Type
boolean
Required
optional
Enum

Description

Skip TLS certificate verification for this backend

* Name
`request_timeout`
Type
string
Required
optional
Enum

Description

Per-target response timeout as a Go duration string (e.g. "30s", "2m")

* Name
`path_rewrite`
Type
string
Required
optional
Enum

Description

Controls how the request path is rewritten before forwarding to the backend. Default strips the matched prefix. "preserve" keeps the full original request path.

* Name
`custom_headers`
Type
object
Required
optional
Enum

Description

Extra headers sent to the backend. Hop-by-hop and proxy-managed headers (Host, Connection, Transfer-Encoding, etc.) are rejected.

* Name
`proxy_protocol`
Type
boolean
Required
optional
Enum

Description

Send PROXY Protocol v2 header to this backend (TCP/TLS only)

* Name
`session_idle_timeout`
Type
string
Required
optional
Enum

Description

Idle timeout before a UDP session is reaped, as a Go duration string (e.g. "30s", "2m").

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether the service is enabled

* Name
`pass_host_header`
Type
boolean
Required
optional
Enum

Description

When true, the original client Host header is passed through to the backend instead of being rewritten to the backend's address

* Name
`rewrite_redirects`
Type
boolean
Required
optional
Enum

Description

When true, Location headers in backend responses are rewritten to replace the backend address with the public-facing domain

* Name
`auth`
Type
object
Required
optional
Enum

Description
More Information

* Name
`password_auth`
Type
object
Required
optional
Enum

Description
More Information

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether password auth is enabled

* Name
`password`
Type
string
Required
required
Enum

Description

Auth password

* Name
`pin_auth`
Type
object
Required
optional
Enum

Description
More Information

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether PIN auth is enabled

* Name
`pin`
Type
string
Required
required
Enum

Description

PIN value

* Name
`bearer_auth`
Type
object
Required
optional
Enum

Description
More Information

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether bearer auth is enabled

* Name
`distribution_groups`
Type
string[]
Required
optional
Enum

Description

List of group IDs that can use bearer auth

* Name
`link_auth`
Type
object
Required
optional
Enum

Description
More Information

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether link auth is enabled

* Name
`header_auths`
Type
object[]
Required
optional
Enum

Description
More Information

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether header auth is enabled

* Name
`header`
Type
string
Required
required
Enum

Description

HTTP header name to check (e.g. "Authorization", "X-API-Key")

* Name
`value`
Type
string
Required
required
Enum

Description

Expected header value. For Basic auth use "Basic base64(user:pass)". For Bearer use "Bearer token". Cleared in responses.

* Name
`access_restrictions`
Type
object
Required
optional
Enum

Description
Connection-level access restrictions based on IP address or geography. Applies to both HTTP and L4 services.

* Name
`allowed_cidrs`
Type
string[]
Required
optional
Enum

Description

CIDR allowlist. If non-empty, only IPs matching these CIDRs are allowed.

* Name
`blocked_cidrs`
Type
string[]
Required
optional
Enum

Description

CIDR blocklist. Connections from these CIDRs are rejected. Evaluated after allowed_cidrs.

* Name
`allowed_countries`
Type
string[]
Required
optional
Enum

Description

ISO 3166-1 alpha-2 country codes to allow. If non-empty, only these countries are permitted.

* Name
`blocked_countries`
Type
string[]
Required
optional
Enum

Description

ISO 3166-1 alpha-2 country codes to block.

* Name
`crowdsec_mode`
Type
string
Required
optional
Enum

Description

CrowdSec IP reputation mode. Only available when the proxy cluster supports CrowdSec.

### Request

POST

/api/reverse-proxies/services
```
curl -X POST https://api.netbird.io/api/reverse-proxies/services \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "myapp.example.netbird.app",
"domain": "myapp.example.netbird.app",
"mode": "http",
"listen_port": 5432,
"targets": [
{
"target_id": "cs8i4ug6lnn4g9hqv7mg",
"target_type": "subnet",
"path": "/",
"protocol": "http",
"host": "10.10.0.1",
"port": 8080,
"enabled": true,
"options": {
"skip_tls_verify": false,
"request_timeout": "30s",
"path_rewrite": "preserve",
"custom_headers": {
"X-Custom-Header": "value"
},
"proxy_protocol": false,
"session_idle_timeout": "2m"
}
}
],
"enabled": true,
"pass_host_header": false,
"rewrite_redirects": false,
"auth": {
"password_auth": {
"enabled": true,
"password": "s3cret"
},
"pin_auth": {
"enabled": false,
"pin": "1234"
},
"bearer_auth": {
"enabled": true,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7mg"
]
},
"link_auth": {
"enabled": false
},
"header_auths": [
{
"enabled": true,
"header": "X-API-Key",
"value": "my-secret-api-key"
}
]
},
"access_restrictions": {
"allowed_cidrs": [
"192.168.1.0/24"
],
"blocked_cidrs": [
"10.0.0.0/8"
],
"allowed_countries": [
"US"
],
"blocked_countries": [
"DE"
],
"crowdsec_mode": {
"type": "string",
"enum": [
"off",
"enforce",
"observe"
],
"default": "off",
"description": "CrowdSec IP reputation mode. Only available when the proxy cluster supports CrowdSec."
}
}
}'

```

### Response
```
{
"id": "cs8i4ug6lnn4g9hqv7mg",
"name": "myapp.example.netbird.app",
"domain": "myapp.example.netbird.app",
"mode": "http",
"listen_port": 8443,
"port_auto_assigned": false,
"proxy_cluster": "eu.proxy.netbird.io",
"targets": [
{
"target_id": "cs8i4ug6lnn4g9hqv7mg",
"target_type": "subnet",
"path": "/",
"protocol": "http",
"host": "10.10.0.1",
"port": 8080,
"enabled": true,
"options": {
"skip_tls_verify": false,
"request_timeout": "30s",
"path_rewrite": "preserve",
"custom_headers": {
"X-Custom-Header": "value"
},
"proxy_protocol": false,
"session_idle_timeout": "2m"
}
}
],
"enabled": true,
"terminated": false,
"pass_host_header": false,
"rewrite_redirects": false,
"auth": {
"password_auth": {
"enabled": true,
"password": "s3cret"
},
"pin_auth": {
"enabled": false,
"pin": "1234"
},
"bearer_auth": {
"enabled": true,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7mg"
]
},
"link_auth": {
"enabled": false
},
"header_auths": [
{
"enabled": true,
"header": "X-API-Key",
"value": "my-secret-api-key"
}
]
},
"access_restrictions": {
"allowed_cidrs": [
"192.168.1.0/24"
],
"blocked_cidrs": [
"10.0.0.0/8"
],
"allowed_countries": [
"US"
],
"blocked_countries": [
"DE"
],
"crowdsec_mode": {
"type": "string",
"enum": [
"off",
"enforce",
"observe"
],
"default": "off",
"description": "CrowdSec IP reputation mode. Only available when the proxy cluster supports CrowdSec."
}
},
"meta": {
"created_at": "2024-02-03T10:30:00Z",
"certificate_issued_at": "2024-02-03T10:35:00Z",
"status": "active"
}
}

```

* * *

GET/api/reverse-proxies/services/{serviceId}

## [Retrieve a Service](https://docs.netbird.io/ipa/resources/services#retrieve-a-service)

Get information about a specific reverse proxy service

### [Path Parameters](https://docs.netbird.io/ipa/resources/services#path-parameters)

* Name
`serviceId`
Type
string
Required
required
Enum

Description

The unique identifier of a service

### Request

GET

/api/reverse-proxies/services/{serviceId}
```
curl -X GET https://api.netbird.io/api/reverse-proxies/services/{serviceId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "cs8i4ug6lnn4g9hqv7mg",
"name": "myapp.example.netbird.app",
"domain": "myapp.example.netbird.app",
"mode": "http",
"listen_port": 8443,
"port_auto_assigned": false,
"proxy_cluster": "eu.proxy.netbird.io",
"targets": [
{
"target_id": "cs8i4ug6lnn4g9hqv7mg",
"target_type": "subnet",
"path": "/",
"protocol": "http",
"host": "10.10.0.1",
"port": 8080,
"enabled": true,
"options": {
"skip_tls_verify": false,
"request_timeout": "30s",
"path_rewrite": "preserve",
"custom_headers": {
"X-Custom-Header": "value"
},
"proxy_protocol": false,
"session_idle_timeout": "2m"
}
}
],
"enabled": true,
"terminated": false,
"pass_host_header": false,
"rewrite_redirects": false,
"auth": {
"password_auth": {
"enabled": true,
"password": "s3cret"
},
"pin_auth": {
"enabled": false,
"pin": "1234"
},
"bearer_auth": {
"enabled": true,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7mg"
]
},
"link_auth": {
"enabled": false
},
"header_auths": [
{
"enabled": true,
"header": "X-API-Key",
"value": "my-secret-api-key"
}
]
},
"access_restrictions": {
"allowed_cidrs": [
"192.168.1.0/24"
],
"blocked_cidrs": [
"10.0.0.0/8"
],
"allowed_countries": [
"US"
],
"blocked_countries": [
"DE"
],
"crowdsec_mode": {
"type": "string",
"enum": [
"off",
"enforce",
"observe"
],
"default": "off",
"description": "CrowdSec IP reputation mode. Only available when the proxy cluster supports CrowdSec."
}
},
"meta": {
"created_at": "2024-02-03T10:30:00Z",
"certificate_issued_at": "2024-02-03T10:35:00Z",
"status": "active"
}
}

```

* * *

PUT/api/reverse-proxies/services/{serviceId}

## [Update a Service](https://docs.netbird.io/ipa/resources/services#update-a-service)

Update an existing service

### [Path Parameters](https://docs.netbird.io/ipa/resources/services#path-parameters-2)

* Name
`serviceId`
Type
string
Required
required
Enum

Description

The unique identifier of a service

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/services#request-body-parameters-2)

* Name
`name`
Type
string
Required
required
Enum

Description

Service name

* Name
`domain`
Type
string
Required
required
Enum

Description

Domain for the service

* Name
`mode`
Type
string
Required
optional
Enum

Description

Service mode. "http" for L7 reverse proxy, "tcp"/"udp"/"tls" for L4 passthrough.

* Name
`listen_port`
Type
integer
Required
optional
Enum
0

**Possible Values:**`<=65535`

0
Description

Port the proxy listens on (L4/TLS only). Set to 0 for auto-assignment.

* Name
`targets`
Type
object[]
Required
optional
Enum

Description
List of target backends for this service

* Name
`target_id`
Type
string
Required
required
Enum

Description

Target ID

* Name
`target_type`
Type
string
Required
required
Enum

Description

Target type

* Name
`path`
Type
string
Required
optional
Enum

Description

URL path prefix for this target (HTTP only)

* Name
`protocol`
Type
string
Required
required
Enum

Description

Protocol to use when connecting to the backend

* Name
`host`
Type
string
Required
optional
Enum

Description

Backend ip or domain for this target

* Name
`port`
Type
integer
Required
required
Enum

**Possible Values:**`>=1` and `<=65535`

Description

Backend port for this target

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether this target is enabled

* Name
`options`
Type
object
Required
optional
Enum

Description
More Information

* Name
`skip_tls_verify`
Type
boolean
Required
optional
Enum

Description

Skip TLS certificate verification for this backend

* Name
`request_timeout`
Type
string
Required
optional
Enum

Description

Per-target response timeout as a Go duration string (e.g. "30s", "2m")

* Name
`path_rewrite`
Type
string
Required
optional
Enum

Description

Controls how the request path is rewritten before forwarding to the backend. Default strips the matched prefix. "preserve" keeps the full original request path.

* Name
`custom_headers`
Type
object
Required
optional
Enum

Description

Extra headers sent to the backend. Hop-by-hop and proxy-managed headers (Host, Connection, Transfer-Encoding, etc.) are rejected.

* Name
`proxy_protocol`
Type
boolean
Required
optional
Enum

Description

Send PROXY Protocol v2 header to this backend (TCP/TLS only)

* Name
`session_idle_timeout`
Type
string
Required
optional
Enum

Description

Idle timeout before a UDP session is reaped, as a Go duration string (e.g. "30s", "2m").

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether the service is enabled

* Name
`pass_host_header`
Type
boolean
Required
optional
Enum

Description

When true, the original client Host header is passed through to the backend instead of being rewritten to the backend's address

* Name
`rewrite_redirects`
Type
boolean
Required
optional
Enum

Description

When true, Location headers in backend responses are rewritten to replace the backend address with the public-facing domain

* Name
`auth`
Type
object
Required
optional
Enum

Description
More Information

* Name
`password_auth`
Type
object
Required
optional
Enum

Description
More Information

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether password auth is enabled

* Name
`password`
Type
string
Required
required
Enum

Description

Auth password

* Name
`pin_auth`
Type
object
Required
optional
Enum

Description
More Information

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether PIN auth is enabled

* Name
`pin`
Type
string
Required
required
Enum

Description

PIN value

* Name
`bearer_auth`
Type
object
Required
optional
Enum

Description
More Information

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether bearer auth is enabled

* Name
`distribution_groups`
Type
string[]
Required
optional
Enum

Description

List of group IDs that can use bearer auth

* Name
`link_auth`
Type
object
Required
optional
Enum

Description
More Information

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether link auth is enabled

* Name
`header_auths`
Type
object[]
Required
optional
Enum

Description
More Information

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Whether header auth is enabled

* Name
`header`
Type
string
Required
required
Enum

Description

HTTP header name to check (e.g. "Authorization", "X-API-Key")

* Name
`value`
Type
string
Required
required
Enum

Description

Expected header value. For Basic auth use "Basic base64(user:pass)". For Bearer use "Bearer token". Cleared in responses.

* Name
`access_restrictions`
Type
object
Required
optional
Enum

Description
Connection-level access restrictions based on IP address or geography. Applies to both HTTP and L4 services.

* Name
`allowed_cidrs`
Type
string[]
Required
optional
Enum

Description

CIDR allowlist. If non-empty, only IPs matching these CIDRs are allowed.

* Name
`blocked_cidrs`
Type
string[]
Required
optional
Enum

Description

CIDR blocklist. Connections from these CIDRs are rejected. Evaluated after allowed_cidrs.

* Name
`allowed_countries`
Type
string[]
Required
optional
Enum

Description

ISO 3166-1 alpha-2 country codes to allow. If non-empty, only these countries are permitted.

* Name
`blocked_countries`
Type
string[]
Required
optional
Enum

Description

ISO 3166-1 alpha-2 country codes to block.

* Name
`crowdsec_mode`
Type
string
Required
optional
Enum

Description

CrowdSec IP reputation mode. Only available when the proxy cluster supports CrowdSec.

### Request

PUT

/api/reverse-proxies/services/{serviceId}
```
curl -X PUT https://api.netbird.io/api/reverse-proxies/services/{serviceId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "myapp.example.netbird.app",
"domain": "myapp.example.netbird.app",
"mode": "http",
"listen_port": 5432,
"targets": [
{
"target_id": "cs8i4ug6lnn4g9hqv7mg",
"target_type": "subnet",
"path": "/",
"protocol": "http",
"host": "10.10.0.1",
"port": 8080,
"enabled": true,
"options": {
"skip_tls_verify": false,
"request_timeout": "30s",
"path_rewrite": "preserve",
"custom_headers": {
"X-Custom-Header": "value"
},
"proxy_protocol": false,
"session_idle_timeout": "2m"
}
}
],
"enabled": true,
"pass_host_header": false,
"rewrite_redirects": false,
"auth": {
"password_auth": {
"enabled": true,
"password": "s3cret"
},
"pin_auth": {
"enabled": false,
"pin": "1234"
},
"bearer_auth": {
"enabled": true,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7mg"
]
},
"link_auth": {
"enabled": false
},
"header_auths": [
{
"enabled": true,
"header": "X-API-Key",
"value": "my-secret-api-key"
}
]
},
"access_restrictions": {
"allowed_cidrs": [
"192.168.1.0/24"
],
"blocked_cidrs": [
"10.0.0.0/8"
],
"allowed_countries": [
"US"
],
"blocked_countries": [
"DE"
],
"crowdsec_mode": {
"type": "string",
"enum": [
"off",
"enforce",
"observe"
],
"default": "off",
"description": "CrowdSec IP reputation mode. Only available when the proxy cluster supports CrowdSec."
}
}
}'

```

### Response
```
{
"id": "cs8i4ug6lnn4g9hqv7mg",
"name": "myapp.example.netbird.app",
"domain": "myapp.example.netbird.app",
"mode": "http",
"listen_port": 8443,
"port_auto_assigned": false,
"proxy_cluster": "eu.proxy.netbird.io",
"targets": [
{
"target_id": "cs8i4ug6lnn4g9hqv7mg",
"target_type": "subnet",
"path": "/",
"protocol": "http",
"host": "10.10.0.1",
"port": 8080,
"enabled": true,
"options": {
"skip_tls_verify": false,
"request_timeout": "30s",
"path_rewrite": "preserve",
"custom_headers": {
"X-Custom-Header": "value"
},
"proxy_protocol": false,
"session_idle_timeout": "2m"
}
}
],
"enabled": true,
"terminated": false,
"pass_host_header": false,
"rewrite_redirects": false,
"auth": {
"password_auth": {
"enabled": true,
"password": "s3cret"
},
"pin_auth": {
"enabled": false,
"pin": "1234"
},
"bearer_auth": {
"enabled": true,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7mg"
]
},
"link_auth": {
"enabled": false
},
"header_auths": [
{
"enabled": true,
"header": "X-API-Key",
"value": "my-secret-api-key"
}
]
},
"access_restrictions": {
"allowed_cidrs": [
"192.168.1.0/24"
],
"blocked_cidrs": [
"10.0.0.0/8"
],
"allowed_countries": [
"US"
],
"blocked_countries": [
"DE"
],
"crowdsec_mode": {
"type": "string",
"enum": [
"off",
"enforce",
"observe"
],
"default": "off",
"description": "CrowdSec IP reputation mode. Only available when the proxy cluster supports CrowdSec."
}
},
"meta": {
"created_at": "2024-02-03T10:30:00Z",
"certificate_issued_at": "2024-02-03T10:35:00Z",
"status": "active"
}
}

```

* * *

DELETE/api/reverse-proxies/services/{serviceId}

## [Delete a Service](https://docs.netbird.io/ipa/resources/services#delete-a-service)

Delete an existing service

### [Path Parameters](https://docs.netbird.io/ipa/resources/services#path-parameters-3)

* Name
`serviceId`
Type
string
Required
required
Enum

Description

The unique identifier of a service

### Request

DELETE

/api/reverse-proxies/services/{serviceId}
```
curl -X DELETE https://api.netbird.io/api/reverse-proxies/services/{serviceId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

GET/api/reverse-proxies/domains

## [Retrieve Service Domains](https://docs.netbird.io/ipa/resources/services#retrieve-service-domains)

Get information about domains that can be used for service endpoints.

### Request

GET

/api/reverse-proxies/domains
```
curl -X GET https://api.netbird.io/api/reverse-proxies/domains \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ds8i4ug6lnn4g9hqv7mg",
"domain": "example.netbird.app",
"validated": true,
"type": "free",
"target_cluster": "eu.proxy.netbird.io",
"supports_custom_ports": true,
"require_subdomain": false,
"supports_crowdsec": false
}
]

```

* * *

POST/api/reverse-proxies/domains

## [Create a Custom domain](https://docs.netbird.io/ipa/resources/services#create-a-custom-domain)

Create a new Custom domain for use with service endpoints, this will trigger an initial validation check

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/services#request-body-parameters-3)

* Name
`domain`
Type
string
Required
required
Enum

Description

Domain name

* Name
`target_cluster`
Type
string
Required
required
Enum

Description

The proxy cluster this domain should be validated against

### Request

POST

/api/reverse-proxies/domains
```
curl -X POST https://api.netbird.io/api/reverse-proxies/domains \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"domain": "myapp.example.com",
"target_cluster": "eu.proxy.netbird.io"
}'

```

### Response
```
{
"id": "cs8i4ug6lnn4g9hqv7mg",
"name": "myapp.example.netbird.app",
"domain": "myapp.example.netbird.app",
"mode": "http",
"listen_port": 8443,
"port_auto_assigned": false,
"proxy_cluster": "eu.proxy.netbird.io",
"targets": [
{
"target_id": "cs8i4ug6lnn4g9hqv7mg",
"target_type": "subnet",
"path": "/",
"protocol": "http",
"host": "10.10.0.1",
"port": 8080,
"enabled": true,
"options": {
"skip_tls_verify": false,
"request_timeout": "30s",
"path_rewrite": "preserve",
"custom_headers": {
"X-Custom-Header": "value"
},
"proxy_protocol": false,
"session_idle_timeout": "2m"
}
}
],
"enabled": true,
"terminated": false,
"pass_host_header": false,
"rewrite_redirects": false,
"auth": {
"password_auth": {
"enabled": true,
"password": "s3cret"
},
"pin_auth": {
"enabled": false,
"pin": "1234"
},
"bearer_auth": {
"enabled": true,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7mg"
]
},
"link_auth": {
"enabled": false
},
"header_auths": [
{
"enabled": true,
"header": "X-API-Key",
"value": "my-secret-api-key"
}
]
},
"access_restrictions": {
"allowed_cidrs": [
"192.168.1.0/24"
],
"blocked_cidrs": [
"10.0.0.0/8"
],
"allowed_countries": [
"US"
],
"blocked_countries": [
"DE"
],
"crowdsec_mode": {
"type": "string",
"enum": [
"off",
"enforce",
"observe"
],
"default": "off",
"description": "CrowdSec IP reputation mode. Only available when the proxy cluster supports CrowdSec."
}
},
"meta": {
"created_at": "2024-02-03T10:30:00Z",
"certificate_issued_at": "2024-02-03T10:35:00Z",
"status": "active"
}
}

```

* * *

DELETE/api/reverse-proxies/domains/{domainId}

## [Delete a Custom domain](https://docs.netbird.io/ipa/resources/services#delete-a-custom-domain)

Delete an existing service custom domain

### [Path Parameters](https://docs.netbird.io/ipa/resources/services#path-parameters-4)

* Name
`domainId`
Type
string
Required
required
Enum

Description

The custom domain ID

### Request

DELETE

/api/reverse-proxies/domains/{domainId}
```
curl -X DELETE https://api.netbird.io/api/reverse-proxies/domains/{domainId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

GET/api/reverse-proxies/domains/{domainId}/validate

## [Validate a custom domain](https://docs.netbird.io/ipa/resources/services#validate-a-custom-domain)

Trigger domain ownership validation for a custom domain

### [Path Parameters](https://docs.netbird.io/ipa/resources/services#path-parameters-5)

* Name
`domainId`
Type
string
Required
required
Enum

Description

The custom domain ID

### Request

GET

/api/reverse-proxies/domains/{domainId}/validate
```
curl -X GET https://api.netbird.io/api/reverse-proxies/domains/{domainId}/validate \
-H 'Authorization: Token <TOKEN>'

```

* * *