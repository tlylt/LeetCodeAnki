# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        rootVal = postorder.pop()
        root = TreeNode(val = rootVal)
        index = inorder.index(rootVal)
                
        root.left = self.buildTree(inorder[:index], postorder[:len(inorder[:index])])
        root.right = self.buildTree(inorder[index+1:], postorder[len(inorder[:index]):])
        return root