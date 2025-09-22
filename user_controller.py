from services.auth_service import AuthService
from models.user import User

class UserController:
    def register(self, username: str, email: str, password: str):
        u = User(username, email)
        return u

    def login(self, username: str, password: str):
        auth = AuthService()
        return auth.login(username, password)
