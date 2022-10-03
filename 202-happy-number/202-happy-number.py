class Solution:
    def isHappy(self, n: int) -> bool:
        ref = {}
        while True:
            n = self.helper(n)
            if n == 1:
                return True
            if n in ref:
                return False
            ref[n] = 1
        return False
        
    def helper(self, n):
        ans = 0
        while n > 0:
            d = n % 10
            n //= 10
            ans += d * d
        return ans