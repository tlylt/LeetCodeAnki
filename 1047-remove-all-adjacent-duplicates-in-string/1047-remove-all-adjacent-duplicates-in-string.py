class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if not stack or stack[-1] != i:
                stack.append(i)
            elif stack[-1] == i:
                stack.pop()
        return "".join(stack)