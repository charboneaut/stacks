import unittest
from stack import Stack


class TestStacks(unittest.TestCase):
    def test_init(self):
        test_stack = Stack()
        self.assertIsInstance(test_stack, Stack)

    def test_init_content(self):
        test_stack = Stack([1, 2, 3])
        self.assertIsInstance(test_stack, Stack)
        self.assertEqual(test_stack.items, [1, 2, 3])

    def test_push(self):
        test_stack = Stack()
        test_stack.push(1)
        self.assertEqual(test_stack.items, [1])
    
    def test_pop(self):
        test_stack = Stack([1, 2, 3])
        test_return = test_stack.pop()
        self.assertEqual(test_stack.items, [1, 2])
        self.assertEqual(test_return, 3)
        
