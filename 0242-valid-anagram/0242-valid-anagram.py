class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ref = [0] * 26
        for i in s:
            ref[ord(i) - ord('a')] += 1
        for j in t:
            ref[ord(j) - ord('a')] -= 1
        for k in ref:
            if k != 0:
                return False
        return True