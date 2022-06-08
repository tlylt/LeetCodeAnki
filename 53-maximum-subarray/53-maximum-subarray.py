class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l > r:
            return 0
        if l == r:
            return nums[l]
        mid = (l+r) // 2
        ls = self.helper(nums, l, mid)
        rs = self.helper(nums, mid+1, r)
        cs = self.cross(nums, l, r, mid)
        return max(ls, rs, cs)
    def cross(self, nums, l, r, mid):
        temp = 0
        l_m = float('-inf')
        for i in range(mid, l-1, -1):
            temp += nums[i]
            l_m = max(l_m, temp)
        temp = 0
        r_m = float('-inf')
        for j in range(mid+1, r+1):
            temp += nums[j]
            r_m = max(r_m, temp)
        return l_m + r_m