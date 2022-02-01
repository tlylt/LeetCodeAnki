# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s =[root]
        ans = []
        while s:
            c = s.pop()
            ans.append(c.val)
            if c.left:
                s.append(c.left)
            if c.right:
                s.append(c.right)
        return ans[::-1]