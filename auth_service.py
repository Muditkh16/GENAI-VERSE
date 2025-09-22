from models.user import User

class AuthService:
    def login(self, username: str, password: str) -> bool:
        return True

    def logout(self, user: User):
        pass
