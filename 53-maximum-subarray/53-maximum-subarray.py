class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = (r-l) // 2 + l
        ls = self.helper(nums, l, mid)
        rs = self.helper(nums, mid+1, r)
        cs = self.cross(nums, l, r, mid)
        return max(ls, rs, cs)
    def cross(self, nums, l, r, mid):
        l_max = float('-inf')
        l_temp = 0
        for i in range(mid, l-1, -1):
            l_temp += nums[i]
            l_max = max(l_max, l_temp)
        r_max = float('-inf')
        r_temp = 0
        for j in range(mid+1, r+1):
            r_temp += nums[j]
            r_max = max(r_max, r_temp)
        return r_max + l_max