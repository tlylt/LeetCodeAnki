# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            l = len(q)
            temp = float('-inf')
            for i in range(l):
                c = q.popleft()
                temp = max(temp, c.val)
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
            ans.append(temp)
        return ans