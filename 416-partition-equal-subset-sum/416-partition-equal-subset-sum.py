class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        half = sum(nums)//2
        dp = [0] * (half + 1)
        for i in range(len(nums)):
            for j in range(half, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return half == dp[-1]