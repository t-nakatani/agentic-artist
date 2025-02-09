from pydantic import BaseModel
from supabase import Client


class Advice(BaseModel):
    user_id: str
    content: str


class AdviserFetcher:
    def __init__(self, supabase: Client):
        self.supabase = supabase

    def fetch_all_content_advices(self) -> list[Advice]:
        response = self.supabase.table("contents_advices").select("*").execute()
        return [Advice(user_id=content["user_id"], content=content["content"]) for content in response.data]

    def fetch_all_posting_advises(self) -> list[Advice]:
        response = self.supabase.table("posting_advices").select("*").execute()
        return [Advice(user_id=posting["user_id"], content=posting["content"]) for posting in response.data]

    def fetch_all_wallet_addresses(self) -> list[str]:
        response = self.supabase.table("wallet_addresses").select("*").execute()
        return [wallet["address"] for wallet in response.data]
