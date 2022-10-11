class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0
        a = min(nums)
        b = max(nums)
        if a == b:
            return 0
        x = a + k
        y = b - k
        diff = y - x
        if diff < 0:
            return 0
        return diff