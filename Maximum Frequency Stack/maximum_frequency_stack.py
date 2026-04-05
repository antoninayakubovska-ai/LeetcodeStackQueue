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
