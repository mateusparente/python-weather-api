from pydantic import BaseModel

class RainForecastResponse(BaseModel):
    city: str
    next_days: int
    will_rain: bool


class TemperatureForecastResponse(BaseModel):
    city: str
    next_days: int
    temperatures_in_celsius: list[float]