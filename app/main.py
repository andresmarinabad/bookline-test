from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database
import logging
from datetime import date

logging.basicConfig(level=logging.INFO)

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/cars", response_model=list[schemas.Car])
def list_available_cars(day: date, db: Session = Depends(get_db)):
    cars = crud.get_available_cars(db, day)
    logging.info(f"Query for available cars on {day}")
    return cars

@app.post("/bookings", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    try:
        b = crud.create_booking(db, booking)
        logging.info(f"Booking successful for car {b.car_id} on {b.date}")
        return b
    except Exception as e:
        logging.error(f"Failed booking: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
