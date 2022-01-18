class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        p = self.pattern(needle)
        l = 0 
        for r in range(len(haystack)):
            while l > 0 and haystack[r] != needle[l]:
                l = p[l-1]
            if haystack[r] == needle[l]:
                l+=1
            if l >= len(p):
                return r-len(needle)+1
        return -1
            
    def pattern(self, s):
        l = 0
        ans = [0] * len(s)
        for r in range(1, len(s)):
            while l > 0 and s[l] != s[r]:
                l = ans[l-1]
            if s[l] == s[r]:
                l+=1
                ans[r] = l
        return ans