import asyncio
from services.user_service import UserService
from exceptions import UserServiceError

async def main():
    service = UserService()
    try:
        user = await service.create_User("", "invalid-email")
        print(user)
    except UserServiceError as exc:
        print(f"Error occurred: {exc}")


if __name__ == "__main__":
    asyncio.run(main())