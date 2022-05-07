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
        temp = 0
        l_s = float('-inf')
        for i in range(mid, l-1, -1):
            temp += nums[i]
            if temp > l_s:
                l_s = temp
        temp = 0
        r_s = float('-inf')
        for j in range(mid+1, r+1):
            temp += nums[j]
            if temp > r_s:
                r_s = temp
        return l_s + r_s