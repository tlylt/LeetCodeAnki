class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        temp = 0
        ans = float('inf')
        l = 0
        for i in range(len(nums)):
            temp += nums[i]
            while temp >= target:
                ans = min(ans, i-l+1)
                temp -= nums[l]
                l += 1
        return ans if ans != float('inf') else 0
                