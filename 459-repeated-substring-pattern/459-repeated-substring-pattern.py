class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ans = self.pattern(s)
        if ans[-1] != 0 and len(s) %(len(s) - ans[-1]) == 0:
            return True
        return False
    def pattern(self, s):
        ans = [0] * len(s)
        l = 0
        for r in range(1, len(s)):
            while l > 0 and s[l] != s[r]:
                l = ans[l-1]
            if s[l] == s[r]:
                l+=1
                ans[r] = l
        return ans