class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        r = 0
        l = 0
        ans = []
        for i in range(len(s)):
            r = max(r, h[s[i]])
            if r == i:
                ans.append(r-l+1)
                l = r+1
        return ans
            