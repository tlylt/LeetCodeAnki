class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, u, d = 0, n - 1, 0, n - 1 # close, open
        ans = [[0 for i in range(n)] for j in range(n)]
        curr = 1
        while l < r and u < d:
            for i in range(l, r):
                ans[u][i] = curr
                curr += 1
            for j in range(u, d):
                ans[j][r] = curr
                curr += 1
            for k in range(r, l, -1):
                ans[d][k] = curr
                curr += 1
            for z in range(d, u, -1):
                ans[z][l] = curr
                curr += 1
            l += 1
            r -= 1
            u += 1
            d -= 1
        if n % 2 == 1:
            ans[n//2][n//2] = curr
        return ans