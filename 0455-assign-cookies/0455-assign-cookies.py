class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        ans = 0
        pt = 0
        for i in s:
            if pt < len(g) and g[pt] <= i:
                ans += 1
                pt += 1
                continue
        return ans