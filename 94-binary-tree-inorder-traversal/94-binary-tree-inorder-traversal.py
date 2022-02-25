# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s = []
        ans = []
        c = root
        while c or s:
            if c:
                s.append(c)
                c = c.left
            else:
                c = s.pop()
                ans.append(c.val)
                c = c.right
        return ans
                
                