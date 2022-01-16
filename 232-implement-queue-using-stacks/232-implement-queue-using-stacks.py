class MyQueue:

    def __init__(self):
        self.ins = []
        self.out = []

    def push(self, x: int) -> None:
        self.ins.append(x)

    def pop(self) -> int:
        if not self.out and not self.ins:
            return None
        if self.out:
            return self.out.pop()
        while self.ins:
            self.out.append(self.ins.pop())
        return self.out.pop()
    
    def peek(self) -> int:
        temp = self.pop()
        self.out.append(temp)
        return temp

    def empty(self) -> bool:
        return not self.ins and not self.out


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()