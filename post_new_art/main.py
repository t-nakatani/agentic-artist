import asyncio

from app.agents.agent_factory import AgentFactory
from app.agents.persona.orchesrator import Orchestrator
from app.agents.persona.prompt_organizer import PromptOrganizer
from app.dependencies.artist_agent import artist_agent_deps
from app.dependencies.sns_marketer_agent import sns_marketer_agent_deps

# def pinata_deps():
#     return PinataClient(api_key=pinata_config.api_key, api_secret=pinata_config.api_secret)


async def main():
    prompt_organizer = PromptOrganizer()
    prompt_organizer_agent = AgentFactory.create_from(prompt_organizer)
    artist_agent = artist_agent_deps(prompt_organizer_agent)
    sns_marketer_agent = sns_marketer_agent_deps()

    orchestrator = Orchestrator(artist_agent, sns_marketer_agent)
    orchestrator_agent = AgentFactory.create_from(orchestrator)

    result = await orchestrator_agent.run("generate a beautiful image of a cat and post it to X(Twitter)")
    print(result.data)


if __name__ == "__main__":
    asyncio.run(main())
