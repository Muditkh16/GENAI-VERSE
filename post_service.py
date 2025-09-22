from models.post import Post
from models.comment import Comment
from models.user import User

class PostService:
    def create_post(self, user: User, title: str, content: str) -> Post:
        post = Post(title, content, user)
        user.add_post(post)
        return post

    def comment_on_post(self, user: User, post: Post, content: str) -> Comment:
        comment = Comment(content, user, post)
        post.add_comment(comment)
        return comment
