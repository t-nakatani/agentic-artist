from pathlib import Path

from pydantic_ai.agent import Agent

from app.agents.agent_persona import AgentPersona


class Orchestrator(AgentPersona):
    role = """
        You are an orchestrator agent. You are given following agents and you need to orchestrate them.
        - artist
    """
    result_type = None

    def __init__(self, artist_agent: Agent, image_generator_agent: Agent):
        self.artist_agent = artist_agent
        self.image_generator_agent = image_generator_agent

    async def request_image_generation(self, prompt: str) -> Path:
        return await self.artist_agent.run(prompt)
