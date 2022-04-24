class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        l = 0
        ans = []
        cover = 0
        for r in range(len(s)):
            cover = max(cover, h[s[r]])
            if r == cover:
                ans.append(r - l + 1)
                l = r + 1
        return ans
                