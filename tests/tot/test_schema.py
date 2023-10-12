from tot.schema import Thought


class TestThought:
    """
    Test the Thought class from the tot.schema module.
    """

    def test_add(self):
        """
        Test the add method of the Thought class.
        """
        parent = Thought("evaluate")
        child = Thought("solve")
        parent.add(child)
        assert parent.child == child
        assert child.parent == parent

    def test_pop(self):
        """
        Test the pop method of the Thought class.
        """
        parent = Thought("evaluate")
        child = Thought("solve")
        parent.add(child)
        parent.pop(child)
        assert parent.child is None
