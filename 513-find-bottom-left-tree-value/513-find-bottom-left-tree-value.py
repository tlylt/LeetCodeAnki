# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        depth = 0
        ans = 0
        def backtrack(root, curr):
            if not root:
                return
            nonlocal depth, ans
            if curr > depth:
                depth = curr
                ans = root.val
            backtrack(root.left, curr+1)
            backtrack(root.right, curr+1)
        backtrack(root, 1)
        return ans