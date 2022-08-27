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
            return 0, 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        rob = root.val + l[1] + r[1]
        not_rob = max(l[0], l[1]) + max(r[0], r[1])
        return rob, not_rob