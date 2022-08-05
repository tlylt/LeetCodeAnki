class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [0] * len(nums)
        path = []
        def backtrack(nums):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(nums)
                used[i] = 0
                path.pop()
        backtrack(nums)
        return ans