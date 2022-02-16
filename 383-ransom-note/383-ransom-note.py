class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        h = {}
        for i in magazine:
            h[i] = h.get(i, 0) + 1
        
        for j in ransomNote:
            if j not in h or h[j] == 0:
                return False
            h[j] -= 1
        return True