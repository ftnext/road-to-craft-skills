from unittest import TestCase

from stack import Stack


class StackTestCase(TestCase):
    def test_can_create_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_can_push(self):
        stack = Stack()
        stack.push(0)
