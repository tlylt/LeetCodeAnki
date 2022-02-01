class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        right = 0
        ans = []
        l = 0
        for r in range(len(s)):
            right = max(right, h[s[r]])
            if right == r:
                ans.append(r-l+1)
                l = r+1
        return ans