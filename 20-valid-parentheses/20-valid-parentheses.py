class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ')' or i == ']' or i == '}':
                if not stack or stack[-1] != i:
                    return False
                stack.pop()
            else:
                if i == '(':
                    stack.append(')')
                if i == '[':
                    stack.append(']')
                if i == '{':
                    stack.append('}')
        return not stack
