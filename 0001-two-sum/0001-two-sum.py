class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for i in range(len(nums)):
            if nums[i] in ref:
                return [ref[nums[i]], i]
            ref[target-nums[i]] = i
