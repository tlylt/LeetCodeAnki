# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans
    def helper(self, root, ans):
        if not root:
            return
        self.helper(root.left, ans)
        self.helper(root.right, ans)
        ans.append(root.val)