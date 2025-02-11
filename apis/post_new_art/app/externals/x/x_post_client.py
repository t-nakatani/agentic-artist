import tweepy

from app.externals.x.x_post_data import XPostData


class XPostClient:
    def __init__(self, client: tweepy.Client, authed_api: tweepy.API):
        self.authed_api = authed_api
        self.client = client

    def post_new_art(self, post_data: XPostData):
        # upload media
        media_ids = []
        for media_path in post_data.media_paths:
            media = self.authed_api.media_upload(filename=media_path)
            media_ids.append(media.media_id)

        # post tweet
        self.client.create_tweet(text=post_data.text, media_ids=media_ids if media_ids else None)
