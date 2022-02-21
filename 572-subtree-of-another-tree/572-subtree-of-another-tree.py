# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        stack = [root]
        while stack:
            c = stack.pop()
            if self.helper(c, subRoot):
                return True
            if c.left:
                stack.append(c.left)
            if c.right:
                stack.append(c.right)
        return False
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
            return self.helper(a.left, b.left) and self.helper(a.right, b.right)