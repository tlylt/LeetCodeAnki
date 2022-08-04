class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ref = self.helper(s)
        if ref[-1] != 0 and (len(s) % (len(s) - ref[-1]) == 0):
            return True
        return False
    def helper(self, s):
        h = [0] * len(s)
        l = 0
        for r in range(1, len(s)):
            while l > 0 and s[l] != s[r]:
                l = h[l-1]
            if s[l] == s[r]:
                h[r] = l + 1
                l += 1
        return h