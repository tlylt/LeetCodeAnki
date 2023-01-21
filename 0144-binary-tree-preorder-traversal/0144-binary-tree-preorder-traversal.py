# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            curr = stack.pop()
            if curr:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
                stack.append(curr)
                stack.append(None)
            else:
                curr = stack.pop()
                result.append(curr.val)
        return result