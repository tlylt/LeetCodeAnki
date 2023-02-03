class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        ans = [0] * len(nums)
        product = 1
        for i in range(len(nums)):
            ans[i] = product
            product *= nums[i]
        product = 1
        for j in range(len(nums)-1, -1, -1):
            ans[j] *= product
            product *= nums[j]
        return ans
        