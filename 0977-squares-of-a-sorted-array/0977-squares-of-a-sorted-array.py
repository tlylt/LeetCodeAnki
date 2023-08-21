class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            a, b = nums[l] ** 2, nums[r] ** 2
            if a > b:
                ans[i] = a
                l += 1
            else:
                ans[i] = b
                r -= 1
        return ans