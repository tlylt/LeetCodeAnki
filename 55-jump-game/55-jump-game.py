class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        for i in range(len(nums)):
            cover = max(nums[i]+i, cover)
            if cover >= len(nums)-1:
                return True
            if cover <= i:
                return False
        return False