from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Notification Service Running in real?"}

@app.post("/notify")
def notify(email: str):
    return {
        "status": "notification sent",
        "email": email
    }

@app.get("/health")
def health():
    return {"status": "ok"}