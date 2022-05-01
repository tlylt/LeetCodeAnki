class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        ans = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        ans += 1
                    elif dp[i+1][j-1]:
                        ans += 1
                        dp[i][j] = True
        return ans