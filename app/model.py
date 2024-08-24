from pydantic import BaseModel

# Pydantic models for input validation
class PredictionInput(BaseModel):
    year: int
    make: str
    trim: str
    body: str
    condition: int
    odometer: float
    transmission: str

class PredictionOutput(BaseModel):
    sellingprice: float
    hourly: float
    daily: float
    weekly: float
    monthly: float