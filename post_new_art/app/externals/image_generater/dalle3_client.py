import base64
import time
from pathlib import Path

from openai import OpenAI

from app.externals.image_generater.i_image_generate_client import IImageGenerateClient


class Dalle3Client(IImageGenerateClient):
    def __init__(self, openai_client: OpenAI, save_dir: str = "./images"):
        self.client = openai_client
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)

    def generate_image(self, prompt: str) -> Path:
        """
        IImageGenerateClientインターフェースの実装
        画像を生成して保存する

        Args:
            prompt: 生成プロンプト

        Returns:
            生成された画像のパス
        """
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="b64_json",
            quality="standard",
            style="natural",
        )
        timestamp = int(time.time())

        saved_path = self.save_dir / f"dalle3_{timestamp}.png"
        with open(saved_path, "wb") as f:
            f.write(base64.b64decode(response.data[0].b64_json))

        return saved_path
