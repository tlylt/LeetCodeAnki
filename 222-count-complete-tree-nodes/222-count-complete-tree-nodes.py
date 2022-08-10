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
        lc = 0
        rc = 0
        while l:
            l = l.left
            lc += 1
        while r:
            r = r.right
            rc += 1
        if lc == rc:
            return 2 **(lc + 1) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)