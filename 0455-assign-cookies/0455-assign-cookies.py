class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        pt = 0
        for i in g:
            while pt < len(s) and s[pt] < i:
                pt += 1
            if pt == len(s):
                return ans
            ans += 1
            pt += 1
        return ans
            