class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ref = [0] * 26
        for i in words[0]:
            ref[ord(i)-ord('a')] += 1
        for j in range(1, len(words)):
            ref2 = [0] * 26
            w = words[j]
            for k in w:
                ref2[ord(k)-ord('a')] += 1
            for z in range(26):
                ref[z] = min(ref[z], ref2[z])
        ans = []
        for y in range(26):
            while ref[y] > 0:
                ans.append(chr(y + ord('a')))
                ref[y]-=1
        return ans