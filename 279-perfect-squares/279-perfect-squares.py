class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n):
            s = i * i
            if s > n:
                break
            for j in range(1, n+1):
                if s <= j:
                    dp[j] = min(dp[j-s]+1, dp[j])
        return dp[n]