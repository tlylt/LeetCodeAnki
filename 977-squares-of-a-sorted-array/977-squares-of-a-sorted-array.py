class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            ls = nums[l] **2
            rs = nums[r] **2
            if ls > rs:
                ans[i] = ls
                l += 1
            else:
                ans[i] = rs
                r -= 1
        return ans