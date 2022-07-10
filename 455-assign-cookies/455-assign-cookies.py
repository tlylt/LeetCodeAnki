class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        if len(g) == 0:
            return 0
        pt = 0
        for i in s:
            if pt >= len(g):
                return ans
            if i >= g[pt]:
                ans += 1
                pt += 1
        return ans