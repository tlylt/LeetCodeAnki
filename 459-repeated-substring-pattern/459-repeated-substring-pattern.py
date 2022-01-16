class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        prefix = self.pattern(s)
        if prefix[-1] != 0 and len(s) % (len(s) - prefix[-1]) == 0:
            return True
        return False
    def pattern(self, s):
        prefix = [0] * len(s)
        l = 0
        for r in range(1, len(s)):
            while l > 0 and s[l] != s[r]:
                l = prefix[l-1]
            if s[l] == s[r]:
                l+=1
                prefix[r] = l
        return prefix