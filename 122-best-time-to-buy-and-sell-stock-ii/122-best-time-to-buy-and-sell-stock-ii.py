class Solution:
    # prices[3] - prices[0]
    # (prices[3] - prices[2]) + (prices[2] - prices[1]) + (prices[1] - prices[0])
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            temp = prices[i] - prices[i-1]
            if temp > 0:
                ans += temp
        return ans