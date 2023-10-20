from typing import Literal


class Thought:
    """
    A thought is a node in a tree of thoughts. It has a state, and a parent and child thought.
    Building block for a thought tree.
    """

    def __init__(
        self,
        state: Literal["evaluate", "solve", "generate"],
        parent: "Thought" = None,
        child: "Thought" = None,
    ):
        """
        Initialize a thought with a state, and a parent and child thought.

        Args:
            state: The state of the thought. One of 'evaluate', 'solve', or 'generate'.
            parent: The parent thought.
            child: The child thought.

        Returns:
            None
        """
        self.state = state
        self.parent = parent
        self.child = child

    def add(self, thought: "Thought"):
        """
        Add a child thought to this thought.

        Args:
            thought: The child thought to add.

        Returns:
            None
        """
        self.child = thought
        thought.parent = self

    def pop(self, thought: "Thought"):
        """
        Remove a child thought from this thought.

        Args:
            thought: The child thought to remove.

        Returns:
            None
        """
        self.child = None
        thought.parent = None
        del thought
