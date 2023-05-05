from flask import current_app
import requests


def weather_by_city(city_name):
	#http://api.worldweatheronline.com/premium/v1/weather.ashx?key=38d7d237f2eb4546975144035232704&q=Kyiv,Ukraine&format=json&num_of_days=1&lang=ru
	#weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?'
	weather_url = current_app.config['WEATHER_URL']

	params1 = {
		#"key"	: '38d7d237f2eb4546975144035232704',
		"key"	: current_app.config['WEATHER_API_KEY'],
		'q'		: city_name,
		"format": "json",
		"num_of_days": 1,
		'lang'	: 'ru' 
	} 
	try:
		result = requests.get(weather_url, params=params1)
		result.raise_for_status()                 # status answer server (error 4xx, 5xx)
		weather = result.json()
		if 'data' in weather:
			if 'current_condition' in weather['data']:
				try:
					return weather['data']['current_condition'][0]
				except(IndexError, TypeError):
					return False
	##################################################
	# except():
	# requests.RequestException - haven't internet
	# ValueError                - incorrect http address (encoder.json - error)
	except(requests.RequestException, ValueError): # Network Error
		print("--/Newwork Error/ --")
		return False
	# except(TypeError): #Server Error
	# 	print('--/Server Error/--')
	# 	return False

	return False


if __name__=='__main__':
	w = weather_by_city('Kyiv,Ukraine')
	print(w)