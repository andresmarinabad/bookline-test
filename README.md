# Car Rental API
[![Run Tests](https://github.com/andresmarinabad/bookline-test/actions/workflows/test.yml/badge.svg)](https://github.com/andresmarinabad/bookline-test/actions/workflows/test.yml)

## Description

This is a REST API for a car rental service.  
The project is developed with **FastAPI**, uses **PostgreSQL** as the database, and is containerized with **Docker Compose**.  
Dependencies are managed with **uv**, a super-fast Python environment and package manager.


## Key Features

- List available cars for a given date  
- Create bookings for a car on a specific date  
- Persist data in a PostgreSQL database  
- Basic logging of operations (queries and bookings)  
- Automated tests with `pytest`  
- Full containerization (API + Database)  



## Architecture

```bash
├── alembic
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── 0001_initial.py
├── alembic.ini
├── app
│   ├── crud.py
│   ├── database.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── seed.py
│   └── tests
│       ├── conftest.py
│       └── test_endpoints.py
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── pyproject.toml
├── README.md
├── test.db
└── uv.lock

```


## Prerequisites

- Docker  
- Docker Compose  
- (Optional) **uv** if you want to run without containers  



## Running the Project

### Using Docker Compose

```bash
# Build and run
docker compose up --build
```

The API will be available at:
-> http://localhost:8000/docs

## Main Endpoints

### GET /cars?day=YYYY-MM-DD
Lists all cars available on a given date.

Example:

```bash 
curl "http://localhost:8000/cars?day=2025-01-01"
```


### POST /bookings
Creates a booking.

Request body:

```json
{
  "car_id": 1,
  "date": "2025-01-01",
  "customer_name": "Juan Pérez"
}
```

## Tests

Run unit tests locally:

```python
PYTHONPATH=. uv run pytest
```

## Logging

Logs include:

- Queries for available cars
- Successful or failed bookings

Example output:

```ruby
INFO:root:Query for available cars on 2025-01-01
INFO:root:Booking successful for car 1 on 2025-01-01
```

## Database

| Table    | Main Fields                  |
|----------|-----------------------------|
| cars     | id, model, available        |
| bookings | id, car_id, date, customer_name |


The database is automatically initialized when the containers are created.

## Technologies Used

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL 16
- Docker & Docker Compose
- uv (super-fast dependency installer)
- pytest

## Design Decisions

- **FastAPI** was chosen for performance and ease of building clean RESTful APIs.
- **SQLAlchemy ORM** is used for a robust and flexible data access layer.
- **uv** simplifies dependency installation and improves Python environment performance.
- **Docker Compose** allows easy setup of the API and database in isolated environments.
- Modular structure facilitates future expansions (e.g., authentication, reports, etc.).

## Future Improvements

- JWT Authentication
- Advanced availability management
- Extended OpenAPI documentation
- Cloud deployment