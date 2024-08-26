import logging
from fastapi import FastAPI, HTTPException
import pandas as pd
from car_price_predictor.scripts.model_prediction import predict_price, load_model, load_encoders_and_scaler, preprocess_new_data
from fastapi_app.model import PredictionInput, PredictionOutput 

# Initialize the FastAPI app
app = FastAPI()

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log message format
    handlers=[
        logging.StreamHandler()  # Log to the console
    ]
)

# Create a logger instance
logger = logging.getLogger(__name__)

# Load model and encoders/scaler
try:
    logger.info("Loading model and preprocessing tools...")
    model = load_model()
    encoders, scaler = load_encoders_and_scaler()
    logger.info("Model and preprocessing tools loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model or preprocessing tools: {e}")
    raise



@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    try:
        logger.info("Received prediction request.")

        # Convert input data to DataFrame
        data_dict = input_data.dict()
        logger.debug(f"Input data: {data_dict}")

        # Preprocess the input data
        scaled_data = preprocess_new_data(data_dict, encoders, scaler)
        logger.debug(f"Preprocessed data: {scaled_data}")

        # Make prediction
        predictions = predict_price(model, scaled_data)
        logger.info("Prediction completed successfully.")

        # Prepare the response
        response = {
            "sellingprice": predictions[0][0],
            "hourly": predictions[0][1],
            "daily": predictions[0][2],
            "weekly": predictions[0][3],
            "monthly": predictions[0][4],
        }

        logger.debug(f"Prediction response: {response}")
        return response

    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=400, detail=str(e))
