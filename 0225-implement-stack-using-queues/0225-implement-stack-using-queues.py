class MyStack:

    def __init__(self):
        self.q = deque([])        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        l = len(self.q)
        for i in range(l-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        temp = self.pop()
        self.push(temp)
        return temp

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()