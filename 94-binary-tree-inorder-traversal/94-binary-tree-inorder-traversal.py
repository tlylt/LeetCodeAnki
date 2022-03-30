# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans
    def helper(self, root, ans):
        if not root:
            return
        if root.left:
            self.helper(root.left, ans)
        ans.append(root.val)
        if root.right:
            self.helper(root.right, ans)
            