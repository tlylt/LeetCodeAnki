class Q:
    def __init__(self):
        self.q = deque()
    def push(self, val):
        while self.q and val > self.q[-1]:
            self.q.pop()
        self.q.append(val)
    def pop(self, val):
        if self.q and self.q[0] == val:
            self.q.popleft()
    def top(self):
        return self.q[0]
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = Q()
        for i in range(k):
            q.push(nums[i])
        ans = []
        ans.append(q.top())
        l = 0
        for r in range(k, len(nums)):
            q.push(nums[r])
            q.pop(nums[l])
            l+=1
            ans.append(q.top())
        return ans