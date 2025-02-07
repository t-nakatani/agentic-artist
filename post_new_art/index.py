from fastapi import FastAPI
from pydantic import BaseModel

from  .main import run

app = FastAPI()

class GenerateArtRequest(BaseModel):
    prompt: str

@app.post("/generate-art")
async def generate_art(request: GenerateArtRequest):
    result = await run(request.prompt)
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)