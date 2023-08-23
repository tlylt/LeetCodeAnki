class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary(0, len(nums)-1, nums, target)
    def binary(self, l, r, nums, target):
        if l > r:
            return -1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        return r+1