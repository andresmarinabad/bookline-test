from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

def get_available_cars(db: Session, day: date):
    booked_car_ids = [b.car_id for b in db.query(models.Booking).filter(models.Booking.date == day).all()]
    return db.query(models.Car).filter(~models.Car.id.in_(booked_car_ids)).all()

def create_booking(db: Session, booking: schemas.BookingCreate):
    car = db.query(models.Car).filter(models.Car.id == booking.car_id).first()
    if not car:
        raise ValueError("Car not found")
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
