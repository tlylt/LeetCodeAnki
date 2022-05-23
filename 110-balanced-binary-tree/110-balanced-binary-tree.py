# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = self.helper(root)
        return True if ans != -1 else False
    def helper(self, root):
        if not root:
            return 0
        ls = self.helper(root.left)
        rs = self.helper(root.right)
        if ls == -1:
            return -1
        if rs == -1:
            return -1
        if abs(rs-ls) > 1:
            return -1
        return 1 + max(ls, rs)