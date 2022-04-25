class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cover = 0
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        l = 0
        ans = []
        for i in range(len(s)):
            cover = max(cover,h[s[i]])
            if cover == i:
                ans.append(i-l+1)
                l = i + 1
        return ans