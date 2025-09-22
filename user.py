class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
