# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        val1, val2 = self.helper(root)
        return max(val1, val2)
    def helper(self, root):
        if not root:
            return (0, 0) # take root, don't take root
        l = self.helper(root.left)
        r = self.helper(root.right)
        val1 = root.val + l[1] + r[1]
        val2 = max(l[0], l[1]) + max(r[0], r[1])
        return (val1, val2)