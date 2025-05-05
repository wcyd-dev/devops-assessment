#!/bin/bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
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
}'
