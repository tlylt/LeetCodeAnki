class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        temp = 0
        ans = float('inf')
        for r in range(len(nums)):
            temp += nums[r]
            while temp >= target:
                ans = min(ans, r-l+1)
                temp -= nums[l]
                l += 1
        return ans if ans != float('inf') else 0
            