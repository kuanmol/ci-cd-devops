from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def root():
    msg = "DevOps works 😎 ✅"
    tip = "Kubernetes deployment updated successfully!"
    name = "It all ready"
    return {"msg": msg, "tip": tip, "name": name}


@app.get("/health")
def health():
    return {"status": "ok"}
