from pathlib import Path

from app.agents.agent_persona import AgentPersona
from app.externals.x.x_post_client import XPostClient
from app.externals.x.x_post_data import XPostData
from pydantic_ai.agent import RunContext
from loguru import logger


class SnsMarketer(AgentPersona):
    role = """
    You are a SNS marketer agent. You are given a file path and you need to post it to SNS.
    Posting text is important. You need to create a posting text that is attractive and engaging.
    Keep the posting text very short and concise.
    """
    deps = Path
    result_type = None

    def __init__(self, x_post_client: XPostClient):
        self.x_post_client = x_post_client

    def post_new_art_to_x(self, ctx_with_file_path: RunContext[Path], post_text: str) -> str:
        """Post new arts to X."""
        post_data = XPostData(
            text=post_text,
            media_paths=[str(ctx_with_file_path.deps)],
        )
        logger.info(f"posting to X: {post_data.text}")
        return self.x_post_client.post_new_art(post_data)
