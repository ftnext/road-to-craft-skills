from unittest import TestCase

from stack import Stack, Underflow


class StackTestCase(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_can_create_stack(self):
        self.assertTrue(self.stack.is_empty())

    def test_after_one_push__is_not_empty(self):
        self.stack.push(0)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(1, self.stack.get_size())

    def test_after_one_push_and_one_pop__is_empty(self):
        self.stack.push(0)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(0, self.stack.get_size())

    def test_after_two_pushes__size_is_two(self):
        self.stack.push(0)
        self.stack.push(0)
        self.assertEqual(2, self.stack.get_size())

    def test_popping_empty_stack__throws_Underflow(self):
        with self.assertRaises(Underflow):
            self.stack.pop()

    def test_after_pushing_X__will_pop_X(self):
        self.stack.push(99)
        self.assertEqual(99, self.stack.pop())
        self.stack.push(88)
        self.assertEqual(88, self.stack.pop())

    def test_after_pushing_X_and_Y__will_pop_Y_then_X(self):
        self.stack.push(99)
        self.stack.push(88)
        self.assertEqual(88, self.stack.pop())
        self.assertEqual(99, self.stack.pop())
