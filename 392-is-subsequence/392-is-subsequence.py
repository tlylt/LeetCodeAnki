class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[len(s)][len(t)] == len(s)