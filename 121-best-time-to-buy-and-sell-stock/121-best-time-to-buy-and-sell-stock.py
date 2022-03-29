class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = float('-inf')
        low = float('inf')
        for i in range(len(prices)):
            low = min(low, prices[i])
            ans = max(ans, prices[i] - low)
        return ans