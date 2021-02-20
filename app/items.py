from json import dumps


class WeatherItem:

    def __init__(self, location_name=None, temperature=None, wind=None, cloudiness=None, pressure=None, humidity=None,
                 sunrise=None, sunset=None, geo_coordinates=None, requested_time=None):
        self.location_name = location_name
        self.temperature = temperature
        self.wind = wind
        self.cloudiness = cloudiness
        self.pressure = pressure
        self.humidity = humidity
        self.sunrise = sunrise
        self.sunset = sunset
        self.geo_coordinates = geo_coordinates
        self.requested_time = requested_time

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return self.__dict__
