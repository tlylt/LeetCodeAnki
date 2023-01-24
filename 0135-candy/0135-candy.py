class Solution:
    def candy(self, ratings: List[int]) -> int:
        dp = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                dp[i] = dp[i-1] + 1
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                dp[j] = max(dp[j], dp[j+1] + 1)
        return sum(dp)