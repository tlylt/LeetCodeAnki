class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        cover = 0
        l = 0
        ans = []
        for r in range(len(s)):
            cover = max(cover, h[s[r]])
            if cover == r:
                ans.append(r-l+1)
                l = r + 1
        return ans