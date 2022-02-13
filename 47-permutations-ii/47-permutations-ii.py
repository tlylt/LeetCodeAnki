class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        path =[]
        used = [0] * len(nums)
        nums.sort()
        def backtrack(nums):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = 1
                backtrack(nums)
                used[i] = 0
                path.pop()
        backtrack(nums)
        return result