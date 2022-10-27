class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ref = {}
        for i in range(len(s)):
            ref[s[i]] = i
        l = 0
        reach = 0
        ans = []
        for r in range(len(s)):
            reach = max(reach, ref[s[r]])
            if reach == r:
                ans.append(r-l+1)
                l = r + 1
        return ans