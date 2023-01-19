class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        pt = 0
        while pt < len(s):
            if stack == []:
                stack.append(s[pt])
            else:
                top = stack[-1]
                if top == s[pt]:
                    stack.pop()
                else:
                    stack.append(s[pt])
            pt += 1
        return "".join(stack)