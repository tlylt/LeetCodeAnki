class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ref = {}
        for i in range(len(s)):
            ref[s[i]] = i
        ans = []
        l = 0
        temp = 0
        for r in range(len(s)):
            temp = max(ref[s[r]], temp)
            if r == temp:
                ans.append(r-l+1)
                l = r + 1
        return ans