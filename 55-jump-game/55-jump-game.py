class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover= 0
        curr = 0
        while curr <= cover:
            cover = max(nums[curr] + curr, cover)
            if cover >= len(nums)-1:
                return True
            curr+=1
        return False