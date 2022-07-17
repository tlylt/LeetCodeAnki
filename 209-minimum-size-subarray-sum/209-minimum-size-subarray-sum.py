class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        ptl = 0
        temp = 0
        for ptr in range(len(nums)):
            temp += nums[ptr]
            while temp >= target:
                temp -= nums[ptl]
                ans = min(ans, ptr-ptl+1)
                ptl += 1
        return ans if ans != float('inf') else 0
