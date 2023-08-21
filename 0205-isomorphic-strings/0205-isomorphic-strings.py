class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        refs = {}
        reft = {}
        for i in range(len(s)):
            if s[i] not in refs:
                refs[s[i]] = t[i]
            if t[i] not in reft:
                reft[t[i]] = s[i]
            if refs[s[i]] != t[i] or reft[t[i]] != s[i]:
                return False
        return True