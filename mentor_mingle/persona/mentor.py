from ..tot.schema import Thought
from .base import BasePersona
from .prompts import answer_format, interviewer


class Mentor(BasePersona):
    """
    Mentor persona.
    """

    def __init__(self):
        super().__init__()
        self.context = None
        self.persona = interviewer
        self.answer_format = answer_format

    def __repr__(self) -> str:
        return f"MentorMingle:\n-> Persona: {self.persona}\n"

    def solve_case(self, prompt: str) -> Thought:
        pass

    def evaluate_case(self, current_case: Thought) -> float:
        pass

    def generate_case(self, next_case: Thought) -> Thought:
        pass
