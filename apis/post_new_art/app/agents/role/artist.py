from pathlib import Path

from loguru import logger
from pydantic_ai import Agent, RunContext

from app.agents.agent_persona import AgentPersona, Personality
from app.externals.datastore.adviser_fetcher import Advice
from app.externals.image_generater.i_image_generate_client import I_ImageGenerateClient
from app.image_generation_prompt import ImageGenerationPrompt


class Artist(AgentPersona):
    """
    Artist agent
    """

    role = """
        You are an artist agent. You are given a prompt and you need to create an image.
        1. Organize the prompt by creating a structured image-generation prompt.
        2. Create an image by using the structured image-generation prompt.
    """

    result_type = Path
    deps = Advice

    def __init__(
        self,
        personality: Personality,
        prompt_organizer_agent: Agent,
        image_generate_client: I_ImageGenerateClient,
    ):
        self.personality = personality
        self.prompt_organizer_agent = prompt_organizer_agent
        self.image_generate_client = image_generate_client

    async def generate_structured_prompt(self, ctx: RunContext[Advice], prompt: str) -> ImageGenerationPrompt:
        """
        generate a structured image-generation prompt to improve the quality of prompt
        """
        logger.info("generating structured image-generation prompt")
        logger.info(f"advice from audience: {ctx.deps.content} by {ctx.deps.user_id}")
        prompt = f"{prompt}\nmost important advice from audience: {ctx.deps.content}"
        return await self.prompt_organizer_agent.run(prompt)

    def create_image(self, ImageGenerationPrompt: ImageGenerationPrompt) -> Path:
        """create an image by using prompt"""
        # TODO: multiple generation and select the best one
        logger.info(f"create image with prompt:\n {ImageGenerationPrompt.format()}")
        return self.image_generate_client.generate_image(ImageGenerationPrompt.format())
