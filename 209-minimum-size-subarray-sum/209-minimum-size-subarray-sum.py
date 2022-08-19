class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ans = float('inf')
        temp = 0
        for r in range(len(nums)):
            temp += nums[r]
            while temp >= target:
                temp -= nums[l]
                ans = min(ans, r-l+1)
                l += 1
        return ans if ans != float('inf') else 0
