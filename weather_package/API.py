import requests

def fetch_weather(city,API_KEY):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
    response=requests.get(URL)
    return response.json()
