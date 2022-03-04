class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if r == l:
            return nums[l]
        mid = (r+l)//2
        l_max = self.helper(nums, l, mid)
        r_max = self.helper(nums, mid+1, r)
        cross_max = self.cross(nums, l, r, mid)
        return max(l_max, r_max, cross_max)
    
    def cross(self, nums, l, r, mid):
        l_max = float('-inf')
        l_sum = 0
        for i in range(mid, l-1, -1):
            l_sum += nums[i]
            if l_sum > l_max:
                l_max = l_sum
        r_max = float('-inf')
        r_sum = 0
        for j in range(mid+1, r+1):
            r_sum += nums[j]
            if r_sum > r_max:
                r_max = r_sum
        return l_max + r_max
        