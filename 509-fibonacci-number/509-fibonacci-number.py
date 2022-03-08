class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        if n <= 1:
            return dp[n]
        for i in range(2, n+1):
            temp = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = temp
        return dp[-1]