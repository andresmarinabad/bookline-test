from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_cars():
    """
    Test GET /cars to retrieve available cars for a given day.
    """
    test_day = "2025-01-01"
    response = client.get(f"/cars?day={test_day}")
    assert response.status_code == 200
    cars = response.json()
    assert isinstance(cars, list)
    if cars:
        assert "id" in cars[0]
        assert "model" in cars[0]
        assert "available" in cars[0]

def test_create_booking():
    """
    Test POST /bookings for booking creation.
    If no cars are available, the API should return 400 with a proper error message.
    """
    test_day = "2025-01-01"
    cars_response = client.get(f"/cars?day={test_day}")
    assert cars_response.status_code == 200
    cars = cars_response.json()

    if cars:
        car_id = cars[0]["id"]
        booking_data = {
            "car_id": car_id,
            "customer_name": "John Doe",
            "date": test_day
        }
        response = client.post("/bookings", json=booking_data)
        assert response.status_code == 200
        booking = response.json()
        assert booking["car_id"] == car_id
        assert booking["customer_name"] == "John Doe"
        assert booking["date"] == test_day
    else:
        booking_data = {
            "car_id": 1,
            "customer_name": "John Doe",
            "date": test_day
        }
        response = client.post("/bookings", json=booking_data)
        assert response.status_code == 400
        detail = response.json().get("detail", "")
        assert detail in ["Car not found", "already booked", "No available car"]
