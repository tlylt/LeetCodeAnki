class Solution:
    def isHappy(self, n: int) -> bool:
        h = {}
        while True:
            if n == 1:
                return True
            n = self.helper(n)
            if n in h:
                return False
            h[n] = 1
        
    def helper(self, n):
        ans = 0
        while n > 0:
            ans += (n % 10)**2
            n //= 10
        return ans