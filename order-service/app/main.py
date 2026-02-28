from fastapi import FastAPI
import requests

app = FastAPI()

USER_SERVICE_URL = "http://user-service"

@app.get("/")
def root():
    return {"message": "Order Service Running"}

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    user_response = requests.get(f"{USER_SERVICE_URL}/users/1")
    user_data = user_response.json()

    return {
        "order_id": order_id,
        "product": "Laptop",
        "user": user_data
    }
@app.get("/health")
def health():
    return {"status": "ok"}