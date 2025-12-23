from services.user_service import UserService


if __name__ == "__main__":
    service = UserService()
    user = service.create_User(username="daniel", email="daniel@example.com")
    print(user)