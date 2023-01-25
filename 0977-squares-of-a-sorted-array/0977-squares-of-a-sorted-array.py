class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        curr = len(nums) - 1
        l = 0
        r = len(nums) - 1
        while l <= r:
            ls = nums[l] * nums[l]
            rs = nums[r] * nums[r]
            if ls < rs:
                ans[curr] = rs
                r -= 1
            else:
                ans[curr] = ls
                l += 1
            curr -= 1
        return ans