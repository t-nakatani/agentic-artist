from pathlib import Path

from app.agents.agent_persona import AgentPersona
from app.externals.x.x_post_client import XPostClient
from app.externals.x.x_post_data import XPostData
from pydantic_ai.agent import RunContext


class SnsMarketer(AgentPersona):
    role = """
    You are a SNS marketer agent. You are given a post and you need to post it to SNS.
    """
    deps = list[Path]
    result_type = None

    def __init__(self, x_post_client: XPostClient):
        self.x_post_client = x_post_client

    def post_new_art_to_x(self, ctx_with_file_paths: RunContext[list[Path]], post_text: str) -> str:
        """Post new arts to X."""
        post_data = XPostData(
            text=post_text,
            media_paths=[str(file_path) for file_path in ctx_with_file_paths.deps],
        )
        # TODO: post_textのチューニング
        return self.x_post_client.post_new_art(post_data)
