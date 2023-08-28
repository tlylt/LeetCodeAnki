class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums, target):
            l = 0
            r = len(nums) - 1
            rightBorder = -2
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
                    rightBorder = l
            return rightBorder
        def getLeftBorder(nums, target):
            l = 0
            r = len(nums) - 1
            leftBorder = -2
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid - 1
                    leftBorder = r
                else:
                    l = mid + 1
            return leftBorder
        l = getLeftBorder(nums, target)
        r = getRightBorder(nums, target)
        if l == -2 or r == -2:
            return [-1, -1]
        if r - l > 1:
            return [l + 1, r - 1]
        return [-1, -1]
                