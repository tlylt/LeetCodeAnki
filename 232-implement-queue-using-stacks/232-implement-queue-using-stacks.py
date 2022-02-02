class MyQueue:

    def __init__(self):
        self.inA = []
        self.out = []
        
    def push(self, x: int) -> None:
        self.inA.append(x)
    def pop(self) -> int:
        if self.out:
            return self.out.pop()
        while self.inA:
            self.out.append(self.inA.pop())
        return self.out.pop()
    def peek(self) -> int:
        temp = self.pop()
        self.out.append(temp)
        return temp
    def empty(self) -> bool:
        return not self.inA and not self.out


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()