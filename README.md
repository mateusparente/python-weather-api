# Python Fast-API Example
Python study project with Fast-API 

## Dependencies
1. Clone the repository.
2. Navigate to the root folder
```
pip install -r requirements.txt
```

## Getting Started
1. Create your Weather API key on https://www.weatherapi.com/

## Running the application
1. Navigate to the root folder
2. Run the project: `WEATHER_API_KEY="your_key" uvicorn app.main:app --reload` or `python3 main.py`.
3. Access the API documentation on `http://localhost:8000/docs`

## Running tests
1. Navigate to the root folder
2. Run `python3 -m pytest`