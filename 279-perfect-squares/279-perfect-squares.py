class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            item = i*i
            if item > n:
                break
            for j in range(1, n+1):
                if j >= item:
                    dp[j] = min(dp[j], dp[j-item] + 1)
        return dp[n] if dp[n] != float('inf') else -1