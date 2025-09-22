from services.post_service import PostService
from models.user import User

class PostController:
    def submit_post(self, username, title, content):
        ps = PostService()
        user = User(username, "dummy@example.com")
        return ps.create_post(user, title, content)
