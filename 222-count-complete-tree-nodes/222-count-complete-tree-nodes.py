# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)
    def helper(self, root):
        if not root:
            return 0
        ln = root.left
        rn = root.right
        l = 0
        r = 0
        while ln:
            ln = ln.left
            l += 1
        while rn:
            rn = rn.right
            r += 1
        if l == r:
            return 2 ** (l+1) - 1
        else:
            return 1 + self.helper(root.left) + self.helper(root.right)