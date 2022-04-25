class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2
        dp = [0] * (target+1)
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                if j >= nums[i]:
                    dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[target] == target