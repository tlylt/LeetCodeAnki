class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ref = {}
        for i in arr:
            ref[i] = ref.get(i, 0) + 1
        check = set()
        for k, v in ref.items():
            if v in check:
                return False
            check.add(v)
        return True