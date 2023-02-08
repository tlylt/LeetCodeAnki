class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ref = {}
        for i in range(len(s)):
            ref[s[i]] = i
        
        ans = []
        l = 0
        cover = 0
        for i in range(len(s)):
            cover = max(cover, ref[s[i]])
            if cover == i:
                ans.append(i-l+1)
                l = i+1
        return ans