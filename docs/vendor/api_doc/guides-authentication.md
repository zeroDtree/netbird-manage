# Authentication


You'll need to authenticate your requests to access any of the endpoints in the NetBird API. In this guide, we'll look at how authentication works. NetBird offers two ways to authenticate your API requests: OAuth2 and personal access tokens (PAT).

## [OAuth2 with bearer token](https://docs.netbird.io/ipa/guides/authentication#o-auth2-with-bearer-token)

When establishing a connection using OAuth2, you will need your access token — you can retrieve one from your IDP manager. Here's how to add the token to the request header using cURL:

### Example request with bearer token
```
curl https://api.netbird.io/api/users \
-H "Authorization: Bearer {token}"

```

Always keep your token safe and reset it if you suspect it has been compromised.

## [Using personal access tokens](https://docs.netbird.io/ipa/guides/authentication#using-personal-access-tokens)

When establishing a connection using [PATs](https://docs.netbird.io/manage/public-api), you will need your access token — you can create one in the [NetBird dashboard](https://app.netbird.io/users) under User settings. It is recommended to use [service users](https://docs.netbird.io/manage/public-api) for all organization wide flows calling the API. If you manage multiple tenants under an MSP account, see [MSP API access](https://docs.netbird.io/api/guides/msp-api-access) for how to scope calls to a specific tenant. Here's how to add the token to the request header using cURL:

For the cloud solution we are limiting the usage to 120 requests per minute with burst of 1200 requests. If your workload requires more requests, please contact us at [support@netbird.io](mailto:support@netbird.io).

### Example request with personal access token
```
curl https://api.netbird.io/api/users \
-H "Authorization: Token {token}"

```

Always keep your token safe and reset it if you suspect it has been compromised.

[How to create tokens](https://docs.netbird.io/manage/public-api#creating-an-access-token)