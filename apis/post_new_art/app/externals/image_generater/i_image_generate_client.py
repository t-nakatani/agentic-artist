from abc import ABC, abstractmethod
from pathlib import Path


class I_ImageGenerateClient(ABC):
    @abstractmethod
    def generate_image(self, prompt: str) -> Path:
        """
        generate an image by using prompt
        Args:
            prompt: str
        Returns:
            saved_image_path: Path
        """
        pass
