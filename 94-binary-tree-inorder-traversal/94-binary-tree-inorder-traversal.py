# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        s = []
        curr = root
        if not root:
            return []
        while s or curr:
            while curr:
                s.append(curr)
                curr = curr.left
            if s:
                curr = s.pop()
                ans.append(curr.val)
                curr = curr.right
        return ans