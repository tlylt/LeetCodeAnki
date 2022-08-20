# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums))
    def helper(self, nums, l, r):
        if l >= r:
            return None
        idx = l
        for i in range(l, r):
            if nums[i] > nums[idx]:
                idx = i
        
        root = TreeNode(val=nums[idx])
        root.left = self.helper(nums, l, idx)
        root.right = self.helper(nums, idx+1, r)
        return root