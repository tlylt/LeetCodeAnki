class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        ans = 0
        for p in prices:
            low = min(low, p)
            ans = max(ans, p-low)
        return ans