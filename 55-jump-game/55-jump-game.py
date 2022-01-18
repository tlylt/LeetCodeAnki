class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        pt = 0
        while pt <= cover:
            cover = max(pt + nums[pt], cover)
            if cover >= len(nums) - 1:
                return True
            pt+=1
        return False