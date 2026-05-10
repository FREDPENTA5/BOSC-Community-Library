from abc import ABC, abstractmethod
import os

class StorageAdapter(ABC):
    @abstractmethod
    def read(self, path: str) -> bytes:
        pass

    @abstractmethod
    def exists(self, path: str) -> bool:
        pass

class LocalStorageAdapter(StorageAdapter):
    def read(self, path: str) -> bytes:
        with open(path, "rb") as f:
            return f.read()

    def exists(self, path: str) -> bool:
        return os.path.exists(path)
