class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, pt = 0, len(nums) - 1, len(nums) - 1
        ans = [0] * len(nums)
        while l <= r:
            ls, rs = nums[l] ** 2, nums[r] ** 2
            if ls > rs:
                ans[pt] = ls
                l += 1
            else:
                ans[pt] = rs
                r -= 1
            pt -= 1
        return ans