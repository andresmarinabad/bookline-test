FROM python:3.12-slim


RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir uv

WORKDIR /app
COPY . .

RUN uv pip compile pyproject.toml --output-file=requirements.txt

RUN uv pip install --system -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
