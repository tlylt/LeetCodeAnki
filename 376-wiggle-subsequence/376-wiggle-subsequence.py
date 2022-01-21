class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        preDiff = 0
        currDiff = 0
        result = 1
        for i in range(len(nums)-1):
            currDiff = nums[i+1] - nums[i]
            if (currDiff > 0 and preDiff <=0) or (currDiff <0 and preDiff >=0):
                preDiff = currDiff
                result+=1
        return result
        