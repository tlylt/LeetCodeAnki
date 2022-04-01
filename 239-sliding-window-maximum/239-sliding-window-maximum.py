class Q:
    def __init__(self):
        self.s = deque()
    def top(self):
        return self.s[0]
    def push(self, val):
        while self.s and self.s[-1] < val:
            self.s.pop()
        self.s.append(val)
    def pop(self, val):
        if self.s and self.s[0] == val:
            self.s.popleft()

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = Q()
        for i in range(k):
            q.push(nums[i])
        ans = []
        ans.append(q.top())
        l = 0
        for r in range(k, len(nums)):
            q.pop(nums[l])
            q.push(nums[r])
            ans.append(q.top())
            l += 1
        return ans