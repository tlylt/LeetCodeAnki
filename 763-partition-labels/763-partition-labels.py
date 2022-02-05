class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        right = 0
        l = 0
        ans = []
        for i in range(len(s)):
            right = max(right, h[s[i]])
            if right == i:
                ans.append(right-l+1)
                l = i+1
        return ans