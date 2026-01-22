from fastapi import FastAPI, HTTPException, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.exceptions import InvalidUserDataError
from app.dependencies import get_user_service
from app.config import APP_NAME

app = FastAPI(title=APP_NAME)

user_service = UserService()

@app.post("/users", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    try:
        return await user_service.create_user(
            username=user.username,
            email=user.email
        )
    except InvalidUserDataError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
