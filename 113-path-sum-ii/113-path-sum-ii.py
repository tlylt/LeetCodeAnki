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
        def backtrack(root, target):
            if root and target == root.val and not root.left and not root.right:
                path.append(root.val)
                result.append(path[:])
                path.pop()
                return
            if not root:
                return
            path.append(root.val)
            backtrack(root.left, target-root.val)
            backtrack(root.right, target-root.val)
            path.pop()
        backtrack(root, targetSum)
        return result