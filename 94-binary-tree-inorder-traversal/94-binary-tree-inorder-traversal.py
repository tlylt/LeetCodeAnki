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
        q = []
        curr = root
        ans = []
        while q or curr:
            while curr:
                q.append(curr)
                curr = curr.left
            if q:
                curr = q.pop()
                ans.append(curr.val)
                curr = curr.right
        return ans