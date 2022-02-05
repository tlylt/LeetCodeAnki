class Q:
    def __init__(self):
        self.q = deque()
    def top(self):
        return self.q[0]
    def push(self, val):
        while self.q and val > self.q[-1]:
            self.q.pop()
        self.q.append(val)
    def pop(self, val):
        if self.q and val == self.q[0]:
            self.q.popleft()
            
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = Q()
        for i in range(k):
            q.push(nums[i])
        ans = []
        ans.append(q.top())
        for r in range(k, len(nums)):
            q.push(nums[r])
            q.pop(nums[r-k])
            ans.append(q.top())
        return ans