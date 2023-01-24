class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp = [[False for i in range(len(s))] for j in range(len(s))]
        ans = 0
        for i in range(len(s)):
            ans += self.helper(s, i, i, len(s))
            ans += self.helper(s, i, i+1, len(s))
        return ans
    def helper(self, s, l, r, size):
        ans = 0
        while l >= 0 and r < size and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        return ans
        
        