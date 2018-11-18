import requests


class Weather:
    def __init__(self, city, description, temp, pressure, humidity, all, speed):
        self.city = city
        self.description = description
        self.temp = temp
        self.pressure = pressure
        self.humidity = humidity
        self.all = all
        self.speed = speed

    def __str__(self):
        return '''City: %s
Description: %s
Temp: %s degree Celsius
Pressure: %s hPa
Humidity: %s percent
Cloudiness: %s percent
Wind speed: %s m/s''' % (self.city, self.description, self.temp, self.pressure, self.humidity, self.all, self.speed)


class WeatherManager:
    URL = 'https://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&lang=ru&appid=ba89be5152a3f2584d8fc4de75381070'

    def get_weather(self, city):
        resp = requests.get(self.URL % city)
        data = resp.json()
        return Weather(data['name'], data['weather'][0]['description'], data['main']['temp'], data['main']['pressure'], data['main']['humidity'], data['clouds']['all'], data['wind']['speed'])
    

manager = WeatherManager()
w = manager.get_weather('Kharkiv')
print(w)

input('Press ENTER to exit')