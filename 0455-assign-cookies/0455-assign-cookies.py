class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        g_idx = 0
        s_idx = 0
        while g_idx < len(g) and s_idx < len(s):
            if s[s_idx] >= g[g_idx]:
                ans += 1
                g_idx += 1
                s_idx += 1
            else:
                s_idx += 1
        return ans
