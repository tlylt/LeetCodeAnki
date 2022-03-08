class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        if n <= 1:
            return dp[n]
        for i in range(2, n+1):
            for j in range(1, n+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[-1]