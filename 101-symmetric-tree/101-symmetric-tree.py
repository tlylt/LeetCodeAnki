# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
    def helper(self, l, r):
        if not l and not r:
            return True
        if l and not r:
            return False
        if not l and r:
            return False
        if l.val != r.val:
            return False
        return self.helper(l.left, r.right) and self.helper(l.right, r.left)