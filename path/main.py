import requests
from pprint import pprint

API_Key = 'dab2e4d2d099b06d753e139496a2fb05'

city = input("Digite a Cidade: ")

base_url = "https://home.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)