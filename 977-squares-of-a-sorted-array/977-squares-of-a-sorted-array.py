class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        curr = len(nums) - 1
        ans = [0] * len(nums)
        while curr >= 0:
            temp_l = nums[l]**2
            temp_r = nums[r]**2
            if temp_r > temp_l:
                ans[curr] = temp_r
                r -= 1
            else:
                ans[curr] = temp_l
                l += 1
            curr -= 1
        return ans