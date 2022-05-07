class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            s = i * i
            if s > n:
                break
            for i in range(1, n+1):
                if i >= s:
                    dp[i] = min(dp[i], dp[i-s] + 1)
        return dp[n]