import requests

KEY = 'ba89be5152a3f2584d8fc4de75381070'

URL = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=' + KEY

resp = requests.get(URL)
data = resp.json()

data['name']
data['weather'][0]['description']


class Weather:
    def __init__(self, city, temp):
        self.city = city
        self.temp = temp

    def __str__(self):
        return '''City: %s
Temp: %s''' % (self.city, self.temp)


class WeatherManager:
    URL = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=ba89be5152a3f2584d8fc4de75381070'

    def get_weather(self, city, lang='ru'):
        resp = requests.get(self.URL % city)
        data = resp.json()
        return Weather(data['name'], data['main']['temp'])

manager = WeatherManager()
w = manager.get_weather('London', lang='ru')
print(w.city)


