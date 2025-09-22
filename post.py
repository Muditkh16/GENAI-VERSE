from models.user import User
from models.comment import Comment

class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author
        self.comments = []

    def add_comment(self, comment: Comment):
        self.comments.append(comment)
