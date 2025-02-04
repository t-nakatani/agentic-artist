import inspect
from typing import TypeVar

from app.agents.agent_persona import AgentPersona
from pydantic_ai.agent import Agent

T = TypeVar("T")


class AgentFactory:
    """A factory class for initializing agents"""

    @classmethod
    def create_from(
        cls,
        persona: AgentPersona,
        model: str = "openai:gpt-4o-mini",
    ) -> Agent:
        """
        create an agent from a persona

        Args:
            name: the name of the agent
            system_prompt: the system prompt
            model: the model name
            result_type: the type of the result
            tools: the list of the tools

        Returns:
            Agent: the initialized agent
        """
        agent_config = {
            "model": model,
            "system_prompt": persona.role,
        }

        agent_config["result_type"] = persona.result_type

        agent_config["tools"] = cls._extract_methods(persona)

        return Agent(**agent_config)

    @staticmethod
    def _extract_methods(instance):
        return [
            method
            for method_name, method in inspect.getmembers(instance, predicate=inspect.ismethod)
            if not method_name.startswith("_")
        ]
