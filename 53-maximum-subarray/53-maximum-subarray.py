class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        temp = 0
        for i in nums:
            temp += i
            ans = max(temp, ans)
            if temp <= 0:
                temp = 0
        return ans