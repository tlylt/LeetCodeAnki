class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, n):
                s = j * j
                if s > i:
                    break
                dp[i] = min(dp[i], dp[i-s] + 1)
        return dp[n]