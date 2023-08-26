class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ref = []
        for i in s:
            ref.append(ord(i) - ord('a'))
        
        dp = [0] * (len(s) + 1)
        for i in range(1, len(s)+1):
            dp[i] = dp[i-1] ^ (1 << ref[i-1])
        
        ones = lambda x: x.bit_count()
        return [
            ones(dp[r+1] ^ dp[l]) >> 1 <= k
            for l, r, k in queries
        ]