import asyncio
from pathlib import Path

from app.agents.artist_agent import run_artist_agent


async def run_artist() -> Path:
    sentense = [
        "Visualize a surreal blue canvas adorned with translucent clouds.",
        "The varying shades of blue merge into a rhythmic, enchanting display, evoking a sense of mystery and wonder.",
    ]

    return await run_artist_agent(" ".join(sentense))


if __name__ == "__main__":
    asyncio.run(run_artist())
