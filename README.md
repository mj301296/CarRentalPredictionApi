# CarRentalPredictionApi

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

docker run --env-file .env -p 8000:8000 my-fastapi-app
