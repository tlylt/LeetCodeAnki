# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        def traverse(root):
            nonlocal prev
            if not root:
                return True
            l = traverse(root.left)
            if prev and prev.val >= root.val:
                return False
            prev = root
            r = traverse(root.right)
            return l and r
        return traverse(root)
