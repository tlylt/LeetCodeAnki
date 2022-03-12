class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        l = 0
        temp = 0
        for r in range(len(nums)):
            temp += nums[r]
            while temp >= target:
                ans = min(r-l+1, ans)
                temp -= nums[l]
                l += 1
        return ans if ans != float('inf') else 0