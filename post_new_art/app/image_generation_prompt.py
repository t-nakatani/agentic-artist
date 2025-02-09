from enum import Enum

from pydantic import BaseModel
from pydantic_ai.format_as_xml import format_as_xml


class Style(Enum):
    POP_ART = "pop_art"
    ABSTRACT = "abstract"
    ANIME = "anime"
    OTAKU = "otaku"
    OTHER = "other"


class ImageGenerationPrompt(BaseModel):
    theme: str
    detailed_description: str
    style: Style
    subject: str
    background: str
    main_color: str

    def format(self) -> str:
        dict_prompt = self.model_dump()
        dict_prompt["style"] = dict_prompt["style"].value
        return format_as_xml(dict_prompt, root_tag="image_generation_prompt")
