# app/main.py

from fastapi import FastAPI
from app.schema import CustomerData
from app.predict import predict_churn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Customer Churn API is running"}

@app.post("/predict")
def predict(data: CustomerData):
    result = predict_churn(data.dict())
    return result