class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = (r+l) // 2
        l_maj = self.helper(nums, l, mid)
        r_maj = self.helper(nums, mid+1, r)
        if l_maj == r_maj:
            return l_maj
        count_l = sum([1 for i in range(l, r+1) if nums[i] == l_maj])
        count_r = sum([1 for i in range(l, r+1) if nums[i] == r_maj])
        if count_l > count_r:
            return l_maj
        return r_maj