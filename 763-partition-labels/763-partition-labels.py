class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        left = 0
        right = 0
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        for j in range(len(s)):
            right = max(h[s[j]], right)
            if right == j:
                ans.append(right-left+1)
                left = right+1
        return ans