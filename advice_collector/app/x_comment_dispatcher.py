from loguru import logger
from pydantic_ai.agent import Agent

from app.objects.wallet_address import WalletAddress
from app.objects.x_comment import XComment, XCommetType
from app.repositories.i_adviser_repository import IAdviserRepository


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

    def handle(self, comment: XComment) -> None:
        comment_type = self._dispatch_by_agent(comment)

        self._store_comment(comment, comment_type)

        # TODO: judge if the comment is useful and uddate allocation here

    def _dispatch_by_agent(self, comment: XComment) -> XCommetType:
        result = self.dispatch_agent.run_sync(comment.text)
        return result.data

    def _store_comment(self, comment: XComment, comment_type: XCommetType) -> None:
        if comment_type.is_content_advice():
            self.adviser_repository.store_contents_advice(comment)

        elif comment_type == XCommetType.POSTING_ADVICE:
            self.adviser_repository.store_posting_advice(comment)

        elif comment_type == XCommetType.REGISTER_WALLET_ADDRESS:
            result = self.wallet_address_extract_agent.run_sync(comment.text)
            wallet_address: WalletAddress = result.data

            self.adviser_repository.store_wallet_address(comment.user_id, wallet_address)
        else:
            logger.error(f"dispatch error: {comment.text}")
            raise ValueError(f"dispatch error: {comment.text}")
