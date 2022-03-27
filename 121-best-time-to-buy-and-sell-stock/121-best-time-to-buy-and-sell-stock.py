class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        result = 0
        for i in range(len(prices)):
            low = min(low, prices[i])
            result = max(result, prices[i] - low)
        return result