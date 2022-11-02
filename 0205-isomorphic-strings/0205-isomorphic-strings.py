class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        if len(s) != len(t):
            return False
        for i, j in zip(s, t):
            if i not in s_t:
                s_t[i] = j
            if j not in t_s:
                t_s[j] = i
            if s_t[i] != j or t_s[j] != i:
                return False
        return True