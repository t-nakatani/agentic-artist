from app.adviser_repository import IAdviserRepository
from app.x_comment import XComment
from app.x_comment_dispatcher import XCommentDispatcher


class DummyAdviserRepository(IAdviserRepository):
    def __init__(self):
        self.storage: list[XComment] = []

    def store_contents_advice(self, comment: XComment):
        print(f"Storing contents advice: {comment}")
        self.storage.append(comment)

    def store_posting_advice(self, comment: XComment):
        print(f"Storing posting advice: {comment}")
        self.storage.append(comment)

    def store_wallet_address(self, comment: XComment):
        print(f"Storing wallet address: {comment}")
        self.storage.append(comment)

    def show_all_comments(self) -> None:
        for comment in self.storage:
            print(comment)


if __name__ == "__main__":
    dispatcher = XCommentDispatcher(adviser_repository=DummyAdviserRepository())
    dispatcher.store_comment_in_db(XComment(user="user", text="Your content is great!"))
    dispatcher.store_comment_in_db(XComment(user="user", text="I dont like your monochrome style!"))
    dispatcher.store_comment_in_db(XComment(user="user", text="My wallet address is 0x1234567890"))
    dispatcher.adviser_repository.show_all_comments()
