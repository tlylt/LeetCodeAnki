class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        h = self.helper(needle)
        l = 0
        for r in range(len(haystack)):
            while l > 0 and haystack[r] != needle[l]:
                l = h[l-1]
            if haystack[r] == needle[l]:
                l += 1
            if l >= len(needle):
                return r - l + 1
        return -1
    def helper(self, s):
        h = [0] * len(s)
        l = 0
        for r in range(1, len(s)):
            while l > 0 and s[l] != s[r]:
                l = h[l-1]
            if s[l] == s[r]:
                h[r] = l+1
                l += 1
        return h