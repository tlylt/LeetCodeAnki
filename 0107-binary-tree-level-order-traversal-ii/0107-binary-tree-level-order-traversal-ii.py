# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        depth = -1
        def backtrack(root, curr):
            nonlocal depth
            if not root:
                return
            if depth < curr:
                depth = curr
                result.append([])
            result[curr].append(root.val)
            backtrack(root.left, curr+1)
            backtrack(root.right, curr+1)
        backtrack(root, 0)
        return result[::-1]