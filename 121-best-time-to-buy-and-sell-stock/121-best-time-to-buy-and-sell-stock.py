class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        ans = 0
        for i in range(len(prices)):
            low = min(low, prices[i])
            ans = max(ans, prices[i] - low)
        return ans