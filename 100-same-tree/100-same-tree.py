# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)
    def helper(self, a, b):
        if not a and b:
            return False
        if not b and a:
            return False
        if not a and not b:
            return True
        if a.val != b.val:
            return False
        l = self.helper(a.left, b.left)
        r = self.helper(a.right, b.right)
        return l and r