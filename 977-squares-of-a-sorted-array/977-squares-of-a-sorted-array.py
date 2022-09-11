class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pt1 = 0
        pt2 = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            a, b = nums[pt1]**2, nums[pt2]**2
            if a < b:
                ans[i] = b
                pt2 -= 1
            else:
                ans[i] = a
                pt1 += 1
        return ans