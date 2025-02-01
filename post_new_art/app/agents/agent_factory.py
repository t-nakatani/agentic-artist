from typing import Callable, Optional, Type, TypeVar

from pydantic_ai.agent import Agent

T = TypeVar("T")


class AgentFactory:
    """エージェントの初期化を管理するファクトリークラス"""

    @staticmethod
    def create_agent(
        name: str,
        system_prompt: str,
        model: str = "openai:gpt-4o-mini",
        result_type: Optional[Type[T]] = None,
        tools: Optional[list[Callable]] = None,
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
            "system_prompt": system_prompt,
        }

        if result_type:
            agent_config["result_type"] = result_type

        if tools:
            agent_config["tools"] = tools

        return Agent(**agent_config)
