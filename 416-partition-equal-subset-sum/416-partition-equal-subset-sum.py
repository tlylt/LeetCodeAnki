class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [0] * (target+1)
        for j in range(len(nums)):
            for i in range(target, -1, -1):
                if nums[j] <= i:
                    dp[i] = max(dp[i], dp[i-nums[j]]+nums[j])
        return dp[target] == target