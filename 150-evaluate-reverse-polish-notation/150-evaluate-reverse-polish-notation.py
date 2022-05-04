class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == '+':
                s.append(s.pop() + s.pop())
            elif t == '-':
                a, b = s.pop(), s.pop()
                s.append(b-a)
            elif t == '/':
                a, b = s.pop(), s.pop()
                s.append(int(float(b)/a))
            elif t == '*':
                s.append(s.pop() * s.pop())
            else:
                s.append(int(t))
        return s[0]