class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            for w in wordDict:
                if i >= len(w):
                    dp[i] = dp[i] or (dp[i-len(w)] and s[i-len(w):i] == w)
        return dp[len(s)]