# importing all the libraries
import requests
import os
import time
import csv
import file_seeker

# programming constants
# csv data
csv_filename = 'weatherdata.csv'
fields = ['No.', 'Time', 'Coordinates', 'Temperature', 'Feels', 'Min', 'Max', 'Description', 'Humidity', 'Pressure', 'Visibility']
mode = file_seeker.GetMode()
if mode == 'csv':
	with open(csv_filename, 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(fields)
elif mode == 'text':
	pass
else:
	print("Error: Unknown mode (use csv/text)")
	exit(1)

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

# shall only work if the data is csv
if mode == 'csv':
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



# --------------------------------------------------
# this works if the data isn't of csv type, ie text type
def SendMessage():
	import os
	import requests

	city_name = 'Belgaum'
	api_key = os.environ.get('W_API')
	api_link = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key
	order = requests.get(api_link)
	data = order.json()
	kc = 273.15 


	if data['coord'] == 404:
		print("City not found on the database")
	else:
			print("City found on the database")
			weather_description = data['weather'][0]['description']
			temp = (data['main']['temp'])-kc
			humidity = data['main']['humidity']

			values = 'Currently weather in Belgaum is:' + temp + ', ' + weather_description + ', ' + humidity

	return values


# --------------------------------------------------