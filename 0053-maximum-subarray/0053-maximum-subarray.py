class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        sofar = 0
        for i in range(len(nums)):
            sofar += nums[i]
            result = max(result, sofar)
            if sofar <= 0:
                sofar = 0
        return result