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


# A basic GET route to fetch a user by ID
@app.get("/user/{user_id}")
def get_user(user_id: int):
    users = {
        1: {"name": "Alice", "age": 30},
        2: {"name": "Bob", "age": 25},
    }

    user = users.get(user_id)
    if user:
        return {"user_id": user_id, "user": user}
    raise HTTPException(status_code=404, detail="User not found")


# A POST route to create a user (this is a basic example without database integration)
@app.post("/user/")
def create_user(user: dict):
    # In a real app, here you would save the user data to the database
    return {"msg": "User created successfully!", "user": user}


# A PUT route to update a user's info
@app.put("/user/{user_id}")
def update_user(user_id: int, user: dict):
    # This is where you would update the user data in your database
    return {"msg": f"User {user_id} updated successfully!", "updated_user": user}


# A DELETE route to remove a user
@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    # In a real app, you would delete the user from your database
    return {"msg": f"User {user_id} deleted successfully!"}
