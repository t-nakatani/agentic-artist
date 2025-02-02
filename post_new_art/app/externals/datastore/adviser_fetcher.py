from supabase import Client


class AdviserFetcher:
    def __init__(self, supabase: Client):
        self.supabase = supabase

    def fetch_all_content_advises(self) -> list[str]:
        response = self.supabase.table("contents_advices").select("*").execute()
        return [content["content"] for content in response.data]

    def fetch_all_posting_advises(self) -> list[str]:
        response = self.supabase.table("posting_advices").select("*").execute()
        return [posting["content"] for posting in response.data]

    def fetch_all_wallet_addresses(self) -> list[str]:
        response = self.supabase.table("wallet_addresses").select("*").execute()
        return [wallet["address"] for wallet in response.data]
