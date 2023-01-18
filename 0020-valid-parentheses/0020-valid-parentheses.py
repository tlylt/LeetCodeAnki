class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pt = 0
        ref = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        while pt < len(s):
            if stack == []:
                if s[pt] in [')', ']', '}']:
                    return False
                stack.append(s[pt])
            else:
                if s[pt] in ref and stack[-1] == ref[s[pt]]:
                    stack.pop()
                else:
                    stack.append(s[pt])
            pt += 1
        return stack == []        