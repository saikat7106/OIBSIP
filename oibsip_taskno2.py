import requests

api_key = '10bbaa7233e3fa8d1991566e63e450bd'

user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")


if weather_data.json()['cod']=='404':
    print('No City Found')

else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    print(f'the weather in {user_input} is = {weather} ')
    print(f'the temperature in {user_input} is = {temp} degree celcius')