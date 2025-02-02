from pydantic import Field
from pydantic_settings import BaseSettings


class SupabaseConfig(BaseSettings):
    supabase_url: str = Field(..., env="SUPABASE_URL")
    supabase_key: str = Field(..., env="SUPABASE_KEY")


supabase_config = SupabaseConfig()
