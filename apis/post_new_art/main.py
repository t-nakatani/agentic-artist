import asyncio

from supabase import create_client

from app.agents.agent_factory import AgentFactory
from app.agents.dependencies.artist_agent import artist_agent_deps
from app.agents.dependencies.sns_marketer_agent import sns_marketer_agent_deps
from app.agents.role.orchestrator import Orchestrator
from app.agents.role.prompt_organizer import PromptOrganizer
from app.config import supabase_config
from app.externals.datastore.adviser_fetcher import AdviserFetcher

# def pinata_deps():
#     return PinataClient(api_key=pinata_config.api_key, api_secret=pinata_config.api_secret)


# async def run(prompt: str):
#     prompt_organizer = PromptOrganizer()
#     prompt_organizer_agent = AgentFactory.create_from(prompt_organizer)
#     artist_agent = artist_agent_deps(prompt_organizer_agent)
#     sns_marketer_agent = sns_marketer_agent_deps()

#     orchestrator = Orchestrator(artist_agent, sns_marketer_agent)
#     orchestrator_agent = AgentFactory.create_from(orchestrator)
#     result = await orchestrator_agent.run(prompt)
#     return result.data


async def generate_new_art(dummy_prompt: str):
    supabase = create_client(supabase_url=supabase_config.supabase_url, supabase_key=supabase_config.supabase_key)
    adviser_fetcher = AdviserFetcher(supabase=supabase)
    prompt_organizer = PromptOrganizer()
    prompt_organizer_agent = AgentFactory.create_from(prompt_organizer)
    artist_agent = artist_agent_deps(prompt_organizer_agent)
    sns_marketer_agent = sns_marketer_agent_deps()

    orchestrator = Orchestrator(adviser_fetcher, artist_agent, sns_marketer_agent)
    orchestrator_agent = AgentFactory.create_from(orchestrator)

    main_runtime_prompt = """
        Think your own prompt to generate profile images that resonate with degens and post it to X(Twitter)
    """
    example_image_generation_prompt = """
    Design a dynamic character portrait of a cybernetic samurai clad in digital armor adorned with futuristic emblems.
    Use a cool blue and silver palette with neon highlights against a backdrop of a high-tech cityscape, evoking an aura of elite sophistication.
    """
    await orchestrator_agent.run(
        f"{main_runtime_prompt=}\n{example_image_generation_prompt=}",
    )


if __name__ == "__main__":
    asyncio.run(generate_new_art())
