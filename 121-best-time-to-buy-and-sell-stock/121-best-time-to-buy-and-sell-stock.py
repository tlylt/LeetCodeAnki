class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            low = min(low, prices[i])
            ans = max(ans, prices[i]-low)
        return ans