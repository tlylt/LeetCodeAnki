# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val = preorder[0]
        preorder.pop(0)
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        root.left = self.buildTree(preorder[:len(inorder[:idx])], inorder[:idx])
        root.right = self.buildTree(preorder[len(inorder[:idx]):], inorder[idx+1:])
        return root