from pathlib import Path

from app.agents.agent_persona import AgentPersona
from pydantic import BaseModel
from pydantic_ai.agent import Agent


class OrchestrationResult(BaseModel):
    x_post_id: str
    nft_address: str
    allocation_update_tx_hash: str


class Orchestrator(AgentPersona):
    role = """
        You are an orchestrator agent. You are given following agents and you need to orchestrate them.
        - artist
    """
    result_type = None

    def __init__(self, artist_agent: Agent, sns_marketer_agent: Agent):
        self.artist_agent = artist_agent
        self.sns_marketer_agent = sns_marketer_agent

    async def request_image_generation(self, prompt: str) -> Path:
        return await self.artist_agent.run(prompt)

    async def request_post_to_sns(self, image_paths: list[Path], prompt: str) -> str:
        return await self.sns_marketer_agent.run(prompt, deps=image_paths)

    # async def create_nft(self, image_path: Path) -> str:
    #     return await self.nft_client.create_nft(image_path)
