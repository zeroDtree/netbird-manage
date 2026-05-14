# Quickstart


This guide will get you all set up and ready to use the NetBird API. We'll cover how to get started using cURL and how to make your first API request. We'll also look at where to go next to find all the information you need to take full advantage of our powerful REST API.

## [Install cURL](https://docs.netbird.io/ipa/guides/quickstart#install-c-url)

For this guide, we'll be using cURL to make our first API request. If you don't already have cURL installed, you can download it from the [cURL website](https://curl.se/download.html).

## [Get an access token](https://docs.netbird.io/ipa/guides/quickstart#get-an-access-token)

Before making your first API request, you need to create an access token to authenticate requests to the API. You can create an access token in the [NetBird dashboard](https://app.netbird.io) under [Users » Me](https://app.netbird.io/users). After the token was created successfully make sure to store it as we need it for the next step.

## [Making your first API request](https://docs.netbird.io/ipa/guides/quickstart#making-your-first-api-request)

After creating your access token, you are ready to make your first call to the NetBird API. Below, you can see how to send a GET request to the peers endpoint to get a list of all peers in your network.

GET

/api/peers
```
curl -X GET https://api.netbird.io/api/peers \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

NOTE: If you are self-hosting netbird, and used the advanced guide, you may need to use port 33073 with your management URL.

[Read the docs for the peers endpoint](https://docs.netbird.io/api/resources/peers)

## [What's next?](https://docs.netbird.io/ipa/guides/quickstart#whats-next)

Great, you're now set up with an API client and have made your first request to the API. Here are a few links that might be handy as you venture further into the NetBird API:

* [Read how to properly authenticate against the NetBird API](https://docs.netbird.io/api/guides/authentication)
* [Check out the users endpoint](https://docs.netbird.io/api/resources/users)
* [Learn about the different error types](https://docs.netbird.io/api/guides/errors)