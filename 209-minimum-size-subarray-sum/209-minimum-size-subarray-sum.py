class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        temp = 0
        l = 0
        ans = float('inf')
        for r in range(len(nums)):
            temp += nums[r]
            while temp >= target:
                ans = min(ans, r-l+1)
                temp -= nums[l]
                l += 1
        return 0 if ans == float('inf') else ans
            