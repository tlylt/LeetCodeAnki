class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        p = self.pattern(s)
        if p[-1] != 0 and len(s) % (len(s) - p[-1]) == 0:
            return True
        return False
    
    def pattern(self, s):
        ans = [0] * len(s)
        l = 0
        for r in range(1, len(s)):
            while l > 0 and s[l] != s[r]:
                l = ans[l-1]
            if s[r] == s[l]:
                ans[r] = l+1
                l += 1
        return ans