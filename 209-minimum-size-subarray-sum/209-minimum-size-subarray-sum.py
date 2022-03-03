class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        temp = 0
        l = 0
        for r in range(len(nums)):
            temp += nums[r]
            while temp >= target:
                ans = min(ans, r-l+1)
                temp -= nums[l]
                l+=1
        return ans if ans != float('inf') else 0
        