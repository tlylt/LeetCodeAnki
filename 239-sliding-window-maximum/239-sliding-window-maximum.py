class Q:
    def __init__(self):
        self.q = deque()
    def add(self, num):
        while self.q and self.q[-1] < num:
            self.q.pop()
        self.q.append(num)
    def pop(self, num):
        if self.q[0] == num:
            self.q.popleft()
    def top(self):
        return self.q[0]
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = Q()
        for i in range(k):
            q.add(nums[i])
        ans = []
        ans.append(q.top())
        l = 0
        for i in range(k, len(nums)):
            q.add(nums[i])
            q.pop(nums[l])
            l += 1
            ans.append(q.top())
        return ans