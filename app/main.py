import uvicorn
from fastapi import FastAPI
from .routers import temperatures, rains

app = FastAPI(
    title="Weather API",
    contact={
        "name": "Mateus Parente"
    }
)

app.include_router(temperatures.router)
app.include_router(rains.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)