# MSP API access


If you manage multiple tenants under an MSP account, the NetBird API accepts an `account` query parameter that scopes a request to a specific tenant. A single personal access token (PAT) can drive automation across every tenant under your MSP account — no token swapping, no separate logins.

## [Who this is for](https://docs.netbird.io/ipa/guides/msp-api-access#who-this-is-for)

MSP and MSSP account holders managing multiple customer tenants from a single NetBird account. The `account` query parameter is meaningful only inside an MSP account; it has no effect on a standalone account.

If you are not yet an MSP, see the [MSP Portal guide](https://docs.netbird.io/manage/for-partners/msp-portal) for how to apply.

## [Setting up an automation user](https://docs.netbird.io/ipa/guides/msp-api-access#setting-up-an-automation-user)

Before you can make cross-tenant API calls you need a PAT issued to a real user inside your MSP account.

1. **Pick a user** inside your MSP account. Any real user with access to the tenants you want to automate will work, including an existing admin. Consider creating a dedicated automation user if you want clean audit attribution, an independent PAT rotation cadence, or independence from any individual employee's account lifecycle. Service users are not supported for cross-tenant calls — they remain fine for single-tenant API automation.
2. **Add the user to a permission group** that has access to every tenant you want to automate.
3. **Generate a PAT** for that user from the dashboard. Go to **Team** → **Users** , open the user, then **Access Tokens** → **Create Access Token**. Save the token securely — it is only shown once.

The `account` query parameter requires a PAT issued to a real user (one with an email-bound identity). It is not honored on PATs issued to service users — those PATs continue to work for API calls scoped to a single tenant.

## [How it works](https://docs.netbird.io/ipa/guides/msp-api-access#how-it-works)

Append `?account=<tenant_id>` to any cross-tenant-capable endpoint to execute the request inside that tenant. Omit the parameter to operate on the MSP account itself.

### [Finding a tenant ID](https://docs.netbird.io/ipa/guides/msp-api-access#finding-a-tenant-id)

List the tenants under your MSP account to retrieve their IDs. Use the same PAT (no `account` parameter — this call targets the MSP):

### List tenants under your MSP account
```
curl https://api.netbird.io/api/integrations/msp/tenants \
-H "Authorization: Token {token}"

```

Each tenant object in the response includes an `id` field — that is the value to pass as `?account=<tenant_id>`. See the [MSP API reference](https://docs.netbird.io/api/resources/msp) for the full schema.

### [Calling endpoints in a tenant](https://docs.netbird.io/ipa/guides/msp-api-access#calling-endpoints-in-a-tenant)

### List setup keys inside a tenant
```
curl https://api.netbird.io/api/setup-keys?account=<tenant_id> \
-H "Authorization: Token {token}"

```

The same pattern works for writes:

### Create a setup key inside a tenant
```
curl -X POST https://api.netbird.io/api/setup-keys?account=<tenant_id> \
-H "Authorization: Token {token}" \
-H "Content-Type: application/json" \
-d '{"name":"bootstrap","type":"reusable"}'

```

## [Common automation flow](https://docs.netbird.io/ipa/guides/msp-api-access#common-automation-flow)

A typical MSP onboarding script looks like this:

* Create the tenant via the MSP API (no `account` parameter — this targets the MSP itself).
* Bootstrap a setup key inside the new tenant: `POST /api/setup-keys?account=<tenant_id>`.
* Create networks, groups, policies, and users inside the tenant: `POST /api/networks?account=<tenant_id>`, `POST /api/users?account=<tenant_id>`, and so on.

The same PAT is used for every step. Only the `account` parameter changes.

## [Auditing and security](https://docs.netbird.io/ipa/guides/msp-api-access#auditing-and-security)

* Activity from cross-tenant calls appears in each target tenant's audit log labeled **External** , the same way an MSP user's UI actions do.
* A PAT with write access across every tenant under your MSP has a wide blast radius. Treat it accordingly — MFA on the underlying SSO identity, regular PAT rotation, and a secrets manager on the caller side.
* Cross-tenant calls share the same rate limit as any other PAT (120 requests per minute, 1200 burst on NetBird Cloud). The budget is per PAT, not per tenant.

[MSP API reference](https://docs.netbird.io/api/resources/msp)