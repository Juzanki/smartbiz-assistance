from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.env_ai import get_weather_by_location
from backend.models import Product
from datetime import datetime

router = APIRouter(prefix="/forecast", tags=["Forecast & Recommendations"])

# Predefined cities (can be moved to DB or settings)
CITIES = [
    {"city": "Dar es Salaam", "lat": -6.8, "lng": 39.28},
    {"city": "Dodoma", "lat": -6.2, "lng": 35.75},
    {"city": "Moshi", "lat": -3.35, "lng": 37.33},
    {"city": "Arusha", "lat": -3.37, "lng": 36.68},
    {"city": "Mbeya", "lat": -8.9, "lng": 33.45}
]


@router.get("/zones", summary="🌦️ Get forecast and product recommendations")
def forecast_zones(db: Session = Depends(get_db)):
    now = datetime.now().strftime("%H:%M")
    result = []

    for city in CITIES:
        try:
            weather_data = get_weather_by_location(city["city"])
            raw_weather = weather_data.get("weather", "").lower()

            # Basic weather classification
            if "clear" in raw_weather:
                weather = "sunny"
            elif "rain" in raw_weather:
                weather = "rainy"
            else:
                weather = "cloudy"

            # Get matching products
            products = db.query(Product).filter(
                Product.weather_type == weather,
                Product.preferred_location.ilike(f"%{city['city']}%"),
                Product.preferred_time_start <= now,
                Product.preferred_time_end >= now
            ).limit(2).all()

            recommendation = ", ".join([p.name for p in products]) or "None"

        except Exception as e:
            weather = "unknown"
            recommendation = "None"

        result.append({
            "city": city["city"],
            "lat": city["lat"],
            "lng": city["lng"],
            "weather": weather,
            "recommendation": recommendation
        })

    return result
