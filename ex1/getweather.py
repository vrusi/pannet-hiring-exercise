import os
import pyowm
from pyowm import OWM

OPENWEATHER_API_KEY = os.environ['OPENWEATHER_API_KEY']
CITY_NAME = os.environ['CITY_NAME']

owm = OWM(OPENWEATHER_API_KEY)
mgr = owm.weather_manager()

observation = mgr.weather_at_place(CITY_NAME)
weather = observation.weather

source = 'openweathermap'
description = weather.detailed_status
temperature = weather.temperature('celsius')['temp']
humidity = weather.humidity

print('source=' + source + ', ', end='')
print('description=' + description + ', ', end='')
print('temp=' + str(temperature) + ', ', end='')
print('humidity=' + str(humidity))