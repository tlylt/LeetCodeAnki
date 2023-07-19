class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        ref = [0] * 26
        for i in magazine:
            ref[ord(i) - ord('a')] += 1
        for j in ransomNote:
            if ref[ord(j) - ord('a')] <= 0:
                return False
            ref[ord(j) - ord('a')] -= 1
        return True