class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ref = {}
        for i in s:
            ref[i] = ref.get(i, 0) + 1
        for j in t:
            if j not in ref or ref[j] <= 0:
                return False
            ref[j] -= 1
        return True