class Stack:
    def __init__(self) -> None:
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, element: int) -> None:
        self.size += 1
        self.element = element

    def pop(self) -> int:
        if self.size == 0:
            raise Underflow()
        self.size -= 1
        return self.element

    def get_size(self) -> int:
        return self.size


class Underflow(RuntimeError):
    ...
