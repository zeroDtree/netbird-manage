# Jobs

GET/api/peers/{peerId}/jobs

## [List Jobs](https://docs.netbird.io/ipa/resources/jobs#list-jobs)

Retrieve all jobs for a given peer

### [Path Parameters](https://docs.netbird.io/ipa/resources/jobs#path-parameters)

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

/api/peers/{peerId}/jobs
```
curl -X GET https://api.netbird.io/api/peers/{peerId}/jobs \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": {
"type": "string"
},
"created_at": {
"type": "string",
"format": "date-time"
},
"completed_at": {
"type": "string",
"format": "date-time",
"nullable": true
},
"triggered_by": {
"type": "string"
},
"status": {
"type": "string",
"enum": [
"pending",
"succeeded",
"failed"
]
},
"failed_reason": {
"type": "string",
"nullable": true
},
"workload": {
"oneOf": [
{
"type": "bundle",
"parameters": {
"bundle_for": true,
"bundle_for_time": 2,
"log_file_count": 100,
"anonymize": false
},
"result": {
"upload_key": "upload_key_123"
}
}
],
"discriminator": {
"propertyName": "type",
"mapping": {
"bundle": "#/components/schemas/BundleWorkloadResponse"
}
}
}
}
]

```

* * *

POST/api/peers/{peerId}/jobs

## [Create Job](https://docs.netbird.io/ipa/resources/jobs#create-job)

Create a new job for a given peer

### [Path Parameters](https://docs.netbird.io/ipa/resources/jobs#path-parameters-2)

* Name
`peerId`
Type
string
Required
required
Enum

Description

The unique identifier of a peer

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/jobs#request-body-parameters)

* Name
`workload`
Type

Required
required
Enum

Description

### Request

POST

/api/peers/{peerId}/jobs
```
curl -X POST https://api.netbird.io/api/peers/{peerId}/jobs \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"workload": {
"oneOf": [
{
"type": "bundle",
"parameters": {
"bundle_for": true,
"bundle_for_time": 2,
"log_file_count": 100,
"anonymize": false
}
}
],
"discriminator": {
"propertyName": "type",
"mapping": {
"bundle": "#/components/schemas/BundleWorkloadRequest"
}
}
}
}'

```

* * *

GET/api/peers/{peerId}/jobs/{jobId}

## [Get Job](https://docs.netbird.io/ipa/resources/jobs#get-job)

Retrieve details of a specific job

### [Path Parameters](https://docs.netbird.io/ipa/resources/jobs#path-parameters-3)

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
`jobId`
Type
string
Required
required
Enum

Description

The unique identifier of a job

### Request

GET

/api/peers/{peerId}/jobs/{jobId}
```
curl -X GET https://api.netbird.io/api/peers/{peerId}/jobs/{jobId} \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"id": {
"type": "string"
},
"created_at": {
"type": "string",
"format": "date-time"
},
"completed_at": {
"type": "string",
"format": "date-time",
"nullable": true
},
"triggered_by": {
"type": "string"
},
"status": {
"type": "string",
"enum": [
"pending",
"succeeded",
"failed"
]
},
"failed_reason": {
"type": "string",
"nullable": true
},
"workload": {
"oneOf": [
{
"type": "bundle",
"parameters": {
"bundle_for": true,
"bundle_for_time": 2,
"log_file_count": 100,
"anonymize": false
},
"result": {
"upload_key": "upload_key_123"
}
}
],
"discriminator": {
"propertyName": "type",
"mapping": {
"bundle": "#/components/schemas/BundleWorkloadResponse"
}
}
}
}

```

* * *