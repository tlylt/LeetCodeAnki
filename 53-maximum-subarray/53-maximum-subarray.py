class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = (l + r) // 2
        ls = self.helper(nums, l, mid)
        rs = self.helper(nums, mid+1, r)
        cs = self.cross(nums, l, r, mid)
        return max(ls, rs, cs)
    def cross(self, nums, l, r, mid):
        ls = float('-inf')
        ltemp = 0
        for i in range(mid, l-1, -1):
            ltemp += nums[i]
            ls = max(ltemp, ls)
        rs = float('-inf')
        rtemp = 0
        for i in range(mid+1, r+1):
            rtemp += nums[i]
            rs = max(rtemp, rs)
        return ls + rs