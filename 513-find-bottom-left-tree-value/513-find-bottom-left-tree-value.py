# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        depth = -1
        left = 0
        def backtrack(root, curr):
            nonlocal depth, left
            if curr > depth:
                depth = curr
                left = root.val
            if root.left:
                backtrack(root.left, curr+1)
            if root.right:
                backtrack(root.right, curr+1)
        backtrack(root, 0)
        return left