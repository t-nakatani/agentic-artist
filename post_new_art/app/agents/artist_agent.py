from pathlib import Path

from pydantic import BaseModel
from pydantic_ai.agent import Agent, RunContext

from app.image_generation_prompt import ImageGenerationPrompt


class ArtistPersonality(BaseModel):
    name: str
    age: int
    gender: str


# ------------------------------ agent definition ------------------------------


class Deps(BaseModel):
    # adviser_db: Any
    prompt_organizer: Agent


def fetch_advices(prompt: str) -> list[str]:
    """fetch advice comments from adviser-db"""
    # TODO: 仮実装
    return ["アドバイス1", "アドバイス2", "アドバイス3"]


def create_image(prompt: str) -> Path:
    # TODO: Midjourneyの画像生成機能と繋げる
    print(f"create image with prompt: {prompt}")
    return Path("path/to/image.png")


def run_prompt_organizer(ctx: RunContext[Deps], prompt: str) -> ImageGenerationPrompt:
    return ctx.deps.prompt_organizer.run(prompt)


artist_agent_system_prompt = """
    You are an artist agent. You are given a prompt and you need to create an image.
    1. Organize the prompt by creating a structured image-generation prompt.
    2. Fetch advice comments from adviser-db and mix them into prompt.
    3. Create an image by using the structured image-generation prompt.
"""
artist_agent = Agent(
    model="openai:gpt-4o-mini",
    system_prompt=artist_agent_system_prompt,
    tools=[run_prompt_organizer, fetch_advices, create_image],
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
