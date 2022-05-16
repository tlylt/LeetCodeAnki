# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        d = []
        if not root:
            return []
        ans = []
        curr = root
        while d or curr:
            while curr:
                d.append(curr)
                curr = curr.left
            if d:
                curr = d.pop()
                ans.append(curr.val)
                curr = curr.right
        return ans