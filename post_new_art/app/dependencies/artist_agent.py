from app.agents.agent_factory import AgentFactory
from app.agents.agent_persona import Personality
from app.agents.persona.artist import Artist
from app.config import supabase_config
from app.externals.datastore.adviser_fetcher import AdviserFetcher
from app.externals.image_generater.dalle3_client import Dalle3Client
from openai import OpenAI
from pydantic_ai import Agent
from supabase import create_client


def artist_agent_deps(prompt_organizer_agent: Agent):
    openai_client = OpenAI()
    dalle3_client = Dalle3Client(openai_client=openai_client)
    supabase = create_client(supabase_url=supabase_config.supabase_url, supabase_key=supabase_config.supabase_key)
    adviser_fetcher = AdviserFetcher(supabase=supabase)
    personality = Personality(name="picasso")  # TODO: ここにpersonalityを渡す
    artist = Artist(
        personality=personality,
        prompt_organizer_agent=prompt_organizer_agent,
        image_generate_client=dalle3_client,
        adviser_fetcher=adviser_fetcher,
    )
    artist_agent = AgentFactory.create_from(artist)
    return artist_agent
