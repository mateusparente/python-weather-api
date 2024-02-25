from fastapi import APIRouter, Query
from ..services.weather_service import get_rain_probability
from ..models.models import RainForecastResponse

router = APIRouter()

@router.get("/rains/probability/next-days", 
            name = "Get the rain probability for a City for the next X days")
def get_rain(city: str = Query("Lisbon", description="City name"),
             days: int = Query(3, description="Number of days")) -> RainForecastResponse:
    return get_rain_probability(city, days)