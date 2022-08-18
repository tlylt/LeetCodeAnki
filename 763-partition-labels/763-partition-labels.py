class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ref = {}
        for i in range(len(s)):
            ref[s[i]] = i
        l = 0
        ans = []
        r = 0
        for i in range(len(s)):
            r = max(ref[s[i]], r)
            if i == r:
                ans.append(r-l+1)
                l = r + 1
        return ans