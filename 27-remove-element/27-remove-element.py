class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] == val:
                continue
            nums[l] = nums[r]
            l+=1
        return l