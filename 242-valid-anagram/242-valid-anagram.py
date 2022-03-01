class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        for i in s:
            h[i] = h.get(i, 0) + 1
        for j in t:
            if h.get(j, 0) == 0:
                return False
            else:
                h[j] -= 1
        for k in h:
            if h[k] >= 1:
                return False
        return True