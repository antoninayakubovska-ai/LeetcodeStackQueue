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

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.floors = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]

        if f not in self.floors:
            self.floors[f] = []

        self.floors[f].append(val)

        if f > self.max_freq:
            self.max_freq = f

    def pop(self) -> int:
        val = self.floors[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.floors[self.max_freq]:
            self.max_freq -= 1

        return val
