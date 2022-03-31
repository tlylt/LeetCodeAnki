class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h = [0] * 26
        for i in magazine:
            h[ord(i)-ord('a')] = h[ord(i)-ord('a')] + 1
        for j in ransomNote:
            if h[ord(j)-ord('a')] <= 0:
                return False
            h[ord(j)-ord('a')] -= 1
        return True