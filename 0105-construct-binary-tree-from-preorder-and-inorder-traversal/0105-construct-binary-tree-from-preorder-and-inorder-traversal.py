# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root_idx = inorder.index(root_val)
        preorder = preorder[1:]
        root = TreeNode(val = root_val)
        root.left = self.buildTree(preorder[:len(inorder[:root_idx])], inorder[:root_idx])
        root.right = self.buildTree(preorder[len(inorder[:root_idx]):], inorder[root_idx+1:])
        return root