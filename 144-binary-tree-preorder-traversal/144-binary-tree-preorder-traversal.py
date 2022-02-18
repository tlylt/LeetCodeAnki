# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s = []
        s.append(root)
        ans = []
        while s:
            c = s.pop()
            ans.append(c.val)
            if c.right:
                s.append(c.right)
            if c.left:
                s.append(c.left)
        return ans