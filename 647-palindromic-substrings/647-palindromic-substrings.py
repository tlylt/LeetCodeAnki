class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.helper(s, i, i+1, len(s)-1)
            ans += self.helper(s, i, i, len(s)-1)
        return ans
    def helper(self, s, l, r, end):
        ans = 0
        while l >= 0 and r <= end and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        return ans