class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        curr = float('inf')
        temp = 0
        for r in range(len(nums)):
            temp += nums[r]
            while temp >= target:
                temp -= nums[l]
                curr = min(curr, r-l+1)
                l += 1
        return curr if curr != float('inf') else 0