from fastapi import Depends
from app.services.user_service import UserService
from typing import AsyncGenerator
from app.database import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession

def get_user_service(db=Depends(get_db)):
    return UserService(db)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session