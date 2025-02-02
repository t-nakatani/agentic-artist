from pydantic import Field
from pydantic_settings import BaseSettings


class PinataConfig(BaseSettings):
    pinata_api_key: str = Field(..., json_schema_extra={"env": "PINATA_API_KEY"})
    pinata_api_secret: str = Field(..., json_schema_extra={"env": "PINATA_API_SECRET"})


class SupabaseConfig(BaseSettings):
    supabase_url: str = Field(..., json_schema_extra={"env": "SUPABASE_URL"})
    supabase_key: str = Field(..., json_schema_extra={"env": "SUPABASE_KEY"})


pinata_config = PinataConfig()
supabase_config = SupabaseConfig()
