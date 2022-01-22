class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r = len(nums) - 1
        ans =[0] * len(nums)
        curr = len(nums) - 1
        while curr >=0:
            a = nums[l]**2
            b = nums[r]**2
            if a >=b:
                ans[curr] = a
                l+=1
            else:
                ans[curr] =  b
                r-=1
            curr-=1
        return ans