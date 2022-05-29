# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if not root:
            return
        s = deque([root])
        while s:
            l = len(s)
            temp = 0
            for i in range(l):
                c = s.popleft()
                temp += c.val
                if c.left:
                    s.append(c.left)
                if c.right:
                    s.append(c.right)
            result.append(temp/l)
        return result