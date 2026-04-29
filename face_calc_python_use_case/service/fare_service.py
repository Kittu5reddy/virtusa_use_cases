from exceptions.vehicle_type_not_found_exception import VehicleTypeNotFoundException
from constants import RATES, NORMAL_HOUR_SURGE, PEAK_HOUR_SURGE
from database import SessionLocal
from database.model import FareRecord
from repository.fare_repository import FareRepository


def calculate_fare(kilometers: float,vehicle_type: str,hour: int) -> tuple[float, float]:

    # =============================
    # Validation
    # =============================
    if not (0 <= hour <= 23):
        raise ValueError("Hour must be between 0 and 23")

    if vehicle_type not in RATES:
        raise VehicleTypeNotFoundException("Vehicle Type Not Found")

    # =============================
    # Business Logic
    # =============================
    rate = RATES[vehicle_type]
    total_amount = kilometers * rate

    surge = PEAK_HOUR_SURGE if 17 <= hour <= 20 else NORMAL_HOUR_SURGE
    final_fare = total_amount * surge

    # =============================
    # DB Transaction
    # =============================
    db = SessionLocal()

    try:
        record = FareRecord(
            distance_km=kilometers,
            vehicle_type=vehicle_type,
            rate_per_km=rate,
            travel_hour=hour,
            surge_multiplier=surge,
            total_fare=final_fare
        )

        FareRepository.add(db, record)

        db.commit()
        db.refresh(record)

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()

    return final_fare, surge