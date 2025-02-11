from abc import ABC, abstractmethod
from pathlib import Path


class I_IPFSClient(ABC):
    @abstractmethod
    def upload_file(self, file_path: Path) -> str:
        """
        upload file to ipfs and return hash
        Args:
            file_path: Path
        Returns:
            str: IPFS hash
        """
        pass
