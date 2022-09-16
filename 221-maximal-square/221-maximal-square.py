class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix) # row
        n = len(matrix[0]) # col
        ref = [[0 for i in range(n)] for j in range(m)]
        ans = 0
        for i in range(m):
            ref[i][0] = 1 if matrix[i][0] == "1" else 0
            ans = max(ans, ref[i][0])
        for j in range(n):
            ref[0][j] = 1 if matrix[0][j] == "1" else 0
            ans = max(ans, ref[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != "0":
                    ref[i][j] = min(ref[i-1][j], ref[i][j-1], ref[i-1][j-1]) + 1
                    ans = max(ans, ref[i][j])
        return ans**2        