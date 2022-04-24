class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = (l+r) // 2
        ls = self.helper(nums, l, mid)
        rs = self.helper(nums, mid+1, r)
        cs = self.cross(nums, l, r, mid)
        return max(ls, rs, cs)
    
    def cross(self, nums, l, r, mid):
        ls = float('-inf')
        temp = 0
        for i in range(mid, l-1, -1):
            temp += nums[i]
            ls = max(temp, ls)
        rs = float('-inf')
        temp = 0
        for j in range(mid+1, r+1):
            temp += nums[j]
            rs = max(temp, rs)
        return ls + rs