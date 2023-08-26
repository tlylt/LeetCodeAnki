class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ref = set()
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in ref:
                ref.remove(s[l])
                l += 1
            ref.add(s[r])
            ans = max(ans, r-l+1)
        return ans
                    
                        