class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0, 1]
        for i in range(2, n+1):
            temp = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = temp
        return dp[1]
            