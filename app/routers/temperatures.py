from fastapi import APIRouter, Query
from ..services.weather_service import get_temperature_forecast
from ..models.models import TemperatureForecastResponse

router = APIRouter()

@router.get("/temperatures/forecasts",
            name="Get the temperature list for a City for the next X days")
def get_temperature(city: str = Query("Lisbon", description="City name"),
                    days: int = Query(3, description="Number of days")) -> TemperatureForecastResponse:
    return get_temperature_forecast(city, days)