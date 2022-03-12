class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [0] * len(nums)
        def backtrack(nums):
            if len(path) >= len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(nums)
                path.pop()
                used[i] = 0
        backtrack(nums)
        return result