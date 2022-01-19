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
        ans = []
        self.helper(root, ans)
        return ans
    def helper(self, node, ans):
        if not node:
            return
        ans.append(node.val)
        self.helper(node.left, ans)
        self.helper(node.right, ans)