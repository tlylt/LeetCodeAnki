class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m): # just nice initialized
            for j in range(1, n): # just nice initialized
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
        