class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        used = [0] * len(nums)
        def backtrack(nums, startIdx):
            result.append(path[:])
            for i in range(startIdx, len(nums)):
                if i > startIdx and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
                used[i] = 0
        backtrack(nums, 0)
        return result