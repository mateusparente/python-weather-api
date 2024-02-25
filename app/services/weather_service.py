from ..clients.weather_api import WeatherAPIClient
from ..models.models import TemperatureForecastResponse, RainForecastResponse

def get_temperature_forecast(city: str, days: int) -> TemperatureForecastResponse:
    weather_data = WeatherAPIClient.get_weather(city, days)
    temperatures = [day['day']['avgtemp_c'] for day in weather_data['forecast']['forecastday']]
    return TemperatureForecastResponse(city=city, 
                                       next_days=days, 
                                       temperatures_in_celsius=temperatures)

def get_rain_probability(city: str, days: int) -> RainForecastResponse:
    weather_data = WeatherAPIClient.get_weather(city, days)
    will_rain = any(day['day']['daily_will_it_rain'] == 1 for day in weather_data['forecast']['forecastday'])
    return RainForecastResponse(city=city, 
                                next_days=days, 
                                will_rain=will_rain)