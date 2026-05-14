# DNS Zones

GET/api/dns/zones

## [List all DNS Zones](https://docs.netbird.io/ipa/resources/dns-zones#list-all-dns-zones)

Returns a list of all custom DNS zones

### Request

GET

/api/dns/zones
```
curl -X GET https://api.netbird.io/api/dns/zones \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"records": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "www.example.com",
"type": "A",
"content": "192.168.1.1",
"ttl": 300
}
],
"name": "Office Zone",
"domain": "example.com",
"enabled": {
"description": "Zone status",
"type": "boolean",
"default": true
},
"enable_search_domain": false,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7m0"
]
}
]

```

* * *

POST/api/dns/zones

## [Create a DNS Zone](https://docs.netbird.io/ipa/resources/dns-zones#create-a-dns-zone)

Creates a new custom DNS zone

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/dns-zones#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

**Possible Values:**`>=1 characters` and `<=255 characters`

Description

Zone name identifier

* Name
`domain`
Type
string
Required
required
Enum

Description

Zone domain (FQDN)

* Name
`enabled`
Type
boolean
Required
optional
Enum

Description

Zone status

* Name
`enable_search_domain`
Type
boolean
Required
required
Enum

Description

Enable this zone as a search domain

* Name
`distribution_groups`
Type
string[]
Required
required
Enum

Description

Group IDs that defines groups of peers that will resolve this zone

### Request

POST

/api/dns/zones
```
curl -X POST https://api.netbird.io/api/dns/zones \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Office Zone",
"domain": "example.com",
"enabled": {
"description": "Zone status",
"type": "boolean",
"default": true
},
"enable_search_domain": false,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7m0"
]
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"records": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "www.example.com",
"type": "A",
"content": "192.168.1.1",
"ttl": 300
}
],
"name": "Office Zone",
"domain": "example.com",
"enabled": {
"description": "Zone status",
"type": "boolean",
"default": true
},
"enable_search_domain": false,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7m0"
]
}

```

* * *

GET/api/dns/zones/{zoneId}

## [Retrieve a DNS Zone](https://docs.netbird.io/ipa/resources/dns-zones#retrieve-a-dns-zone)

Returns information about a specific DNS zone

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns-zones#path-parameters)

* Name
`zoneId`
Type
string
Required
required
Enum

Description

The unique identifier of a zone

### Request

GET

/api/dns/zones/{zoneId}
```
curl -X GET https://api.netbird.io/api/dns/zones/{zoneId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"records": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "www.example.com",
"type": "A",
"content": "192.168.1.1",
"ttl": 300
}
],
"name": "Office Zone",
"domain": "example.com",
"enabled": {
"description": "Zone status",
"type": "boolean",
"default": true
},
"enable_search_domain": false,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7m0"
]
}

```

* * *

PUT/api/dns/zones/{zoneId}

## [Update a DNS Zone](https://docs.netbird.io/ipa/resources/dns-zones#update-a-dns-zone)

Updates a custom DNS zone

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns-zones#path-parameters-2)

* Name
`zoneId`
Type
string
Required
required
Enum

Description

The unique identifier of a zone

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/dns-zones#request-body-parameters-2)

* Name
`name`
Type
string
Required
required
Enum

**Possible Values:**`>=1 characters` and `<=255 characters`

Description

Zone name identifier

* Name
`domain`
Type
string
Required
required
Enum

Description

Zone domain (FQDN)

* Name
`enabled`
Type
boolean
Required
optional
Enum

Description

Zone status

* Name
`enable_search_domain`
Type
boolean
Required
required
Enum

Description

Enable this zone as a search domain

* Name
`distribution_groups`
Type
string[]
Required
required
Enum

Description

Group IDs that defines groups of peers that will resolve this zone

### Request

PUT

/api/dns/zones/{zoneId}
```
curl -X PUT https://api.netbird.io/api/dns/zones/{zoneId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Office Zone",
"domain": "example.com",
"enabled": {
"description": "Zone status",
"type": "boolean",
"default": true
},
"enable_search_domain": false,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7m0"
]
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"records": [
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "www.example.com",
"type": "A",
"content": "192.168.1.1",
"ttl": 300
}
],
"name": "Office Zone",
"domain": "example.com",
"enabled": {
"description": "Zone status",
"type": "boolean",
"default": true
},
"enable_search_domain": false,
"distribution_groups": [
"ch8i4ug6lnn4g9hqv7m0"
]
}

```

* * *

DELETE/api/dns/zones/{zoneId}

## [Delete a DNS Zone](https://docs.netbird.io/ipa/resources/dns-zones#delete-a-dns-zone)

Deletes a custom DNS zone

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns-zones#path-parameters-3)

* Name
`zoneId`
Type
string
Required
required
Enum

Description

The unique identifier of a zone

### Request

DELETE

/api/dns/zones/{zoneId}
```
curl -X DELETE https://api.netbird.io/api/dns/zones/{zoneId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

GET/api/dns/zones/{zoneId}/records

## [List all DNS Records](https://docs.netbird.io/ipa/resources/dns-zones#list-all-dns-records)

Returns a list of all DNS records in a zone

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns-zones#path-parameters-4)

* Name
`zoneId`
Type
string
Required
required
Enum

Description

The unique identifier of a zone

### Request

GET

/api/dns/zones/{zoneId}/records
```
curl -X GET https://api.netbird.io/api/dns/zones/{zoneId}/records \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "www.example.com",
"type": "A",
"content": "192.168.1.1",
"ttl": 300
}
]

```

* * *

POST/api/dns/zones/{zoneId}/records

## [Create a DNS Record](https://docs.netbird.io/ipa/resources/dns-zones#create-a-dns-record)

Creates a new DNS record in a zone

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns-zones#path-parameters-5)

* Name
`zoneId`
Type
string
Required
required
Enum

Description

The unique identifier of a zone

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/dns-zones#request-body-parameters-3)

* Name
`name`
Type
string
Required
required
Enum

Description

FQDN for the DNS record. Must be a subdomain within or match the zone's domain.

* Name
`type`
Type
string
Required
required
Enum

Description

DNS record type

* Name
`content`
Type
string
Required
required
Enum

**Possible Values:**`>=1 characters` and `<=255 characters`

Description

DNS record content (IP address for A/AAAA, domain for CNAME)

* Name
`ttl`
Type
integer
Required
required
Enum
00
Description

Time to live in seconds

### Request

POST

/api/dns/zones/{zoneId}/records
```
curl -X POST https://api.netbird.io/api/dns/zones/{zoneId}/records \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "www.example.com",
"type": "A",
"content": "192.168.1.1",
"ttl": 300
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "www.example.com",
"type": "A",
"content": "192.168.1.1",
"ttl": 300
}

```

* * *

GET/api/dns/zones/{zoneId}/records/{recordId}

## [Retrieve a DNS Record](https://docs.netbird.io/ipa/resources/dns-zones#retrieve-a-dns-record)

Returns information about a specific DNS record

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns-zones#path-parameters-6)

* Name
`zoneId`
Type
string
Required
required
Enum

Description

The unique identifier of a zone

* Name
`recordId`
Type
string
Required
required
Enum

Description

The unique identifier of a DNS record

### Request

GET

/api/dns/zones/{zoneId}/records/{recordId}
```
curl -X GET https://api.netbird.io/api/dns/zones/{zoneId}/records/{recordId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "www.example.com",
"type": "A",
"content": "192.168.1.1",
"ttl": 300
}

```

* * *

PUT/api/dns/zones/{zoneId}/records/{recordId}

## [Update a DNS Record](https://docs.netbird.io/ipa/resources/dns-zones#update-a-dns-record)

Updates a DNS record in a zone

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns-zones#path-parameters-7)

* Name
`zoneId`
Type
string
Required
required
Enum

Description

The unique identifier of a zone

* Name
`recordId`
Type
string
Required
required
Enum

Description

The unique identifier of a DNS record

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/dns-zones#request-body-parameters-4)

* Name
`name`
Type
string
Required
required
Enum

Description

FQDN for the DNS record. Must be a subdomain within or match the zone's domain.

* Name
`type`
Type
string
Required
required
Enum

Description

DNS record type

* Name
`content`
Type
string
Required
required
Enum

**Possible Values:**`>=1 characters` and `<=255 characters`

Description

DNS record content (IP address for A/AAAA, domain for CNAME)

* Name
`ttl`
Type
integer
Required
required
Enum
00
Description

Time to live in seconds

### Request

PUT

/api/dns/zones/{zoneId}/records/{recordId}
```
curl -X PUT https://api.netbird.io/api/dns/zones/{zoneId}/records/{recordId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "www.example.com",
"type": "A",
"content": "192.168.1.1",
"ttl": 300
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "www.example.com",
"type": "A",
"content": "192.168.1.1",
"ttl": 300
}

```

* * *

DELETE/api/dns/zones/{zoneId}/records/{recordId}

## [Delete a DNS Record](https://docs.netbird.io/ipa/resources/dns-zones#delete-a-dns-record)

Deletes a DNS record from a zone

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns-zones#path-parameters-8)

* Name
`zoneId`
Type
string
Required
required
Enum

Description

The unique identifier of a zone

* Name
`recordId`
Type
string
Required
required
Enum

Description

The unique identifier of a DNS record

### Request

DELETE

/api/dns/zones/{zoneId}/records/{recordId}
```
curl -X DELETE https://api.netbird.io/api/dns/zones/{zoneId}/records/{recordId} \
-H 'Authorization: Token <TOKEN>'

```

* * *