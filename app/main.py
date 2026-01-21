from fastapi import FastAPI, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.exceptions import InvalidUserDataError

app = FastAPI(title="Backend Engineering API")

user_service = UserService()

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    try:
        return await user_service.create_user(
            username=user.username,
            email=user.email
        )
    except InvalidUserDataError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
