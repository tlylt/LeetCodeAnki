class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(n, k, startIdx):
            if len(path) == k:
                result.append(path[:])
                return
            if len(path) >= k:
                return
            for i in range(startIdx, n-(k-len(path))+2):
                path.append(i)
                backtrack(n, k, i+1)
                path.pop()
        backtrack(n, k, 1)
        return result