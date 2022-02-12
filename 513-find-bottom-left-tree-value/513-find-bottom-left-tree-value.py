# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        left = 0
        depth = -1
        def backtrack(node, curr):
            nonlocal left, depth
            if curr > depth:
                depth = curr
                left = node.val
            if node.left:
                backtrack(node.left, curr+1)
            if node.right:
                backtrack(node.right, curr+1)
        backtrack(root, 0)
        return left