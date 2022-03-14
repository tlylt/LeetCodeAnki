class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                return [i, h[nums[i]]]
            else:
                h[target-nums[i]] = i
