class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pt = len(nums) - 1
        l, r = 0, len(nums) - 1
        ans = [0] * len(nums)
        while l <= r:
            l2, r2 = nums[l] ** 2, nums[r] ** 2
            if l2 < r2:
                ans[pt] = r2
                r -= 1
            else:
                ans[pt] = l2
                l += 1
            pt -= 1
        return ans
            