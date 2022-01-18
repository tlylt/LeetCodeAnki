# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = root.left
        r = root.right
        ls = 1
        rs = 1
        while l:
            l = l.left
            ls +=1
        while r:
            r = r.right
            rs +=1
        if ls == rs:
            return 2**ls - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)