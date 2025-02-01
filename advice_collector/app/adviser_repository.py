from abc import ABC, abstractmethod

from app.wallet_address import WalletAddress
from app.x_comment import XComment


class IAdviserRepository(ABC):
    @abstractmethod
    def store_contents_advice(self, comment: XComment):
        pass

    @abstractmethod
    def store_posting_advice(self, comment: XComment):
        pass

    @abstractmethod
    def store_wallet_address(self, wallet_address: WalletAddress):
        pass
