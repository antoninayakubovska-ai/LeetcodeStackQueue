
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for el in path.split('/'):
            if el == '.' or el == "":
                continue
            elif el == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(el)

        return "/"+"/".join(stack)
        