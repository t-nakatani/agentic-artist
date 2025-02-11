from pydantic import Field
from pydantic_settings import BaseSettings


class PinataConfig(BaseSettings):
    pinata_api_key: str = Field(..., json_schema_extra={"env": "PINATA_API_KEY"})
    pinata_api_secret: str = Field(..., json_schema_extra={"env": "PINATA_API_SECRET"})


class SupabaseConfig(BaseSettings):
    supabase_url: str = Field(..., json_schema_extra={"env": "SUPABASE_URL"})
    supabase_key: str = Field(..., json_schema_extra={"env": "SUPABASE_KEY"})


class XConfig(BaseSettings):
    x_bearer_token: str = Field(..., json_schema_extra={"env": "X_BEARER_TOKEN"})
    x_api_key: str = Field(..., json_schema_extra={"env": "X_API_KEY"})
    x_api_secret: str = Field(..., json_schema_extra={"env": "X_API_SECRET"})
    x_access_token: str = Field(..., json_schema_extra={"env": "X_ACCESS_TOKEN"})
    x_access_secret: str = Field(..., json_schema_extra={"env": "X_ACCESS_SECRET"})


class MidjourneyConfig(BaseSettings):
    mdjn_server_endpoint: str = Field(..., json_schema_extra={"env": "MDJN_SERVER_ENDPOINT"})


pinata_config = PinataConfig()
supabase_config = SupabaseConfig()
x_config = XConfig()
midjourney_config = MidjourneyConfig()
