class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        c = len(nums) - 1
        l = 0
        r = len(nums) - 1
        while l <= r:
            a, b = nums[l]**2, nums[r]**2
            if a > b:
                ans[c] = a
                l += 1
                c -= 1
            else:
                ans[c] = b
                r -= 1
                c -= 1
        return ans