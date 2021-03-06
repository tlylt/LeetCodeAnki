# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            ans += root.left.val
        return ans + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)