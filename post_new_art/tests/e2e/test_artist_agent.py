import pytest
from openai import OpenAI
from supabase import create_client

from app.agents.agent_factory import AgentFactory
from app.agents.role.artist import Artist, Personality
from app.agents.role.prompt_organizer import PromptOrganizer
from app.config import supabase_config
from app.externals.datastore.adviser_fetcher import AdviserFetcher
from app.externals.image_generater.dalle3_client import Dalle3Client


@pytest.fixture
def image_generate_client():
    openai_client = OpenAI()
    return Dalle3Client(openai_client=openai_client)


@pytest.fixture
def prompt_organizer_agent():
    return AgentFactory.create_from(PromptOrganizer())


@pytest.fixture
def supabase_adviser_fetcher():
    supabase = create_client(supabase_config.supabase_url, supabase_config.supabase_key)
    return AdviserFetcher(supabase=supabase)


@pytest.mark.asyncio
async def test_artist_agent(prompt_organizer_agent, image_generate_client, supabase_adviser_fetcher):
    personality = Personality(name="Picasso")
    agent = AgentFactory.create_from(
        Artist(
            personality=personality,
            prompt_organizer_agent=prompt_organizer_agent,
            image_generate_client=image_generate_client,
            adviser_fetcher=supabase_adviser_fetcher,
        )
    )
    runtime_prompts = ["Visualize a surreal blue canvas adorned with translucent clouds."]

    result = await agent.run(" ".join(runtime_prompts))

    assert isinstance(result.data, Artist.result_type)
