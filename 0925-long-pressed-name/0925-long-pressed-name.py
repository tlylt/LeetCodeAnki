class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 0
        for r in range(len(typed)):
            if l < len(name) and name[l] == typed[r]:
                l += 1
            elif r == 0:
                return False
            elif typed[r] != typed[r-1]:
                return False
        return l == len(name)