from fastapi import FastAPI
from app.services.user_service import UserService
from app.exceptions import UserServiceError

app = FastAPI(title="Backend Engineering API")

user_service = UserService()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/users")
async def create_user(name: str, email: str):
    try:
        user = await user_service.create_user(name, email)
        return user
    except UserServiceError as exc:
        return {"error": str(exc)}
