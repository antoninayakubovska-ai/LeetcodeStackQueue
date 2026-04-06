class Node:
    def __init__(self, data, node=None):
        self.data = data
        self.next = node

class Stack:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        self.head = Node(x, self.head)

    def is_empty(self) -> bool:
        return self.head is None

    def pop(self) -> int:
        result = self.head.data
        self.head = self.head.next
        return result

    def peek(self) -> int:
        return self.head.data


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
