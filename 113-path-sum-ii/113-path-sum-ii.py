# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        path = []
        def backtrack(node, targetSum):
            if not node:
                return
            if node.val == targetSum and not node.left and not node.right:
                path.append(node.val)
                result.append(path[:])
                path.pop()
            if node.left:
                path.append(node.val)
                backtrack(node.left, targetSum - node.val)
                path.pop()
            if node.right:
                path.append(node.val)
                backtrack(node.right, targetSum - node.val)
                path.pop()
        backtrack(root, targetSum)
        return result