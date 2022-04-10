class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        ans = 0
        for i in range(len(prices)):
            low = min(prices[i], low)
            ans = max(ans, prices[i] - low)
        return ans