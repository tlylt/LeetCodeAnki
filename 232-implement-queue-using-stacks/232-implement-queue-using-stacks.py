class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []
    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        if self.b:
            return self.b.pop()
        else:
            while self.a:
                self.b.append(self.a.pop())
        return self.b.pop()

    def peek(self) -> int:
        temp = self.pop()
        self.b.append(temp)
        return temp
            
    def empty(self) -> bool:
        return not self.b and not self.a


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()