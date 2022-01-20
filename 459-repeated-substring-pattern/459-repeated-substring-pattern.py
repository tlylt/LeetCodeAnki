class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s = self.pattern(s)
        if s[-1] != 0 and len(s) % (len(s) - s[-1]) == 0:
            return True
        return False
        
    def pattern(self, s):
        result = [0] * len(s)
        l = 0
        for r in range(1, len(s)):
            while l > 0 and s[l] != s[r]:
                l = result[l-1]
            if s[r] == s[l]:
                result[r] = l+1
                l+=1
        return result