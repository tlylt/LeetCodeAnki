class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        ans = float('-inf')
        for i in range(len(prices)):
            low = min(low, prices[i])
            ans = max(ans, prices[i] - low)
        return ans