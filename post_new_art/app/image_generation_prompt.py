from enum import Enum

from pydantic import BaseModel


class Style(Enum):
    POP_ART = "pop_art"
    OTHER = "other"


class ImageGenerationPrompt(BaseModel):
    theme: str
    style: Style
    subject: str
    background: str
    color: str
    size: str

    def format(self) -> str:
        # [仮実装] TODO: roo-clineを参考にして、構造データであることを活かす
        return f"{self.theme} {self.style} {self.subject} {self.background} {self.color} {self.size}"
