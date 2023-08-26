class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        for i in range(len(s)):
            if s[i] in ['(', '*']:
                left += 1
            else:
                left -= 1
            if left < 0:
                return False
        if left == 0:
            return True
        right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] in [')', '*']:
                right += 1
            else:
                right -= 1
            if right < 0:
                return False
        return True