class Stack:
    def __init__(self) -> None:
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, element: int) -> None:
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return -1

    def get_size(self) -> int:
        return self.size
