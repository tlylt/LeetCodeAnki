class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        l = 0
        temp = 0
        for r in range(len(nums)):
            temp += nums[r]
            if temp < target:
                continue
            while temp >= target:
                ans = min(ans, r-l+1)
                temp -= nums[l]
                l += 1
        return 0 if ans == float('inf') else ans