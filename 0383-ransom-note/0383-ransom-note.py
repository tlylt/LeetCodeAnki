class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ref = {}
        for i in magazine:
            ref[i] = ref.get(i, 0) + 1
        for j in ransomNote:
            if j not in ref:
                return False
            ref[j] -= 1
            if ref[j] < 0:
                return False
        return True
