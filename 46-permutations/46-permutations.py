class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [0] * len(nums)
        path = []
        def backtrack(nums, path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(nums, path)
                path.pop()
                used[i] = False
        backtrack(nums, path)
        return result