class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = float('-inf')
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if temp > ans:
                ans = temp
            if temp < 0:
                temp = 0
        return ans