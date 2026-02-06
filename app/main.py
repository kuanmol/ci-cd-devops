from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    # Added a few extra lines to see changes
    msg = "DevOps works 😎 ✅"
    tip = "Kubernetes deployment updated successfully!"
    return {"msg": msg, "tip": tip}

@app.get("/health")
def health():
    return {"status": "ok"}
