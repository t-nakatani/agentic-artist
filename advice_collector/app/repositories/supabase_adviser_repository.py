from supabase import Client

from app.objects.wallet_address import WalletAddress
from app.objects.x_comment import XComment
from app.repositories.i_adviser_repository import IAdviserRepository


class SupabaseAdviserRepository(IAdviserRepository):
    def __init__(self, supabase_client: Client) -> None:
        self.supabase: Client = supabase_client

    def store_contents_advice(self, comment: XComment) -> None:
        data = {
            "user_id": comment.user_id,
            "content": comment.text,
        }
        self.supabase.table("contents_advices").insert(data).execute()

    def store_posting_advice(self, comment: XComment) -> None:
        data = {
            "user_id": comment.user_id,
            "content": comment.text,
        }
        self.supabase.table("posting_advices").insert(data).execute()

    def store_wallet_address(self, user_id: str, wallet_address: WalletAddress) -> None:
        data = {
            "user_id": user_id,
            "address": wallet_address.address,
        }
        self.supabase.table("wallet_addresses").insert(data).execute()
