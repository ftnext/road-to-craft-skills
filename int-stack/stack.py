class Stack:
    def __init__(self) -> None:
        self.empty = True

    def is_empty(self) -> bool:
        return self.empty

    def push(self, element: int) -> None:
        self.empty = False
