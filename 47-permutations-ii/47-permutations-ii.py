class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        used = [0] * len(nums)
        def backtrack(nums):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                if used[i]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(nums)
                path.pop()
                used[i] = 0
        backtrack(nums)
        return result