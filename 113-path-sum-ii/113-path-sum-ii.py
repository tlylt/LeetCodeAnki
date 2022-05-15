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
        def helper(root, targetSum):
            if not root:
                return
            if root.val == targetSum and not root.left and not root.right:
                path.append(root.val)
                result.append(path[:])
                path.pop()
                return
            path.append(root.val)
            helper(root.left, targetSum - root.val)
            path.pop()
            path.append(root.val)
            helper(root.right, targetSum - root.val)
            path.pop()
        helper(root, targetSum)
        return result