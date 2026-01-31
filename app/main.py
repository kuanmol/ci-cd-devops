from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "devops works 😎"}

@app.get("/health")
def health():
    return {"status": "ok"}
