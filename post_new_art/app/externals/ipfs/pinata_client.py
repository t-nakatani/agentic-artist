from pathlib import Path

import requests

from app.externals.ipfs.i_ipfs_client import I_IPFSClient


class PinataClient(I_IPFSClient):
    endpoint = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    def __init__(self, api_key: str, api_secret: str):
        """
        constructor
        Args:
            api_key: Pinata API key
            api_secret: Pinata API secret
        """
        self.api_key = api_key
        self.api_secret = api_secret

    def upload_file(self, file_path: Path) -> str:
        """
        upload file to ipfs and return hash
        Args:
            file_path: Path
        Returns:
            str: IPFS hash
        """

        with open(file_path, "rb") as file:
            files = {"file": (str(file_path), file)}
            headers = {"pinata_api_key": self.api_key, "pinata_secret_api_key": self.api_secret}
            response = requests.post(self.endpoint, headers=headers, files=files)

        if response.status_code == 200:
            json_response = response.json()
            ipfs_hash = json_response.get("IpfsHash")
            if ipfs_hash:
                return ipfs_hash
            raise Exception("レスポンスに IpfsHash が含まれていません。")
        raise Exception(f"アップロードに失敗しました: {response.status_code} {response.text}")
