class Solution:
    def minMoves(self, t: int, m: int) -> int:
        if m == 0:
            return t - 1
        ans = 0
        while t > 1: # 4
            if m == 0:
                return ans + (t-1)
            # m > 0
            if t % 2 == 0: 
                t = t // 2 # t = 4
                m -= 1 # m = 0
            else:
                t -= 1 # t = 8
            ans += 1 # ans = 4
        return ans        