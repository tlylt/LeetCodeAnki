class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = (l + r) // 2
        lm = self.helper(nums, l, mid)
        rm = self.helper(nums, mid+1, r)
        cm = self.crossSum(nums, l, r, mid)
        return max(lm, rm, cm)
    def crossSum(self, nums, l, r, mid):
        left = float('-inf')
        temp = 0
        for i in range(mid, l-1, -1):
            temp += nums[i]
            if temp > left:
                left = temp
        temp = 0
        right = float('-inf')
        for j in range(mid+1, r+1):
            temp += nums[j]
            right = max(temp, right)
        return left + right