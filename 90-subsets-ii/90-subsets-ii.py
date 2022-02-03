class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        def backtrack(nums, startIdx):
            result.append(path[:])
            if startIdx >= len(nums):
                return
            for i in range(startIdx, len(nums)):
                if i > startIdx and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
        backtrack(nums, 0)
        return result