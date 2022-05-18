class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        l = 0
        temp = 0
        
        for i in range(len(nums)):
            temp += nums[i]
            while temp >= target:
                ans = min(i - l + 1, ans)
                temp -= nums[l]                
                l += 1
        return ans if ans != float('inf') else 0
