class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if abs(j-i) <= 1:
                        ans += 1
                        dp[i][j] = True
                    else:
                        if dp[i+1][j-1]:
                            ans += 1
                            dp[i][j] = True
        return ans