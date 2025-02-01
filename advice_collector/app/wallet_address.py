from pydantic import BaseModel, field_validator


class WalletAddress(BaseModel):
    address: str

    # TODO: バリデーションを強化
    @field_validator("address", mode="before")
    def validate_address(cls, value: str) -> str:
        if not value.startswith("0x"):
            raise ValueError("Wallet address must start with 0x")
        return value
