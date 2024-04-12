class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ans = [0] * len(nums)
        pt = len(nums) - 1
        while l <= r:
            x, y = nums[l] ** 2, nums[r] ** 2
            if x < y:
                ans[pt] = y
                r -= 1
            else:
                ans[pt] = x
                l += 1
            pt -= 1
        return ans