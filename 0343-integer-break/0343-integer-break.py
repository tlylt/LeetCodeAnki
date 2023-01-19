class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [float('-inf')] * (n + 1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i+1):
                dp[i] = max(dp[i], dp[i-j]*j, (i-j)*j)
        return dp[n]
            