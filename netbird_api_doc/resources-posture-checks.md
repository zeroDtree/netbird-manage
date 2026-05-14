# Posture Checks

GET/api/posture-checks

## [List all Posture Checks](https://docs.netbird.io/ipa/resources/posture-checks#list-all-posture-checks)

Returns a list of all posture checks

### Request

GET

/api/posture-checks
```
curl -X GET https://api.netbird.io/api/posture-checks \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7mg",
"name": "Default",
"description": "This checks if the peer is running required NetBird's version",
"checks": {
"nb_version_check": {
"min_version": "14.3"
},
"os_version_check": {
"android": {
"min_version": "13"
},
"ios": {
"min_version": "17.3.1"
},
"darwin": {
"min_version": "14.2.1"
},
"linux": {
"min_kernel_version": "5.3.3"
},
"windows": {
"min_kernel_version": "10.0.1234"
}
},
"geo_location_check": {
"locations": [
{
"country_code": "DE",
"city_name": "Berlin"
}
],
"action": "allow"
},
"peer_network_range_check": {
"ranges": [
"192.168.1.0/24",
"10.0.0.0/8",
"2001:db8:1234:1a00::/56"
],
"action": "allow"
},
"process_check": {
"processes": [
{
"linux_path": "/usr/local/bin/netbird",
"mac_path": "/Applications/NetBird.app/Contents/MacOS/netbird",
"windows_path": "C: rogramDataetBird\netbird.exe"
}
]
}
}
}
]

```

* * *

POST/api/posture-checks

## [Create a Posture Check](https://docs.netbird.io/ipa/resources/posture-checks#create-a-posture-check)

Creates a posture check

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/posture-checks#request-body-parameters)

* Name
`name`
Type
string
Required
required
Enum

Description

Posture check name identifier

* Name
`description`
Type
string
Required
required
Enum

Description

Posture check friendly description

* Name
`checks`
Type
object
Required
optional
Enum

Description
List of objects that perform the actual checks

* Name
`nb_version_check`
Type
object
Required
optional
Enum

Description
Posture check for the version of operating system

* Name
`min_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`os_version_check`
Type
object
Required
optional
Enum

Description
Posture check for the version of operating system

* Name
`android`
Type
object
Required
optional
Enum

Description
Posture check for the version of operating system

* Name
`min_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`darwin`
Type
object
Required
optional
Enum

Description
Posture check for the version of operating system

* Name
`min_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`ios`
Type
object
Required
optional
Enum

Description
Posture check for the version of operating system

* Name
`min_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`linux`
Type
object
Required
optional
Enum

Description
Posture check with the kernel version

* Name
`min_kernel_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`windows`
Type
object
Required
optional
Enum

Description
Posture check with the kernel version

* Name
`min_kernel_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`geo_location_check`
Type
object
Required
optional
Enum

Description
Posture check for geo location

* Name
`locations`
Type
object[]
Required
required
Enum

Description
List of geo locations to which the policy applies

* Name
`country_code`
Type
string
Required
required
Enum

Description

2-letter ISO 3166-1 alpha-2 code that represents the country

* Name
`city_name`
Type
string
Required
optional
Enum

Description

Commonly used English name of the city

* Name
`action`
Type
string
Required
required
Enum

Description

Action to take upon policy match

* Name
`peer_network_range_check`
Type
object
Required
optional
Enum

Description
Posture check for allow or deny access based on the peer's IP addresses. A range matches when it contains any of the peer's local network interface IPs or its public connection (NAT egress) IP, so ranges may target private subnets, public CIDRs, or single hosts via a /32 or /128.

* Name
`ranges`
Type
string[]
Required
required
Enum

Description

List of network ranges in CIDR notation, matched against the peer's local interface IPs and its public connection IP

* Name
`action`
Type
string
Required
required
Enum

Description

Action to take upon policy match

* Name
`process_check`
Type
object
Required
optional
Enum

Description
Posture Check for binaries exist and are running in the peer’s system

* Name
`processes`
Type
object[]
Required
required
Enum

Description
More Information

* Name
`linux_path`
Type
string
Required
optional
Enum

Description

Path to the process executable file in a Linux operating system

* Name
`mac_path`
Type
string
Required
optional
Enum

Description

Path to the process executable file in a Mac operating system

* Name
`windows_path`
Type
string
Required
optional
Enum

Description

Path to the process executable file in a Windows operating system

### Request

POST

/api/posture-checks
```
curl -X POST https://api.netbird.io/api/posture-checks \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Default",
"description": "This checks if the peer is running required NetBird's version",
"checks": {
"nb_version_check": {
"min_version": "14.3"
},
"os_version_check": {
"android": {
"min_version": "13"
},
"ios": {
"min_version": "17.3.1"
},
"darwin": {
"min_version": "14.2.1"
},
"linux": {
"min_kernel_version": "5.3.3"
},
"windows": {
"min_kernel_version": "10.0.1234"
}
},
"geo_location_check": {
"locations": [
{
"country_code": "DE",
"city_name": "Berlin"
}
],
"action": "allow"
},
"peer_network_range_check": {
"ranges": [
"192.168.1.0/24",
"10.0.0.0/8",
"2001:db8:1234:1a00::/56"
],
"action": "allow"
},
"process_check": {
"processes": [
{
"linux_path": "/usr/local/bin/netbird",
"mac_path": "/Applications/NetBird.app/Contents/MacOS/netbird",
"windows_path": "C: rogramDataetBird\netbird.exe"
}
]
}
}
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7mg",
"name": "Default",
"description": "This checks if the peer is running required NetBird's version",
"checks": {
"nb_version_check": {
"min_version": "14.3"
},
"os_version_check": {
"android": {
"min_version": "13"
},
"ios": {
"min_version": "17.3.1"
},
"darwin": {
"min_version": "14.2.1"
},
"linux": {
"min_kernel_version": "5.3.3"
},
"windows": {
"min_kernel_version": "10.0.1234"
}
},
"geo_location_check": {
"locations": [
{
"country_code": "DE",
"city_name": "Berlin"
}
],
"action": "allow"
},
"peer_network_range_check": {
"ranges": [
"192.168.1.0/24",
"10.0.0.0/8",
"2001:db8:1234:1a00::/56"
],
"action": "allow"
},
"process_check": {
"processes": [
{
"linux_path": "/usr/local/bin/netbird",
"mac_path": "/Applications/NetBird.app/Contents/MacOS/netbird",
"windows_path": "C: rogramDataetBird\netbird.exe"
}
]
}
}
}

```

* * *

GET/api/posture-checks/{postureCheckId}

## [Retrieve a Posture Check](https://docs.netbird.io/ipa/resources/posture-checks#retrieve-a-posture-check)

Get information about a posture check

### [Path Parameters](https://docs.netbird.io/ipa/resources/posture-checks#path-parameters)

* Name
`postureCheckId`
Type
string
Required
required
Enum

Description

The unique identifier of a posture check

### Request

GET

/api/posture-checks/{postureCheckId}
```
curl -X GET https://api.netbird.io/api/posture-checks/{postureCheckId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7mg",
"name": "Default",
"description": "This checks if the peer is running required NetBird's version",
"checks": {
"nb_version_check": {
"min_version": "14.3"
},
"os_version_check": {
"android": {
"min_version": "13"
},
"ios": {
"min_version": "17.3.1"
},
"darwin": {
"min_version": "14.2.1"
},
"linux": {
"min_kernel_version": "5.3.3"
},
"windows": {
"min_kernel_version": "10.0.1234"
}
},
"geo_location_check": {
"locations": [
{
"country_code": "DE",
"city_name": "Berlin"
}
],
"action": "allow"
},
"peer_network_range_check": {
"ranges": [
"192.168.1.0/24",
"10.0.0.0/8",
"2001:db8:1234:1a00::/56"
],
"action": "allow"
},
"process_check": {
"processes": [
{
"linux_path": "/usr/local/bin/netbird",
"mac_path": "/Applications/NetBird.app/Contents/MacOS/netbird",
"windows_path": "C: rogramDataetBird\netbird.exe"
}
]
}
}
}

```

* * *

PUT/api/posture-checks/{postureCheckId}

## [Update a Posture Check](https://docs.netbird.io/ipa/resources/posture-checks#update-a-posture-check)

Update/Replace a posture check

### [Path Parameters](https://docs.netbird.io/ipa/resources/posture-checks#path-parameters-2)

* Name
`postureCheckId`
Type
string
Required
required
Enum

Description

The unique identifier of a posture check

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/posture-checks#request-body-parameters-2)

* Name
`name`
Type
string
Required
required
Enum

Description

Posture check name identifier

* Name
`description`
Type
string
Required
required
Enum

Description

Posture check friendly description

* Name
`checks`
Type
object
Required
optional
Enum

Description
List of objects that perform the actual checks

* Name
`nb_version_check`
Type
object
Required
optional
Enum

Description
Posture check for the version of operating system

* Name
`min_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`os_version_check`
Type
object
Required
optional
Enum

Description
Posture check for the version of operating system

* Name
`android`
Type
object
Required
optional
Enum

Description
Posture check for the version of operating system

* Name
`min_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`darwin`
Type
object
Required
optional
Enum

Description
Posture check for the version of operating system

* Name
`min_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`ios`
Type
object
Required
optional
Enum

Description
Posture check for the version of operating system

* Name
`min_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`linux`
Type
object
Required
optional
Enum

Description
Posture check with the kernel version

* Name
`min_kernel_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`windows`
Type
object
Required
optional
Enum

Description
Posture check with the kernel version

* Name
`min_kernel_version`
Type
string
Required
required
Enum

Description

Minimum acceptable version

* Name
`geo_location_check`
Type
object
Required
optional
Enum

Description
Posture check for geo location

* Name
`locations`
Type
object[]
Required
required
Enum

Description
List of geo locations to which the policy applies

* Name
`country_code`
Type
string
Required
required
Enum

Description

2-letter ISO 3166-1 alpha-2 code that represents the country

* Name
`city_name`
Type
string
Required
optional
Enum

Description

Commonly used English name of the city

* Name
`action`
Type
string
Required
required
Enum

Description

Action to take upon policy match

* Name
`peer_network_range_check`
Type
object
Required
optional
Enum

Description
Posture check for allow or deny access based on the peer's IP addresses. A range matches when it contains any of the peer's local network interface IPs or its public connection (NAT egress) IP, so ranges may target private subnets, public CIDRs, or single hosts via a /32 or /128.

* Name
`ranges`
Type
string[]
Required
required
Enum

Description

List of network ranges in CIDR notation, matched against the peer's local interface IPs and its public connection IP

* Name
`action`
Type
string
Required
required
Enum

Description

Action to take upon policy match

* Name
`process_check`
Type
object
Required
optional
Enum

Description
Posture Check for binaries exist and are running in the peer’s system

* Name
`processes`
Type
object[]
Required
required
Enum

Description
More Information

* Name
`linux_path`
Type
string
Required
optional
Enum

Description

Path to the process executable file in a Linux operating system

* Name
`mac_path`
Type
string
Required
optional
Enum

Description

Path to the process executable file in a Mac operating system

* Name
`windows_path`
Type
string
Required
optional
Enum

Description

Path to the process executable file in a Windows operating system

### Request

PUT

/api/posture-checks/{postureCheckId}
```
curl -X PUT https://api.netbird.io/api/posture-checks/{postureCheckId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"name": "Default",
"description": "This checks if the peer is running required NetBird's version",
"checks": {
"nb_version_check": {
"min_version": "14.3"
},
"os_version_check": {
"android": {
"min_version": "13"
},
"ios": {
"min_version": "17.3.1"
},
"darwin": {
"min_version": "14.2.1"
},
"linux": {
"min_kernel_version": "5.3.3"
},
"windows": {
"min_kernel_version": "10.0.1234"
}
},
"geo_location_check": {
"locations": [
{
"country_code": "DE",
"city_name": "Berlin"
}
],
"action": "allow"
},
"peer_network_range_check": {
"ranges": [
"192.168.1.0/24",
"10.0.0.0/8",
"2001:db8:1234:1a00::/56"
],
"action": "allow"
},
"process_check": {
"processes": [
{
"linux_path": "/usr/local/bin/netbird",
"mac_path": "/Applications/NetBird.app/Contents/MacOS/netbird",
"windows_path": "C: rogramDataetBird\netbird.exe"
}
]
}
}
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7mg",
"name": "Default",
"description": "This checks if the peer is running required NetBird's version",
"checks": {
"nb_version_check": {
"min_version": "14.3"
},
"os_version_check": {
"android": {
"min_version": "13"
},
"ios": {
"min_version": "17.3.1"
},
"darwin": {
"min_version": "14.2.1"
},
"linux": {
"min_kernel_version": "5.3.3"
},
"windows": {
"min_kernel_version": "10.0.1234"
}
},
"geo_location_check": {
"locations": [
{
"country_code": "DE",
"city_name": "Berlin"
}
],
"action": "allow"
},
"peer_network_range_check": {
"ranges": [
"192.168.1.0/24",
"10.0.0.0/8",
"2001:db8:1234:1a00::/56"
],
"action": "allow"
},
"process_check": {
"processes": [
{
"linux_path": "/usr/local/bin/netbird",
"mac_path": "/Applications/NetBird.app/Contents/MacOS/netbird",
"windows_path": "C: rogramDataetBird\netbird.exe"
}
]
}
}
}

```

* * *

DELETE/api/posture-checks/{postureCheckId}

## [Delete a Posture Check](https://docs.netbird.io/ipa/resources/posture-checks#delete-a-posture-check)

Delete a posture check

### [Path Parameters](https://docs.netbird.io/ipa/resources/posture-checks#path-parameters-3)

* Name
`postureCheckId`
Type
string
Required
required
Enum

Description

The unique identifier of a posture check

### Request

DELETE

/api/posture-checks/{postureCheckId}
```
curl -X DELETE https://api.netbird.io/api/posture-checks/{postureCheckId} \
-H 'Authorization: Token <TOKEN>'

```

* * *