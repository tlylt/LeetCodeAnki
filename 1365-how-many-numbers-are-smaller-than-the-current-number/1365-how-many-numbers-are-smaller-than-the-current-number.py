class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        duplicate = nums[:]
        ref = {}
        duplicate.sort()
        for i in range(len(duplicate)-1, -1, -1):
            ref[duplicate[i]] = i
        for i in range(len(nums)):
            duplicate[i] = ref[nums[i]]
        return duplicate