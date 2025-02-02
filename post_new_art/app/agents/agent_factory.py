import inspect
from typing import Optional, Type, TypeVar

from pydantic_ai.agent import Agent

from app.agents.agent_persona import AgentPersona

T = TypeVar("T")


class AgentFactory:
    """エージェントの初期化を管理するファクトリークラス"""

    @classmethod
    def create_agent(
        cls,
        persona: AgentPersona,
        model: str = "openai:gpt-4o-mini",
        result_type: Optional[Type[T]] = None,
    ) -> Agent:
        """
        エージェントを作成する共通メソッド

        Args:
            name: エージェントの名前
            system_prompt: システムプロンプト
            model: 使用するモデル名
            result_type: 戻り値の型
            tools: 使用するツールのリスト

        Returns:
            Agent: 初期化されたエージェント
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
