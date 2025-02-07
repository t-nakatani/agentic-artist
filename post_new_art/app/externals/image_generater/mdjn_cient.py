import base64
import os
import time
from pathlib import Path

from openai import OpenAI
import requests

from app.externals.image_generater.i_image_generate_client import I_ImageGenerateClient


class MdjnClient(I_ImageGenerateClient):
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
        url = os.getenv("MDJN_SERVER_ENDPOINT", "http://localhost:3030/generate")
        payload = {"prompt": prompt}
        response = requests.post(url, json=payload)
        img_url = response.json()["img_url"]
        
        # Download image from Midjourney CDN
        img_response = requests.get(img_url)
        img_response.raise_for_status()
        
        # Save image with timestamp
        timestamp = int(time.time())
        saved_path = self.save_dir / f"midjourney_{timestamp}.png"
        
        with open(saved_path, "wb") as f:
            f.write(img_response.content)
        
        return saved_path
