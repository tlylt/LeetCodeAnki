class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = l + (r-l) // 2
        lm = self.helper(nums, l, mid)
        rm = self.helper(nums, mid+1, r)
        if lm == rm:
            return lm
        lc = sum([1 for i in range(l, r+1) if nums[i] == lm])
        rc = sum([1 for i in range(l, r+1) if nums[i] == rm])
        if lc > rc:
            return lm
        return rm