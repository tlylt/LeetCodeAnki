class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] *(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for w in wordDict:
                if len(w) <= i:
                    dp[i] = dp[i] or (dp[i-len(w)] and s[i-len(w):i] == w)
        return dp[-1]