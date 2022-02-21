# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        q = deque([root])
        while q:
            temp = []
            l = len(q)
            for i in range(l):
                c = q.popleft()
                temp.append(c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            result.append(temp)
        return result[::-1]