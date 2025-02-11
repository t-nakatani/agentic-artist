import asyncio

from fastapi import FastAPI
from pydantic import BaseModel

from main import generate_new_art

app = FastAPI()


class GenerateArtRequest(BaseModel):
    prompt: str


@app.get("/")
async def health():
    return {"status": "ok"}


@app.post("/generate-art")
async def generate_art(request: GenerateArtRequest):
    asyncio.create_task(generate_new_art(request.prompt))
    return {"status": "accepted", "message": "generate-art request accepted"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
