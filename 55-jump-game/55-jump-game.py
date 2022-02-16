class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        for r in range(len(nums)):
            cover = max(nums[r] + r, cover)
            if cover >= len(nums) - 1:
                return True
            if cover <= r:
                return False
        return False