class Solution:
    def reverse(self, l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        for i in range(len(nums) - 1, -1, -1):
            r = len(nums) -1
            while r > i:
                if nums[r] > nums[i]:
                    nums[i], nums[r] = nums[r], nums[i]
                    self.reverse(i+1, len(nums) - 1, nums)
                    return
                r -= 1
        self.reverse(0, len(nums)-1, nums)
    