class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp =[[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if s[j-1] == t[i-1]:
                    dp[j][i] = dp[j-1][i-1] + dp[j-1][i]
                else:
                    dp[j][i] = dp[j-1][i]
        return dp[len(s)][len(t)]