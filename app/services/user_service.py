from models.user import User

class UserService:
    def create_User(self, username: str, email: str) -> User:
        return User(username=username, email=email)