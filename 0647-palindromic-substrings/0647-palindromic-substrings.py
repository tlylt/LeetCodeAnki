class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp = [[False for i in range(len(s))] for j in range(len(s))]
        ans = 0
        for i in range(len(s)):
            ans += self.helper(s, i, i, len(s))
            ans += self.helper(s, i, i+1, len(s))
        return ans
    def helper(self, s, i, j, n):
        ans = 0
        while i >= 0 and j < n and s[i] == s[j]:
            ans += 1
            i -= 1
            j += 1
        return ans