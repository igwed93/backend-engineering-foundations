from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    is_active: bool