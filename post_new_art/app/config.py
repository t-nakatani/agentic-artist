from pydantic import Field
from pydantic_settings import BaseSettings


class PinataConfig(BaseSettings):
    pinata_api_key: str = Field(..., env="PINATA_API_KEY")
    pinata_secret_api_key: str = Field(..., env="PINATA_API_SECRET")


pinata_config = PinataConfig()
