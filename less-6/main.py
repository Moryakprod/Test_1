import requests

KEY='ba89be5152a3f2584d8fc4de75381070'

URL = 'http://api.openweathermap.org/data/2.5/weather?q=Kharkiv,UA&units=metric&appid=' + KEY

resp = requests.get(URL)
data = resp.json()

Name = data['name']
Description = data['weather'][0]['description']
Temp = data['main']['temp']
Pressure = data['main']['pressure']
Humid = data['main']['humidity']
Clouds = data['clouds']['all']

print('Город : %s' % data['name'])
print('Описание : {}'.format(Description))
print('Температура : {}'.format(Temp))
print('Давление : {}'.format(Pressure))
print('Влажность : {}'.format(Humid))
print('Облака : {}'.format(Clouds))