# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.helper(root, targetSum)
    def helper(self, root, targetSum):
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        l = self.helper(root.left, targetSum - root.val)
        r = self.helper(root.right, targetSum - root.val)
        return l or r