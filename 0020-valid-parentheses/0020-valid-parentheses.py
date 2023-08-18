class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append({
                    "(": ")",
                    "[": "]",
                    "{":"}",
                }.get(i))
            else:
                if not stack:
                    return False    
                last = stack[len(stack)-1]
                if i != last:
                    return False
                stack.pop()
        return not stack