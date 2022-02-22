class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        right = 0
        l = 0
        result = []
        for j in range(len(s)):
            right = max(right, h[s[j]])
            if right == j:
                result.append(j-l+1)
                l = j+1
        return result