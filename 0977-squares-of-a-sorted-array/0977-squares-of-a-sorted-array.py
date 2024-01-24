class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pt = len(ans) - 1
        l, r = 0, len(ans) - 1
        while l <= r:
            a, b = nums[l] ** 2, nums[r] ** 2
            if a > b:
                ans[pt] = a
                l += 1
            else:
                ans[pt] = b
                r -= 1
            pt -= 1
        return ans
        