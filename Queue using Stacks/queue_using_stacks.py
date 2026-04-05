class Stack:

    def __init__(self):
        self._data = []

    def push(self, x: int) -> None:
        self._data.append(x)

    def pop(self) -> int:
        if self._data:
            return self._data.pop()
        return None

    def peek(self) -> int:
        if self._data:
            return self._data[-1]
        return None

    def is_empty(self) -> bool:
        return len(self._data) == 0


class MyQueue:

    def __init__(self):
        self.s_in = Stack()
        self.s_out = Stack()

    def _transfer(self):
        if self.s_out.is_empty():
            while not self.s_in.is_empty():
                self.s_out.push(self.s_in.pop())

    def push(self, x: int) -> None:
        self.s_in.push(x)

    def pop(self) -> int:
        self._transfer()
        return self.s_out.pop()

    def peek(self) -> int:
        self._transfer()
        return self.s_out.peek()

    def empty(self) -> bool:
        return self.s_in.is_empty() and self.s_out.is_empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
