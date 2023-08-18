class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ref = [0] * 26
        for i in s:
            ref[ord(i) - ord('a')] += 1
        for j in t:
            if ref[ord(j) - ord('a')] <= 0:
                return False
            ref[ord(j) - ord('a')] -= 1
        return True