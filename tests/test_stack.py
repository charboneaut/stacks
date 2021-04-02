import unittest
from stack import Stack


class TestStacks(unittest.TestCase):
    def test_init(self):
        test_stack = Stack()
        self.assertIsInstance(test_stack, Stack)
