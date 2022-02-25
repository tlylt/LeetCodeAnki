class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(k, n, startIdx):
            if len(path) == k and sum(path) == n:
                result.append(path[:])
                return
            if len(path) >= k:
                return
            for i in range(startIdx, 9-(k-len(path))+2):
                path.append(i)
                backtrack(k, n, i+1)
                path.pop()
        backtrack(k, n, 1)
        return result