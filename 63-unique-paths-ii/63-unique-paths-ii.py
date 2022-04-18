class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        flag = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                flag = 0
            dp[i][0] = flag
        flag = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                flag = 0
            dp[0][j] = flag
        dp[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]