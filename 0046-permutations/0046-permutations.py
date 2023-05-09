class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [0] * len(nums)
        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = 0
        backtrack()
        return result
                            