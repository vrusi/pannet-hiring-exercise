import os
import pyowm
from pyowm import OWM
import sys

OWM_API_KEY = os.environ['OWM_API_KEY']
OWM_CITY = os.environ['OWM_CITY']

def get_weather():
    owm = OWM(OWM_API_KEY)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(OWM_CITY)
    weather = observation.weather

    return weather


def log_weather_info():
    weather = get_weather()
    description = weather.detailed_status
    temperature = weather.temperature('celsius')['temp']
    humidity = weather.humidity
    
    to_log = 'city="' + OWM_CITY + '", description="' + description + '", temp=' + str(temperature) + ', humidity=' + str(humidity)
    sys.stdout.write(to_log)


if __name__ == "__main__":
   log_weather_info()
