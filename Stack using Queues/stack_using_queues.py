class Node:
    def __init__(self, data, node=None):
        self.data = data
        self.next = node

class Queue:

    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, x: int) -> None:
        if self.is_empty():
            self.head = Node(x)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(x)

    def pop(self) -> int:
        result = self.head.data
        self.head = self.head.next
        return result

    def top(self) -> int:
        return self.head.data


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
