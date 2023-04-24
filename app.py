import requests
import datetime as dt

api_key="0a9884a01fa9d5fd411aba10a40cc497"

user_input = input ("Enter City: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

print(weather_data.json())

if weather_data.json()['cod'] =='404' :
    print("No City Found!")
else :
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    
    sunset = dt.datetime.utcfromtimestamp(weather_data.json()['sys']['sunset'] + weather_data.json()['timezone'])

    print(f"The weather in {user_input} is {weather}")
    print(f"The temperature is {temp}°C")
    print(f"Sunset is at {sunset}")
