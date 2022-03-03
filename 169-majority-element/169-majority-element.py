class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = (l+r)//2
        l_major = self.helper(nums, l, mid)
        r_major = self.helper(nums, mid+1, r)
        
        if l_major == r_major:
            return l_major
        else:
            count_l_major = sum(1 for i in range(l, r+1) if nums[i] == l_major)
            count_r_major = sum(1 for i in range(l, r+1) if nums[i] == r_major)
            if count_l_major > count_r_major:
                return l_major
            return r_major