# DNS

GET/api/dns/nameservers

## [List all Nameserver Groups](https://docs.netbird.io/ipa/resources/dns#list-all-nameserver-groups)

Returns a list of all Nameserver Groups

### Request

GET

/api/dns/nameservers
```
curl -X GET https://api.netbird.io/api/dns/nameservers \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "Google DNS",
"description": "Google DNS servers",
"nameservers": [
{
"ip": "8.8.8.8",
"ns_type": "udp",
"port": 53
}
],
"enabled": true,
"groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"primary": true,
"domains": [
"example.com"
],
"search_domains_enabled": true
}
]

```

* * *

POST/api/dns/nameservers

## [Create a Nameserver Group](https://docs.netbird.io/ipa/resources/dns#create-a-nameserver-group)

Creates a Nameserver Group

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/dns#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

**Possible Values:**`>=1 characters` and `<=40 characters`

Description

Name of nameserver group name

* Name
`description`
Type
string
Required
required
Enum

Description

Description of the nameserver group

* Name
`nameservers`
Type
object[]
Required
required
Enum

**Possible Values:**`>=1 objects` and `<=3 objects`

Description
Nameserver list

* Name
`ip`
Type
string
Required
required
Enum

Description

Nameserver IP

* Name
`ns_type`
Type
string
Required
required
Enum

Description

Nameserver Type

* Name
`port`
Type
integer
Required
required
Enum

Description

Nameserver Port

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Nameserver group status

* Name
`groups`
Type
string[]
Required
required
Enum

Description

Distribution group IDs that defines group of peers that will use this nameserver group

* Name
`primary`
Type
boolean
Required
required
Enum

Description

Defines if a nameserver group is primary that resolves all domains. It should be true only if domains list is empty.

* Name
`domains`
Type
string[]
Required
required
Enum

Description

Match domain list. It should be empty only if primary is true.

* Name
`search_domains_enabled`
Type
boolean
Required
required
Enum

Description

Search domain status for match domains. It should be true only if domains list is not empty.

### Request

POST

/api/dns/nameservers
```
curl -X POST https://api.netbird.io/api/dns/nameservers \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Google DNS",
"description": "Google DNS servers",
"nameservers": [
{
"ip": "8.8.8.8",
"ns_type": "udp",
"port": 53
}
],
"enabled": true,
"groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"primary": true,
"domains": [
"example.com"
],
"search_domains_enabled": true
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "Google DNS",
"description": "Google DNS servers",
"nameservers": [
{
"ip": "8.8.8.8",
"ns_type": "udp",
"port": 53
}
],
"enabled": true,
"groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"primary": true,
"domains": [
"example.com"
],
"search_domains_enabled": true
}

```

* * *

GET/api/dns/nameservers/{nsgroupId}

## [Retrieve a Nameserver Group](https://docs.netbird.io/ipa/resources/dns#retrieve-a-nameserver-group)

Get information about a Nameserver Groups

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns#path-parameters)

* Name
`nsgroupId`
Type
string
Required
required
Enum

Description

The unique identifier of a Nameserver Group

### Request

GET

/api/dns/nameservers/{nsgroupId}
```
curl -X GET https://api.netbird.io/api/dns/nameservers/{nsgroupId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "Google DNS",
"description": "Google DNS servers",
"nameservers": [
{
"ip": "8.8.8.8",
"ns_type": "udp",
"port": 53
}
],
"enabled": true,
"groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"primary": true,
"domains": [
"example.com"
],
"search_domains_enabled": true
}

```

* * *

PUT/api/dns/nameservers/{nsgroupId}

## [Update a Nameserver Group](https://docs.netbird.io/ipa/resources/dns#update-a-nameserver-group)

Update/Replace a Nameserver Group

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns#path-parameters-2)

* Name
`nsgroupId`
Type
string
Required
required
Enum

Description

The unique identifier of a Nameserver Group

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/dns#request-body-parameters-2)

* Name
`name`
Type
string
Required
required
Enum

**Possible Values:**`>=1 characters` and `<=40 characters`

Description

Name of nameserver group name

* Name
`description`
Type
string
Required
required
Enum

Description

Description of the nameserver group

* Name
`nameservers`
Type
object[]
Required
required
Enum

**Possible Values:**`>=1 objects` and `<=3 objects`

Description
Nameserver list

* Name
`ip`
Type
string
Required
required
Enum

Description

Nameserver IP

* Name
`ns_type`
Type
string
Required
required
Enum

Description

Nameserver Type

* Name
`port`
Type
integer
Required
required
Enum

Description

Nameserver Port

* Name
`enabled`
Type
boolean
Required
required
Enum

Description

Nameserver group status

* Name
`groups`
Type
string[]
Required
required
Enum

Description

Distribution group IDs that defines group of peers that will use this nameserver group

* Name
`primary`
Type
boolean
Required
required
Enum

Description

Defines if a nameserver group is primary that resolves all domains. It should be true only if domains list is empty.

* Name
`domains`
Type
string[]
Required
required
Enum

Description

Match domain list. It should be empty only if primary is true.

* Name
`search_domains_enabled`
Type
boolean
Required
required
Enum

Description

Search domain status for match domains. It should be true only if domains list is not empty.

### Request

PUT

/api/dns/nameservers/{nsgroupId}
```
curl -X PUT https://api.netbird.io/api/dns/nameservers/{nsgroupId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Google DNS",
"description": "Google DNS servers",
"nameservers": [
{
"ip": "8.8.8.8",
"ns_type": "udp",
"port": 53
}
],
"enabled": true,
"groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"primary": true,
"domains": [
"example.com"
],
"search_domains_enabled": true
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7m0",
"name": "Google DNS",
"description": "Google DNS servers",
"nameservers": [
{
"ip": "8.8.8.8",
"ns_type": "udp",
"port": 53
}
],
"enabled": true,
"groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"primary": true,
"domains": [
"example.com"
],
"search_domains_enabled": true
}

```

* * *

DELETE/api/dns/nameservers/{nsgroupId}

## [Delete a Nameserver Group](https://docs.netbird.io/ipa/resources/dns#delete-a-nameserver-group)

Delete a Nameserver Group

### [Path Parameters](https://docs.netbird.io/ipa/resources/dns#path-parameters-3)

* Name
`nsgroupId`
Type
string
Required
required
Enum

Description

The unique identifier of a Nameserver Group

### Request

DELETE

/api/dns/nameservers/{nsgroupId}
```
curl -X DELETE https://api.netbird.io/api/dns/nameservers/{nsgroupId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

GET/api/dns/settings

## [Retrieve DNS settings](https://docs.netbird.io/ipa/resources/dns#retrieve-dns-settings)

Returns a DNS settings object

### Request

GET

/api/dns/settings
```
curl -X GET https://api.netbird.io/api/dns/settings \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"items": {
"disabled_management_groups": [
"ch8i4ug6lnn4g9hqv7m0"
]
}
}

```

* * *

PUT/api/dns/settings

## [Update DNS Settings](https://docs.netbird.io/ipa/resources/dns#update-dns-settings)

Updates a DNS settings object

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/dns#request-body-parameters-3)

* Name
`disabled_management_groups`
Type
string[]
Required
required
Enum

Description

Groups whose DNS management is disabled

### Request

PUT

/api/dns/settings
```
curl -X PUT https://api.netbird.io/api/dns/settings \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"disabled_management_groups": [
"ch8i4ug6lnn4g9hqv7m0"
]
}'

```

### Response
```
{
"disabled_management_groups": [
"ch8i4ug6lnn4g9hqv7m0"
]
}

```

* * *