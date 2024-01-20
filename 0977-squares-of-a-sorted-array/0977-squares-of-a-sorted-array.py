class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        l, r, pt = 0, len(nums) - 1, len(nums) - 1
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                ans[pt] = nums[l] ** 2
                l += 1
            else:
                ans[pt] = nums[r] ** 2
                r -= 1
            pt -= 1
        return ans
                