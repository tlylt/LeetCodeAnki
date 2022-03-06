class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = (r+l)//2
        l_sum = self.helper(nums, l, mid)
        r_sum = self.helper(nums, mid+1, r)
        cross_sum = self.cross(nums, l, r, mid)
        return max(l_sum, r_sum, cross_sum)
    def cross(self, nums, l, r, mid):
        l_sum = 0
        l_max = float('-inf')
        for i in range(mid, l-1, -1):
            l_sum += nums[i]
            if l_sum > l_max:
                l_max = l_sum
        r_sum = 0
        r_max = float('-inf')
        for i in range(mid+1, r+1):
            r_sum += nums[i]
            if r_sum > r_max:
                r_max = r_sum
        return l_max + r_max