class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = 0        
        ans = 0
        for c in range(len(s)):
            if l > len(g) - 1:
                return ans
            if s[c] >= g[l]:
                ans += 1
                l += 1
        return ans