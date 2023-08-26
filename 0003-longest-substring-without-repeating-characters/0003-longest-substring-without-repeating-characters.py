class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        ref = set()
        l = 0
        ref.add(s[0])
        ans = 1
        for r in range(1, len(s)):
            if s[r] in ref:
                ref.discard(s[r])
                while s[l] != s[r]:
                    ref.discard(s[l])
                    l += 1
                l += 1
                ref.add(s[r])
            else:
                ref.add(s[r])
                ans = max(ans, r-l+1)
        return ans
                    
                        