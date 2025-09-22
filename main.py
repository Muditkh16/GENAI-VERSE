from controllers.user_controller import UserController
from controllers.post_controller import PostController

def run():
    uc = UserController()
    pc = PostController()

    u = uc.register("alice", "alice@example.com", "pass")
    post = pc.submit_post("alice", "Hello", "This is a test post")
    print(post.title)

if __name__ == "__main__":
    run()
