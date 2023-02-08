class Solution:
    def maxArea(self, height: List[int]) -> int:
          max_so_far = 0
          l = 0
          r = len(height) - 1
          while l < r:
            max_so_far = max(max_so_far, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
              l += 1
            else:
              r -= 1
          return max_so_far