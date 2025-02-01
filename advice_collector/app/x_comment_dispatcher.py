from pydantic_ai.agent import Agent

from app.adviser_repository import IAdviserRepository
from app.wallet_address import WalletAddress
from app.x_comment import XComment, XCommetType


class XCommentDispatcher:
    def __init__(self, adviser_repository: IAdviserRepository):
        self.wallet_address_extract_agent = Agent(
            model="openai:gpt-4o-mini",
            result_type=WalletAddress,
            system_prompt="You are a wallet address extractor. You extract the wallet address from the text.",
        )
        self.dispatch_agent = Agent(
            model="openai:gpt-4o-mini",
            result_type=XCommetType,
            system_prompt="You are a helpful assistant that can help with content advice for X comments.",
        )
        self.adviser_repository = adviser_repository

    def store_comment_in_db(self, comment: XComment) -> None:
        comment_type = self._dispatch_by_agent(comment)
        if comment_type in [XCommetType.CONTENT_POSITIVE_ADVICE, XCommetType.CONTENT_NEGATIVE_ADVICE]:
            self.adviser_repository.store_contents_advice(comment)
        elif comment_type == XCommetType.POSTING_ADVICE:
            self.adviser_repository.store_posting_advice(comment)
        elif comment_type == XCommetType.REGISTER_WALLET_ADDRESS:
            result = self.wallet_address_extract_agent.run_sync(comment.text)
            wallet_address: WalletAddress = result.data

            self.adviser_repository.store_wallet_address(wallet_address)

    def _dispatch_by_agent(self, comment: XComment) -> XCommetType:
        result = self.dispatch_agent.run_sync(comment.text)
        return result.data
