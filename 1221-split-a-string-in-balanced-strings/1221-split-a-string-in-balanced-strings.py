class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        diff = 0
        for i in s:
            if i == 'L':
                diff -= 1
            if i == 'R':
                diff += 1
            if diff == 0:
                ans += 1
        return ans