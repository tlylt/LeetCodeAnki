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
        s = deque([root])
        temp = 0
        while s:
            l = len(s)
            for i in range(l):
                c = s.popleft()
                if not c.left and not c.right:
                    return temp + 1
                if c.left:
                    s.append(c.left)
                if c.right:
                    s.append(c.right)
            temp += 1
        return temp