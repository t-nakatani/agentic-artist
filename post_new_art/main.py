from app.agents.agent_factory import AgentFactory
from app.agents.agent_persona import Personality
from app.agents.persona.artist import Artist
from app.agents.persona.prompt_organizer import PromptOrganizer
from app.config import pinata_config
from app.externals.image_generater.dalle3_client import Dalle3Client
from app.externals.ipfs.pinata_client import PinataClient
from openai import OpenAI


def artist_agent_deps(prompt_organizer: PromptOrganizer):
    openai_client = OpenAI()
    dalle3_client = Dalle3Client(openai_client=openai_client)
    personality = Personality("example")
    artist = Artist(
        personality=personality,
        prompt_organizer_agent=prompt_organizer,
        image_generate_client=dalle3_client,
    )
    artist_agent = AgentFactory.create_from(artist)
    return artist_agent


def pinata_deps():
    return PinataClient(api_key=pinata_config.api_key, api_secret=pinata_config.api_secret)


def main():
    pass


if __name__ == "__main__":
    main()
