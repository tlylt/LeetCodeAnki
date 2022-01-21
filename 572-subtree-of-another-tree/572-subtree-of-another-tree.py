# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if self.helper(root, subRoot):
                return True
            else:
                if root:
                    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
                else:
                    if not root and subRoot:
                        return False
                    else:
                        return True
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
            l = self.helper(a.left, b.left)
            r = self.helper(a.right, b.right)
            return l and r