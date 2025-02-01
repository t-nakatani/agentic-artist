import asyncio
from pathlib import Path

from openai import OpenAI

from app.agents.artist_agent import run_artist_agent
from app.externals.image_generater.dalle3_client import Dalle3Client


async def run_artist() -> Path:
    sentense = [
        "Visualize a surreal blue canvas adorned with translucent clouds.",
        "The varying shades of blue merge into a rhythmic, enchanting display, evoking a sense of mystery and wonder.",
    ]

    openai_client = OpenAI()
    return await run_artist_agent(" ".join(sentense), Dalle3Client(openai_client=openai_client))


if __name__ == "__main__":
    asyncio.run(run_artist())
