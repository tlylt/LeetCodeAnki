# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            l = len(q)
            temp = None
            for i in range(l):
                c = q.popleft()
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
                temp = c.val
            result.append(temp)
        return result
        