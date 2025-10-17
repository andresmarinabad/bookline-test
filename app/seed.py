from app.database import SessionLocal
from app.models import Car
import logging

logging.basicConfig(level=logging.INFO)

def seed_data():
    db = SessionLocal()
    if db.query(Car).count() == 0:
        cars = [
            Car(model="Toyota Corolla", available=True),
            Car(model="Ford Focus", available=True),
            Car(model="Tesla Model 3", available=True),
            Car(model="Chevrolet Onix", available=True),
            Car(model="Honda Civic", available=True),
            Car(model="Hyundai Elantra", available=True),
            Car(model="Volkswagen Golf", available=True),
            Car(model="Nissan Sentra", available=True),
            Car(model="Mazda 3", available=True),
            Car(model="Kia Rio", available=True),
            Car(model="BMW 3 Series", available=True),
            Car(model="Mercedes-Benz C-Class", available=True),
            Car(model="Audi A4", available=True),
            Car(model="Renault Clio", available=True),
            Car(model="Peugeot 208", available=True),
            Car(model="Fiat 500", available=True),
            Car(model="Subaru Impreza", available=True),
            Car(model="Mitsubishi Lancer", available=True),
            Car(model="Volkswagen Passat", available=True),
            Car(model="Toyota Prius", available=True),
            Car(model="Ford Mustang", available=True),
            Car(model="Chevrolet Camaro", available=True),
            Car(model="Tesla Model Y", available=True),
            Car(model="Honda Accord", available=True),
            Car(model="Hyundai Sonata", available=True)
        ]
        db.add_all(cars)
        db.commit()
        logging.info("Seed data inserted successfully")
    else:
        logging.info("Seed data already present, skipping...")
    db.close()

if __name__ == "__main__":
    seed_data()
