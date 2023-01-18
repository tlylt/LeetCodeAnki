class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + ((r-l) // 2)
            curr = nums[mid]
            if target == curr:
                return mid
            elif curr > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
            