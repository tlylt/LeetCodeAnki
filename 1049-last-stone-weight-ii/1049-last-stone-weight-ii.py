class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [0] * (target+1)
        for i in range(len(stones)):
            for j in range(target, -1, -1):
                if stones[i] <= j:
                    dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        return (total - dp[target]) - dp[target]