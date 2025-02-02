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
