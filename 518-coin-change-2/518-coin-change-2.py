class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for j in range(len(coins)):
            for i in range(1, amount+1):
                if i >= coins[j]:
                    dp[i] += dp[i-coins[j]]
        return dp[amount]