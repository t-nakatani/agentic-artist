from enum import Enum

from pydantic import BaseModel


class Style(Enum):
    POP_ART = "pop_art"
    OTHER = "other"


class ImageGenerationPrompt(BaseModel):
    theme: str
    detailed_description: str
    style: Style
    subject: str
    background: str
    main_color: str

    def format(self) -> str:
        # [仮実装] TODO: roo-clineを参考にして、構造データであることを活かす
        return (
            f"{self.theme} {self.style} {self.subject} {self.background} {self.main_color} {self.detailed_description}"
        )
