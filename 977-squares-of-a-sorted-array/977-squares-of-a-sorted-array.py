class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        l = 0
        r = len(nums)-1
        pt = len(nums)-1
        while pt >= 0:
            ls = nums[l]**2
            rs = nums[r]**2
            if ls > rs:
                ans[pt] = ls
                l+=1
            else:
                ans[pt] = rs
                r-=1
            pt-=1
        return ans