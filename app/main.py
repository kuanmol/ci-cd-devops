from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    # Added a few extra lines to see changes
    msg = "DevOps works 😎 ✅"
    tip = "Kubernetes deployment updated successfully!"
    note = "Refresh to see changes in pods"
    return {"msg": msg, "tip": tip, "note": note}

@app.get("/health")
def health():
    return {"status": "ok"}
