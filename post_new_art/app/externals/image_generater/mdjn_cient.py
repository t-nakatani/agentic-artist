import os
import time
from pathlib import Path

from openai import OpenAI
import requests

from app.externals.image_generater.i_image_generate_client import I_ImageGenerateClient

STORAGE_BASE_URL = "https://lipbpiidmsjeuqemorzv.supabase.co/storage/v1/object/public/images/mdjn/"
MIDJOURNEY_BASE_URL = "https://cdn.midjourney.com/"
MIDJOURNEY_SUFFIX = "/0_0.png"

def convert_midjourney_to_storage_url(midjourney_url: str) -> str:
    if not midjourney_url.startswith(MIDJOURNEY_BASE_URL):
        raise ValueError("無効なMidjourney URLです")
    image_id = midjourney_url[len(MIDJOURNEY_BASE_URL):len(midjourney_url)-len(MIDJOURNEY_SUFFIX)]
    return STORAGE_BASE_URL + image_id

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
        storage_url = convert_midjourney_to_storage_url(img_url)
        saved_path = self.save_dir / storage_url
        response = requests.get(storage_url, stream=True)
        with open(saved_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        
        return saved_path



