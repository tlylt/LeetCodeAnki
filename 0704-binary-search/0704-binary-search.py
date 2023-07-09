class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            curr = l + (r - l)//2
            if nums[curr] == target:
                return curr
            if nums[curr] > target:
                r = curr - 1
            else:
                l = curr + 1
        return -1