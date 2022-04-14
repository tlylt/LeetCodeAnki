class Solution:
    def isHappy(self, n: int) -> bool:
        h = set()
        while n != 1:
            n = self.helper(n)
            if n in h:
                return False
            h.add(n)
        return True
    def helper(self, n):
        ans = 0
        while n > 0:
            d = n % 10
            n = n // 10
            ans += d*d
        return ans