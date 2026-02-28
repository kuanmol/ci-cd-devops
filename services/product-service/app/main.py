from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Product Service Running"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "name": "Laptop",
        "price": 1000
    }

@app.get("/health")
def health():
    return {"status": "ok"}
