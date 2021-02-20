# WeatherAPI
This is a project that returns weather information given country and city parameters through the following endpoint

```http
GET /weather?city=$City&country=$Country
```
## Parameters
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `city` | `string` | **Required**. city  |
| `country` | `string` | **Required**. Country in two letters ISO CODE |

## Responses
WeatherAPI returns a JSON response in the following format

| Parameter | Type | Example |
| :--- | :--- | :--- |
|location_name| string | "Bogota, CO"|
|temperature| string | "17 °C"|
|wind| string | "Gentle breeze, 3.6 m/s, west-northwest"|
|cloudiness| string | "Scattered clouds"|
|pressure| string | "1027 hpa"|
|humidity| string | "63%"|
|sunrise| string | "06:07"|
|sunset| string | "18:00"|
|geo_coordinates| string | "4.61, -74.08]"|
|requested_time| string | "2018-01-09 11:57:00|
