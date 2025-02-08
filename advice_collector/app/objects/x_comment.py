from enum import Enum

from pydantic import BaseModel


class XComment(BaseModel):
    user_id: str  # TODO
    text: str


class XCommetType(Enum):
    CONTENT_POSITIVE_ADVICE = "content_positive_advice"
    CONTENT_NEGATIVE_ADVICE = "content_negative_advice"
    POSTING_ADVICE = "posting_advice"
    REGISTER_WALLET_ADDRESS = "register_wallet_address"
    OTHER = "other"

    def is_content_advice(self) -> bool:
        return self in [self.CONTENT_POSITIVE_ADVICE, self.CONTENT_NEGATIVE_ADVICE]
