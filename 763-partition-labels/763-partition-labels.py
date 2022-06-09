class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        result = []
        l = 0
        r = 0
        temp = 0
        for i in range(len(s)):
            r = max(h[s[i]], r)
            if r == i:
                result.append(r-l+1)
                l = r + 1
        return result