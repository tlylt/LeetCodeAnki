class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        pt = len(g) - 1
        for cookie in range(len(s)-1, -1, -1):
            while pt > 0 and g[pt] > s[cookie]:
                pt -= 1
            if pt >= 0 and g[pt] <= s[cookie]:
                ans += 1
                pt -= 1
        return ans