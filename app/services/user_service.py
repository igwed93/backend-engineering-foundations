from sqlalchemy.ext.asyncio import AsyncSession
from app.db_models.user import UserDB
from app.exceptions import InvalidUserDataError

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_user(self, username: str, email: str):
        if not username or not email:
            raise InvalidUserDataError("Username and email are required.")
        
        if "@" not in email:
            raise InvalidUserDataError("Invalid email format.")
        
        user = UserDB(username=username, email=email)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user