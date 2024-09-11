# CarRentalPredictionApi

This repository is part of the **Car Rental Front Office Operations** application, which consists of the following components:

- [**CarRentalPricingPrediction**](https://github.com/mj301296/CarRentalPricingPrediction): A Python package for predicting car rental prices.
- [**CarRentalPredictionApi**](https://github.com/mj301296/CarRentalPredictionApi): A FastAPI microservice that provides car rental price predictions.
- [**Rateshop Backend**](https://github.com/mj301296/RateShop): A Spring Boot application that handles car fleet management.
- [**Rateshop Frontend**](https://github.com/mj301296/rateshop-frontend): A React application offering an interactive user interface for managing car fleet operations.

## CarRentalPredictionApi

- A FastAPI microservice that provides car rental price predictions.
- Utilizes the Python package uploaded to an S3 bucket from [**CarRentalPricingPrediction**](https://github.com/mj301296/CarRentalPricingPrediction).

## Explanation of Files and Directories

- **`fastapi_app/`**: FastAPI app source code.
  - **`main.py`**: Main application script.
  - **`predictor.py`**: Model logic for rent prediction input and output data.
- **`Dockerfile`**: Docker configuration for containerizing the app.
- **`entrypoint.sh`**: Entrypoint script for starting the FastAPI app.
- **`.env`**: Contains credentials for AWS and S3 rent predictor package path.
- **`rent-predictor-deployment.yaml`**: Kubernetes deployment configuration.
- **`requirements.txt`**: Python dependencies for the FastAPI app.

## Installation

1. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. For the car predictor package, refer to the steps from [**CarRentalPricingPrediction**](https://github.com/mj301296/CarRentalPricingPrediction).

## Steps to Run the App via Docker

1. Build the Docker image:

    ```bash
    docker build -t my-fastapi-app .
    ```

2. Run the application locally:

    ```bash
    docker run --env-file .env -p 8000:8000 my-fastapi-app
    ```

3. Sample request:

    ```bash
    curl -X POST "http://localhost:8000/predict" \
    -H "Content-Type: application/json" \
    -d '{
        "year": 2013,
        "make": "Toyota",
        "trim": "LE",
        "body": "Sedan",
        "condition": 4,
        "odometer": 15000.5,
        "transmission": "automatic"
    }'
    ```
## For Steps to setup Kubernetes refer Readme of [**Rateshop Frontend**](https://github.com/mj301296/rateshop-frontend):
