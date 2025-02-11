from pydantic import BaseModel


class XPostData(BaseModel):
    text: str
    media_paths: list[str]
