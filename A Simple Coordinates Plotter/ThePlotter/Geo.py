from pytz import timezone
from datetime import datetime
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Marker

class Geopoint(Marker):

    def __init__(self, latitude, longitude):
        super().__init__(location=[latitude, longitude])
        self.latitude = latitude
        self.longitude = longitude

    def closest_parallel(self):
        return round(self.latitude)

    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat=self.latitude, lng=self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        return time_now

    def get_weather(self):
        weather = Weather(apikey="", lat=self.latitude, lon=self.longitude)
        return weather.next_12h_simplified()

    #class method (cls)
    @classmethod
    def random(cls):
        return cls(latitude=uniform(-90,90), longitude=uniform(-180,180))
