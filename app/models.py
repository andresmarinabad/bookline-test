from sqlalchemy import Column, Integer, String, Date, Boolean
from .database import Base

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, index=True)
    available = Column(Boolean, default=True)

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, index=True)
    date = Column(Date, index=True)
    customer_name = Column(String)
