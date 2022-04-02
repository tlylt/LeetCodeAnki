class Solution:
    def count(self, s, target):
        ans = 0
        for i in s:
            if i == target:
                ans += 1
        return ans
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for s in strs:
            zero = self.count(s, '0')
            one = self.count(s, '1')
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zero][j-one]+1)
        return dp[m][n]
        