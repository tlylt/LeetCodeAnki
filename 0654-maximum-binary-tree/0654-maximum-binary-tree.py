# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_max(self, nums, l, r):
        idx = l # impt!!!!! not != 0
        for i in range(l, r):
            if nums[idx] < nums[i]:
                idx = i
        return idx
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_val_idx = self.find_max(nums, 0, len(nums))
        root = TreeNode(nums[max_val_idx])
        root.left = self.constructMaximumBinaryTree(nums[:max_val_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_val_idx+1:])
        return root