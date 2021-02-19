from weather.utils import get_GEO_API_KEY
import json
import requests


def get_weather(cityName, isoCountry):
    """
    Pending doc
    """
    endpoint = "http://api.openweathermap.org/data/2.5/weather?q={cityName},{isoCountry}&appid={API_KEY}"
    response = requests.get(endpoint.format(cityName=cityName, isoCountry=isoCountry, API_KEY=get_GEO_API_KEY()))
    weather_data = json.loads(response.text)
    return weather_data


get_weather('Bogota', 'CO')
