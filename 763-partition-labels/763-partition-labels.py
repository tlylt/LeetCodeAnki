class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
        ans = []
        l = 0
        temp = 0
        for r in range(len(s)):
            temp = max(h[s[r]], temp)
            if temp == r:
                ans.append(r-l+1)
                l = r + 1
        return ans