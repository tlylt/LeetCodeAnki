class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(amount+1):
                if coins[i] <= j:
                    dp[j] = min(dp[j], dp[j-coins[i]]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
        