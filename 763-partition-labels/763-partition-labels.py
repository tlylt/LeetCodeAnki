class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        ans = []
        l = 0
        right = 0
        for j in range(len(s)):
            right = max(right, h[s[j]])
            if right == j:
                ans.append(right - l + 1)
                l = j+1
        return ans
            