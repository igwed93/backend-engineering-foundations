from sqlalchemy.ext.asyncio import AsyncSession
from app.db_models.user import UserDB
from app.exceptions import InvalidUserDataError
from app.security import hash_password

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_user(self, username: str, email: str, password: str) -> UserDB:
        if not username or not email or not password:
            raise InvalidUserDataError("All fields required.")
        
        if "@" not in email:
            raise InvalidUserDataError("Invalid email format.")
        
        user = UserDB(
            username=username,
            email=email,
            hashed_password=hash_password(password),
            )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user