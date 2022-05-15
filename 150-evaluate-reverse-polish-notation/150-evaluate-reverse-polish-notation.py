class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = []
        for t in tokens:
            if t == '+':
                d.append(d.pop() + d.pop())
            elif t == '-':
                a, b = d.pop(), d.pop()
                d.append(b-a)
            elif t == '/':
                a, b = d.pop(), d.pop()
                d.append(int(float(b)/a))
            elif t == '*':
                d.append(d.pop() * d.pop())
            else:
                d.append(int(t))
        return d[0]