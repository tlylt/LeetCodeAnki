class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        pt = len(s) - 1
        ans = 0
        for i in range(len(g)-1, -1, -1):
            if pt >= 0 and s[pt] >= g[i]:
                ans += 1
                pt -= 1
        return ans
            