class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            left_sum += nums[i]
            if total - left_sum + nums[i] == left_sum:
                return i
        return -1        