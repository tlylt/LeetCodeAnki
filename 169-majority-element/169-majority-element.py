class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(nums,0, len(nums)-1)
    def helper(self, nums, l, r):
        if r == l:
            return nums[l]
        mid = (r+l)//2
        left_maj = self.helper(nums, l, mid)
        right_maj = self.helper(nums, mid+1, r)
        if left_maj == right_maj:
            return left_maj
        else:
            left_count = sum(1 for i in range(l, r+1) if nums[i] == left_maj)
            right_count = sum(1 for i in range(l, r+1) if nums[i] == right_maj)
            if left_count > right_count:
                return left_maj
            return right_maj