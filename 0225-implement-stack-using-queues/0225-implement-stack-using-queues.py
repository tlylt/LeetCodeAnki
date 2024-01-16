class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        l = len(self.queue)
        while l >= 2:
            self.queue.append(self.queue.popleft())
            l -= 1
        return self.queue.popleft()

    def top(self) -> int:
        t = self.pop()
        self.push(t)
        return t

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()