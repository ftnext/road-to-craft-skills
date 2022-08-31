from unittest import TestCase

from stack import Stack


class StackTestCase(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_can_create_stack(self):
        self.assertTrue(self.stack.is_empty())

    def test_can_push(self):
        self.stack.push(0)
        self.assertFalse(self.stack.is_empty())
