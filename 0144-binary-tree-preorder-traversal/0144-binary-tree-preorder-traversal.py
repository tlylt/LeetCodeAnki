# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        return self.pre(root, result)
    def pre(self, root, result):
        if not root:
            return result
        result.append(root.val)
        self.pre(root.left, result)
        self.pre(root.right, result)
        return result