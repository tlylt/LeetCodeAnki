class Q:
    def __init__(self):
        self.ref = deque()
    def add(self, val):
        while self.ref and self.ref[-1] < val:
            self.ref.pop()
        self.ref.append(val)
    def pop(self, val):
        if val == self.ref[0]:
            self.ref.popleft()
    def top(self):
        return self.ref[0]
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ref = Q()
        for i in range(k):
            ref.add(nums[i])
        ans = []
        ans.append(ref.top())
        l = 0
        for i in range(k, len(nums)):
            ref.pop(nums[l])
            ref.add(nums[i])
            ans.append(ref.top())
            l += 1
        return ans