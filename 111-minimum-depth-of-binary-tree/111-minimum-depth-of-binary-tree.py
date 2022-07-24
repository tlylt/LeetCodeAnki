# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = deque([root])
        ans = 0
        while d:
            l = len(d)
            for i in range(l):
                c = d.popleft()
                if not c.left and not c.right:
                    return ans + 1
                if c.left:
                    d.append(c.left)
                if c.right:
                    d.append(c.right)
            ans += 1
        return ans