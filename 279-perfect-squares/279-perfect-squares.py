class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            sq = i * i
            if sq > n:
                break
            for j in range(sq, n+1):
                dp[j] = min(dp[j], dp[j-sq] + 1)
        return dp[n] if dp[n] != float('inf') else 0