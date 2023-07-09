class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = curr = len(nums) - 1
        result = [0] * len(nums)
        while l <= r:
            a, b = nums[l] ** 2, nums[r] ** 2
            if a < b:
                result[curr] = b
                r -= 1
            else:
                result[curr] = a
                l += 1
            curr -= 1
        return result