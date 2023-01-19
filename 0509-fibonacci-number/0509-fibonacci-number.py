class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        if n < 2:
            return dp[n]
        for i in range(2, n+1):
            curr = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], curr
        return dp[1]