from supabase import create_client

from app.config import supabase_config
from app.repositories.supabase_adviser_repository import SupabaseAdviserRepository
from app.objects.x_comment import XComment
from app.x_comment_dispatcher import XCommentDispatcher


def deps():
    supabase_client = create_client(supabase_config.supabase_url, supabase_config.supabase_key)
    adviser_repository = SupabaseAdviserRepository(supabase_client)
    return XCommentDispatcher(adviser_repository=adviser_repository)


if __name__ == "__main__":
    dispatcher = deps()
    dispatcher.store_comment_in_db(XComment(user_id="example_user_id", text="Your content is great!"))
    dispatcher.store_comment_in_db(XComment(user_id="example_user_id", text="I dont like your monochrome style!"))
    dispatcher.store_comment_in_db(XComment(user_id="example_user_id", text="My wallet address is 0x1234567890"))
    dispatcher.adviser_repository.show_all_comments()
