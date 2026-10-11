import os

from weather_package.API import fetch_weather
def test_weather():
    KEY =os.getenv("OPEN_WEATHER_API_KEY")
    result = fetch_weather("London",KEY)
    assert result.get("cod") == 200
    assert "name" in result
    assert "id" in result