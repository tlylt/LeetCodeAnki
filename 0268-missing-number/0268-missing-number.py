class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      ref = set(nums)
      ans = 0
      while ans in ref:
        ans += 1
      return ans        