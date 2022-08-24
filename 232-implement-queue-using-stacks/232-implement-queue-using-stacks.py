class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2:
            temp = self.s2[-1]
            self.s2 = self.s2[:-1]
            return temp
        while self.s1:
            temp = self.s1[-1]
            self.s2.append(temp)
            self.s1 = self.s1[:-1]
        ans = self.s2[-1]
        self.s2 = self.s2[:-1]
        return ans

    def peek(self) -> int:
        ans = self.pop()
        self.s2.append(ans)
        return ans
        
    def empty(self) -> bool:
        return self.s1 == [] and self.s2 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()