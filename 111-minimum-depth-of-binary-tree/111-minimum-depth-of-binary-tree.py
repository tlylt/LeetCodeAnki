# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        if not root:
            return 0
        q = deque([root])
        while q:
            l = len(q)
            for i in range(l):
                c = q.popleft()
                if not c.left and not c.right:
                    return depth
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            depth+=1
        return depth