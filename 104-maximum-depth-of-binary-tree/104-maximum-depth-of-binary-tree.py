# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        ans = 0
        while q:
            l = len(q)
            for i in range(l):
                c = q.popleft()
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            ans+=1
        return ans