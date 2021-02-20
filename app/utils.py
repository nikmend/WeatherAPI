import os
from datetime import datetime


# Get environment variables

def get_api_key():
    """
    :return: Sys environment variable: GEO_API_KEY
    """

    return os.getenv('GEO_API_KEY')


def parse_cloudiness(per_cloudiness: int) -> str:
    """
    Replacing percentage returned by the api mapping to text according to the specification
    https://openweathermap.org/weather-data
    :param per_cloudiness: percentage 0-100
    :return: human-readable description
    """
    if per_cloudiness >= 85:
        cloudiness = 'Overcast clouds'
    elif per_cloudiness >= 51:
        cloudiness = 'Broken clouds'
    elif per_cloudiness >= 25:
        cloudiness = 'Scattered clouds'
    elif per_cloudiness >= 11:
        cloudiness = 'Few clouds'
    else:
        cloudiness = 'Clear sky'
    return cloudiness


def parse_unix_date(stamp: int) -> str:
    """

    :param stamp: Unix form
    :return:
    """
    return datetime.utcfromtimestamp(stamp).strftime('%H:%M')


def get_beaufort(speed: float) -> str:
    beaufort_dict = [(32.7, 'Hurricane force'), (28.5, 'Violent storm'), (24.5, 'Storm'), (20.8, 'Strong'),
                     (17.2, 'Gale'), (13.9, 'High wind'), (10.8, 'Strong breeze'), (8, 'Fresh breeze'),
                     (5.5, 'Moderate breeze'), (3.4, 'Gentle breeze'), (1.6, 'Light breeze'), (0.5, 'Light air'),
                     (0, 'Calm')]
    beaufort = ''
    for limit, description in beaufort_dict:
        if speed >= limit:
            beaufort = description
            break
    return beaufort


def get_compass_rose(deg: float) -> str:
    compass_dict = [(11.25, "north"), (33.75, "north-northeast"), (56.25, "northeast"), (78.75, "east-northeast"),
                    (101.25, "east"), (123.75, " east-south-east"), (146.25, "south-east"),
                    (168.75, "south-south-east"), (191.25, "south"), (213.75, "south-southwest"),
                    (236.25, "southwest"), (258.75, "west-southwest"), (281.25, "west"), (303.75, "west-north-west"),
                    (326.25, "northwest"), (348.75, "north-northwest"), (360, "north")]
    rose = ''
    for limit, description in compass_dict:
        if deg <= limit:
            rose = description
            break
    return rose


def parse_wind(speed: float, deg: float) -> str:
    """
    Replace deg replaces the existing value in deg to returned by the api mapping to text according to the specification
    https://openweathermap.org/weather-data
    https://en.wikipedia.org/wiki/Beaufort_scale#Modern_scale
    :param speed:
    :param deg:
    :return:human-readable description of the wind
    """
    beaufort = get_beaufort(speed)
    rose = get_compass_rose(deg)
    return '{beaufort}, {speed:.1f} m/s, {rose}'.format(beaufort=beaufort, speed=speed, rose=rose)
