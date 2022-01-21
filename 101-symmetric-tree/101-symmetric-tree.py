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
        
    def helper(self, a, b):
        if not a and not b:
            return True
        if not a and b:
            return False
        if not b and a:
            return False
        if a.val != b.val:
            return False
        else:
            l = self.helper(a.left, b.right)
            r = self.helper(a.right, b.left)
            return l and r