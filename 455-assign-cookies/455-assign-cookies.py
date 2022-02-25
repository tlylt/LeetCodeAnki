class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        ans = 0
        pt = 0
        for cookie in s:
            if pt >= len(g):
                return ans
            if g[pt] > cookie:
                continue
            else:
                ans+=1
                pt+=1
        return ans