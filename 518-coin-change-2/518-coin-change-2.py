class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    dp[j] += dp[j-coins[i]]
        return dp[amount]