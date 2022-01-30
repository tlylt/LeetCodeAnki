class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        ans = []
        l = 0
        right = 0
        for i in range(len(s)):
            right = max(right, h[s[i]])
            if right == i:
                ans.append(right - l + 1)
                l = right + 1
        return ans