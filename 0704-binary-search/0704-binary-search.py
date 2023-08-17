class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(nums, 0, len(nums)-1, target)
    def binary(self, nums, l, r, target):
        if l > r:
            return -1
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary(nums, l, mid - 1, target)
        else:
            return self.binary(nums, mid + 1, r, target)
        