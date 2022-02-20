# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return False if self.helper(root) == -1 else True
    def helper(self, node):
        if not node:
            return 0
        l = self.helper(node.left)
        r = self.helper(node.right)
        if l == -1:
            return -1
        if r == -1:
            return -1
        if abs(l-r) > 1:
            return -1
        return 1 + max(l, r)