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
        def backtrack(root, targetSum):
            if not root.left and not root.right and targetSum == 0:
                result.append(path[:])
                return
            if root.left:
                path.append(root.left.val)
                backtrack(root.left, targetSum-root.left.val)
                path.pop()
            if root.right:
                path.append(root.right.val)
                backtrack(root.right, targetSum-root.right.val)
                path.pop()
        if not root:
            return []
        path.append(root.val)
        backtrack(root, targetSum-root.val)
        return result