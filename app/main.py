from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def root():
    msg = "DevOps works 😎 ✅"
    tip = "Kubernetes deployment updated successfully!"
    return {"msg": msg, "tip": tip}


@app.get("/health")
def health():
    return {"status": "ok"}
