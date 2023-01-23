class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+','-', '*', '/']:
                r = stack.pop()
                l = stack.pop()
                if i == '+':
                    stack.append(l + r)
                elif i == '-':
                    stack.append(l - r)
                elif i == '*':
                    stack.append(l * r)
                else:
                    stack.append(int(float(l)/r))
            else:
                stack.append(int(i))
        return stack.pop()