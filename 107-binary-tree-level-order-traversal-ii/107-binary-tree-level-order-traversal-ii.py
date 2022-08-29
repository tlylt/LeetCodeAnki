# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        depth = -1
        def backtrack(root, curr):
            nonlocal depth, ans
            if curr > depth:
                ans.append([])
                depth = curr
            ans[curr].append(root.val)
            if root.left:
                backtrack(root.left, curr+1)
            if root.right:
                backtrack(root.right, curr+1)
        backtrack(root, 0)
        return ans[::-1]