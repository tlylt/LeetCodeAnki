class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [float('-inf')] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, n+1):
                dp[i] = max(dp[i], j * (i-j), j * dp[i-j])
        return dp[n]