# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        ans = []
        self.helper(root, ans)
        return ans
    def helper(self, node, ans):
        if not node:
            return
        self.helper(node.left, ans)
        self.helper(node.right, ans)
        ans.append(node.val)