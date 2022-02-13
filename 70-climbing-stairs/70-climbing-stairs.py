class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for r in range(3, n+1):
            dp[r] = dp[r-1] + dp[r-2]
        return dp[n]
        