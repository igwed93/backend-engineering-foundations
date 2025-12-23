class User():
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.is_active = True

    def deactivate(self):
        self.is_active = False


if __name__ == "__main__":
    user = User(username="daniel", email="daniel@example.com")
    print(user.username, user.is_active)
    user.deactivate()
    print(user.is_active)