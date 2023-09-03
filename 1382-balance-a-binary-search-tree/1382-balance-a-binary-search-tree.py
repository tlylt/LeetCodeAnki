# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            lst.append(root.val)
            traverse(root.right)
        traverse(root)
        def build(lst, l, r):
            if l > r:
                return None
            mid = l + (r - l) // 2
            root = TreeNode(lst[mid])
            root.left = build(lst, l, mid - 1)
            root.right = build(lst, mid + 1, r)
            return root
        return build(lst, 0, len(lst) - 1)
        