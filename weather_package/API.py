import requests
import os
def fetch_weather(city,API_KEY):
    if not API_KEY:
        API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
    if not API_KEY:
        raise ValueError("Нет ключа")
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
    response=requests.get(URL)
    return response.json()
