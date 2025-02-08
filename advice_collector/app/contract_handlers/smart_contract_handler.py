from functools import wraps

from web3 import Web3

from app.config import wallet_settings


def with_signer(gas_limit: int = 2_000_000, private_key: str = wallet_settings.private_key):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            account_address = self.provider.eth.account.from_key(private_key).address
            tx_function = func(self, *args, **kwargs)
            tx_params = {
                "from": account_address,
                "gas": gas_limit,
                "gasPrice": 100_000,
                "nonce": self.provider.eth.get_transaction_count(account_address),
                "chainId": self.provider.eth.chain_id,
            }
            tx = tx_function.build_transaction(tx_params)
            signed_tx = self.provider.eth.account.sign_transaction(tx, private_key=private_key)
            return self.provider.eth.send_raw_transaction(signed_tx.raw_transaction)

        return wrapper

    return decorator


class SmartContractHandler:
    def __init__(self, provider: Web3, address: str, abi: list):
        self.provider = provider
        self.contract = self.provider.eth.contract(address=address, abi=abi)
