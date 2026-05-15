# Accounts

GET/api/accounts

## [List all Accounts](https://docs.netbird.io/ipa/resources/accounts#list-all-accounts)

Returns a list of accounts of a user. Always returns a list of one account.

### Request

GET

/api/accounts
```
curl -X GET https://api.netbird.io/api/accounts \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
{
"id": "ch8i4ug6lnn4g9hqv7l0",
"settings": {
"peer_login_expiration_enabled": true,
"peer_login_expiration": 43200,
"peer_inactivity_expiration_enabled": true,
"peer_inactivity_expiration": 43200,
"regular_users_view_blocked": true,
"groups_propagation_enabled": true,
"jwt_groups_enabled": true,
"jwt_groups_claim_name": "roles",
"jwt_allow_groups": [
"Administrators"
],
"routing_peer_dns_resolution_enabled": true,
"dns_domain": "my-organization.org",
"network_range": "100.64.0.0/16",
"peer_expose_enabled": false,
"peer_expose_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"extra": {
"peer_approval_enabled": true,
"user_approval_required": false,
"network_traffic_logs_enabled": true,
"network_traffic_logs_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"network_traffic_packet_counter_enabled": true
},
"lazy_connection_enabled": true,
"auto_update_version": "0.51.2",
"auto_update_always": false,
"embedded_idp_enabled": false,
"local_auth_disabled": false
},
"domain": "netbird.io",
"domain_category": "private",
"created_at": "2023-05-05T09:00:35.477782Z",
"created_by": "google-oauth2|277474792786460067937",
"onboarding": {
"signup_form_pending": true,
"onboarding_flow_pending": false
}
}
]

```

* * *

DELETE/api/accounts/{accountId}

## [Delete an Account](https://docs.netbird.io/ipa/resources/accounts#delete-an-account)

Deletes an account and all its resources. Only account owners can delete accounts.

### [Path Parameters](https://docs.netbird.io/ipa/resources/accounts#path-parameters)

* Name
`accountId`
Type
string
Required
required
Enum

Description

The unique identifier of an account

### Request

DELETE

/api/accounts/{accountId}
```
curl -X DELETE https://api.netbird.io/api/accounts/{accountId} \
-H 'Authorization: Token <TOKEN>'

```

* * *

PUT/api/accounts/{accountId}

## [Update an Account](https://docs.netbird.io/ipa/resources/accounts#update-an-account)

Update information about an account

### [Path Parameters](https://docs.netbird.io/ipa/resources/accounts#path-parameters-2)

* Name
`accountId`
Type
string
Required
required
Enum

Description

The unique identifier of an account

### [Request-Body Parameters](https://docs.netbird.io/ipa/resources/accounts#request-body-parameters)

* Name
`settings`
Type
object
Required
required
Enum

Description
More Information

* Name
`peer_login_expiration_enabled`
Type
boolean
Required
required
Enum

Description

Enables or disables peer login expiration globally. After peer's login has expired the user has to log in (authenticate). Applies only to peers that were added by a user (interactive SSO login).

* Name
`peer_login_expiration`
Type
integer
Required
required
Enum

Description

Period of time after which peer login expires (seconds).

* Name
`peer_inactivity_expiration_enabled`
Type
boolean
Required
required
Enum

Description

Enables or disables peer inactivity expiration globally. After peer's session has expired the user has to log in (authenticate). Applies only to peers that were added by a user (interactive SSO login).

* Name
`peer_inactivity_expiration`
Type
integer
Required
required
Enum

Description

Period of time of inactivity after which peer session expires (seconds).

* Name
`regular_users_view_blocked`
Type
boolean
Required
required
Enum

Description

Allows blocking regular users from viewing parts of the system.

* Name
`groups_propagation_enabled`
Type
boolean
Required
optional
Enum

Description

Allows propagate the new user auto groups to peers that belongs to the user

* Name
`jwt_groups_enabled`
Type
boolean
Required
optional
Enum

Description

Allows extract groups from JWT claim and add it to account groups.

* Name
`jwt_groups_claim_name`
Type
string
Required
optional
Enum

Description

Name of the claim from which we extract groups names to add it to account groups.

* Name
`jwt_allow_groups`
Type
string[]
Required
optional
Enum

Description

List of groups to which users are allowed access

* Name
`routing_peer_dns_resolution_enabled`
Type
boolean
Required
optional
Enum

Description

Enables or disables DNS resolution on the routing peers

* Name
`dns_domain`
Type
string
Required
optional
Enum

Description

Allows to define a custom dns domain for the account

* Name
`network_range`
Type
string
Required
optional
Enum

Description

Allows to define a custom network range for the account in CIDR format

* Name
`peer_expose_enabled`
Type
boolean
Required
required
Enum

Description

Enables or disables peer expose. If enabled, peers can expose local services through the reverse proxy using the CLI.

* Name
`peer_expose_groups`
Type
string[]
Required
required
Enum

Description

Limits which peer groups are allowed to expose services. If empty, all peers are allowed when peer expose is enabled.

* Name
`extra`
Type
object
Required
optional
Enum

Description
More Information

* Name
`peer_approval_enabled`
Type
boolean
Required
required
Enum

Description

(Cloud only) Enables or disables peer approval globally. If enabled, all peers added will be in pending state until approved by an admin.

* Name
`user_approval_required`
Type
boolean
Required
required
Enum

Description

Enables manual approval for new users joining via domain matching. When enabled, users are blocked with pending approval status until explicitly approved by an admin.

* Name
`network_traffic_logs_enabled`
Type
boolean
Required
required
Enum

Description

Enables or disables network traffic logging. If enabled, all network traffic events from peers will be stored.

* Name
`network_traffic_logs_groups`
Type
string[]
Required
required
Enum

Description

Limits traffic logging to these groups. If unset all peers are enabled.

* Name
`network_traffic_packet_counter_enabled`
Type
boolean
Required
required
Enum

Description

Enables or disables network traffic packet counter. If enabled, network packets and their size will be counted and reported. (This can have an slight impact on performance)

* Name
`lazy_connection_enabled`
Type
boolean
Required
optional
Enum

Description

Enables or disables experimental lazy connection

* Name
`auto_update_version`
Type
string
Required
optional
Enum

Description

Set Clients auto-update version. "latest", "disabled", or a specific version (e.g "0.50.1")

* Name
`auto_update_always`
Type
boolean
Required
optional
Enum

Description

When true, updates are installed automatically in the background. When false, updates require user interaction from the UI.

* Name
`embedded_idp_enabled`
Type
boolean
Required
optional
Enum

Description

Indicates whether the embedded identity provider (Dex) is enabled for this account. This is a read-only field.

* Name
`local_auth_disabled`
Type
boolean
Required
optional
Enum

Description

Indicates whether local (email/password) authentication is disabled. When true, users can only authenticate via external identity providers. This is a read-only field.

* Name
`onboarding`
Type
object
Required
optional
Enum

Description
More Information

* Name
`signup_form_pending`
Type
boolean
Required
required
Enum

Description

Indicates whether the account signup form is pending

* Name
`onboarding_flow_pending`
Type
boolean
Required
required
Enum

Description

Indicates whether the account onboarding flow is pending

### Request

PUT

/api/accounts/{accountId}
```
curl -X PUT https://api.netbird.io/api/accounts/{accountId} \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Token <TOKEN>' \
--data-raw '{
"settings": {
"peer_login_expiration_enabled": true,
"peer_login_expiration": 43200,
"peer_inactivity_expiration_enabled": true,
"peer_inactivity_expiration": 43200,
"regular_users_view_blocked": true,
"groups_propagation_enabled": true,
"jwt_groups_enabled": true,
"jwt_groups_claim_name": "roles",
"jwt_allow_groups": [
"Administrators"
],
"routing_peer_dns_resolution_enabled": true,
"dns_domain": "my-organization.org",
"network_range": "100.64.0.0/16",
"peer_expose_enabled": false,
"peer_expose_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"extra": {
"peer_approval_enabled": true,
"user_approval_required": false,
"network_traffic_logs_enabled": true,
"network_traffic_logs_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"network_traffic_packet_counter_enabled": true
},
"lazy_connection_enabled": true,
"auto_update_version": "0.51.2",
"auto_update_always": false,
"embedded_idp_enabled": false,
"local_auth_disabled": false
},
"onboarding": {
"signup_form_pending": true,
"onboarding_flow_pending": false
}
}'

```

### Response
```
{
"id": "ch8i4ug6lnn4g9hqv7l0",
"settings": {
"peer_login_expiration_enabled": true,
"peer_login_expiration": 43200,
"peer_inactivity_expiration_enabled": true,
"peer_inactivity_expiration": 43200,
"regular_users_view_blocked": true,
"groups_propagation_enabled": true,
"jwt_groups_enabled": true,
"jwt_groups_claim_name": "roles",
"jwt_allow_groups": [
"Administrators"
],
"routing_peer_dns_resolution_enabled": true,
"dns_domain": "my-organization.org",
"network_range": "100.64.0.0/16",
"peer_expose_enabled": false,
"peer_expose_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"extra": {
"peer_approval_enabled": true,
"user_approval_required": false,
"network_traffic_logs_enabled": true,
"network_traffic_logs_groups": [
"ch8i4ug6lnn4g9hqv7m0"
],
"network_traffic_packet_counter_enabled": true
},
"lazy_connection_enabled": true,
"auto_update_version": "0.51.2",
"auto_update_always": false,
"embedded_idp_enabled": false,
"local_auth_disabled": false
},
"domain": "netbird.io",
"domain_category": "private",
"created_at": "2023-05-05T09:00:35.477782Z",
"created_by": "google-oauth2|277474792786460067937",
"onboarding": {
"signup_form_pending": true,
"onboarding_flow_pending": false
}
}

```

* * *