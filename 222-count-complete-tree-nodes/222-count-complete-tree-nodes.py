# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = root.left
        r = root.right
        lc = 1
        rc = 1
        while l:
            lc += 1
            l = l.left
        while r:
            rc += 1
            r = r.right
        if lc == rc:
            return 2**(lc) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)