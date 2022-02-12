class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        if not tokens:
            return 0
        for i in tokens:
            if i == '+':
                s.append(s.pop() + s.pop())
            elif i == '-':
                a, b = s.pop(), s.pop()
                s.append(b - a)
            elif i == '/':
                a, b = s.pop(), s.pop()
                s.append(int(float(b)/a))
            elif i == '*':
                a, b = s.pop(), s.pop()
                s.append(b * a)
            else:
                s.append(int(i))
        return s[-1]