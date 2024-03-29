# importing all the libraries
import requests
import os
import time

# programming constants
# csv data
csv_filename = 'weatherdata.csv'
fields = ['No.', 'Time', 'Coordinates', 'Temperature', 'Feels', 'Min', 'Max', 'Description', 'Humidity', 'Pressure', 'Visibility']
with open(csv_filename, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)

# constants
kc = 273.15 # kelvin to celsius conversion constant
lever = 1

# api functions
city_name = 'Belgaum'
api_key = os.environ.get('W_API')
api_link = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key
order = requests.get(api_link)
data = order.json()

# taking in the data
if data['coord'] == 404:
	print("City not found on the database")
else:
	while lever == 1:
		print("City found on the database")
		srno = 1
		curtime = time.strftime('%Y/%m/%d %H:%M:%S')
		coord = str(data['coord']['lat'])+', '+str(data['coord']['lon'])
		weather_description = data['weather'][0]['description']
		temp = (data['main']['temp'])-kc
		feels_like = (data['main']['feels_like'])-kc
		temp_min = (data['main']['temp_min'])-kc
		temp_max = (data['main']['temp_max'])-kc
		humidity = data['main']['humidity']
		pressure = data['main']['pressure']
		visibility = data['visibility']
		values = [srno, curtime, coord, temp, feels_like, temp_min, temp_max, weather_description, humidity, pressure, visibility]

		# will print out the values in the csv file append function
		with open(csv_filename, 'a') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerow(values)
		print('Data written to CSV file')
		lever = 0
