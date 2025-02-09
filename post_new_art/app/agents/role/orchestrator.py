from pathlib import Path

from loguru import logger
from pydantic import BaseModel
from pydantic_ai.agent import Agent

from app.agents.agent_persona import AgentPersona
from app.externals.datastore.adviser_fetcher import Advice, AdviserFetcher


class OrchestrationResult(BaseModel):
    x_post_id: str
    nft_address: str
    allocation_update_tx_hash: str


class Orchestrator(AgentPersona):
    role = """
        You are an orchestrator agent. You are given following agents and you need to orchestrate them.
        - adviser_fetcher
        - artist
        - sns_marketer
    """
    result_type = None

    def __init__(self, adviser_fetcher: AdviserFetcher, artist_agent: Agent, sns_marketer_agent: Agent):
        self.adviser_fetcher = adviser_fetcher
        self.artist_agent = artist_agent
        self.sns_marketer_agent = sns_marketer_agent

    def fetch_art_content_advices_from_audience(self) -> list[Advice]:
        """fetch advice comments from adviser-db"""
        logger.info("fetching art content advices from audience")
        return self.adviser_fetcher.fetch_all_content_advices()

    async def request_image_generation(self, prompt: str, most_important_advice: Advice) -> Path:
        """request image generation from artist agent"""
        return await self.artist_agent.run(prompt, deps=most_important_advice)

    async def request_post_to_sns(self, image_path: Path, prompt: str) -> str:
        """request post to sns from sns_marketer agent"""
        logger.info(f"image_path: {image_path}")
        return await self.sns_marketer_agent.run(prompt, deps=image_path)

    # async def create_nft(self, image_path: Path) -> str:
    #     return await self.nft_client.create_nft(image_path)
