# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        result = []
        def backtrack(root):
            if not root:
                return
            if not root.left and not root.right:
                path.append(str(root.val))
                result.append("->".join(path))
                path.pop()
            path.append(str(root.val))
            if root.left:
                backtrack(root.left)
            if root.right:
                backtrack(root.right)
            path.pop()
        backtrack(root)
        return result