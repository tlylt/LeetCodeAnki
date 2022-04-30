class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        ans = 0
        for p in prices:
            lowest = min(lowest, p)
            ans = max(ans, p-lowest)
        return ans
            