# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        s = deque([root])
        ans = []
        while s:
            l = len(s)
            temp = []
            for i in range(l):
                c = s.popleft()
                temp.append(c.val)
                if c.left:
                    s.append(c.left)
                if c.right:
                    s.append(c.right)
            ans.append(temp)
        return ans
                