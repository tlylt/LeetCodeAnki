class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        for i in s:
            arr[(ord(i) - ord('a')) % 26] += 1
        for j in t:
            idx = (ord(j) - ord('a')) % 26
            arr[idx] -= 1
            if arr[idx] < 0:
                return False
        return sum(arr) == 0