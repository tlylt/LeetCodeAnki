class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i, t_i = 0, 0
        while s_i < len(s) and t_i < len(t):
            if s[s_i] == t[t_i]:
                s_i += 1
            t_i += 1
        return s_i == len(s)