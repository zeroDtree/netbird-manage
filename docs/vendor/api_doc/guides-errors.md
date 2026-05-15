# Errors


When working with APIs, it's important to understand the different types of HTTP errors that you might encounter. These errors can help you diagnose issues with your API requests and determine how to resolve them.

You can tell if your request was successful by checking the status code when receiving an API response. If a response comes back unsuccessful, you can use the error type and error message to figure out what has gone wrong and do some rudimentary debugging.

The API is still in Beta state so some errors might not be handled properly yet.

* * *

## [Status codes](https://docs.netbird.io/ipa/guides/errors#status-codes)

Here is a list of the different categories of status codes returned by the NetBird API. Use these to understand if a request was successful.

* Name
`2xx`
Type

Required
optional
Enum

Description

A 2xx status code indicates a successful response.

* Name
`4xx`
Type

Required
optional
Enum

Description

A 4xx status code indicates a client error - those are mostly related to missing permissions or invalid parameters inside the request.

* Name
`5xx`
Type

Required
optional
Enum

Description

A 5xx status code indicates a server error - in this case please reach out to us via [Slack](https://docs.netbird.io/slack-url) or [GitHub](https://github.com/netbirdio/netbird/issues).

* * *