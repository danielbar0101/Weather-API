import datetime as dt
import requests

# defining the Base URL, API, and destination city
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('API_KEY', 'r').read()
CITY = input(str('Which city are you looking for?'))

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
#desc = response['weather']['description']
country = response['sys']['country']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# Printing the desired info from the API
print(f'Below are the stats for {CITY} in {country}')
print(f"the temperature in Celsius is: {temp_cel:.2f}°C")
print(f'But it actually feels like: {feels_Like}°C')
print(f"The humidity is: {humidity}%")
print(f"The sun sets in {CITY} at {sunset_time}")
print(f"The sun rises in {CITY} at {sunrise_time}")
