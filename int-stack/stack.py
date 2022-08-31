class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.elements: list[int] = []

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, element: int) -> None:
        self.size += 1
        self.elements.append(element)

    def pop(self) -> int:
        if self.size == 0:
            raise Underflow()
        self.size -= 1
        return self.elements.pop(self.size)

    def get_size(self) -> int:
        return self.size


class Underflow(RuntimeError):
    ...
