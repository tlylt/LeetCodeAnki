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
        preorder = preorder[1:]
        root = TreeNode(root_val)
        
        index = inorder.index(root_val)
        root.left = self.buildTree(preorder[:len(inorder[:index])], inorder[:index])
        root.right = self.buildTree(preorder[len(inorder[:index]):], inorder[index+1:])
        return root