class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                s.append(s.pop() + s.pop())
            elif tokens[i] == '-':
                a, b = s.pop(), s.pop()
                s.append(b-a)
            elif tokens[i] == '/':
                a, b = s.pop(), s.pop()
                s.append(int(float(b)/a))
            elif tokens[i] == '*':
                s.append(s.pop() * s.pop())
            else:
                s.append(int(tokens[i]))
        return s[-1]