# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    #assert response.json() == {"message": "Welcome to the Delivery Predictor API1-fail assert"}
    assert response.json() == {"message": "Welcome to the Delivery Predictor API"}

def test_predict():
    response = client.post("/predict", json={
        "Warehouse_block": "D",
        "Mode_of_Shipment": "Ship",
        "Customer_care_calls": 3,
        "Customer_rating": 2,
        "Cost_of_the_Product": 204,
        "Prior_purchases": 10,
        "Product_importance": "medium",
        "Gender": "F",
        "Discount_offered": 10,
        "Weight_in_gms": 4534
    })
    #print(response.json())
    assert response.status_code == 200
    assert "predicted_delivery" in response.json()

test_predict()

#success input - deliver = 1
# "Warehouse_block": "D",
# "Mode_of_Shipment": "Flight",
# "Customer_care_calls": 4,
# "Customer_rating": 2,
# "Cost_of_the_Product": 177,
# "Prior_purchases": 3,
# "Product_importance": "low",
# "Gender": "F",
# "Discount_offered": 44,
# "Weight_in_gms": 1233

#fail input - deliver = 0
# "Warehouse_block": "D",
# "Mode_of_Shipment": "Ship",
# "Customer_care_calls": 3,
# "Customer_rating": 2,
# "Cost_of_the_Product": 204,
# "Prior_purchases": 10,
# "Product_importance": "medium",
# "Gender": "F",
# "Discount_offered": 10,
# "Weight_in_gms": 4534