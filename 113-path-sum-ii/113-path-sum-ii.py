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
        if not root:
            return []
        def backtrack(node, targetSum):
            if not node.left and not node.right and targetSum == node.val:
                path.append(node.val)
                result.append(path[:])
                path.pop()
                return
            path.append(node.val)
            if node.left:
                backtrack(node.left, targetSum - node.val)
            if node.right:
                backtrack(node.right, targetSum - node.val)
            path.pop()
        backtrack(root, targetSum)
        return result