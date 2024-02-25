from unittest.mock import patch
import pytest
from app.services.weather_service import get_temperature_forecast, get_rain_probability

@pytest.fixture
def mock_weather_data():
    return {
        "forecast": {
            "forecastday": [
                {"day": {"avgtemp_c": 20, "daily_will_it_rain": 0}},
                {"day": {"avgtemp_c": 21, "daily_will_it_rain": 1}},
                {"day": {"avgtemp_c": 22, "daily_will_it_rain": 0}},
            ]
        }
    }

@patch('app.clients.weather_api.WeatherAPIClient.get_weather')
def test_get_temperature_forecast(mock_get_weather, mock_weather_data):
    mock_get_weather.return_value = mock_weather_data
    response = get_temperature_forecast("TestCity", 3)

    assert response.city == "TestCity"
    assert response.next_days == 3
    assert response.temperatures_in_celsius == [20, 21, 22]

@patch('app.clients.weather_api.WeatherAPIClient.get_weather')
def test_get_rain_probability(mock_get_weather, mock_weather_data):
    mock_get_weather.return_value = mock_weather_data
    response = get_rain_probability("Lisbon", 3)
    assert response.will_rain == True