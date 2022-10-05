class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [0] * len(nums)
        def backtrack(nums, idx):
            result.append(path[:])
            for i in range(idx, len(nums)):
                if used[i] == 1:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
                used[i] = 0
        backtrack(nums, 0)
        return result