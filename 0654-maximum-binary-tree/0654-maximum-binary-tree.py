# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_max(self, nums, l, r):
        idx = l # impt!!!!! not != 0
        for i in range(l, r+1):
            if nums[idx] < nums[i]:
                idx = i
        return idx
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l > r:
            return None
        idx = self.find_max(nums, l, r)
        root = TreeNode(val = nums[idx])
        root.left = self.helper(nums, l, idx-1)
        root.right = self.helper(nums, idx+1, r)
        return root
