import os

import requests
import datetime as dt

from flask import Flask, render_template
# flask variables #
app = Flask(__name__)

# api key #
api_key="0a9884a01fa9d5fd411aba10a40cc497"

user_input = input ("Enter City: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

print(weather_data.json())

# 1st check if city exists - maybe a typo in the input was received #
if weather_data.json()['cod'] =='404' :
    print("No City Found!")
else :
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    
    sunset = dt.datetime.fromtimestamp(weather_data.json()['sys']['sunset'] + weather_data.json()['timezone'])
    
    # extract hours and minutes from sunset time #
    sunset_time = sunset.strftime("%I:%M %p") 

    print(f"The weather in {user_input} is {weather}")
    print(f"The temperature is {temp} °C")
    print(f"Sunset is at {sunset_time}")



# flask routes #
@app.route("/")
def index():
    return render_template("index.html", city=user_input.capitalize(), weather=weather, temp=temp, sunset=sunset_time)


if __name__ == "__main__" :
    app.run()


