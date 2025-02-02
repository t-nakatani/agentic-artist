import pytest
from app.agents.agent_factory import AgentFactory
from app.agents.persona.artist import Artist, Personality
from app.agents.persona.prompt_organizer import PromptOrganizer
from app.externals.image_generater.dalle3_client import Dalle3Client
from openai import OpenAI


@pytest.fixture
def image_generate_client():
    openai_client = OpenAI()
    return Dalle3Client(openai_client=openai_client)


@pytest.fixture
def prompt_organizer_agent():
    return AgentFactory.create_from(PromptOrganizer())


@pytest.mark.asyncio
async def test_artist_agent(prompt_organizer_agent, image_generate_client):
    personality = Personality(name="Picasso")
    agent = AgentFactory.create_from(
        Artist(
            personality=personality,
            prompt_organizer_agent=prompt_organizer_agent,
            image_generate_client=image_generate_client,
        )
    )
    runtime_prompts = ["Visualize a surreal blue canvas adorned with translucent clouds."]

    result = await agent.run(" ".join(runtime_prompts))

    assert isinstance(result.data, Artist.result_type)
