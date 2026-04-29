# models.py

from sqlalchemy import Column, Integer, Float, String, DateTime

from datetime import datetime
from database import Base


class FareRecord(Base):
    __tablename__ = "fare_records"

    id = Column(Integer, primary_key=True, index=True)

    distance_km = Column(Float, nullable=False)
    vehicle_type = Column(String, nullable=False)
    rate_per_km = Column(Float, nullable=False)

    travel_hour = Column(Integer, nullable=False)
    surge_multiplier = Column(Float, nullable=False)

    total_fare = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)