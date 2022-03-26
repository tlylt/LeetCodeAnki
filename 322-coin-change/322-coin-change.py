class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount+1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1