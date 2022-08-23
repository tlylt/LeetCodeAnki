class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        for i in magazine:
            arr[ord(i)-ord('a')] += 1
        for j in ransomNote:
            if arr[ord(j)-ord('a')] >= 1:
                arr[ord(j)-ord('a')] -= 1
            else:
                return False
        return True