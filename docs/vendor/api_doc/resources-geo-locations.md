# Geo Locations

GET/api/locations/countries

## [List all country codes](https://docs.netbird.io/ipa/resources/geo-locations#list-all-country-codes)

Get list of all country in 2-letter ISO 3166-1 alpha-2 codes

### Request

GET

/api/locations/countries
```
curl -X GET https://api.netbird.io/api/locations/countries \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
[
"DE"
]

```

* * *

GET/api/locations/countries/{country}/cities

## [List all city names by country](https://docs.netbird.io/ipa/resources/geo-locations#list-all-city-names-by-country)

Get a list of all English city names for a given country code

### [Path Parameters](https://docs.netbird.io/ipa/resources/geo-locations#path-parameters)

* Name
`country`
Type
string
Required
required
Enum

Description

### Request

GET

/api/locations/countries/{country}/cities
```
curl -X GET https://api.netbird.io/api/locations/countries/{country}/cities \
-H 'Accept: application/json' \
-H 'Authorization: Token <TOKEN>'

```

### Response
```
{
"geoname_id": 2950158,
"city_name": "Berlin"
}

```

* * *