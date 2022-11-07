import datetime as dt
import requests

# defining the Base URL, API, and destination city
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('API_KEY', 'r').read()
CITY = 'Meitar'

# defining the search URL structure
URL = BASE_URL + "appid=" + API_KEY + '&q=' + CITY

response = requests.get(URL).json()


# converting kelvin temperature to celsius
def kelvinToCelsius(kelvin):
    return kelvin - 273.15

# converting celsius temperature to fahrenheit
def kelvinToFahrenheit(kelvin):
    return kelvin * 1.8 - 459.67

temp_kelvin = response['main']['temp']
temp_cel = kelvinToCelsius(temp_kelvin)
humidity = response['main']['humidity']
feels_Like = response['main']['feels_like']

print(f"temperature in {CITY}: {temp_cel:.2f}°C")
print(f"Humidity in {CITY}: {humidity}%")