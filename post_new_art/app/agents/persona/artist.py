from pathlib import Path

from pydantic_ai import Agent

from app.agents.agent_persona import AgentPersona, Personality
from app.externals.image_generater.i_image_generate_client import I_ImageGenerateClient
from app.image_generation_prompt import ImageGenerationPrompt


class Artist(AgentPersona):
    """
    Artist agent
    """

    role = """
        You are an artist agent. You are given a prompt and you need to create an image.
        1. Organize the prompt by creating a structured image-generation prompt.
        2. Fetch advice comments from adviser-db and mix them into prompt.
        3. Create an image by using the structured image-generation prompt.
    """

    result_type = Path

    def __init__(
        self, personality: Personality, prompt_organizer_agent: Agent, image_generate_client: I_ImageGenerateClient
    ):
        self.personality = personality
        self.prompt_organizer_agent = prompt_organizer_agent
        self.image_generate_client = image_generate_client

    def create_image(self, ImageGenerationPrompt: ImageGenerationPrompt) -> Path:
        """create an image by using prompt"""
        # TODO: Midjourneyの画像生成機能と繋げる
        # TODO: multiple generation and select the best one
        print(f"create image with prompt: {ImageGenerationPrompt.format()}")
        return self.image_generate_client.generate_image(ImageGenerationPrompt.format())

    def fetch_advices(self, prompt: str) -> list[str]:
        """fetch advice comments from adviser-db"""
        # TODO: 仮実装
        return ["アドバイス1", "アドバイス2", "アドバイス3"]

    async def generate_structured_prompt(self, prompt: str) -> ImageGenerationPrompt:
        """
        generate a structured image-generation prompt to improve the quality of prompt
        """
        return await self.prompt_organizer_agent.run(prompt)
