class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            lowest = min(lowest, prices[i])
            ans = max(ans, prices[i]-lowest)
        return ans