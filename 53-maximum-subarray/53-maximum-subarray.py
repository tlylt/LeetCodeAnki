class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = max(nums)
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if temp > 0:
                ans = max(ans, temp)
            else:
                temp = 0
        return ans