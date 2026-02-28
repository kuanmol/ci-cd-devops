from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Payment Service Running"}

@app.post("/pay")
def pay(amount: float):
    return {
        "status": "success",
        "amount_paid": amount
    }

@app.get("/health")
def health():
    return {"status": "ok"}