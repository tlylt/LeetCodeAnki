# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def helper(node, depth):
            if depth == len(result):
                result.append([])
            if node:
                result[depth].append(node.val)
                if node.left:
                    helper(node.left, depth+1)
                if node.right:
                    helper(node.right, depth+1)
        if not root:
            return []
        helper(root, 0)
        return result[::-1]