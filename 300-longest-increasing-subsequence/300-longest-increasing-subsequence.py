class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            for j in range(1, i):
                if nums[j-1] < nums[i-1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)