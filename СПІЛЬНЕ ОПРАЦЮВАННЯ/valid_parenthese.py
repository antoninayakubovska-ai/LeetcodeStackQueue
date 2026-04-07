from queue import LifoQueue
class Solution:
    def isValid(self, s: str) -> bool:
        stack = LifoQueue()
        parentheses = {'(':')', '[':']', '{':'}'}
        for ch in s:
            if ch in parentheses:
                stack.put(ch)
            elif stack.empty() or parentheses[stack.get()] != ch:
                return False
        if not stack.empty():
            return False

        return True
