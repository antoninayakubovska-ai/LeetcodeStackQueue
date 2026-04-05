class Queue:
    def __init__(self):
        self._data = []

    def push(self, x: int) -> None:
        self._data.append(x)

    def pop(self) -> int:
        if self._data:
            return self._data.pop(0)
        return None

    def top(self) -> int:
        if self._data:
            return self._data[0]
        return None

    def is_empty(self) -> bool:
        return len(self._data) == 0


class MyStack:
    def __init__(self):
        self.q_in = Queue()
        self.q_out = Queue()

    def push(self, x: int) -> None:
        self.q_out.push(x)
        while not self.q_in.is_empty():
            self.q_out.push(self.q_in.pop())

        self.q_in, self.q_out = self.q_out, self.q_in

    def pop(self) -> int:
        return self.q_in.pop()

    def top(self) -> int:
        return self.q_in.top()

    def empty(self) -> bool:
        return self.q_in.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
