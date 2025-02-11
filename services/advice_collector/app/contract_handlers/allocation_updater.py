from web3 import Web3

from app.contract_handlers.config.allocation_storage import contract_abi, contract_address
from app.contract_handlers.smart_contract_handler import SmartContractHandler, with_signer


class AllocationUpdater(SmartContractHandler):
    def __init__(self, provider: Web3):
        super().__init__(provider, contract_address, contract_abi)

    @with_signer()
    def add_allocation(self, user_address: str, allocation_amount: int = 1):
        return self.contract.functions.addAllocation(user_address, allocation_amount)
