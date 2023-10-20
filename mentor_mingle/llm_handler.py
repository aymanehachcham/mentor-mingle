import logging
import os
from pathlib import Path

import openai
from dotenv import load_dotenv
from typing import Generator

from .config import Config
from .persona.base import BasePersona

load_dotenv()
logger = logging.getLogger(__name__)


class ChatHandler:
    """Handler for chat with GPT-3"""

    def __init__(
        self,
        persona: BasePersona,
    ):
        """Initialize the chat handler"""
        openai.api_key = os.getenv("OPENAI_KEY")
        self.agent = persona

        # Load config
        self.model = Config.from_toml(Path("../config.toml")).models.gpt3

    def stream_chat(self, user_prompt: str) -> Generator[str, None, None]:
        """
        Stream a chat with GPT-3

        Args:
            user_prompt (str): The user's prompt

        Returns:
            None
        """
        completion = openai.ChatCompletion.create(
            model=self.model.name,
            messages=[
                {"role": "system", "content": self.agent.persona},
                {"role": "user", "content": f"User: {user_prompt}" f"\n{self.agent.answer_format}"},
            ],
            **self.model.config.model_dump(),
        )
        for chunk in completion:
            print(chunk)
            content = chunk.choices[0].delta.get("content", "")
            if content != "":
                yield content

