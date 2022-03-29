class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l >= r:
            return nums[l]
        mid = (l+r) // 2
        ls = self.helper(nums, l, mid)
        rs = self.helper(nums, mid+1, r)
        cross = self.cross(nums, l, r, mid)
        return max(ls, rs, cross)
    def cross(self, nums, l, r, mid):
        ltemp = 0
        ls = float('-inf')
        for i in range(mid, l-1, -1):
            ltemp += nums[i]
            ls = max(ltemp, ls)
        rtemp = 0
        rs = float('-inf')
        for j in range(mid+1, r+1):
            rtemp += nums[j]
            rs = max(rtemp, rs)
        return ls + rs