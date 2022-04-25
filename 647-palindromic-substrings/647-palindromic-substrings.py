class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            mid = self.extend(s, i, i, len(s))
            twoMid = self.extend(s, i, i+1, len(s))
            ans += mid + twoMid
        return ans
    def extend(self, s, l, r, n):
        ans = 0
        while l >=0 and r < n and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
        return ans