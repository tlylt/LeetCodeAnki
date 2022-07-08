class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        for i in tokens:
            if i == '+':
                a, b = q.pop(), q.pop()
                q.append(a+b)
            elif i == '-':
                a, b = q.pop(), q.pop()
                q.append(b-a)
            elif i == '/':
                a, b = q.pop(), q.pop()
                q.append(int(float(b)/a))
            elif i == '*':
                a, b = q.pop(), q.pop()
                q.append(a*b)
            else:
                q.append(int(i))
        return q.pop()