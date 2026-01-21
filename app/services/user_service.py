import asyncio
from app.models.user import User
from app.exceptions import InvalidUserDataError

class UserService:
    async def create_user(self, username: str, email: str) -> User:
        if not username or not email:
            raise InvalidUserDataError("Username and email are required.")
        
        if "@" not in email:
            raise InvalidUserDataError("Invalid email format.")
        
        await asyncio.sleep(1)
        return User(username=username, email=email)