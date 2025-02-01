from pathlib import Path

from pydantic import BaseModel

from app.agents.agent_factory import AgentFactory
from app.agents.prompt_organizer import prompt_organizer_agent
from app.image_generation_prompt import ImageGenerationPrompt


class ArtistPersonality(BaseModel):
    name: str
    age: int
    gender: str


# ------------------------------ agent definition ------------------------------


def fetch_advices(prompt: str) -> list[str]:
    """fetch advice comments from adviser-db"""
    # TODO: 仮実装
    return ["アドバイス1", "アドバイス2", "アドバイス3"]


def create_image(ImageGenerationPrompt: ImageGenerationPrompt) -> Path:
    """create an image by using prompt"""
    # TODO: Midjourneyの画像生成機能と繋げる
    # TODO: multiple generation and select the best one
    print(f"create image with prompt: {ImageGenerationPrompt.format()}")
    return Path("path/to/image.png")


async def generate_structured_prompt(prompt: str) -> ImageGenerationPrompt:
    """
    generate a structured image-generation prompt to improve the quality of prompt
    """
    return await prompt_organizer_agent.run(prompt)


artist_agent_system_prompt = """
    You are an artist agent. You are given a prompt and you need to create an image.
    1. Organize the prompt by creating a structured image-generation prompt.
    2. Fetch advice comments from adviser-db and mix them into prompt.
    3. Create an image by using the structured image-generation prompt.
"""

artist_agent = AgentFactory.create_agent(
    name="artist",
    system_prompt=artist_agent_system_prompt,
    tools=[generate_structured_prompt, fetch_advices, create_image],
    result_type=Path,
)

# ------------------------------ export ------------------------------


async def run_artist_agent(runtime_prompt: str) -> Path:
    """
    run agent to create a new image
    Args:
        runtime_prompt: str
    Returns:
        saved_image_path: Path
    """
    result = await artist_agent.run(
        runtime_prompt,
        result_type=Path,
    )
    return result.data
