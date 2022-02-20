# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        temp = []
        def helper(node, targetSum):
            if not node:
                return
            if node.val == targetSum and not node.left and not node.right:
                temp.append(node.val)
                ans.append(temp[:])
                temp.pop()
                return
            if node.left:
                temp.append(node.val)
                helper(node.left, targetSum-node.val)
                temp.pop()
            if node.right:
                temp.append(node.val)
                helper(node.right, targetSum-node.val)
                temp.pop()
        helper(root, targetSum)
        return ans