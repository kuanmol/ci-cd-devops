from fastapi import FastAPI
import requests

app = FastAPI()

USER_SERVICE = "http://user-service"
PRODUCT_SERVICE = "http://product-service"
PAYMENT_SERVICE = "http://payment-service"
NOTIFICATION_SERVICE = "http://notification-service"

@app.get("/")
def root():
    return {"message": "Order Service Running"}

@app.get("/orders/{order_id}")
def create_order(order_id: int):

    user = requests.get(f"{USER_SERVICE}/users/1").json()
    product = requests.get(f"{PRODUCT_SERVICE}/products/1").json()

    payment = requests.post(
        f"{PAYMENT_SERVICE}/pay",
        params={"amount": product["price"]}
    ).json()

    notify = requests.post(
        f"{NOTIFICATION_SERVICE}/notify",
        params={"email": user["email"]}
    ).json()

    return {
        "order_id": order_id,
        "user": user,
        "product": product,
        "payment": payment,
        "notification": notify
    }

@app.get("/health")
def health():
    return {"status": "ok"}