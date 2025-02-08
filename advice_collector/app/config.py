from pydantic import Field
from pydantic_settings import BaseSettings


class SupabaseConfig(BaseSettings):
    supabase_url: str = Field(..., env="SUPABASE_URL")
    supabase_key: str = Field(..., env="SUPABASE_KEY")


class ChainSettings(BaseSettings):
    rpc_url: str = Field(..., env="RPC_URL")


class WalletSettings(BaseSettings):
    private_key: str = Field(..., env="PRIVATE_KEY")


supabase_config = SupabaseConfig()
chain_settings = ChainSettings()
wallet_settings = WalletSettings()
