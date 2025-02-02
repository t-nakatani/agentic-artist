import os
from pathlib import Path

import pytest

from app.externals.ipfs.pinata_client import PinataClient


@pytest.fixture
def pinata_client():
    api_key = os.getenv("PINATA_API_KEY", "")
    api_secret = os.getenv("PINATA_API_SECRET", "")
    if not api_key or not api_secret:
        raise ValueError("PINATA_API_KEY と PINATA_API_SECRET を環境変数に設定してください")
    return PinataClient(api_key=api_key, api_secret=api_secret)


def test_pinata_client(pinata_client):
    test_image_path = Path("tests/test_data/example.png")

    ipfs_hash = pinata_client.upload_file(test_image_path)

    assert ipfs_hash is not None
