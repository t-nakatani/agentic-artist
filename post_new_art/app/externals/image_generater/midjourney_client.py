import os
import time
from pathlib import Path

import requests

from app.externals.image_generater.i_image_generate_client import I_ImageGenerateClient
from app.externals.image_generater.image_downloader import ImageDownloader


class MidjourneyClient(I_ImageGenerateClient):
    def __init__(self, image_downloader: ImageDownloader, save_dir: str = "./images"):
        self.image_downloader = image_downloader
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
        timestamp = int(time.time())
        output_path = self.save_dir / f"midjourney_{timestamp}.png"
        self.image_downloader.download(img_url, output_path)

        return output_path
