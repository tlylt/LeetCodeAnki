# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return []
        stack = [root]
        while stack:
            if stack[-1]:
                # visit
                top = stack.pop()
                if top.right:
                    stack.append(top.right)
                
                stack.append(top)
                stack.append(None) # identifier
                
                if top.left:
                    stack.append(top.left)
            else:
                stack.pop()
                top = stack.pop()
                ans.append(top.val)
        return ans