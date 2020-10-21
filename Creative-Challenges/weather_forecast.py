import requests
from json import dumps

API_KEY = "0fef2bbb2fc2a5d70edd4f5000ec748e"
LAT, LON = "50.738530", "-3.545040"

onecall_url = "https://api.openweathermap.org/data/2.5/onecall?units=metric&lat={}&lon={}&appid={}".format(
LAT, LON, API_KEY)


def get_weather_data():
    """Returns a dictonary containing current weather & forecasts"""
    # Try and reach the API 4 times
    for retry in range(4):
        r = requests.get(onecall_url)
        if r.status_code == 200:
            return r.json()
    return False


weather_data = get_weather_data()
if not weather_data:
    print("Failed to get current weather and forecasts after 4 retries.")
    print("Please try again later.")
else:
    current_weather = weather_data["current"]
    weather = current_weather["weather"]
    temp = current_weather["temp"]
    feels_like = current_weather["feels_like"]
    wind_speed = current_weather["wind_speed"]

    print("Here's today's clothing tips for Exeter:\n")
    current_outfit = []

    output = ""
    jacket = False
    # Temperature
    output += "It's {}ºC out, but it feels like {}ºC".format(
        temp, feels_like)
    if feels_like < 0:
        current_outfit.append("several layers of warm clothing")
    elif feels_like < 8:
        current_outfit.append("something warm")
    elif feels_like < 15:
        current_outfit.append("a light jacket or a hoodie")
        jacket = True
    elif feels_like < 25:
        current_outfit.append("nothing too warm")
    else:
        current_outfit.append("something nice and cool")

    # Wind
    if wind_speed < 15:
        output += ", and it's a little breezy out."
        if not jacket:
            current_outfit.append("a light jacket or a hoodie")
    elif wind_speed < 25:
        output += ", and it's quite windy out."
        if not jacket:
            current_outfit.append("a good jacket or a hoodie")
    elif wind_speed < 60:
        output += ", and it's very windy out!"
        current_outfit.append("a good coat")
    else:
        output += ", and it's gale force winds out!"
        current_outfit.append("a very good coat!")

    # Outfit
    outfit = ""
    if len(current_outfit) == 1:
        outfit += current_outfit[0]
    else:
        for i in range(len(current_outfit)):
            if i == len(current_outfit) - 1:
                outfit += ", and "
            outfit += current_outfit[i]
    output += "\nWe recommend you wear {}.".format(outfit)
    

    # Rain
    raining = False
    for w in weather:
        if w["main"] == "Rain":
            raining = True
            output += "\nIt also looks like it's raining, so wear a waterproof!"
            break

    # Will it be raining later today?
    for forecast in weather_data["daily"]:
        if not raining:
            for w in forecast["weather"]:
                if w["main"] == "Rain":
                    raining = True
                    output += "\nIt looks like it'll rain later, so bring a waterproof!"

    print(output)
