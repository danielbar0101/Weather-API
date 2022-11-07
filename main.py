import datetime as dt
import requests

# defining the Base URL, API, and destination city
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('Weather-API/API_KEY', 'r').read()
CITY = 'Meitar'

# defining the access URL structure
URL = BASE_URL + "appid=" + API_KEY + '&q=' + CITY

# reaching the API
response = requests.get(URL).json()


# converting kelvin temperature to celsius
def kelvinToCelsius(kelvin):
    return kelvin - 273.15


# converting celsius temperature to fahrenheit
def kelvinToFahrenheit(kelvin):
    return kelvin * 1.8 - 459.67


# defining object to be pulled from the API
temp_kelvin = response['main']['temp']
temp_cel = kelvinToCelsius(temp_kelvin)
humidity = response['main']['humidity']
feels_Like = response['main']['feels_like']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# Printing the desired info from the API
print(f"temperature in {CITY}: {temp_cel:.2f}°C")
print(f"Humidity in {CITY}: {humidity}%")
print(f"The sun sets in {CITY} at {sunset_time}")
