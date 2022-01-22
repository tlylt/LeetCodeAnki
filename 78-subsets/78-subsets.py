class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtrack(nums, startIdx):
            result.append(path[:])
            if len(path) == len(nums):
                return
            for i in range(startIdx, len(nums)):
                path.append(nums[i])
                backtrack(nums, i + 1)
                path.pop()
        backtrack(nums, 0)
        return result