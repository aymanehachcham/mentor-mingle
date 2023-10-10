from pathlib import Path
from typing import List

import toml
from pydantic import BaseModel


class CFGGpt(BaseModel):
    """
    Config for OpenAI GPT-3 API
    """

    temperature: float
    max_tokens: int
    n: int
    stop: List[str]
    stream: bool


class Gpt(BaseModel):
    """
    GPT-3 Model
    """

    name: str
    description: str
    config: CFGGpt


class GptModels(BaseModel):
    """
    GPT-3 Models
    """

    gpt3: Gpt
    gpt3_16: Gpt


class Config(BaseModel):
    """
    Config for MentorMingle
    """

    models: GptModels

    @classmethod
    def from_toml(cls, config_file: Path) -> "Config":
        """
        Load config from toml file

        Args:
            config_file (Path): Path to config file

        Returns:
            Config: Config object
        """
        return cls(**toml.load(config_file))
