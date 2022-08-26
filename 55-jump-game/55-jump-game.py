class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0]
        for i in range(1, len(nums)):
            if curr < i:
                return False
            curr = max(curr, i + nums[i])
        return True