class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ref = {}
        for i in words[0]:
            ref[i] = ref.get(i, 0) + 1
        for j in range(1, len(words)):
            w = words[j]
            ref2 = {}
            for k in w:
                ref2[k] = ref2.get(k, 0) + 1
            for key, val in ref.items():
                if key in ref2:
                    ref[key] = min(val, ref2[key])
                else:
                    ref[key] = 0
        ans = []
        for key, val in ref.items():
            while val >= 1:
                ans.append(key)
                val -= 1
        return ans
                