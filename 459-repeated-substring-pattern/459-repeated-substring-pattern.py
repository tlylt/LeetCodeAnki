class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ref = self.helper(s)
        if ref[-1] != 0 and (len(s) % (len(s) - ref[-1])) == 0:
            return True
        return False
    def helper(self, s):
        ref = [0] * len(s)
        l = 0
        for r in range(1, len(s)):
            while l > 0 and s[l] != s[r]:
                l = ref[l-1]
            if s[l] == s[r]:
                ref[r] = l + 1
                l += 1
        return ref