import requests
import os
from datetime import datetime

KC = 273.15

city_name = 'Belgaum'
api_key = os.environ.get('W_API')
api_link = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key

order = requests.get(api_link)
data = order.json()

if data['coord'] == 404:
	print("City not found on the database")
else:
	print("City found on the database")
	coord = str(data['coord']['lat'])+', '+str(data['coord']['lon'])
	weather_description = data['weather'][0]['description']
	temp = (data['main']['temp'])-KC
	feels_like = (data['main']['feels_like'])-KC
	temp_min = (data['main']['temp_min'])-KC
	temp_max = (data['main']['temp_max'])-KC
	humidity = data['main']['humidity']
	pressure = data['main']['pressure']
	visibility = data['visibility']
	print(coord, weather_description, temp, feels_like, temp_min, temp_max, humidity, pressure, visibility)
