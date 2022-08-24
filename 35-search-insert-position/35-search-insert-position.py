class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        return self.binary_search(nums, target)

    def binary_search(self, arr, target):
        return self.helper(arr, 0, len(arr), target)

    def helper(self, arr, l, r, target):
        if l >= r:
            return l
        mid = (r-l) // 2 + l
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return self.helper(arr, l, mid, target)
        else:
            return self.helper(arr, mid+1, r, target)