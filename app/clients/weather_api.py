from pydantic_settings import BaseSettings
import requests

class Settings(BaseSettings):
    weather_api_key: str = ""

settings = Settings()

class WeatherAPIClient:
    BASE_URL = "http://api.weatherapi.com/v1/forecast.json"
    API_KEY = settings.weather_api_key

    @staticmethod
    def get_weather(city: str, days: int):
        params = {
            "key": WeatherAPIClient.API_KEY,
            "q": city,
            "days": days,
            "aqi": "no",
            "alerts": "no"
        }
        response = requests.get(WeatherAPIClient.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()