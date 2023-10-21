from abc import ABC, abstractmethod

from ..tot.schema import Thought


class BasePersona(ABC):
    """
    Base class for all personas.
    Each persona has its own:
        - solve_case logic -> solves the current Thought but remains in same state.
        - evaluate_case logic -> evaluates the current logic Thought and scores it.
        - generate_case logic -> generates next state of Thought.
    """

    def __init__(self):
        """
        Initializes the persona.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Returns a string representation of the persona.

        Returns:
            str: string representation of the persona.
        """
        pass

    @abstractmethod
    def solve_case(self, prompt: str) -> Thought:
        """
        Solves the current Thought but remains in same state.

        Args:
            prompt (str): prompt to solve.

        Returns:
            Thought: solved Thought.
        """
        pass

    @abstractmethod
    def evaluate_case(self, current_case: Thought) -> float:
        """
        Evaluates the current logic Thought and scores it.

        Args:
            current_case (Thought): current Thought to evaluate.

        Returns:
            float: score of the current Thought.
        """
        pass

    @abstractmethod
    def generate_case(self, next_case: Thought) -> Thought:
        """
        Generates next state of Thought.

        Args:
            next_case (Thought): next Thought to generate.

        Returns:
            Thought: generated Thought.
        """
        pass
