from weather.utils import (
    get_GEO_API_KEY, parse_Cloudiness, parse_Wind, parse_Unix_Date
)

from weather.items import Weather_Item
from json import loads
from datetime import datetime
from requests import get


def extract_item_data(weather_data: dict) -> Weather_Item:
    """

    :param weather_data:
    :return: Weather_Item
    """
    my_item = Weather_Item()
    my_item.location_name = weather_data['name'] + ', ' + weather_data['sys']['country']
    my_item.temperature = "{temp} °C".format(temp=weather_data['main']['temp'])
    my_item.wind = parse_Wind(speed=weather_data['wind']['speed'], deg=weather_data['wind']['speed'])
    my_item.cloudiness = parse_Cloudiness(weather_data['clouds']['all'])
    my_item.pressure = "{pressure} hPa".format(pressure=weather_data['main']['pressure'])
    my_item.humidity = "{humidity}%".format(humidity=weather_data['main']['humidity'])
    my_item.sunrise = parse_Unix_Date(weather_data['sys']['sunrise'] + weather_data['timezone'])
    my_item.sunset = parse_Unix_Date(weather_data['sys']['sunset'] + weather_data['timezone'])
    my_item.geo_coordinates = "[{lat:.2f} {lon:.2f}]".format(lat=weather_data['coord']['lat'],
                                                             lon=weather_data['coord']['lon'])
    my_item.requested_time = datetime.now().strftime('%Y/%M/%D %H:%M:%S')

    return my_item


def get_weather(cityName: str, isoCountry: str) -> Weather_Item:
    """

    :param cityName:
    :param isoCountry:
    :return:
    """
    endpoint = "http://api.openweathermap.org/data/2.5/weather?q={cityName},{isoCountry}&appid={API_KEY}&units=metric"
    response = get(endpoint.format(cityName=cityName, isoCountry=isoCountry, API_KEY=get_GEO_API_KEY()))
    weather_data = loads(response.text)
    return extract_item_data(weather_data)
