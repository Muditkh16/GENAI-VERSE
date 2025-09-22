from models.user import User

class Comment:
    def __init__(self, content: str, author: User, post):
        self.content = content
        self.author = author
        self.post = post
