from pydantic import BaseModel
from datetime import date

class CarBase(BaseModel):
    model: str
    available: bool = True

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int
    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    car_id: int
    date: date
    customer_name: str

class Booking(BookingCreate):
    id: int
    class Config:
        orm_mode = True
