# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import model

app = FastAPI()

class PredictionInput(BaseModel):
    Warehouse_block: str
    Mode_of_Shipment: str
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: int
    Prior_purchases: int
    Product_importance: str
    Gender: str
    Discount_offered: int
    Weight_in_gms: int

@app.get("/")
def home():
    return {"message": "Welcome to the Delivery Predictor API"}

@app.post("/predict")
def predict(data: PredictionInput):
    try:
        prediction = model.predict_delivery(data.dict())
        return {"predicted_delivery": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
