class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = [0]*26
        for i in range(len(s)):
            h[ord(s[i])-ord('a')] = i
        result = []
        l = 0
        right = 0
        for j in range(len(s)):
            right = max(right, h[ord(s[j]) - ord('a')])
            if right == j:
                result.append(right-l+1)
                l = j+1
        return result