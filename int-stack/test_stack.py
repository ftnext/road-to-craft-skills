from unittest import TestCase

from stack import MyStack


class StackTestCase(TestCase):
    def test_can_create_stack(self):
        stack = MyStack()
