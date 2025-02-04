import tweepy
from app.agents.agent_factory import AgentFactory
from app.agents.persona.sns_marketer import SnsMarketer
from app.config import x_settings
from app.externals.x.x_post_client import XPostClient


def sns_marketer_agent_deps():
    client = tweepy.Client(
        bearer_token=x_settings.x_bearer_token,
        consumer_key=x_settings.x_api_key,
        consumer_secret=x_settings.x_api_secret,
        access_token=x_settings.x_access_token,
        access_token_secret=x_settings.x_access_secret,
    )
    auth = tweepy.OAuthHandler(x_settings.x_api_key, x_settings.x_api_secret)
    auth.set_access_token(x_settings.x_access_token, x_settings.x_access_secret)
    api = tweepy.API(auth)

    x_post_client = XPostClient(client=client, authed_api=api)
    sns_marketer = SnsMarketer(x_post_client=x_post_client)
    sns_marketer_agent = AgentFactory.create_from(sns_marketer)
    return sns_marketer_agent
