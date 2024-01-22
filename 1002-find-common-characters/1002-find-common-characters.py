class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words or len(words) == 0:
            return []
        ref = [0] * 26
        for i in words[0]:
            ref[ord(i) - ord('a')] += 1
        for j in range(1, len(words)):
            ref2 = [0] * 26
            for k in words[j]:
                ref2[ord(k) - ord('a')] += 1
            for x in range(26):
                ref[x] = min(ref[x], ref2[x])
        ans = []
        for y in range(26):
            while ref[y] != 0:
                ans.append(chr(ord('a') + y))
                ref[y] -= 1
        return ans