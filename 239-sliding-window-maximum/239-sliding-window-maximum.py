class Q:
    def __init__(self):
        self.s = deque()
    def add(self, val):
        while self.s and val > self.s[-1]:
            self.s.pop()
        self.s.append(val)
    def pop(self, val):
        if self.s and self.s[0] == val:
            self.s.popleft()
    def top(self):
        return self.s[0]
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = Q()
        for i in range(k):
            q.add(nums[i])
        ans = []
        ans.append(q.top())
        for i in range(k, len(nums)):
            q.add(nums[i])
            q.pop(nums[i-k])
            ans.append(q.top())
        return ans