# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        ans = self.helper(root)
        return max(ans[0], ans[1])
    def helper(self, root):
        if not root:
            return 0, 0 # rob, don't rob
        l = self.helper(root.left)
        r = self.helper(root.right)
        val1 = root.val + l[1] + r[1] # rob root
        val2 = max(l[0], l[1]) + max(r[0], r[1]) # don't rob root
        return val1, val2