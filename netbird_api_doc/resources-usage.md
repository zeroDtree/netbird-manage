# Usage

GET/api/integrations/billing/usage

## [Get current usage](https://docs.netbird.io/ipa/resources/usage#get-current-usage)

### Request

GET

/api/integrations/billing/usage
```
curl -X GET https://api.netbird.io/api/integrations/billing/usage \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"active_users": 15,
"total_users": 20,
"active_peers": 10,
"total_peers": 25
}

```

* * *