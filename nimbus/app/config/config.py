from typing import Any

class AppConfig:
    _instance = None

    def __new__(cls, *args: Any, **kwargs: Any) -> "AppConfig":
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, provider: str, model: str):
        self.provider = provider
        self.model = model

    def get_provider(self) -> str:
        return self.provider

    def get_model(self) -> str:
        return self.model